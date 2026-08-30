#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, json, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")
THEME = {
 "训练-free 扩散编辑：靠注意力和反演改图": ["SDEdit","Prompt-to-Prompt","Imagic","DiffEdit","Plug-and-Play","pix2pix-zero","MasaCtrl","Cross-Image-Attention","StyleAligned","Self-Guidance","LEDITSpp","Blended-Latent-Diffusion","Add-it","editing-manifold"],
 "反演精度：真实图片怎么无损映回噪声": ["Null-text-Inversion","EDICT","ReNoise","RF-Inversion","RF-Solver-Edit","InfEdit","TurboEdit","directedit","cfg-inversion-fail"],
 "指令式编辑：说人话改图，以及数据从哪来": ["InstructPix2Pix","MagicBrush","HIVE","InstructDiffusion","MGIE","SmartEdit","Emu-Edit","Instruct-Imagen","HQ-Edit","SEED-Data-Edit","UltraEdit","AnyEdit","OmniEdit","SeedEdit","SeedEdit3","Step1X-Edit","ICEdit","implicit-preservation"],
 "条件控制：结构、身份、参考图怎么注入": ["ControlNet","T2I-Adapter","IP-Adapter","Concept-Sliders","InstantID","PhotoMaker","OminiControl","EasyControl","UNO","DreamO","In-Context-LoRA","ACEpp","care-edit","spatialfusion"],
 "个性化与主体保持": ["Textual-Inversion","DreamBooth","Custom-Diffusion","decompose-subject"],
 "局部与对象级：抠图、补全、搬物体": ["SAM","Inpaint-Anything","BrushNet","PowerPaint","AnyDoor","MimicBrush","Paint-by-Example","Imagen-Editor-EditBench","Insert-Anything","MagicQuill","edit-where-you-mean","moebius-inpainting"],
 "拖拽与点控编辑": ["DragGAN","DragDiffusion","DragonDiffusion","DiffEditor"],
 "统一多模态：理解与生成同一个模型": ["Transfusion","Show-o","Show-o2","OmniGen","OmniGen2","Emu3","Emu2","Janus-Pro","Chameleon","SEED-X","BAGEL","UniWorld-V1","UniReal","MetaQuery","BLIP3-o","Ovis-U1","VAR","nextflow","ug-fight-dpo","hydra-x"],
 "生成骨干：编辑方法赖以运行的底座": ["Latent-Diffusion","Classifier-Free-Guidance","SD3-RectifiedFlow","PixArt-alpha","FLUX-Kontext","Qwen-Image","HiDream-I1","rethink-global-text","tuna-2","masked-gen-transformer"],
 "推理、强化学习与评测": ["GoT","T2I-R1","Flow-GRPO","DanceGRPO","RISEBench","ImgEdit","KRIS-Bench","Complex-Edit"],
 "奖励模型与在线 RL（2025H2 起）": ["EditScore","EditReward","Edit-R1-UniWorld-V2","ThinkRL-Edit","reward-hacking-t2i","spatialreward-edit","qwen-image-rl","read-it-back","rl-no-edit-rewards"],
 "会推理再动手：think-then-edit": ["ReasonEdit","ChronoEdit","UniREditBench","unireason","coco-code-cot","meta-cot","mind-the-gap"],
 "编辑数据工程：三元组从哪来": ["GPT-Image-Edit-1.5M","Pico-Banana-400K","OpenGPT-4o-Image","NoHumansRequired","X2Edit","bootstrap-generator"],
 "2025H2–2026 的编辑与统一模型": ["Seedream4","HunyuanImage3","Emu3.5","Z-Image","Lumina-DiMOO","Qwen-Image-Layered","Qwen-Image-2.0","FireRed-Image-Edit","EditVerse","InstructX","DreamOmni2","VAREdit","ChordEdit","Kontinuous-Kontext","internvl-u","sensenova-u1","arm-unified"],
 "新一代评测：物理合理性与多轮": ["PICABench","EdiVal-Agent","IIE-Survey","reasoning-to-pixels","banana100","beyond-accuracy","edit-compass","lighting-edit-bench"],
}
info = {}
for d in os.listdir(PAPERS):
    fd = os.path.join(PAPERS, d)
    mt = os.path.join(fd, "meta.json")
    if not (os.path.isdir(fd) and re.match(r"^20\d\d-\d\d_", d) and os.path.exists(mt)): continue
    m = json.load(open(mt, encoding="utf-8"))
    md = open(os.path.join(fd, "解读.md"), encoding="utf-8").read()
    sec = re.search(r"## 1\. 30 秒定位\s*\n(.+?)(?=\n## )", md, re.S)
    one = ""
    if sec:
        t = re.sub(r"[*`#>\[\]()]|\n", "", sec.group(1)).strip()
        parts = [x for x in re.split(r"(?<=[。！？])", t) if x.strip()]
        one = parts[0] if parts else ""
        if len(one) > 96:            # 过长就在标点处截，不要断在词中间
            cut = max(one.rfind("，", 0, 94), one.rfind("；", 0, 94), one.rfind("：", 0, 94))
            one = (one[:cut] if cut > 40 else one[:94]) + "……"
    m["one"] = one; m["dir"] = d
    info[m["short"]] = m

lines = ["# 图像编辑论文库索引", "",
 f"> 读者：要系统补齐 2022–2026 图像编辑技术脉络的人",
 f"> 目标：按脉络挑论文，点进任意一篇能直接读完整深读笔记，不用再读原文",
 f"> 覆盖：{len(info)} 篇，{min(m['date'] for m in info.values())[:7].replace('/','-')} ～ {max(m['date'] for m in info.values())[:7].replace('/','-')}",
 f"> 最后核对：{datetime.date.today().isoformat()}", "",
 "## 0. 先说这个库怎么用", "",
 "每篇论文一个文件夹，里面是 `paper.pdf`（arXiv 原文）、`解读.md`（11 节中文深读）、",
 "`meta.json`（arXiv ID、日期、字数）。解读按 [prompt.md](prompt.md) 的规范写：",
 "先定位问题，再画数据流，然后拆公式、训练、推理、实验、选型、工程风险。",
 "**它的定位是替代第一次泛读**，不是替代精读——要抠实现细节仍然得回 PDF。", "",
 "所有 arXiv ID 都实抓 `arxiv.org/abs` 比对过标题与日期，不是凭记忆写的。", "",
 f"## 1. {len([k for k,v in THEME.items() if any(x in info for x in v)])} 条脉络", ""]
used = set()
for theme, shorts in THEME.items():
    have = [s for s in shorts if s in info]
    if not have: continue
    have.sort(key=lambda s: info[s]["date"])
    lines += [f"### {theme}", "", "| 时间 | 简称 | 论文标题 | 一句话 |", "| --- | --- | --- | --- |"]
    for s in have:
        m = info[s]; used.add(s)
        ttl = m["title"].replace("|", "/").replace("$", "")
        lines.append(f"| {m['date'][:7].replace('/','-')} | [{s}](../papers/{m['dir']}/解读.md) | {ttl} | {m['one']} |")
    lines.append("")
rest = sorted(set(info) - used, key=lambda s: info[s]["date"])
if rest:
    lines += ["### 其他", "", "| 时间 | 简称 | 论文标题 | 一句话 |", "| --- | --- | --- | --- |"]
    for s in rest:
        m = info[s]
        lines.append(f"| {m['date'][:7].replace('/','-')} | [{s}](../papers/{m['dir']}/解读.md) | {m['title'].replace('|','/')} | {m['one']} |")
    lines.append("")
lines += ["## 2. 可信度边界", "",
 "160 个 arXiv ID 全部实抓 `arxiv.org/abs` 比对过标题与日期；160 篇解读结构完整、篇幅达标、PDF 全部可解析。",
 "**但 2026 的 38 篇里有 33 篇是模型从 1123 篇候选里筛出来的，人工只定了标准**，还有图表信息丢失、公式失真等已知问题——",
 "详见 [总结分析.md](总结分析.md) 第 5 节，用之前先看那一节。", "",
 "## 3. 按时间的全量清单", "", "| 时间 | 简称 | arXiv | 解读字数 |", "| --- | --- | --- | --- |"]
for s in sorted(info, key=lambda s: (info[s]["date"], s)):
    m = info[s]
    lines.append(f"| {m['date'].replace('/','-')} | [{s}](../papers/{m['dir']}/解读.md) | [{m['arxiv_id']}]({m['url']}) | {m['cn_chars']} |")
open(os.path.join(ROOT, "docs", "INDEX.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("INDEX.md 已生成，收录", len(info), "篇")
