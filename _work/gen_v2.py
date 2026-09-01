#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新增篇目的生成管线（v2 规范：8 节 / 3000～5000 汉字）。

和 pipeline.py 的关系：pipeline.py 记录的是库里 186 篇按旧规范（11 节 / 6500～8500）
产出的过程，不改动。2026-09 起 docs/prompt.md 换成 v2 规范，新增篇目走这个脚本。

用法：
    LLM_ENV_FILE=~/ZhangYu/self_learning/BaseModel/.env \
    python3 _work/gen_v2.py <papers 下的目录名>
目录里要先有 paper.pdf；meta.json 若已存在则复用其 arxiv_id/title/date/url。
"""
import json, os, re, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "_work")
PROMPT = open(os.path.join(ROOT, "docs", "prompt.md"), encoding="utf-8").read()

LO, HI = 3000, 5000
HEADS = ["## 1. 30 秒定位", "## 2. 为什么这篇论文会出现", "## 3. 方法全景：先看数据流",
         "## 4. 核心公式与直觉", "## 5. 训练与推理怎么跑", "## 6. 实验和消融证明了什么",
         "## 7. 与前作怎么选", "## 8. 工程判断与收束"]


def load_env(p):
    e = {}
    for ln in open(os.path.expanduser(p), encoding="utf-8"):
        ln = ln.strip()
        if ln and not ln.startswith("#") and "=" in ln:
            k, v = ln.split("=", 1)
            e[k] = v.strip().strip('"').strip("'")
    return e


ENV = load_env(os.environ.get("LLM_ENV_FILE", "~/ZhangYu/self_learning/BaseModel/.env"))


def log(*a):
    print(*a, flush=True)


def extract(pdf, dst):
    """pypdf 抽正文；去掉孤立代理项和过长的参考文献块。"""
    if os.path.exists(dst) and os.path.getsize(dst) > 8000:
        return open(dst, encoding="utf-8").read()
    from pypdf import PdfReader
    rd = PdfReader(pdf)
    pages = []
    for p in rd.pages:
        try:
            pages.append(p.extract_text() or "")
        except Exception:
            pages.append("")
    t = "\n".join(pages)
    t = re.sub(r"[\ud800-\udfff]", "", t)
    # 控制字符（含 NUL）会让 grep/file 把抽出的 txt 当二进制，后续排查很难受
    t = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", t)
    t = re.sub(r"[ \t]{3,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    if len(t) > 130000:
        m = list(re.finditer(r"\n\s*(References|REFERENCES|Bibliography)\s*\n", t))
        if m:
            s = m[0].end()
            nxt = re.search(r"\n\s*(A(ppendix)?\.?\s|Appendix|Supplementary|APPENDIX)", t[s:])
            e = s + nxt.start() if nxt else min(len(t), s + 60000)
            t = t[:s] + "\n[参考文献块已省略]\n" + t[e:]
    open(dst, "w", encoding="utf-8").write(t)
    return t


def deepseek(sysmsg, usermsg, max_tokens=16000, temp=0.35):
    """v4-pro 是 reasoning 模型，正文取 content，reasoning_content 丢掉。"""
    body = json.dumps({
        "model": ENV.get("DEEPSEEK_V4_PRO_MODEL", "deepseek-v4-pro"),
        "messages": [{"role": "system", "content": sysmsg},
                     {"role": "user", "content": usermsg}],
        "max_tokens": max_tokens, "temperature": temp}).encode()
    req = urllib.request.Request(
        ENV["DEEPSEEK_BASE_URL"].rstrip("/") + "/chat/completions", data=body,
        headers={"Authorization": "Bearer " + ENV["DEEPSEEK_API_KEY"],
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=1800) as r:
        d = json.loads(r.read())
    return d["choices"][0]["message"]["content"] or ""


def cn_len(s):
    return len(re.findall(r"[一-鿿]", s))


def validate(md):
    errs = []
    if not md.lstrip().startswith("# 大白话深读"):
        errs.append("缺少 H1 大白话深读")
    for h in HEADS:
        if h not in md:
            errs.append("缺章节 " + h)
    if "## 9." in md or "## 10." in md:
        errs.append("多出规范外的章节")
    if "<!-- COMPLETE -->" not in md[-400:]:
        errs.append("结尾缺 COMPLETE 标记")
    n = cn_len(md)
    if n < LO:
        errs.append(f"中文字符过少 {n}，需 {LO}~{HI}")
    if n > HI:
        errs.append(f"中文字符过多 {n}，需 {LO}~{HI}")
    return errs, n


def clean(md):
    md = md.strip()
    if md.startswith("```"):
        md = re.sub(r"^```[a-z]*\n", "", md)
        md = re.sub(r"\n```$", "", md)
    return md.strip()


def run(dirname):
    folder = os.path.join(ROOT, "papers", dirname)
    pdf = os.path.join(folder, "paper.pdf")
    out = os.path.join(folder, "解读.md")
    mpath = os.path.join(folder, "meta.json")
    meta = json.load(open(mpath, encoding="utf-8")) if os.path.exists(mpath) else {}
    short = meta.get("short") or dirname.split("_", 1)[1]
    txt = os.path.join(WORK, f"txt_{dirname}.txt")

    body = extract(pdf, txt)
    if len(body) < 6000:
        log(f"[FAIL] {short} 抽取正文过短 {len(body)}")
        return 1
    body = body[:160000]

    user = (f"论文简称：{short}\n论文标题：{meta.get('title','')}\n"
            f"来源：{meta.get('url','')}（{meta.get('date','')}）\n\n"
            "以下是该论文的完整正文（PDF 抽取，含排版噪声，公式符号可能丢失）：\n\n"
            f"<paper>\n{body}\n</paper>\n\n"
            f"请严格按系统提示的规范，输出《{short}》的中文深读笔记。"
            f"正文汉字数必须落在 {LO}~{HI} 之间，8 节一节不能少，第 6 节证据表至少 4 行。")

    last = None
    for att in range(4):
        sysmsg = PROMPT
        if last:
            sysmsg += ("\n\n【上一次输出未通过校验，问题如下，请修正后重新完整输出】\n"
                       + "\n".join("- " + e for e in last)
                       + f"\n必须输出全部 8 个二级标题，正文 {LO}~{HI} 汉字，"
                         "结尾单独一行 <!-- COMPLETE -->。")
        try:
            md = clean(deepseek(sysmsg, user, temp=0.35 + 0.05 * att))
        except Exception as ex:
            log(f"    [{short}] API 第{att+1}次异常: {ex}")
            time.sleep(10 + 10 * att)
            continue
        errs, n = validate(md)
        if not errs:
            open(out, "w", encoding="utf-8").write(md + "\n")
            meta.update({"cn_chars": n, "attempts": att + 1,
                         "note": meta.get("note", ""), "spec": "v2-8节-3000~5000"})
            json.dump(meta, open(mpath, "w"), ensure_ascii=False, indent=2)
            log(f"[OK] {short} {n}字 (第{att+1}次)")
            return 0
        last = errs
        log(f"    [{short}] 第{att+1}次未过: {errs[:3]}（{n}字）")
    log(f"[FAIL] {short} 四次未达标")
    return 1


if __name__ == "__main__":
    sys.exit(run(sys.argv[1]))
