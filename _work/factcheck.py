#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数字溯源检查：解读里出现的数字断言，是否能在论文抽取文本中找到。
不做语义判断，只标出'原文里根本没有这个数'的高风险条目，供人工复核。"""
import os, re, json, sys
ROOT = "/Users/yuzhang/ZhangYu/image_edit_paper"
SEC = re.compile(r"^(#|\|?\s*)?\d{1,2}\.\d?$")

def normalize(t):
    # pypdf 常把 "66.4%" 抽成 "66 .4%"、"1,024" 抽成 "1 ,024"，先粘回去
    t = re.sub(r"(\d)\s+\.\s*(\d)", r"\1.\2", t)
    t = re.sub(r"(\d)\s+,\s*(\d)", r"\1,\2", t)
    t = re.sub(r"(\d)\s+(\d)", r"\1\2", t)
    return t

def nums_of(text, md=False):
    out = set()
    for m in re.finditer(r"(?<![\w.\-])(\d[\d,]*(?:\.\d+)?)", text):
        v = m.group(1).replace(",", "")
        if v.startswith("0") and len(v) > 1 and "." not in v: continue
        out.add(v)
        if "." in v: out.add(v.split(".")[0])
    return out

def strip_noise(md):
    md = re.sub(r"```.*?```", " ", md, flags=re.S)          # ASCII 图/代码块
    md = re.sub(r"\$[^$]*\$", " ", md)                       # 行内公式
    md = re.sub(r"^#{1,6}\s*\d+[\.、].*$", " ", md, flags=re.M)  # 章节号标题
    md = re.sub(r"\b(19|20)\d\d\b", " ", md)                 # 年份
    md = re.sub(r"第\s*\d+\s*[节章条]", " ", md)
    return md

rows = []
for d in sorted(os.listdir(ROOT)):
    fd = os.path.join(ROOT, d)
    mt, mdp = os.path.join(fd, "meta.json"), os.path.join(fd, "解读.md")
    if not (os.path.isdir(fd) and os.path.exists(mt) and os.path.exists(mdp)): continue
    meta = json.load(open(mt, encoding="utf-8"))
    src_p = os.path.join(ROOT, "_work", f"txt_{meta['arxiv_id']}.txt")
    if not os.path.exists(src_p): continue
    raw = open(src_p, encoding="utf-8").read()
    src = nums_of(raw) | nums_of(normalize(raw))
    md_raw = open(mdp, encoding="utf-8").read()
    cand = nums_of(strip_noise(md_raw))
    cand = {c for c in cand if len(c) >= 2 and float(c) >= 2}
    miss = sorted(cand - src, key=lambda x: -len(x))
    rate = len(miss) / max(1, len(cand))
    rows.append((rate, len(miss), len(cand), d, miss[:12]))
rows.sort(reverse=True)
print(f"{'未溯源率':>8} {'未溯源/总数':>12}  论文")
for rate, nm, nc, d, miss in rows:
    flag = "⚠️ " if rate > 0.25 and nm >= 5 else "   "
    print(f"{flag}{rate*100:5.1f}%  {nm:3d}/{nc:3d}   {d}")
    if flag.strip(): print(f"            可疑数字: {miss}")
tot_m = sum(r[1] for r in rows); tot_c = sum(r[2] for r in rows)
print(f"\n合计 {len(rows)} 篇；数字总数 {tot_c}，未在原文出现 {tot_m}（{tot_m/max(1,tot_c)*100:.1f}%）")
