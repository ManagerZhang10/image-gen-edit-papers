#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 factcheck.py 标出的每个未溯源数字，连同它在解读里的那句话导出，供逐条复核。"""
import os, re, io, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_work"))
from factcheck import audit, strip_noise  # noqa: E402

out = []
for _rate, _nm, _nc, d, miss in audit():
    if not miss: continue
    clean = strip_noise(io.open(os.path.join(ROOT, "papers", d, "解读.md"),
                                encoding="utf-8").read())
    sents = re.split(r"(?<=[。！？\n])", clean)
    for n in sorted(miss, key=lambda x: -float(x)):
        # md 里可能写成千分位形式（2,998），而 miss 里是归一化后的 2998，
        # 所以定位时允许数字之间夹逗号
        loose = ",?".join(re.escape(ch) for ch in n)
        pat = re.compile(r"(?<![\w.\-])%s(?![\d])" % loose)
        hit = [s.strip() for s in sents if pat.search(s)]
        out.append((d, n, hit[0][:230] if hit else "(定位不到)"))

out.sort()
p = os.path.join(ROOT, "_work", "unsourced_numbers.txt")
io.open(p, "w", encoding="utf-8").write("\n".join("%-30s %-10s %s" % r for r in out) + "\n")
print("导出 %d 条 → _work/unsourced_numbers.txt" % len(out))
c = collections.Counter(r[0] for r in out)
print("涉及 %d 篇；定位不到的 %d 条" % (len(c), sum(1 for r in out if r[2] == "(定位不到)")))
for d, n in c.most_common(10): print("   %-32s %d" % (d, n))
