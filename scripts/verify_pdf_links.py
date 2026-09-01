#!/usr/bin/env python3
"""核验 README 里每条 PDF 直链是否真的指向本库对应的那篇论文。

对每个目录：
  1. 由 meta.json 推出 PDF 直链（与 fetch_pdfs.py 的 pdf_url 同一套规则）
  2. 发一个 1KB Range 请求，读回 HTTP 状态、Content-Type、前 4 字节、以及
     Content-Range 里的资源总长度
  3. 把总长度和本地 paper.pdf 的字节数逐字节比对

四项全过才记 OK。只连得通不算核验通过——那只能证明链接活着，
不能证明它指向的是本库读的那一份。

    python3 scripts/verify_pdf_links.py              # 全量核验，写 _work/pdf_link_check.json
    python3 scripts/verify_pdf_links.py 2023-02_ControlNet   # 只核一个
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_sources import pdf_url          # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")
UA = "image-gen-edit-papers/1.0 (https://github.com/ManagerYu10/image-gen-edit-papers)"
DELAY = 3.0          # arXiv 对批量访问要求 >=3s 间隔
OUT = os.path.join(ROOT, "_work", "pdf_link_check.json")



def probe(url):
    """取远端前 1KB，返回 (http 状态, content-type, 前4字节, 资源总字节数)。"""
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Range": "bytes=0-1023"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        head = resp.read(1024)
        ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
        crange = resp.headers.get("Content-Range") or ""
        total = int(crange.rsplit("/", 1)[1]) if "/" in crange else None
        return resp.status, ctype, head[:4], total


def main(argv):
    dirs = sorted(
        d for d in os.listdir(PAPERS)
        if os.path.isdir(os.path.join(PAPERS, d)) and d[0].isdigit()
    )
    if argv:
        dirs = [d for d in dirs if d in argv]
    rows, first = [], True
    for d in dirs:
        meta = json.load(open(os.path.join(PAPERS, d, "meta.json")))
        url = pdf_url(meta, d)
        row = {"dir": d, "short": meta.get("short"), "url": url}
        if url is None:
            row["status"] = "NO_PAPER"
            row["fallback"] = meta.get("url")
            rows.append(row)
            print(f"  --  {d:44s} 无独立论文，回落官方来源")
            continue
        if not first:
            time.sleep(DELAY)
        first = False
        local = os.path.join(PAPERS, d, "paper.pdf")
        row["local_bytes"] = os.path.getsize(local) if os.path.exists(local) else None
        try:
            code, ctype, magic, total = probe(url)
        except (urllib.error.URLError, OSError, ValueError) as e:
            row["status"], row["error"] = "ERROR", str(e)
            rows.append(row)
            print(f"  !!  {d:44s} {e}")
            continue
        row.update(http=code, content_type=ctype,
                   magic=magic.decode("latin-1"), remote_bytes=total)
        # Content-Type 的例外：GitHub raw 对 .pdf 一律回 application/octet-stream。
        # 只在「魔数是 %PDF 且远端字节数与本地完全一致」时放行，并在行里留痕。
        # 不放宽到全部主机——arXiv / CVF 回错 Content-Type 才是真该报的问题。
        CTYPE_EXCEPT = {"raw.githubusercontent.com": {"application/octet-stream"}}
        host = urllib.parse.urlparse(url).netloc
        ctype_ok = (ctype == "application/pdf"
                    or ctype in CTYPE_EXCEPT.get(host, set()))
        if ctype_ok and ctype != "application/pdf":
            row["content_type_note"] = f"{host} 对 PDF 回 {ctype}，按主机例外放行"
        ok = (code == 206 and ctype_ok and magic == b"%PDF"
              and total is not None and total == row["local_bytes"])
        row["status"] = "OK" if ok else "MISMATCH"
        rows.append(row)
        flag = "OK " if ok else "!! "
        print(f"  {flag} {d:44s} http={code} {ctype} {magic!r} "
              f"remote={total} local={row['local_bytes']}")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if argv and os.path.exists(OUT):        # 只核了几条：并回既有结果
        old = json.load(open(OUT))["rows"]
        merged = {r["dir"]: r for r in old}
        merged.update({r["dir"]: r for r in rows})
        rows_out = [merged[k] for k in sorted(merged)]
    else:
        rows_out = rows
    json.dump({"checked_at": time.strftime("%Y-%m-%d"), "rows": rows_out},
              open(OUT, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(r["status"] for r in rows)
    print(f"\n合计 {len(rows)}：" + "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
    print(f"明细写入 {os.path.relpath(OUT, ROOT)}")
    return 0 if not (c["MISMATCH"] or c["ERROR"]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
