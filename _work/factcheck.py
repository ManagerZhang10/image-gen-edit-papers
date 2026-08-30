#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数字溯源检查：解读里出现的数字断言，是否能在论文抽取文本中找到。

不做语义判断，只标出"原文里根本没有这个数"的高风险条目，供人工复核。
判为未溯源不等于写错——见 _work/unsourced_review.md 里对残留项的分类。
"""
import os, re, json, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")

# 千分位分组的数（1,024）整体取；其余按纯数字串取。
# 不能写成 [\d,]* —— 那会把"10,20,30,40,50"这种无空格逗号列表粘成 1020304050，
# 制造出原文里当然找不到的假数字（2026-08-30 修，此前 6 篇被误报）。
NUM = re.compile(r"(?<![\w.\-])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)")
CN_UNIT = re.compile(r"(\d+(?:\.\d+)?)\s*(万|亿)")


def normalize_light(t):
    """只修 pypdf 拆散的小数点和千分位："66 .4%" → 66.4%，"1 ,024" → 1,024。"""
    t = re.sub(r"(\d)\s+\.\s*(\d)", r"\1.\2", t)
    return re.sub(r"(\d)\s+,\s*(\d)", r"\1,\2", t)


def normalize(t):
    """再把表格里被空格拆开的整数粘回去。
    ⚠️ 这一步会顺手把相邻两个数也粘在一起（"1.13 79.05" → "1.1379.05"），
    所以调用方必须同时取 raw / light / full 三版的并集，不能只用这一版。"""
    return re.sub(r"(\d)\s+(\d)", r"\1\2", normalize_light(t))


def nums_of(text):
    out = set()
    for m in NUM.finditer(text):
        v = m.group(1).replace(",", "")
        if v.startswith("0") and len(v) > 1 and "." not in v: continue
        out.add(v)
        if "." in v: out.add(v.split(".")[0])
    return out


def cn_unit_forms(md):
    """解读写"1600 万"、"1.9 亿"，原文写 16M / 190 million / 16000000。
    把中文计数单位展开成原文可能的几种写法，避免把单位换算误判成编造。"""
    extra = {}
    for m in CN_UNIT.finditer(md):
        v, u = float(m.group(1)), m.group(2)
        full = v * (1e4 if u == "万" else 1e8)
        forms = {full, full / 1e3, full / 1e6, full / 1e9}
        s = {("%d" % f) if f == int(f) else ("%g" % f) for f in forms}
        extra[m.group(1)] = s
    return extra


def strip_noise(md):
    md = re.sub(r"```.*?```", " ", md, flags=re.S)               # ASCII 图/代码块
    md = re.sub(r"\$[^$]*\$", " ", md)                            # 行内公式
    # URL、DOI、外部库 ID 里的数字是标识符不是量，溯源无从谈起
    md = re.sub(r"https?://\S+", " ", md)
    md = re.sub(r"\b10\.\d{4,}/\S+", " ", md)
    md = re.sub(r"^\s*[-*]\s*\*\*(DOI|页码|引用来源|备注|OpenAlex|Semantic Scholar)\*\*.*$",
                " ", md, flags=re.M)
    md = re.sub(r"HTTP\s*\d{3}", " ", md)
    md = re.sub(r"^#{1,6}\s*\d+[\.、].*$", " ", md, flags=re.M)   # 章节号标题
    md = re.sub(r"\b(19|20)\d\d\b", " ", md)                      # 年份
    md = re.sub(r"第\s*\d+\s*[节章条]", " ", md)
    return md


def audit():
    rows = []
    for d in sorted(os.listdir(PAPERS)):
        fd = os.path.join(PAPERS, d)
        mt, mdp = os.path.join(fd, "meta.json"), os.path.join(fd, "解读.md")
        if not (os.path.isdir(fd) and os.path.exists(mt) and os.path.exists(mdp)): continue
        # key 与 extract_missing_txt.py 一致：优先 arxiv_id，没有就用目录名
        ax = json.load(open(mt, encoding="utf-8")).get("arxiv_id") or d
        src_p = os.path.join(ROOT, "_work", "txt_%s.txt" % ax)
        if not os.path.exists(src_p): continue
        raw = open(src_p, encoding="utf-8", errors="replace").read()
        src = nums_of(raw) | nums_of(normalize_light(raw)) | nums_of(normalize(raw))
        md_raw = open(mdp, encoding="utf-8").read()
        clean = strip_noise(md_raw)
        units = cn_unit_forms(clean)
        cand = {c for c in nums_of(clean) if len(c) >= 2 and float(c) >= 2}
        miss = sorted((c for c in cand - src if not (units.get(c, set()) & src)),
                      key=lambda x: -len(x))
        rows.append((len(miss) / max(1, len(cand)), len(miss), len(cand), d, miss))
    return sorted(rows, reverse=True)


if __name__ == "__main__":
    rows = audit()
    print("%8s %12s  论文" % ("未溯源率", "未溯源/总数"))
    for rate, nm, nc, d, miss in rows:
        flag = "⚠️ " if rate > 0.25 and nm >= 5 else "   "
        print("%s%5.1f%%  %3d/%3d   %s" % (flag, rate * 100, nm, nc, d))
        if flag.strip(): print("            可疑数字: %s" % miss[:12])
    tot_m, tot_c = sum(r[1] for r in rows), sum(r[2] for r in rows)
    print("\n合计 %d 篇；数字总数 %d，未在原文出现 %d（%.1f%%）"
          % (len(rows), tot_c, tot_m, tot_m / max(1, tot_c) * 100))
