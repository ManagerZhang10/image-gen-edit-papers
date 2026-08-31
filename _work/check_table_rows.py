"""全量核对 README 全量清单每一行：解读路径、标题、原文链接必须来自同一个目录。"""
import io, json, os, re, sys
sys.path.insert(0, "scripts")
from pdf_sources import RENDITION_DIFFERS
chk = {r["dir"]: r for r in json.load(open("_work/pdf_link_check.json"))["rows"]}
s = io.open("README.md", encoding="utf-8").read().split("## 全量清单")[1]
rows = re.findall(r"^\| ([^|]+) \| \[([^\]]+)\]\(papers/([^)]+)/解读\.md\) \| (.+?) \| \[(?:PDF|官方来源)\]\(([^)]+)\)( ⚠️)? \| (\d+) \|$", s, re.M)
print(f"解析出 {len(rows)} 行")
bad = 0
seen = set()
for date, short, d, title, url, warn, cn in rows:
    m = json.load(open(f"papers/{d}/meta.json", encoding="utf-8"))
    r = chk.get(d, {})
    errs = []
    if not os.path.exists(f"papers/{d}/解读.md"): errs.append("解读.md 不存在")
    if (m.get("short") or d) != short: errs.append(f"简称不符 meta={m.get('short')}")
    if (m.get("title") or "").replace("|", r"\|").strip() != title: errs.append("标题不符")
    expect = r["url"] if r.get("status") != "NO_PAPER" else None
    if expect and expect != url: errs.append(f"链接不符 应为 {expect}")
    if r.get("status") == "NO_PAPER" and "arxiv.org" in url: errs.append("无论文条目却给了 arXiv 链接")
    if (d in RENDITION_DIFFERS) != bool(warn): errs.append("⚠️ 标注与 RENDITION_DIFFERS 不一致")
    body = io.open(f"papers/{d}/解读.md", encoding="utf-8").read()
    if len(re.findall(r"[一-鿿]", body)) != int(cn): errs.append("字数不符")
    seen.add(d)
    if errs:
        bad += 1; print(f"  !! {d}: {'; '.join(errs)}")
allq = {d for d in os.listdir("papers")
        if os.path.isdir(os.path.join("papers", d)) and d[0].isdigit()}
print(f"覆盖目录 {len(seen)}/{len(allq)}，缺 {sorted(allq - seen) or '无'}")
print(f"有问题的行：{bad}")
sys.exit(1 if bad or seen != allq else 0)
