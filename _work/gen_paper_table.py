#!/usr/bin/env python3
"""由 meta.json + _work/pdf_link_check.json 生成 README 附二的全量论文表。

只有核验状态 OK 的条目拿到干净的 PDF 直链；渲染版本对不上的加 ⚠️ 并在脚注
说明；没有独立论文的给官方来源。任何未核过的东西不会以"PDF"的名义出现。
"""
import collections
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from pdf_sources import RENDITION_DIFFERS  # noqa: E402

chk = json.load(open(os.path.join(ROOT, "_work", "pdf_link_check.json")))
by_dir = {r["dir"]: r for r in chk["rows"]}

dirs = sorted(d for d in os.listdir(PAPERS)
              if os.path.isdir(os.path.join(PAPERS, d)) and d[0].isdigit())

# meta.json 里这条已 301，用解析后的终点
URL_FIX = {"https://docs.x.ai/docs/models": "https://docs.x.ai/developers/models"}

rows, stat = [], collections.Counter()
for d in dirs:
    m = json.load(open(os.path.join(PAPERS, d, "meta.json"), encoding="utf-8"))
    r = by_dir.get(d, {})
    st = r.get("status", "MISSING")
    date = (m.get("date") or "").replace("/", "-")
    short = m.get("short") or d
    title = (m.get("title") or "").replace("|", r"\|").strip()
    # 字数当场从 解读.md 数（口径同 meta.json 的 cn_chars：U+4E00–U+9FFF），
    # 不读 meta.json，这样即使忘了跑 _work/sync_cnchars.py 也不会出错
    body = io.open(os.path.join(PAPERS, d, "解读.md"), encoding="utf-8").read()
    cn = len(re.findall(r"[\u4e00-\u9fff]", body))
    # Grok-Aurora 的 meta.json 没有 date，退回目录名里的年月
    date = date or d.split("_")[0]
    if st == "NO_PAPER":
        u = URL_FIX.get(r.get("fallback") or "", r.get("fallback") or "")
        link = f"[官方来源]({u})"
        stat["官方来源"] += 1
    elif st == "OK" and d not in RENDITION_DIFFERS:
        link = f"[PDF]({r['url']})"
        stat["PDF 已核验"] += 1
    elif d in RENDITION_DIFFERS:
        link = f"[PDF]({r['url']}) ⚠️"
        stat["PDF 版本存疑"] += 1
    else:
        link = f"⚠️ 未核过（{st}）"
        stat["未核过"] += 1
    rows.append(
        f"| {date} | [{short}](papers/{d}/解读.md) | {title} | {link} | {cn} |")

out = os.path.join(ROOT, "_work", "paper_table.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("| 时间 | 简称（→ 解读） | 论文标题 | 原文 | 解读字数 |\n")
    f.write("| --- | --- | --- | --- | ---: |\n")
    f.write("\n".join(rows) + "\n")
print("行数", len(rows), dict(stat))
print("写入", os.path.relpath(out, ROOT))
