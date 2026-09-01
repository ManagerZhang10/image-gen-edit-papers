#!/usr/bin/env python3
"""交叉核验 papers.json 的发表信息：arXiv comment/journal_ref + DBLP + OpenAlex。

三个源互相独立。结果写 _work/venue_probe.json，冲突处人工裁决后再回填 papers.json。
"""
import json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# OpenAlex / Semantic Scholar 的 polite pool 要一个联系邮箱。
# 本仓库是公开的，不把邮箱写死在代码里——从环境变量读，没设就不带 mailto
# （不带也能用，只是走匿名池、限流更严）。
#     export PAPER_CONTACT_MAIL=you@example.com
MAILTO = os.environ.get("PAPER_CONTACT_MAIL", "")
UA = {"User-Agent": f"img-gen-papers/1.0 (mailto:{MAILTO})"}


def get(url, timeout=90):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def arxiv_meta(ids):
    """一次批量取 comment / journal_ref / 作者。"""
    url = "http://export.arxiv.org/api/query?id_list=" + ",".join(ids) + "&max_results=50"
    x = ET.fromstring(get(url))
    ns = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}
    out = {}
    for e in x.findall("a:entry", ns):
        aid = e.find("a:id", ns).text.rsplit("/", 1)[-1].split("v")[0]
        c = e.find("ar:comment", ns)
        j = e.find("ar:journal_ref", ns)
        out[aid] = {
            "published": e.find("a:published", ns).text[:10],
            "updated": e.find("a:updated", ns).text[:10],
            "comment": " ".join(c.text.split()) if c is not None else None,
            "journal_ref": " ".join(j.text.split()) if j is not None else None,
            "n_authors": len(e.findall("a:author", ns)),
        }
    return out


def dblp(title):
    url = "https://dblp.org/search/publ/api?format=json&h=5&q=" + urllib.parse.quote(title)
    hits = json.loads(get(url)).get("result", {}).get("hits", {}).get("hit", [])
    res = []
    for h in hits:
        i = h["info"]
        res.append({"venue": i.get("venue"), "year": i.get("year"),
                    "type": i.get("type"), "title": i.get("title", "")[:70]})
    return res


def openalex(title):
    url = ("https://api.openalex.org/works?per-page=3&mailto=" + MAILTO +
           "&filter=title.search:" + urllib.parse.quote(title[:110]))
    rs = json.loads(get(url)).get("results", [])
    out = []
    for r in rs:
        loc = (r.get("primary_location") or {}).get("source") or {}
        insts = []
        for a in r.get("authorships", [])[:40]:
            for ins in a.get("institutions", []):
                if ins.get("display_name") and ins["display_name"] not in insts:
                    insts.append(ins["display_name"])
        out.append({"title": (r.get("title") or "")[:70], "date": r.get("publication_date"),
                    "source": loc.get("display_name"), "type": r.get("type"),
                    "cited_by": r.get("cited_by_count"), "institutions": insts[:8]})
    return out


def main():
    papers = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    ids = [p["arxiv_id"] for p in papers if p["arxiv_id"]]
    ax = arxiv_meta(ids)
    probe = {}
    for p in papers:
        k = p["short"]
        rec = {"title": p["title"], "arxiv": ax.get(p["arxiv_id"]) if p["arxiv_id"] else None}
        try:
            rec["dblp"] = dblp(p["title"])
        except Exception as e:
            rec["dblp"] = f"ERR {e}"
        time.sleep(1.5)
        try:
            rec["openalex"] = openalex(p["title"])
        except Exception as e:
            rec["openalex"] = f"ERR {e}"
        time.sleep(1.5)
        probe[k] = rec
        print(f"[done] {k}", file=sys.stderr)
    os.makedirs(f"{ROOT}/_work", exist_ok=True)
    json.dump(probe, open(f"{ROOT}/_work/venue_probe.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
