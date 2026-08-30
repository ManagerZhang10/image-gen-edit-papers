#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 meta.json 的 cn_chars 与 解读.md 正文重新对齐，并同步 docs/INDEX.md 的字数列。

口径：len(re.findall(r"[一-鿿]", 正文))，即 U+4E00–U+9FFF，与 README 一致。

改过任何一篇解读之后都要跑一次。2026-08-29 给 14 篇追加「本轮决策核验补充」
一节后没跑，导致这 14 个 cn_chars 一直少 88～141 字——这个脚本就是为了不再靠人记。

    python3 _work/sync_cnchars.py           # 只报告，不写
    python3 _work/sync_cnchars.py --write   # 实际写回
"""
import io, os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")
INDEX = os.path.join(ROOT, "docs", "INDEX.md")
CJK = re.compile(r"[一-鿿]")
WRITE = "--write" in sys.argv


def cn_of(path):
    return len(CJK.findall(io.open(path, encoding="utf-8").read()))


def main():
    fixed, total = [], 0
    for d in sorted(os.listdir(PAPERS)):
        fd = os.path.join(PAPERS, d)
        mt, mdp = os.path.join(fd, "meta.json"), os.path.join(fd, "解读.md")
        if not (os.path.isdir(fd) and os.path.exists(mt) and os.path.exists(mdp)): continue
        real = cn_of(mdp)
        total += real
        meta = json.load(io.open(mt, encoding="utf-8"))
        if meta.get("cn_chars") != real:
            fixed.append((d, meta.get("cn_chars"), real))
            if WRITE:
                meta["cn_chars"] = real
                with io.open(mt, "w", encoding="utf-8") as f:
                    json.dump(meta, f, ensure_ascii=False, indent=2)
                    f.write("\n")

    idx_hits = 0
    if os.path.exists(INDEX):
        s = io.open(INDEX, encoding="utf-8").read()
        for d, _old, real in fixed:
            # 表格行形如：... [简称](../papers/<dir>/解读.md) | ... | 7136 |
            pat = re.compile(r"(\(\.\./papers/%s/解读\.md\)[^\n]*?\|\s*)(\d[\d,]*)(\s*\|?\s*)$"
                             % re.escape(d), re.M)
            s, n = pat.subn(lambda m: m.group(1) + str(real) + m.group(3), s)
            idx_hits += n
        if WRITE:
            io.open(INDEX, "w", encoding="utf-8").write(s)

    for d, old, real in fixed:
        print("  %-32s %s → %d" % (d, old, real))
    print("%s：meta.json 需改 %d 个，INDEX.md 命中 %d 行；全库汉字合计 %s"
          % ("已写回" if WRITE else "仅报告（加 --write 写回）",
             len(fixed), idx_hits, format(total, ",")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
