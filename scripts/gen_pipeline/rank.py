#!/usr/bin/env python3
"""时间加权排序：引用速率（次/月）为主轴，HF upvote 与 GitHub star 为副轴。
输出 _work/rank.tsv（按速率）与 _work/rank_recent.tsv（近 6 个月按 upvote）。"""
import json, os, datetime as dt

W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_work")
os.makedirs(W, exist_ok=True)
TODAY = dt.date(2026, 8, 31)
cand = json.load(open(f"{W}/cand.json", encoding="utf-8"))
cites = json.load(open(f"{W}/cites.json", encoding="utf-8"))

rows = []
for c in cand:
    m = cites.get(c["id"], {})
    try:
        pub = dt.date.fromisoformat(c["published"])
    except Exception:
        continue
    months = max((TODAY - pub).days / 30.44, 1.0)
    n = m.get("cites")
    rows.append({"id": c["id"], "pub": c["published"], "months": round(months, 1),
                 "cites": n, "rate": round(n / months, 1) if n is not None else None,
                 "up": c.get("upvotes") or 0, "stars": c.get("stars") or 0,
                 "prov": m.get("provider"), "venue": m.get("venue"),
                 "title": c["title"][:95]})

def dump(rs, path, head):
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + "\n")
        for i, r in enumerate(rs, 1):
            f.write(f"{i}\t{r['pub']}\t{r['cites'] if r['cites'] is not None else '-'}\t"
                    f"{r['rate'] if r['rate'] is not None else '-'}\t{r['up']}\t{r['stars']}\t"
                    f"{r['id']}\t{(r['venue'] or '')[:22]}\t{r['title']}\n")

HEAD = "#\t日期\t引用\t引用/月\tupvote\tstars\tarXiv\tvenue\t标题"
byrate = sorted([r for r in rows if r["rate"] is not None], key=lambda r: -r["rate"])
dump(byrate[:150], f"{W}/rank.tsv", HEAD)
recent = sorted([r for r in rows if r["pub"] >= "2026-02-01"], key=lambda r: -(r["up"] or 0))
dump(recent[:80], f"{W}/rank_recent.tsv", HEAD)
nocite = [r for r in rows if r["rate"] is None]
print("rows", len(rows), "有引用", len(byrate), "无引用", len(nocite))
print("引用速率 top1:", byrate[0]["title"][:60], byrate[0]["rate"])
