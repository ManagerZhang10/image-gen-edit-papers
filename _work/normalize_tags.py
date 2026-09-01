#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""规范化 _work/class_cache.json 的标签，并把基准类论文按本库既有约定归位。

三件事：
1. task 顺序统一成 ["生成","编辑"]；type 的空格统一（「奖励与RL」→「奖励与 RL」）。
2. 基准/综述类论文归到两条评测脉络。依据是本库已有成员的分界，不是我另定的：
   「推理、强化学习与评测」现有 Complex-Edit 2025-04、RISEBench 2025-04、
   ImgEdit 2025-05、KRIS-Bench 2025-05；「新一代评测：物理合理性与多轮」现有
   EdiVal-Agent 2025-09 起的全部。所以分界取 2025-09。
   只对「本库原先没归脉络」的 27 项生效——已经人工归好的一律不动。
3. 少数确实两栖的论文列成显式例外，每条写清理由。
"""
import json

CACHE = "_work/class_cache.json"
LM = json.load(open("_work/line_map.json", encoding="utf-8"))
EVAL_EARLY = "推理、强化学习与评测"
EVAL_LATE = "新一代评测：物理合理性与多轮"

# 两项四次调用都返回非 JSON，手工指定。都是评测类，归属按上面同一条分界规则。
MANUAL = {
    "2025-07_LMM4Edit": (["编辑"], "基准", EVAL_EARLY,
                         "LMM 做图像编辑评测；模型四次未返回合法 JSON，手工按标题与 §4 记录指定"),
    "2026-03_TIEdit-EditProbe": (["编辑"], "基准", EVAL_LATE,
                                 "编辑评测 + 中间层探针；模型四次未返回合法 JSON，手工指定"),
}

# 显式例外：同时给出方法/模型贡献的评测类论文，留在主题脉络里，不归评测
EXCEPT_KEEP_LINE = {
    "2025-06_RefEdit": "标题写明 A Benchmark and Method——同时给了指代表达的编辑方法，"
                       "留在「指令式编辑」比归评测更贴",
}


def main():
    c = json.load(open(CACHE, encoding="utf-8"))
    for d, (task, typ, line, why) in MANUAL.items():
        c[d] = {"task": task, "type": typ, "line": line, "reason": why, "source": "manual"}

    moved, fixed = [], 0
    for d, v in c.items():
        if "error" in v:
            print(f"!! 仍失败: {d}"); continue
        t = v.get("task") or []
        order = [x for x in ("生成", "编辑") if x in t]
        if order != t:
            v["task"] = order; fixed += 1
        if v.get("type") == "奖励与RL":
            v["type"] = "奖励与 RL"; fixed += 1

        if d in LM or d in MANUAL or d in EXCEPT_KEEP_LINE:
            continue                      # 已人工归好 / 已手工指定 / 显式例外，不动
        if v.get("type") in ("基准", "综述") and v.get("line") not in (EVAL_EARLY, EVAL_LATE):
            date = d[:7]                  # 目录名前缀就是 YYYY-MM
            tgt = EVAL_EARLY if date < "2025-09" else EVAL_LATE
            moved.append((d, v["type"], v["line"], tgt))
            v["line"] = tgt

    json.dump(c, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"规范化 {fixed} 处；按约定归位 {len(moved)} 项：")
    for d, ty, a, b in moved:
        print(f"   {d:32s} [{ty}] {a}  ->  {b}")
    for d, why in EXCEPT_KEEP_LINE.items():
        print(f"   例外保留 {d:26s} 在 {c[d]['line']} —— {why}")


if __name__ == "__main__":
    main()
