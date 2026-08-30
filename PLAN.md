# 图像编辑论文库建设规划

> 目标：2022–2026 图像编辑关键论文全量本地化 + 每篇一份可替代首次泛读的中文深读笔记
> 最后核对：2026-08-28

## 交付形态

```
image_edit_paper/
├── prompt.md                    ← 解读规范（用户提供，唯一标准）
├── PLAN.md                      ← 本文件
├── INDEX.md                     ← 总索引：按主题分组 + 演进脉络
├── 2022-11_InstructPix2Pix/
│   ├── paper.pdf                ← arXiv 原文
│   ├── 解读.md                  ← 11 节深读笔记
│   └── meta.json                ← arXiv ID / 日期 / 校验后字数 / token 用量
└── ...（每篇一个 YYYY-MM_简称 文件夹，按时间自然排序）
```

## 五个阶段

| 阶段 | 做什么 | 状态 |
| --- | --- | --- |
| 1. 选题 | 按 7 条技术脉络列候选论文 | 完成，67 篇 |
| 2. 核实 | 逐个抓 arxiv.org/abs 比对 citation_title / citation_date | 完成，67/67 匹配 |
| 3. 补近期 | 子代理检索 2025-07～2026-08 的新论文，同样逐个核实 ID | 进行中 |
| 4. 生产 | 下载 PDF → pypdf 抽正文 → DeepSeek v4 Pro → 校验 → 落盘 | 进行中 |
| 5. 沉淀 | INDEX.md 主题索引 + 演进脉络 | 待做 |

## 事实纪律怎么落地

**arXiv ID 是最容易出错的环节**——凭记忆写 ID 会张冠李戴。所以 67 个 ID 全部实抓
`https://arxiv.org/abs/<id>` 的 `citation_title` meta 标签比对，不匹配的直接剔除。
子代理找的新论文走同一道关卡。

**解读内容只以 PDF 正文为事实来源**。pipeline 把抽取的正文整篇塞给模型，
prompt.md 里「不确定就写论文未明确披露」的约束原样作为 system prompt。
模型看不到网上的二手评价，也就编不出「引用量」「社区反响」这类东西。

**机器校验挡住截断**。每篇生成后自动检查：H1 标题、11 个二级标题齐全、
中文字符数在区间内、结尾有 `<!-- COMPLETE -->`。不过就把失败原因回传重生成，最多 4 次。

## 论文选择的 7 条脉络

| 脉络 | 关心的问题 | 代表 |
| --- | --- | --- |
| 训练-free 扩散编辑 | 不训练，靠注意力/反演改图 | Prompt-to-Prompt、MasaCtrl、Plug-and-Play |
| 反演精度 | 真实图片怎么无损映回噪声 | Null-text Inversion、EDICT、ReNoise、RF-Inversion |
| 指令式编辑 | 说人话改图，数据从哪来 | InstructPix2Pix、MagicBrush、Emu Edit、UltraEdit |
| 条件控制 | 结构/身份/参考图怎么注入 | ControlNet、IP-Adapter、InstantID |
| 局部与对象级 | 抠图、补全、搬物体 | SAM、BrushNet、AnyDoor、MimicBrush |
| 统一多模态 | 理解与生成同一个模型 | OmniGen、BAGEL、FLUX.1 Kontext、Qwen-Image |
| 推理·RL·评测 | 想清楚再改、对齐人类偏好、怎么打分 | GoT、Flow-GRPO、RISEBench、ImgEdit |

## 成本

单篇实测：输入约 15k token（论文正文），输出约 8k token，耗时约 3 分钟，6 路并发。
解读由 DeepSeek v4 Pro 产出，不占主对话上下文；主对话只做编排、核实与索引。

## 未决

- **INDEX.md 是否转 Lark**：按 CLAUDE.md 默认应转公司 Lark 云文档，但每篇解读天然属于
  这个本地论文库（类似 docs/ 工程文档），保持本地。总索引等你确认是否要一份 Lark 版。
