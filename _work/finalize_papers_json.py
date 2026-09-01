#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成最终的 scripts/papers.json，并把结果同步回每篇 meta.json。

幂等：每次都从 papers/*/meta.json + 四份缓存重算，不做增量。

venue 的来源优先级（高到低），每条都记 venue_source，说不清就写「arXiv 预印本」：
  1. docs/review/ 四份人工核验 manifest 与 INDEX.md §4  —— 人对着一手页面核过的
  2. meta.json 的 publication.venue                  —— 同一轮核验写进单篇的
  3. arXiv journal_ref                               —— arXiv 官方元数据字段
  4. arXiv comment 里明确写了「已接收」的            —— 只认接收，不认投稿
  5. DBLP 标题检索（会议名 + 年份）                  —— 本机连 DBLP 稳定超时，当前缓存为空
  6. Semantic Scholar 批量（只取会议名，不取年份）   —— 它的 year 是论文年份不是会议年份
  7. image-generation-papers 第一期清单             —— 该库未记录 venue 的核验来源，证据最弱
  8. 兜底 arXiv 预印本 / 官方资料（无独立论文）

机构只认 PDF 首页作者块（_work/org_cache.json）。OpenAlex 对 arXiv 预印本
几乎没有机构字段（182 篇里 1 篇），且已知会误配，所以不用它补机构。
抽不到的写 null，README 渲染成「未核」。
"""
import json, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, f"{ROOT}/scripts")
from pdf_sources import pdf_url, OVERRIDES

GEN_SRC = "/Users/yuzhang/ZhangYu/self_learning/paper_reading/image-generation-papers/scripts/papers.json"
CHECKED = "2026-09-01"

CJK = lambda t: sum(1 for ch in t if "一" <= ch <= "鿿")
J = lambda p: json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}

ORG_FIX = {           # 只归一确有歧义的团队名，其余保留原文抽取的写法
    "Qwen Team": "阿里巴巴通义千问团队",
    "谷歌研究院，大脑团队": "谷歌大脑",
}
# 12 篇与 image-generation-papers 重叠的：short 对不齐，按 arxiv_id 匹配
NO_VENUE = {"", "—", "-", "n/a", "arxiv", "仅 arxiv", "仅 arxiv 预印本", "arxiv 预印本",
            "arxiv预印本", "未查到正式 venue", "截至核对日仅确认 arxiv",
            "无论文 venue", "无论文venue"}


def clean_venue(v):
    """把 manifest 里的写法收成一个 venue 名；表示「还是预印本」的返回 None。"""
    if not v:
        return None
    v = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", v).strip()      # 去 markdown 链接
    v = re.sub(r"^\d{4}-\d{2}[，,]\s*", "", v).strip()           # 「2025-10，ICCV 2025」
    v = re.sub(r"\s*（[^）]*）\s*$", "", v).strip()
    v = re.sub(r"^(截至核对日)?仅确认\s*", "", v).strip()
    if v.lower() in NO_VENUE:
        return None
    if re.fullmatch(r"\d{4}(-\d{2})?", v):                       # 只有日期，不是 venue
        return None
    return v


ACCEPT = re.compile(
    r"(?:accepted\s+(?:as\s+\w+\s+)?(?:by|to|at|in)|to\s+appear\s+in|published\s+(?:in|at)|"
    r"camera[- ]ready\s+(?:for|of)|proceedings\s+of)\s+(?:the\s+)?([^.;,]{3,70})", re.I)
LEADING = re.compile(
    r"^\s*(?:accepted\s+)?(?:at\s+|by\s+|to\s+)?"
    r"((?:CVPR|ICCV|ECCV|NeurIPS|NIPS|ICLR|ICML|AAAI|IJCAI|ACM\s*MM|ACMMM|SIGGRAPH(?:\s*Asia)?|"
    r"WACV|BMVC|TMLR|TPAMI|TIP|IJCV|EMNLP|ACL|NAACL|COLM|Displays)[^.;,]{0,30})", re.I)
REJECT = re.compile(r"submitt|under\s+review|in\s+submission|preprint|rejected", re.I)


def venue_from_comment(cmt):
    if not cmt or REJECT.search(cmt):
        return None
    m = ACCEPT.search(cmt) or LEADING.match(cmt)
    if not m:
        return None
    v = re.sub(r"\s+", " ", m.group(1)).strip(" .;,")
    v = re.sub(r"^(the)\s+", "", v, flags=re.I)
    return v if 3 <= len(v) <= 70 else None


def main():
    org_c, cls_c = J(f"{ROOT}/_work/org_cache.json"), J(f"{ROOT}/_work/class_cache.json")
    enr = J(f"{ROOT}/_work/enrich_cache.json")
    man = J(f"{ROOT}/_work/manifest_venue.json")
    # INDEX.md §4 那 26 项是 2026-08-29 补的决策型短笔记批次，本库自己的记录。
    # 用这份名单分写作规范，比数二级标题准——11 节那批里有 12 节和 19 节的变体。
    batch2 = {d for d, v in man.items() if v.get("venue_index4")}
    dblp_raw = J(f"{ROOT}/_work/dblp_cache.json")
    s2 = J(f"{ROOT}/_work/s2_cache.json")
    ax, oa = enr.get("arxiv", {}), enr.get("openalex", {})
    links = {r["dir"]: r for r in (J(f"{ROOT}/_work/pdf_link_check.json") or {}).get("rows", [])}
    gen, gen_by_short = {}, {}
    for g in J(GEN_SRC) or []:
        gen_by_short[g["short"]] = g
        if g.get("arxiv_id"):
            gen[g["arxiv_id"]] = g

    def dblp_venue(d, title):
        """只认标题归一化后前 55 字符一致、且 venue 不是 CoRR 的命中。"""
        r = dblp_raw.get(d) or {}
        if "hits" not in r:
            return None
        nt = re.sub(r"[^a-z0-9]", "", (title or "").lower())
        for h in r["hits"]:
            v, y = h.get("venue"), h.get("year")
            if not v or not y or re.fullmatch(r"(CoRR|arXiv)", str(v).strip(), re.I):
                continue
            nh = re.sub(r"[^a-z0-9]", "", (h.get("title") or "").lower())
            if nh and nt and (nh[:55] == nt[:55] or nh == nt):
                return f"{v} {y}"
        return None

    out, audit = [], Counter()
    for d in sorted(os.listdir(f"{ROOT}/papers")):
        mp = f"{ROOT}/papers/{d}/meta.json"
        if not os.path.isdir(f"{ROOT}/papers/{d}") or not os.path.exists(mp):
            print(f"!! 跳过（无 meta.json）: {d}"); continue
        m = json.load(open(mp, encoding="utf-8"))
        aid = m.get("arxiv_id")
        a, o = (ax.get(aid) or {}) if aid else {}, (oa.get(aid) or {}) if aid else {}
        pub, imp, mf = m.get("publication") or {}, m.get("impact") or {}, man.get(d) or {}

        # ---- venue ----
        vsrc, venue = None, None
        for cand, tag in ((mf.get("venue_manifest"), "人工核验 manifest"),
                          (mf.get("venue_index4"), "人工核验 INDEX§4"),
                          (pub.get("venue"), "meta.publication"),
                          (a.get("journal_ref"), "arXiv journal_ref")):
            venue = clean_venue(cand)
            if venue:
                vsrc = tag; break
        if not venue:
            venue = venue_from_comment(a.get("comment"))
            vsrc = "arXiv comment（已接收）" if venue else None
        if not venue:
            venue = dblp_venue(d, m["title"])
            vsrc = "DBLP 标题检索" if venue else None
        if not venue and aid:
            # Semantic Scholar 只采信会议名，不采信年份：它的 year 是论文年份而非会议年份
            # （SDEdit venue=ICLR / year=2021，实际发在 ICLR 2022）。拼年份等于造事实。
            venue = (s2.get(aid) or {}).get("venue_short")
            vsrc = "Semantic Scholar（会议名已核，年份未核）" if venue else None
        if not venue:
            # image-generation-papers 第一期清单里写了 venue 的，带过来但降级标注：
            # 那个库的 docs/影响力口径.md 没有记录 venue 的核验来源，证据强度低于上面几档。
            g0 = gen.get(aid) or gen_by_short.get(m["short"]) or {}
            venue = clean_venue(g0.get("venue"))
            vsrc = "image-generation-papers 清单（该库未记录核验来源）" if venue else None
        if not venue:
            if not aid:
                venue, vsrc = (pub.get("venue") or "官方资料（无独立论文）"), "官方来源"
            else:
                venue, vsrc = "arXiv 预印本", "兜底：无接收证据"
        # S2 那一档只有会议名。不在 venue 里拼假年份，也不让读者以为年份核过了，
        # 落一个 venue_note，由 README / INDEX 渲染成「（年份未核）」。
        vnote = "年份未核" if vsrc and vsrc.startswith("Semantic Scholar") else None
        audit[f"venue<-{vsrc}"] += 1

        # ---- 机构：只认 PDF 首页 ----
        oc = org_c.get(d) or {}
        orgs = [ORG_FIX.get(x, x) for x in (oc.get("orgs_cn") or [])]
        if not orgs and m.get("org"):
            orgs = [m["org"]] if isinstance(m["org"], str) else list(m["org"])
            osrc = m.get("org_source") or "meta.json 自带"
        elif orgs:
            osrc = "PDF 首页作者块（模型抽取）" + ("，置信 low" if oc.get("confidence") == "low" else "")
        else:
            orgs, osrc = [], None
        audit["org 未核" if not orgs else "org 已核"] += 1

        # ---- task / type / line ----
        cc = cls_c.get(d) or {}
        task = m.get("task") or cc.get("task")
        typ = m.get("type") or cc.get("type")
        if typ == "技术报告":
            typ = "模型"          # 分类口径里「模型」= 发布模型/系统或厂商技术报告
        line = m.get("line") or cc.get("line")
        tsrc = "meta.json（人工指定）" if m.get("task") else "解读第1节分类"
        if not task:
            audit["!! 无 task"] += 1

        # ---- 引用量 ----
        cites, csrc = None, None
        if isinstance(mf.get("cites_manifest"), int):
            cites, csrc = mf["cites_manifest"], f"人工核验 manifest（{mf.get('src',[''])[0]}）"
        elif isinstance(imp.get("citation_count"), int):
            cites, csrc = imp["citation_count"], imp.get("provider") or "meta.impact"
        elif isinstance(o.get("cites"), int):
            cites, csrc = o["cites"], "OpenAlex"

        note = f"{ROOT}/papers/{d}/解读.md"
        body = open(note, encoding="utf-8").read() if os.path.exists(note) else ""
        g = gen.get(aid) or {}

        out.append({
            "short": m["short"], "dir": d, "date": m.get("date"),
            "arxiv_id": aid, "title": m["title"], "url": m["url"],
            "pdf": OVERRIDES.get(d) or pdf_url(m, d),
            "venue": venue, "venue_source": vsrc, "venue_note": vnote,
            "org": orgs, "org_source": osrc,
            "task": task, "type": typ, "line": line, "tag_source": tsrc,
            "cn_chars": CJK(body) or None,
            "sections": len(re.findall(r"^## \d+\.", body, re.M)) or None,
            "spec": ("v2" if (m.get("spec") or "").startswith("v2")
                     else ("短版" if d in batch2 else "v1-11节")),
            "cites": cites, "cites_source": csrc,
            "upvotes": g.get("upvotes"), "hub": g.get("hub"),
            "gen_list": g.get("group"),          # 入选 image-generation 第一期的组别
            "why": g.get("why"),
            "link_status": (links.get(d) or {}).get("status"),
            "paper_pdf": m.get("paper_pdf", os.path.exists(f"{ROOT}/papers/{d}/paper.pdf")),
            "checked_at": m.get("checked_at") or CHECKED,
            "note": m.get("note"),
        })

    out.sort(key=lambda p: (p["date"] or "9999/99/99", p["short"]))
    json.dump(out, open(f"{ROOT}/scripts/papers.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # 只回写 cn_chars——它是从 解读.md 当场数出来的实测值。
    #
    # 不回写 venue / task / type / line / impact：这些字段是本脚本"算出来"的，
    # 而算的时候又要读 meta.json 的 publication.venue 和 task 作为高优先来源。
    # 写回去下一轮就会把自己的输出当成一手证据，来源标注全部塌成 "meta.publication"。
    # papers.json 是元数据唯一事实来源（见 ../CLAUDE.md），meta.json 只保留
    # 单篇的一手记录与核验痕迹，两者分工不能反过来。
    synced = 0
    for p in out:
        mp = f"{ROOT}/papers/{p['dir']}/meta.json"
        m = json.load(open(mp, encoding="utf-8"))
        if p["cn_chars"] is not None and m.get("cn_chars") != p["cn_chars"]:
            m["cn_chars"] = p["cn_chars"]
            json.dump(m, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            synced += 1
    print(f"papers.json：{len(out)} 条；回写 meta.json {synced} 份\n")
    for k, v in sorted(audit.items()):
        print(f"  {v:4d}  {k}")
    print()
    for f in ("date", "arxiv_id", "pdf", "venue", "org", "task", "type", "line", "cn_chars"):
        miss = [p["short"] for p in out if not p[f]]
        print(f"  {f:10s} 缺 {len(miss):3d}" + (f"  {miss[:10]}" if miss else ""))
    print("\n  task 分布:", Counter(tuple(p["task"] or []) for p in out).most_common())
    print("  type 分布:", Counter(p["type"] for p in out).most_common())
    print(f"  line 条数: {len(set(p['line'] for p in out if p['line']))}")
    bad = [p["short"] for p in out if p["cn_chars"] and not 300 <= p["cn_chars"] <= 9000]
    print("  字数离群:", bad or "无")


if __name__ == "__main__":
    main()
