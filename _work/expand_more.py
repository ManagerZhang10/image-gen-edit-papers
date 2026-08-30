#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对偏短但结构完整的解读做强化扩写：逐节点名，最多两轮，只补论文里已有的细节。"""
import os, re, sys, json, time
ROOT = "/Users/yuzhang/ZhangYu/image_edit_paper"
sys.path.insert(0, ROOT + "/_work")
from pipeline import deepseek, validate, validate_struct, cn_len, PROMPT, extract, fetch_pdf

TARGETS = {"1":350,"2":550,"3":500,"4":850,"5":700,"6":650,"7":500,"8":950,"9":500,"10":750,"11":700}

def sec_lens(md):
    out = {}
    parts = re.split(r"\n(?=## (\d{1,2})\.)", md)
    for i, p in enumerate(parts):
        m = re.match(r"## (\d{1,2})\.", p)
        if m: out[m.group(1)] = cn_len(p)
    return out

def clean(md):
    md = md.strip()
    if md.startswith("```"):
        md = re.sub(r"^```[a-z]*\n", "", md); md = re.sub(r"\n```$", "", md)
    return md.strip()

def run(aid, short, date, title):
    folder = os.path.join(ROOT, f"{date[:7].replace('/','-')}_{short}")
    out = os.path.join(folder, "解读.md")
    txt = os.path.join(ROOT, "_work", f"txt_{aid}.txt")
    if not os.path.exists(txt):
        pdf = os.path.join(folder, "paper.pdf")
        if not fetch_pdf(aid, pdf): print(f"[FAIL] {short} 无 PDF"); return 1
        extract(pdf, txt)
    body = open(txt, encoding="utf-8").read()[:160000]
    base = f"论文简称：{short}\n标题：{title}\narXiv：{aid}\n\n<paper>\n{body}\n</paper>\n"

    cur = open(out, encoding="utf-8").read() if os.path.exists(out) else None
    if cur is None or validate_struct(cur)[0]:
        md, _ = deepseek(PROMPT + "\n\n【务必写足篇幅】正文中文字符必须达到 7000~8500，"
                         "每节按规范给定字数写满，第 8 节证据表至少 5 行。",
                         base + f"请输出《{short}》的中文深读笔记。", temp=0.4)
        cur = clean(md)
        if not validate(cur)[0]:
            open(out, "w", encoding="utf-8").write(cur + "\n"); print(f"[OK] {short} {cn_len(cur)}字 (重生成)"); return 0

    for rnd in range(2):
        n = cn_len(cur)
        if n >= 6500: break
        sl = sec_lens(cur)
        thin = sorted(((TARGETS[k] - sl.get(k, 0), k) for k in TARGETS), reverse=True)[:6]
        want = "；".join(f"第 {k} 节现{sl.get(k,0)}字→目标{TARGETS[k]}字" for _, k in thin)
        sysm = (PROMPT + "\n\n【本轮是扩写，不是重写】保持草稿的结构、结论、全部事实与章节顺序不变，"
                "只把内容写厚：补充论文中已有但草稿没展开的实现细节、超参数、数据规模、消融设置、"
                "失败模式，并补上 § / Table / Figure / Equation 证据锚点。"
                "严禁引入草稿和论文里都没有的新事实；不要写论文发表后的评价。\n"
                f"当前全文 {n} 字，需扩到 6800~8500。重点补足这些偏薄的节：{want}。\n"
                "输出完整的 11 节 Markdown 全文，结尾单独一行 <!-- COMPLETE -->。")
        try:
            md2, _ = deepseek(sysm, base + "\n以下是需要扩写的草稿：\n\n<draft>\n" + cur + "\n</draft>", temp=0.45)
        except Exception as ex:
            print(f"    [{short}] 扩写异常 {ex}"); time.sleep(20); continue
        md2 = clean(md2)
        if not validate_struct(md2)[0] and cn_len(md2) > n:
            cur = md2
    n = cn_len(cur)
    open(out, "w", encoding="utf-8").write(cur + "\n")
    mt = os.path.join(folder, "meta.json")
    meta = json.load(open(mt, encoding="utf-8")) if os.path.exists(mt) else {}
    meta.update({"arxiv_id": aid, "short": short, "date": date, "title": title,
                 "url": f"https://arxiv.org/abs/{aid}", "cn_chars": n,
                 "note": "达标" if n >= 6500 else f"结构完整，{n}字，低于 6500"})
    json.dump(meta, open(mt, "w"), ensure_ascii=False, indent=2)
    print(f"[{'OK' if n>=6500 else 'SHORT'}] {short} {n}字")
    return 0

if __name__ == "__main__":
    aid, short, date, title = sys.argv[1].split("|", 3)
    sys.exit(run(aid.strip(), short.strip(), date.strip(), title.strip()))
