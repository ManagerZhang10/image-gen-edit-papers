#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给每个未溯源数字定性，把需要人工看原文的那部分单独择出来。

分类（互斥，按顺序判定）：
  自述推算  解读自己就写了"推断/推算/估算/换算/可推出"，不是在转述原文数字
  外部知识  数字属于底座模型/硬件的常识（SD 1.5、A100 40GB、512×512 之类）
  精度差异  原文有个数与它相差 <0.5%，多半是解读四舍五入或 PDF 抽取掉精度
  抽取粘连  数字串在原文的纯数字流里作为子串出现，是 PDF 抽表格时被粘住了
  待核      以上都不是——必须翻原文
"""
import os, re, io, sys, json, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_work"))
from factcheck import audit, strip_noise, nums_of, normalize, normalize_light  # noqa: E402

DERIVE = re.compile(r"推断|推算|估算|换算|可推出|反推|折合|约等于|粗算|自行计算|论文未|未披露|未明确|未给出")
EXTERN = re.compile(r"SD ?1\.[45]|Stable Diffusion (?:v)?[12]|A100|H100|V100|RTX|TPU|CUDA|"
                    r"CLIP ViT|ViT-[BLH]|DDIM|DDPM|ImageNet|COCO|batch size|显存|GB")

rows, out = [], []
for _r, _nm, _nc, d, miss in audit():
    if not miss: continue
    ax = json.load(open(os.path.join(ROOT, "papers", d, "meta.json"), encoding="utf-8")).get("arxiv_id") or d
    raw = io.open(os.path.join(ROOT, "_work", "txt_%s.txt" % ax),
                  encoding="utf-8", errors="replace").read()
    srcn = sorted({float(x) for x in (nums_of(raw) | nums_of(normalize_light(raw))
                                     | nums_of(normalize(raw)))})
    digits = re.sub(r"[^\d.]", "", raw)
    clean = strip_noise(io.open(os.path.join(ROOT, "papers", d, "解读.md"),
                                encoding="utf-8").read())
    sents = re.split(r"(?<=[。！？\n])", clean)
    for n in sorted(miss, key=lambda x: -float(x)):
        loose = ",?".join(re.escape(c) for c in n)
        pat = re.compile(r"(?<![\w.\-])%s(?![\d])" % loose)
        hit = [s.strip() for s in sents if pat.search(s)]
        ctx = hit[0] if hit else ""
        v = float(n)
        if DERIVE.search(ctx):                                   cls = "自述推算"
        elif EXTERN.search(ctx):                                 cls = "外部知识"
        elif any(abs(x - v) <= max(abs(v) * 0.005, 0.05) for x in srcn): cls = "精度差异"
        elif n in digits:                                        cls = "抽取粘连"
        else:                                                    cls = "待核"
        out.append((cls, d, n, ctx[:200] or "(定位不到)"))

c = collections.Counter(r[0] for r in out)
order = ["待核", "精度差异", "抽取粘连", "自述推算", "外部知识"]
print("合计 %d 条：" % len(out))
for k in order: print("   %-6s %3d" % (k, c[k]))
with io.open(os.path.join(ROOT, "_work", "unsourced_triage.txt"), "w", encoding="utf-8") as f:
    for k in order:
        f.write("\n########## %s（%d 条）##########\n" % (k, c[k]))
        for cls, d, n, ctx in sorted(out):
            if cls == k: f.write("%-30s %-10s %s\n" % (d, n, ctx))
print("→ _work/unsourced_triage.txt")
