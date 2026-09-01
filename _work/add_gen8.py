#!/usr/bin/env python3
"""并入 image-generation-papers 那 8 篇不重复的生成论文：建目录 + meta.json + 拉原文。

12 篇重复的不在这里处理（它们已在库里，只需把生成侧指标并进 papers.json）。
脉络归属沿用本库 15 条脉络的既有约定，只新增 1 条「少步与一步生成」——
Consistency Models 与 DMD 这条线本库原先确实没有。
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "/Users/yuzhang/ZhangYu/self_learning/paper_reading/image-generation-papers/scripts/papers.json"

# short -> (task, type, line)  —— 归属依据见 _work/add_gen8.py 的说明
TAGS = {
    "SDXL":               (["生成"], "模型",   "生成骨干：编辑方法赖以运行的底座"),
    "DALL·E 3":           (["生成"], "技术报告", "数据工程：三元组与重标注从哪来"),
    "Kolors":             (["生成"], "技术报告", "生成骨干：编辑方法赖以运行的底座"),
    "Consistency Models": (["生成"], "方法",   "少步与一步生成"),
    "GenEval":            (["生成"], "基准",   "推理、强化学习与评测"),
    "DMD":                (["生成"], "方法",   "少步与一步生成"),
    "MAR":                (["生成"], "方法",   "统一多模态：理解与生成同一个模型"),
    "REPA":               (["生成"], "方法",   "生成骨干：编辑方法赖以运行的底座"),
}

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) paper-reading/1.0"}


def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 50000:
        return "skip", os.path.getsize(dest)
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180)
            b = r.read()
            if b[:4] != b"%PDF":
                return f"非 PDF（前 4 字节 {b[:4]!r}）", len(b)
            open(dest, "wb").write(b)
            return "ok", len(b)
        except Exception as e:
            if i == 3:
                return f"{type(e).__name__}: {e}", 0
            time.sleep(6 * (i + 1))


def main():
    src = {p["short"]: p for p in json.load(open(SRC, encoding="utf-8"))}
    for short, (task, typ, line) in TAGS.items():
        p = src[short]
        d = f"{ROOT}/papers/{p['dir']}"
        os.makedirs(d, exist_ok=True)
        mp = f"{d}/meta.json"
        if not os.path.exists(mp):
            json.dump({
                "short": short, "date": p["date"], "arxiv_id": p["arxiv_id"],
                "title": p["title"], "url": p["url"], "venue": p["venue"], "org": p["org"],
                "task": task, "type": typ, "line": line,
                "source_type": "tech_report" if p["arxiv_id"] is None else None,
                "impact": {"citation_count": p["cites"], "provider":
                           "Semantic Scholar / HF Papers（image-generation-papers 口径）",
                           "hf_upvotes": p["upvotes"], "checked_at": "2026-08-31"},
                "hub": p["hub"],
                "note": "自 image-generation-papers 并入，解读待生成",
            }, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        st, n = fetch(p["pdf"], f"{d}/paper.pdf")
        print(f"[{st:34s}] {short:20s} {n:>10,} B  {p['pdf'][:70]}")
        if st == "ok":
            time.sleep(3)          # arXiv 要求节流


if __name__ == "__main__":
    main()
