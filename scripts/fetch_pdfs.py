#!/usr/bin/env python3
"""把 arXiv 原文 PDF 拉回本地。

仓库不含 PDF（182 份合计 3.3 GB）。每个论文目录的 meta.json 里有 arxiv_id，
这个脚本按它去 arxiv.org 下载，落到 <目录>/paper.pdf。

    python3 scripts/fetch_pdfs.py                  # 补齐所有缺失的
    python3 scripts/fetch_pdfs.py 2024-11_OmniEdit # 只下一篇
    python3 scripts/fetch_pdfs.py --list           # 只列出缺什么，不下载

Inter-Edit 只有 CVF proceedings 版没有 arXiv 版，脚本从 meta.json 的 url 推出 PDF 地址。
另外 4 个目录（FLUX.1、Grok-Aurora、Qwen-Image-Edit-2511、GPT-Image-2）本来就没有独立
论文，会被跳过——它们的 解读.md 是官方资料核验笔记，不是论文解读。

arXiv 要求下载间隔 ≥3 秒，脚本按这个节流，全量约 10 分钟。
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_sources import pdf_url          # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")
UA = "image-gen-edit-papers/1.0 (https://github.com/ManagerYu10/image-gen-edit-papers)"
DELAY = 3.0


def paper_dirs():
    return sorted(
        d for d in os.listdir(PAPERS)
        if re.match(r"^\d{4}-\d{2}_", d) and os.path.isdir(os.path.join(PAPERS, d))
    )




def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    if not data.startswith(b"%PDF"):
        raise ValueError(f"返回的不是 PDF（前 16 字节 {data[:16]!r}）")
    tmp = dest + ".part"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, dest)
    return len(data)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    list_only = "--list" in sys.argv[1:]
    targets = args or paper_dirs()

    todo, skipped, done = [], [], []
    for d in targets:
        meta_path = os.path.join(PAPERS, d, "meta.json")
        if not os.path.exists(meta_path):
            skipped.append((d, "没有 meta.json"))
            continue
        meta = json.load(open(meta_path, encoding="utf-8"))
        src = pdf_url(meta, d)
        if not src:
            skipped.append((d, "无独立论文，按设计不放 paper.pdf"))
            continue
        pdf = os.path.join(PAPERS, d, "paper.pdf")
        (done if os.path.exists(pdf) else todo).append((d, src, pdf))

    print(f"已有 {len(done)} 份，待下载 {len(todo)} 份，跳过 {len(skipped)} 个目录")
    for d, why in skipped:
        print(f"  跳过 {d}：{why}")
    if list_only or not todo:
        for d, src, _ in todo:
            print(f"  缺 {d}  {src}")
        return 0

    failed = []
    for i, (d, src, pdf) in enumerate(todo, 1):
        try:
            size = download(src, pdf)
            print(f"[{i}/{len(todo)}] {d}  {src}  {size/1e6:.1f} MB")
        except (urllib.error.URLError, ValueError, OSError) as e:
            print(f"[{i}/{len(todo)}] {d}  {src}  失败：{e}")
            failed.append((d, src, str(e)))
        if i < len(todo):
            time.sleep(DELAY)

    if failed:
        print(f"\n{len(failed)} 份没下成，重跑一次脚本会只补这几份：")
        for d, src, e in failed:
            print(f"  {d}  {src}  {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
