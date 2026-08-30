#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描所有已生成的解读，把不达标的挑出来交回 pipeline 重生成"""
import os, re, sys, subprocess, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")
sys.path.insert(0, os.path.join(ROOT, "_work"))
from pipeline import validate, cn_len

bad = []
for d in sorted(os.listdir(PAPERS)):
    fd = os.path.join(PAPERS, d)
    if not (os.path.isdir(fd) and re.match(r"^20\d\d-\d\d_", d)): continue
    mdp, mtp = os.path.join(fd, "解读.md"), os.path.join(fd, "meta.json")
    if not os.path.exists(mdp): bad.append((d, "缺解读")); continue
    errs, n = validate(open(mdp, encoding="utf-8").read())
    if errs: bad.append((d, f"{errs[:2]} ({n}字)"))
for d, why in bad: print(f"{d}\t{why}")
print(f"--- 需修复 {len(bad)} 篇 ---")
