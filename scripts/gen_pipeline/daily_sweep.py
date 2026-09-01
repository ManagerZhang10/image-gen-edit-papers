#!/usr/bin/env python3
"""补齐近期覆盖：2026-03 → 2026-08 全天 daily papers，合并进 hf_pool.json。"""
import json, os, time, urllib.request, datetime as dt

W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_work")
os.makedirs(W, exist_ok=True)
# OpenAlex / Semantic Scholar 的 polite pool 要一个联系邮箱。
# 本仓库是公开的，不把邮箱写死在代码里——从环境变量读，没设就不带 mailto
# （不带也能用，只是走匿名池、限流更严）。
#     export PAPER_CONTACT_MAIL=you@example.com
MAIL = os.environ.get("PAPER_CONTACT_MAIL", "")
UA = {"User-Agent": "img-gen-papers/1.0" + (f" (mailto:{MAIL})" if MAIL else "")}
pool = {r["id"]: r for r in json.load(open(f"{W}/hf_pool.json", encoding="utf-8"))}
before = len(pool)

d = dt.date(2026, 3, 1)
end = dt.date(2026, 8, 31)
added = 0
while d <= end:
    if d.weekday() < 5:                      # 周末几乎没有 daily papers
        try:
            u = f"https://huggingface.co/api/daily_papers?date={d.isoformat()}&limit=100"
            items = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read())
            for it in items:
                p = it["paper"]
                if p["id"] not in pool:
                    pool[p["id"]] = {"id": p["id"], "title": " ".join(p["title"].split()),
                                     "published": p.get("publishedAt", "")[:10],
                                     "upvotes": p.get("upvotes", 0), "stars": p.get("githubStars"),
                                     "kw": p.get("ai_keywords") or [], "src": ["daily-full"]}
                    added += 1
                else:
                    pool[p["id"]]["upvotes"] = max(pool[p["id"]]["upvotes"] or 0, p.get("upvotes") or 0)
        except Exception as e:
            print(f"[fail] {d} {e}", flush=True)
        time.sleep(0.5)
    d += dt.timedelta(days=1)
    if d.day == 1: print(f"[sweep] {d} pool={len(pool)} (+{added})", flush=True)

json.dump(sorted(pool.values(), key=lambda r: r["published"]),
          open(f"{W}/hf_pool.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("before", before, "after", len(pool), "added", added)
