#!/usr/bin/env python3
"""一次性迁移：187 个 papers/*/meta.json → scripts/papers.json。

papers.json 从此是元数据唯一事实来源，README 由它渲染。
本脚本只负责把已有事实搬过来 + 从解读正文实测字数与节数，
不发明任何新事实；venue / org / task / type 由后续 enrich 脚本补。
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, f"{ROOT}/scripts")
from pdf_sources import pdf_url, OVERRIDES

CJK = lambda t: sum(1 for ch in t if "一" <= ch <= "鿿")


def load_link_check():
    p = f"{ROOT}/_work/pdf_link_check.json"
    if not os.path.exists(p):
        return {}
    d = json.load(open(p, encoding="utf-8"))
    return {r["dir"]: r for r in d.get("rows", [])}


def main():
    links = load_link_check()
    out = []
    for d in sorted(os.listdir(f"{ROOT}/papers")):
        mp = f"{ROOT}/papers/{d}/meta.json"
        if not os.path.exists(mp):
            print(f"!! 缺 meta.json: {d}")
            continue
        m = json.load(open(mp, encoding="utf-8"))

        # 从解读正文实测：字数 + 二级标题节数（判定写作规范代次）
        note = f"{ROOT}/papers/{d}/解读.md"
        cn, secs = None, None
        if os.path.exists(note):
            body = open(note, encoding="utf-8").read()
            cn = CJK(body)
            secs = len(re.findall(r"^## ", body, re.M))

        pub = m.get("publication") or {}
        imp = m.get("impact") or {}
        lc = links.get(d) or {}

        out.append({
            "short": m["short"],
            "dir": d,
            "date": m.get("date"),
            "first_public": pub.get("first_public"),
            "arxiv_id": m.get("arxiv_id"),
            "title": m["title"],
            "url": m["url"],
            "pdf": OVERRIDES.get(d) or pdf_url(m, d),
            "venue": pub.get("venue"),
            "venue_type": pub.get("venue_type") or m.get("source_type"),
            "org": None,               # enrich 补
            "org_source": None,
            "task": None,              # 打标补
            "type": None,
            "line": None,
            "cn_chars": cn,
            "meta_cn_chars": m.get("cn_chars"),
            "sections": secs,
            "spec": m.get("spec"),
            "attempts": m.get("attempts"),
            "cites": imp.get("citation_count"),
            "cites_provider": imp.get("provider"),
            "checked_at": m.get("checked_at") or imp.get("checked_at"),
            "link_status": lc.get("status"),
            "paper_pdf": m.get("paper_pdf", True),
            "note": m.get("note"),
        })

    out.sort(key=lambda p: (p["date"] or "9999/99/99", p["short"]))
    json.dump(out, open(f"{ROOT}/scripts/papers.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # 体检报告
    n = len(out)
    print(f"papers.json 已生成：{n} 条")
    for f in ("date", "arxiv_id", "pdf", "venue", "cn_chars", "cites", "link_status"):
        miss = [p["short"] for p in out if not p[f]]
        print(f"  {f:12s} 缺 {len(miss):3d}/{n}" + (f"  {miss[:6]}" if miss and len(miss) <= 8 else ""))
    drift = [(p["short"], p["cn_chars"], p["meta_cn_chars"]) for p in out
             if p["cn_chars"] and p["meta_cn_chars"] and abs(p["cn_chars"] - p["meta_cn_chars"]) > 2]
    print(f"  meta.json 字数与实测不一致：{len(drift)} 条 {drift[:5]}")
    from collections import Counter
    print("  节数分布:", dict(sorted(Counter(p["sections"] for p in out).items(),
                                     key=lambda x: (x[0] is None, x[0]))))


if __name__ == "__main__":
    main()
