"""全库站内链接检查：每个 .md 里的相对链接，目标文件必须真实存在。"""
import io, os, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP = ("http://", "https://", "mailto:", "#")

# 只查进了版本库的文件：_work/ 下的中间产物和本地 review 件按 .gitignore 不发布，
# 它们指向旧路径不影响读者。core.quotePath=false 否则中文路径会被 git 转成八进制。
tracked = subprocess.check_output(
    ["git", "-c", "core.quotePath=false", "ls-files", "*.md"],
    cwd=ROOT).decode("utf-8").split("\n")

files, links, bad = 0, 0, []
for rel in tracked:
    if not rel.endswith(".md"):
        continue
    p = os.path.join(ROOT, rel)
    dp = os.path.dirname(p)
    files += 1
    for m in LINK.finditer(io.open(p, encoding="utf-8").read()):
        t = m.group(1)
        if t.startswith(SKIP):
            continue
        links += 1
        tgt = urllib.parse.unquote(t.split("#")[0])
        if not tgt:
            continue
        # paper.pdf 按设计不进仓库，跑 scripts/fetch_pdfs.py 才有
        if tgt.endswith("paper.pdf"):
            continue
        if not os.path.exists(os.path.join(dp, tgt)):
            bad.append("%s -> %s" % (rel, t))

print("扫了 %d 个进仓库的 .md，站内链接 %d 条，指不到的 %d 条" % (files, links, len(bad)))
for b in bad[:40]:
    print("   !!", b)
sys.exit(1 if bad else 0)
