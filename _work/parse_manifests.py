#!/usr/bin/env python3
"""把 docs/review/ 四份人工核验 manifest 里的 venue 与引用量解析出来。

这四份是 2026-08-29 那轮逐项核验的产物，是本库 venue 的最高优先来源——
比 arXiv comment 和 OpenAlex 都可靠，因为是人对着一手页面核的。
四份表列布局各不相同，所以按文件写死列号，不做通用推断。
"""
import json, re, os

# 文件 -> (目录所在列, venue 所在列, 引用量所在列, 表头判别词)
LAYOUT = {
    "bench_early_manifest.md":   (1, 3, 6, "正式 venue"),
    "bench_late_manifest.md":    (2, 4, 7, "正式 venue"),
    "models_core_manifest.md":   (0, 3, 4, "落盘目录"),
    "models_methods_manifest.md":(1, 3, 4, "本地目录"),
}
# models_core 的「正式发表」写成「2025-10，ICCV 2025」/「仅 arXiv」，另有「载体与权威性」列更完整
CARRIER_COL = {"models_core_manifest.md": 1}

out = {}
for fn, (dc, vc, cc, hdr) in LAYOUT.items():
    path = f"docs/review/{fn}"
    if not os.path.exists(path):
        print("!! 缺", path); continue
    n = 0
    for ln in open(path, encoding="utf-8"):
        if not ln.startswith("|") or set(ln.strip()) <= set("|- :"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) <= max(dc, vc, cc) or hdr in ln:
            continue
        raw = c[dc]
        m = re.search(r"`([^`]+)`", raw) or re.match(r"^([0-9]{4}-[0-9]{2}_[^\s,，]+)", raw)
        if not m:
            continue
        d = m.group(1)
        rec = out.setdefault(d, {})
        rec.setdefault("venue_manifest", c[vc])
        if fn in CARRIER_COL:
            rec["carrier"] = c[CARRIER_COL[fn]]
        cites = re.search(r"(\d[\d,]*)", c[cc])
        if cites and "cites_manifest" not in rec:
            rec["cites_manifest"] = int(cites.group(1).replace(",", ""))
        rec.setdefault("src", []).append(fn)
        n += 1
    print(f"{fn:32s} 解析 {n} 行")

# INDEX.md §4 的 venue 列（同一轮核验的产物，与 manifest 互为补充）
txt = open("docs/INDEX.md", encoding="utf-8").read()
if "## 4. 第二批" in txt:
    for ln in txt.split("## 4. 第二批")[1].splitlines():
        if not ln.startswith("|") or "论文 / 条目" in ln or set(ln.strip()) <= set("|- :"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) < 6: continue
        m = re.search(r"\.\./papers/([^/]+)/", c[1])
        if m:
            rec = out.setdefault(m.group(1), {})
            rec.setdefault("venue_index4", c[4])
            rec.setdefault("src", []).append("INDEX.md§4")

ps = json.load(open("scripts/papers.json", encoding="utf-8"))
dirs = {p["dir"] for p in ps}
bad = sorted(set(out) - dirs)
print(f"\n合计 {len(out)} 个目录有人工核验记录；目录名对不上的: {bad}")
for d in bad: out.pop(d)
json.dump(out, open("_work/manifest_venue.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
have = sum(1 for v in out.values() if v.get("venue_manifest") or v.get("venue_index4"))
print(f"其中有 venue 的 {have} 条；有引用量的 {sum(1 for v in out.values() if 'cites_manifest' in v)} 条")
