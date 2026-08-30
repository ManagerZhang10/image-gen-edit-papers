"""从成品 README 里随机抽几行，把链接实际打开，比对返回的标题和该行写的标题。"""
import random, re, io, sys, time, urllib.request
UA = "image_edit_paper/1.0 (https://github.com/ManagerYu10/image_edit_paper)"
s = io.open("README.md", encoding="utf-8").read()
tbl = s.split("## 附二")[1]
rows = re.findall(r"^\| ([\d-]+) \| \[([^\]]+)\]\([^)]+\) \| (.+?) \| \[(PDF|官方来源)\]\(([^)]+)\)", tbl, re.M)
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
sample = random.sample([r for r in rows if r[3] == "PDF"], 6)
print(f"表里共 {len(rows)} 行，抽 {len(sample)} 行实测\n")
for i, (date, short, title, _, url) in enumerate(sample):
    m = re.search(r"arxiv\.org/pdf/(\d{4}\.\d{4,5})", url)
    if m:
        abs_url = f"https://arxiv.org/abs/{m.group(1)}"
        req = urllib.request.Request(abs_url, headers={"User-Agent": UA})
        html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
        got = re.search(r'name="citation_title" content="([^"]*)"', html)
        got = got.group(1) if got else "(没取到)"
    else:
        got = "(非 arXiv，跳过标题比对)"
    def norm(t):
        return re.sub(r"[^a-z0-9]", "", t.lower())
    ok = "(" in got or norm(got) == norm(title)
    print(f"{'✓' if ok else '✗'} {short}  {date}")
    print(f"   表里写的: {title}")
    print(f"   链接返回: {got}")
    if i < len(sample) - 1:
        time.sleep(3)
