#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给还没有抽取文本的目录补抽 PDF 正文。

文件名是 _work/txt_<key>.txt，key 优先取 meta.json 的 arxiv_id；
Inter-Edit 这种只有 CVF proceedings 版、没有 arXiv ID 的，退回用目录名，
否则它有 paper.pdf 也进不了数字溯源。

抽取口径与 _work/pipeline.py 的 extract() 一致（pypdf，去孤立代理项、压空白），
但不砍参考文献——数字溯源要用全文，砍掉会让参考文献里的数字变成"未溯源"。
"""
import io, os, re, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from pypdf import PdfReader

done = []
for d in sorted(os.listdir(os.path.join(ROOT, "papers"))):
    fd = os.path.join(ROOT, "papers", d)
    if not os.path.isdir(fd): continue
    ax = json.load(io.open(os.path.join(fd, "meta.json"), encoding="utf-8")).get("arxiv_id")
    pdf = os.path.join(fd, "paper.pdf")
    if not os.path.exists(pdf): continue
    ax = ax or d                     # 没有 arXiv ID 就用目录名当 key
    dst = os.path.join(ROOT, "_work", "txt_%s.txt" % ax)
    if os.path.exists(dst) and os.path.getsize(dst) > 8000: continue
    pages = []
    for p in PdfReader(pdf).pages:
        try: pages.append(p.extract_text() or "")
        except Exception: pages.append("")
    t = "\n".join(pages)
    t = re.sub(r"[\ud800-\udfff]", "", t)
    t = re.sub(r"[ \t]{3,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    io.open(dst, "w", encoding="utf-8").write(t)
    done.append((d, ax, len(t)))
for d, ax, n in done: print("  %-32s txt_%s.txt  %s 字符" % (d, ax, format(n, ",")))
print("补抽 %d 份" % len(done))
