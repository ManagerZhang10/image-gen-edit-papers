#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Semantic Scholar 批量查 venue → _work/s2_cache.json。

为什么只取 venue 不取年份：S2 的 year 是论文年份而不是会议年份。
SDEdit 的 venue 是 ICLR、year 是 2021，但它发在 ICLR 2022；
Latent-Diffusion 的 venue 是 CVPR、year 是 2021，实际是 CVPR 2022。
拼成「ICLR 2021」就是造了一个假事实，所以这一档只写会议名，年份标未核。

DBLP 能给正确的会议年份，但本机连它稳定超时（大概被限流），这一档暂缺。
"""
import json, os, re, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = f"{ROOT}/_work/s2_cache.json"
API = ("https://api.semanticscholar.org/graph/v1/paper/batch"
       "?fields=title,venue,year,publicationVenue,externalIds,publicationTypes")

SHORT = [
    (r"international conference on learning representations", "ICLR"),
    (r"computer vision and pattern recognition", "CVPR"),
    (r"international conference on computer vision\b", "ICCV"),
    (r"european conference on computer vision", "ECCV"),
    (r"(advances in )?neural information processing systems|neurips", "NeurIPS"),
    (r"international conference on machine learning", "ICML"),
    (r"aaai conference on artificial intelligence|^aaai", "AAAI"),
    (r"international joint conference on artificial intelligence", "IJCAI"),
    (r"acm multimedia|acm international conference on multimedia", "ACM MM"),
    (r"siggraph asia", "SIGGRAPH Asia"),
    (r"siggraph", "SIGGRAPH"),
    (r"acm transactions on graphics", "ACM TOG"),
    (r"winter conference on applications of computer vision", "WACV"),
    (r"transactions on machine learning research", "TMLR"),
    (r"transactions on pattern analysis and machine intelligence", "TPAMI"),
    (r"transactions on image processing", "TIP"),
    (r"international journal of computer vision", "IJCV"),
    (r"empirical methods in natural language processing", "EMNLP"),
    (r"annual meeting of the association for computational linguistics", "ACL"),
    (r"british machine vision conference", "BMVC"),
]
REJECT = re.compile(r"arxiv|corr|preprint|^$", re.I)


def shorten(v):
    if not v or REJECT.match(v.strip()):
        return None
    low = v.lower()
    for pat, s in SHORT:
        if re.search(pat, low):
            return s
    return v.strip() if len(v.strip()) <= 46 else None


def batch(ids, tries=4):
    body = json.dumps({"ids": ids}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Content-Type": "application/json", "User-Agent": "paper-reading/1.0"})
    for i in range(tries):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=120).read())
        except Exception as e:
            print(f"   第{i+1}次失败 {type(e).__name__} {getattr(e,'code','')}", flush=True)
            time.sleep(15 * (i + 1))
    return None


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    ids = [p["arxiv_id"] for p in ps if p.get("arxiv_id")]
    cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    todo = [i for i in ids if i not in cache]
    print(f"待查 {len(todo)} / {len(ids)}")
    for k in range(0, len(todo), 100):
        b = todo[k:k + 100]
        res = batch(["ARXIV:" + i for i in b])
        if res is None:
            print(f"!! 批次 {k} 放弃"); continue
        for aid, r in zip(b, res):
            if not r:
                cache[aid] = {"found": False}; continue
            cache[aid] = {"found": True, "title": r.get("title"),
                          "venue_raw": r.get("venue"),
                          "venue_short": shorten(r.get("venue")),
                          "s2_year": r.get("year"),
                          "pub_types": r.get("publicationTypes")}
        json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"  {k + len(b)}/{len(todo)}", flush=True)
        time.sleep(3)

    # 标题一致性校验：S2 偶尔会把 arXiv ID 配到别的论文上
    def words(s):
        return set(re.findall(r"[a-z0-9]+", (s or "").lower())) - {"a", "the", "of", "for", "with", "and"}

    def same(a, b):
        """词集重叠判同一篇。前缀比对会被排版差异误伤：
        PixArt-$alpha$ vs PixArt-α、Edit-Compass &amp; vs &、副标题增删都是同一篇。"""
        wa, wb = words(a), words(b)
        if not wa or not wb:
            return False
        return len(wa & wb) / max(1, min(len(wa), len(wb))) >= 0.6

    by_id = {p["arxiv_id"]: p for p in ps if p.get("arxiv_id")}
    ok, mismatch, novenue = 0, [], 0
    for aid, r in cache.items():
        if not r.get("found"):
            continue
        p = by_id.get(aid)
        r.pop("title_mismatch", None)
        if p and not same(r["title"], p["title"]):
            mismatch.append((aid, p["short"], r["title"][:44]))
            r["venue_short"] = None
            r["title_mismatch"] = True
        if r.get("venue_short"):
            ok += 1
        else:
            novenue += 1
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\n有可用 venue {ok}；只在 arXiv 或名字太长 {novenue}；标题对不上（已弃用）{len(mismatch)}")
    for a, s, t in mismatch[:10]:
        print(f"   {s:24s} arXiv {a}  S2 标题: {t}")
    import collections
    print("\nvenue 分布:", collections.Counter(
        r.get("venue_short") for r in cache.values() if r.get("venue_short")).most_common(18))


if __name__ == "__main__":
    main()
