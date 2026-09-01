#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给还没有 venue 证据的篇目做 DBLP 标题检索 → _work/dblp_cache.json。

为什么需要这一步：人工核验 manifest 覆盖 55 项、arXiv comment 给出 27 项，
其余 126 项在 arXiv 和 OpenAlex 上都查不到 venue（OpenAlex 对这批只回 "arXiv"），
但其中相当一部分确实正式发表过。DBLP 对 CV/ML 会议的收录比 OpenAlex 完整。

纪律：
- 只认标题高度一致的命中，标题对不上就丢弃，不靠年份或作者猜。
- DBLP 把 arXiv 预印本记成 CoRR，必须排除——否则等于把预印本写成发表。
- 不带 mailto，不向第三方发用户邮箱。

⚠️ 现状（2026-09-01）：本机连 dblp.org 稳定读超时，126 篇一条都没拿到，
_work/dblp_cache.json 为空，这一档在 finalize 里等于跳过。venue 的会议年份因此
主要来自人工核验 manifest 与 arXiv comment；Semantic Scholar 那一档只有会议名。
换网络环境后重跑本脚本，就能把「（年份未核）」那 47 篇补上年份。
"""
import json, os, re, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = f"{ROOT}/_work/dblp_cache.json"
UA = {"User-Agent": "paper-reading/1.0"}
BAD_VENUE = re.compile(r"^(CoRR|arXiv)$", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def get(url, tries=4):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e:
            code = getattr(e, "code", None)
            if i == tries - 1:
                return None
            time.sleep((20 if code == 429 else 6) * (i + 1))


def probe(title):
    url = "https://dblp.org/search/publ/api?format=json&h=6&q=" + urllib.parse.quote(title[:180])
    raw = get(url)
    if raw is None:
        return {"error": "请求失败"}
    try:
        hits = json.loads(raw).get("result", {}).get("hits", {}).get("hit", [])
    except Exception as e:
        return {"error": f"解析失败 {e}"}
    if isinstance(hits, dict):
        hits = [hits]
    out = []
    for h in hits:
        i = h.get("info", {})
        out.append({"title": i.get("title"), "venue": i.get("venue"),
                    "year": i.get("year"), "type": i.get("type")})
    return {"hits": out}


def pick(title, res):
    """只在标题归一化后前 55 字符一致、且 venue 不是 CoRR 时采信。"""
    if "hits" not in res:
        return None
    nt = norm(title)
    for h in res["hits"]:
        v, y = h.get("venue"), h.get("year")
        if not v or not y or BAD_VENUE.match(str(v).strip()):
            continue
        nh = norm(h.get("title"))
        if not nh or not nt:
            continue
        if nh[:55] == nt[:55] or nh == nt:
            return f"{v} {y}"
    return None


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    todo = [p for p in ps
            if p["venue_source"] == "兜底：无接收证据"
            and (p["dir"] not in cache or "error" in cache[p["dir"]])]
    print(f"待查 {len(todo)} 篇（DBLP 每 1.2 秒一次）", flush=True)
    for k, p in enumerate(todo, 1):
        cache[p["dir"]] = probe(p["title"])
        if k % 15 == 0 or k == len(todo):
            json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"  {k}/{len(todo)}", flush=True)
        time.sleep(1.2)
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    hit = []
    for p in ps:
        r = cache.get(p["dir"])
        if not r:
            continue
        v = pick(p["title"], r)
        if v:
            hit.append((p["short"], v))
    print(f"\n标题一致且非 CoRR 的命中 {len(hit)} 篇：")
    for s, v in hit:
        print(f"   {s:26s} {v}")
    err = [d for d, v in cache.items() if "error" in v]
    print(f"\n请求/解析失败 {len(err)}: {err[:8]}")


if __name__ == "__main__":
    main()
