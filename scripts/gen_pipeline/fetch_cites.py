#!/usr/bin/env python3
"""给候选 arXiv ID 取引用量：Semantic Scholar 批量优先，失败逐条回退 OpenAlex 标题检索。
输入 _work/cand.json  [{"id","title"},...]   输出 _work/cites.json
"""
import json, os, re, sys, time, urllib.parse, urllib.request

W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_work")
os.makedirs(W, exist_ok=True)
# OpenAlex / Semantic Scholar 的 polite pool 要一个联系邮箱。
# 本仓库是公开的，不把邮箱写死在代码里——从环境变量读，没设就不带 mailto
# （不带也能用，只是走匿名池、限流更严）。
#     export PAPER_CONTACT_MAIL=you@example.com
MAIL = os.environ.get("PAPER_CONTACT_MAIL", "")
UA = {"User-Agent": f"img-gen-papers/1.0 (mailto:{MAIL})"}

def norm(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())

def get(u, t=90):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read()

def s2_batch(ids):
    body = json.dumps({"ids": ["ARXIV:" + i for i in ids]}).encode()
    h = dict(UA); h["Content-Type"] = "application/json"
    req = urllib.request.Request(
        "https://api.semanticscholar.org/graph/v1/paper/batch"
        "?fields=title,citationCount,publicationDate,venue,externalIds", data=body, headers=h)
    return json.loads(urllib.request.urlopen(req, timeout=180).read())

def openalex(title):
    u = ("https://api.openalex.org/works?per-page=5&mailto=" + MAIL +
         "&select=title,publication_date,cited_by_count,primary_location,type"
         "&filter=title.search:" + urllib.parse.quote(re.sub(r"[:,]", " ", title)[:110]))
    rs = json.loads(get(u)).get("results", [])
    tgt = norm(title)
    best = None
    for r in rs:
        if norm(r.get("title")) == tgt or (tgt and norm(r.get("title")).startswith(tgt[:40])):
            if best is None or (r.get("cited_by_count") or 0) > best[0]:
                loc = (r.get("primary_location") or {}).get("source") or {}
                best = ((r.get("cited_by_count") or 0), r.get("publication_date"), loc.get("display_name"))
    return best

def main():
    cand = json.load(open(f"{W}/cand.json", encoding="utf-8"))
    out = {}
    ids = [c["id"] for c in cand]
    for k in range(0, len(ids), 100):
        chunk = ids[k:k + 100]
        for attempt, wait in enumerate([0, 8, 20, 45, 90, 150]):
            if wait: time.sleep(wait)
            try:
                res = s2_batch(chunk)
                for aid, r in zip(chunk, res):
                    if r and r.get("citationCount") is not None:
                        out[aid] = {"cites": r["citationCount"], "s2_title": r.get("title"),
                                    "s2_date": r.get("publicationDate"), "venue": r.get("venue"),
                                    "provider": "s2"}
                print(f"[s2] {k}-{k+len(chunk)} ok, got {len([1 for a in chunk if a in out])}", flush=True)
                break
            except Exception as e:
                print(f"[s2] {k} attempt{attempt} {type(e).__name__} {e}", flush=True)
        time.sleep(2)
    miss = [c for c in cand if c["id"] not in out]
    print(f"[fallback] {len(miss)} 条走 OpenAlex", flush=True)
    for i, c in enumerate(miss):
        try:
            b = openalex(c["title"])
            if b:
                out[c["id"]] = {"cites": b[0], "s2_title": None, "s2_date": b[1],
                                "venue": b[2], "provider": "openalex"}
            else:
                out[c["id"]] = {"cites": None, "provider": "none"}
        except Exception as e:
            out[c["id"]] = {"cites": None, "provider": "err:" + type(e).__name__}
        if i % 25 == 0: print(f"[oa] {i}/{len(miss)}", flush=True)
        time.sleep(1.1)
    json.dump(out, open(f"{W}/cites.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("DONE", len(out), "with cites:", sum(1 for v in out.values() if v.get("cites") is not None))

if __name__ == "__main__":
    main()
