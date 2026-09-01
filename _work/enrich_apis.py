#!/usr/bin/env python3
"""arXiv API + OpenAlex 批量核对 → _work/enrich_cache.json。

arXiv 给权威的标题 / 首发日 / comment（venue 线索）；OpenAlex 给 venue、机构、引用量。
只写缓存，不直接改 papers.json——核对结果先出报告，人看过再合并。
只用标准库。arXiv 节流 3 秒/批，OpenAlex 1 秒/批。不带 mailto。
"""
import json, os, re, time, urllib.request, urllib.error, xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = f"{ROOT}/_work/enrich_cache.json"
ATOM = "{http://www.w3.org/2005/Atom}"
ARX = "{http://arxiv.org/schemas/atom}"


def get(url, tries=4):
    for i in range(tries):
        try:
            return urllib.request.urlopen(url, timeout=60).read()
        except Exception as e:
            if i == tries - 1:
                print(f"   FAIL {type(e).__name__} {url[:110]}")
                return None
            time.sleep(10 * (i + 1))


def arxiv_batch(ids):
    """一批 ID → {id: {title, published, updated, comment, categories, authors}}"""
    url = ("http://export.arxiv.org/api/query?id_list=" + ",".join(ids)
           + f"&max_results={len(ids)}")
    raw = get(url)
    if not raw:
        return {}
    out = {}
    for e in ET.fromstring(raw).findall(f"{ATOM}entry"):
        eid = e.findtext(f"{ATOM}id") or ""
        m = re.search(r"abs/([^v]+)(v\d+)?$", eid)
        if not m:
            continue
        cmt = e.findtext(f"{ARX}comment")
        jr = e.findtext(f"{ARX}journal_ref")
        out[m.group(1)] = {
            "title": " ".join((e.findtext(f"{ATOM}title") or "").split()),
            "published": (e.findtext(f"{ATOM}published") or "")[:10],
            "updated": (e.findtext(f"{ATOM}updated") or "")[:10],
            "comment": " ".join(cmt.split()) if cmt else None,
            "journal_ref": " ".join(jr.split()) if jr else None,
            "primary_category": (e.find(f"{ARX}primary_category") or {}).get("term")
                if e.find(f"{ARX}primary_category") is not None else None,
            "authors": [a.findtext(f"{ATOM}name") for a in e.findall(f"{ATOM}author")][:12],
        }
    return out


def openalex_batch(ids):
    """一批 arXiv ID → {id: {venue, venue_type, cites, institutions, year}}"""
    dois = "|".join(f"10.48550/arxiv.{i}" for i in ids)
    url = ("https://api.openalex.org/works?filter=doi:" + dois
           + "&per-page=50&select=doi,display_name,cited_by_count,publication_year,"
             "primary_location,type,authorships,best_oa_location")
    raw = get(url)
    if not raw:
        return {}
    out = {}
    for w in json.loads(raw).get("results", []):
        doi = (w.get("doi") or "").lower()
        m = re.search(r"arxiv\.(.+)$", doi)
        if not m:
            continue
        pl = w.get("primary_location") or {}
        src = pl.get("source") or {}
        insts, seen = [], set()
        for a in (w.get("authorships") or []):
            for it in (a.get("institutions") or []):
                nm = it.get("display_name")
                if nm and nm not in seen:
                    seen.add(nm); insts.append(nm)
        out[m.group(1)] = {
            "openalex_title": w.get("display_name"),
            "venue": src.get("display_name"),
            "venue_host_type": src.get("type"),
            "oa_type": w.get("type"),
            "cites": w.get("cited_by_count"),
            "year": w.get("publication_year"),
            "institutions": insts[:8],
        }
    return out


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    ids = [p["arxiv_id"] for p in ps if p.get("arxiv_id")]
    print(f"待核 arXiv ID：{len(ids)} 条")

    cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    cache.setdefault("arxiv", {}); cache.setdefault("openalex", {})

    todo = [i for i in ids if i not in cache["arxiv"]]
    for k in range(0, len(todo), 40):
        b = todo[k:k + 40]
        print(f"arXiv  {k + 1}-{k + len(b)}/{len(todo)}")
        cache["arxiv"].update({i: None for i in b})   # 先占位，查不到就是 None
        cache["arxiv"].update(arxiv_batch(b))
        json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        time.sleep(3)

    todo = [i for i in ids if i not in cache["openalex"]]
    for k in range(0, len(todo), 40):
        b = todo[k:k + 40]
        print(f"OpenAlex {k + 1}-{k + len(b)}/{len(todo)}")
        cache["openalex"].update({i: None for i in b})
        cache["openalex"].update(openalex_batch(b))
        json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        time.sleep(1)

    ah = sum(1 for i in ids if cache["arxiv"].get(i))
    oh = sum(1 for i in ids if cache["openalex"].get(i))
    print(f"完成：arXiv 命中 {ah}/{len(ids)}，OpenAlex 命中 {oh}/{len(ids)}")


if __name__ == "__main__":
    main()
