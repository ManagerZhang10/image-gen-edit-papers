#!/usr/bin/env python3
"""合并种子清单与筛选池，按关注度门槛裁剪出要查引用的候选集。"""
import json, os

W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_work")
os.makedirs(W, exist_ok=True)
cand = json.load(open(f"{W}/cand.json", encoding="utf-8"))
seeds = json.load(open(f"{W}/seeds_resolved.json", encoding="utf-8"))
by = {c["id"]: c for c in cand}

for s in seeds:
    if not s.get("id"):
        continue
    if s["id"] in by:
        by[s["id"]]["seed"] = True
    else:
        by[s["id"]] = {"id": s["id"], "title": s["title"], "published": s.get("published", ""),
                       "upvotes": s.get("upvotes") or 0, "stars": None, "kw": s.get("kw") or [],
                       "seed": True}

def keep(c):
    if c.get("seed"): return True
    y = c["published"][:4]
    up, st = c.get("upvotes") or 0, c.get("stars") or 0
    if y in ("2023", "2024"): return up >= 2 or st >= 50
    return up >= 6 or st >= 100

sel = [c for c in by.values() if keep(c) and c["published"] >= "2023-01-01"]
sel.sort(key=lambda c: c["published"])
json.dump(sel, open(f"{W}/cand.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
import collections
print("merged cand:", len(sel), sorted(collections.Counter(c["published"][:4] for c in sel).items()))
print("seeds resolved:", sum(1 for s in seeds if s.get("id")), "/", len(seeds))
