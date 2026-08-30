# 图像编辑论文库 2021–2026

[![papers](https://img.shields.io/badge/papers-186-2b7489)](#附二全量清单186-项每项一条核验过的原文直链)
[![notes](https://img.shields.io/badge/notes-1.23M_CJK_chars-4c9a2a)](#4-两批笔记格式和验收口径都不一样)
[![coverage](https://img.shields.io/badge/coverage-2021.08_--_2026.08-e07b39)](#2-五年读下来的结论)
[![links](https://img.shields.io/badge/source_links-181%2F186_byte--verified-1f883d)](#附二全量清单186-项每项一条核验过的原文直链)
[![license](https://img.shields.io/badge/license-CC_BY_4.0-777777)](LICENSE)

**186 篇图像编辑论文的中文深读笔记，2021-08 → 2026-08，合计 1,231,636 个汉字。**
每篇笔记都配一条核验过的原文直链——181 条与写笔记时用的本地 PDF 逐字节比对一致，1 条渲染版本存疑已标注，4 项确实没有独立论文。

*186 in-depth Chinese reading notes on image-editing papers (Aug 2021 – Aug 2026, 1.23M CJK characters). Every source link is byte-verified against the exact PDF the note was written from — see [附二](#附二全量清单186-项每项一条核验过的原文直链).*

> **读者**：要系统补齐图像编辑技术脉络的算法同学，或者要为某个具体方案（人像编辑、身份保持、局部保持、评测选型）找证据的人
> **目标**：读完这页知道该从哪儿进去、每篇笔记能替代什么、哪些结论可以直接拿去做决策、哪些必须回原文
> **元信息**：186 项 · 2021-08 ～ 2026-08 · 约 123 万中文字 · 维护者 [@ManagerYu10](https://github.com/ManagerYu10)
> **原文直链**：[附二](#附二全量清单186-项每项一条核验过的原文直链)有全部 186 项的直链——181 条 PDF 与本地副本逐字节对过，1 条标注版本存疑，4 项无独立论文给官方来源
> **授权**：[CC BY 4.0](LICENSE)——署名即可自由转载、改写、商用
> **最后核对**：2026-08-30

`papers/` 下每篇论文一个目录，里面是 `解读.md`（中文深读笔记）和 `meta.json`（arXiv ID、日期、字数、venue、引用量）。
**笔记的定位是替代第一次完整泛读**——读完能复述问题、画出数据流、解释关键公式、判断实验是否支持结论。
它不替代精读：要抠实现细节仍然得回 PDF。

---

## 0. 先破三个误解

| 你以为 | 实际 |
| --- | --- |
| clone 下来就有 182 篇论文 PDF | **PDF 不在仓库里**，3.3 GB 超出 GitHub 建议的仓库体积。但**每一篇的 PDF 直链都在 [附二](#附二全量清单186-项每项一条核验过的原文直链)**，点开就能读；要批量拉到本地用 [`scripts/fetch_pdfs.py`](scripts/fetch_pdfs.py)，约 10 分钟 |
| 186 篇笔记是同一套格式、同一个质量档 | **两批，格式和验收口径都不同**。160 篇是 11 节结构的深读（6500 字起），26 项是 2026-08-29 那轮补的决策型短笔记（2500 字起），另有 4 项根本没有独立论文，只是官方资料核验。见 [§3](#4-两批笔记格式和验收口径都不一样) |
| 笔记是人写的，可以直接引用 | **正文由 DeepSeek v4 Pro 依据 PDF 抽取的文字生成**，人定标准、做校验、抽查。图表里的信息模型读不到，公式符号会在 PDF 抽取时丢失。哪些能当依据、哪些不能，见 [§5](#6-可信度边界什么能当依据什么不能) |

---

## 1. 从哪儿开始读

| 你现在要干的事 | 从这里进 |
| --- | --- |
| 只想拿结论，不想读论文 | [§2](#2-五年读下来的结论)，就在本页——认知误区、五年的六个转折点、全领域没解决的六条 |
| 要找某一篇的原文或解读 | [附二](#附二全量清单186-项每项一条核验过的原文直链)，186 项按时间排，每行一条核验过的原文直链 + 解读链接 |
| 系统补齐五年脉络，不知道先读哪篇 | [INDEX.md](docs/INDEX.md) §1，15 条脉络分组，每篇一句话说清它解决什么 |
| 已经读了一批，想要跨论文的结论 | [总结分析.md](docs/总结分析.md)——五年的真正转折点、15 条脉络怎么互相咬合、全领域还没解决的问题。**只讲跨论文结论，不重复单篇内容** |
| 想先看一眼五年主线长什么样 | [主线.html](docs/主线.html)，clone 后用浏览器打开（GitHub 网页上不会渲染，只会显示源码） |
| 要给某个具体方案找证据（身份保持 / 局部保持 / 评测选型） | 直接进对应论文目录的 `解读.md`。第 8 节是实验证据表，第 10 节是工程判断与风险 |
| 要判断某篇论文的权威性、是不是真发表了、被引多少 | [LARK清单_权威性与影响力.md](docs/LARK清单_权威性与影响力.md) → [`docs/review/`](docs/review/) 下四份逐项 manifest |
| 想知道笔记是按什么标准写的 | [prompt.md](docs/prompt.md)（11 节深读规范）、[LARK论文短版解读_PROMPT.md](docs/LARK论文短版解读_PROMPT.md)（短版规范） |

---

## 2. 五年读下来的结论

下面三块是 [总结分析.md](docs/总结分析.md) 的核心结论，**原样搬到 README，打开仓库就能读，不用再点进去**。
完整版另有「十五条脉络怎么互相咬合」和「十五条脉络各自的结论」（每条千字级），在 [总结分析.md](docs/总结分析.md) 里。

⚠️ 归纳素材只有第一批 160 篇，2026-08-29 补的第二批 26 项没有参与，见 [§4](#4-两批笔记格式和验收口径都不一样)。

### 2.1 最容易想当然的那个认知错误

读者最容易想当然的一个认知错误是：只要把图像、指令和文本一起交给更大的统一多模态模型，编辑一致性和评估可靠性就会自动变好。

| 你以为 | 实际 |
|---|---|
| 统一多模态模型把源图、文本、目标图放进同一序列，未编辑区域自然保持不变 | 统一序列仍出现条件泄漏和像素漂移，InternVL-U 必须把理解特征与 VAE 潜变量解耦；Qwen-Image-Layered 需要输出多层 RGBA 才能显式隔离编辑区域 |
| 用更大的 VLM/奖励模型当裁判，评估与 RL 更可靠 | EdiVal-Agent 换 OWL-ViT 后人类一致率从 81.3% 跌到 53.67%；banana100 里传统 NR-IQA 给后轮退化图更好或同等分数；T2I-R1 的单一 VQA 奖励会被策略 hack |
| 合成编辑数据越多，下游模型越好 | NoHumansRequired 基准提升仅 +0.03 且置信区间重叠；OpenGPT-4o-Image 数据从 30k 扩到 40k 已有回退 |
| 强化学习进入生成轨迹后，推理编辑任务会稳定提升 | reward hacking 仍只能缓解不能根除，多篇只能靠提前停止、正则或选早 checkpoint 规避，DanceGRPO 只用 HPS 会产出油腻图像 |

这些失败共同说明，把“更大/更统一”当成路线本身会掩盖真正的瓶颈：细粒度跨图比较、局部信用分配、表示解耦。模型规模没有自动解决编辑中的局部保持与语义对齐矛盾，反而把问题转移到奖励设计、评测锚点和数据验证上。技术判断应聚焦于表示层级解耦和可验证局部事实，而不是默认统一模型会顺手解决编辑问题。

### 2.2 五年里真正的转折点

| 时间 | 转折 | 触发它的工作 | 之前怎么做 → 之后怎么做 |
|---|---|---|---|
| 2022 H2 | 编辑控制从外部掩码/噪声投影迁移到模型内部注意力表示 | Prompt-to-Prompt | 之前 SDEdit 加噪/掩码混合或 Blended-Latent-Diffusion 在潜空间按掩码混合，编辑区域由外部 mask 指定；之后交叉注意力图注入/引导，换词、加短语等语义编辑不再绑定像素级掩码 |
| 2022 H2–2023 H1 | 指令编辑从单图反演/无训练转向可训练的双条件扩散与配对数据合成 | InstructPix2Pix | 之前指令式编辑缺乏可扩展成对监督，真实图编辑多为 per-image inversion 或注意力注入；之后用 GPT-3 生成指令、Stable Diffusion + Prompt-to-Prompt 生成配对图，训练双条件潜扩散，MagicBrush、HIVE、HQ-Edit、UltraEdit 等后续沿用并改进该数据/条件范式 |
| 2023 H2 | 显式反演可被绕开，少步/免反演编辑可行 | InfEdit 的 DDCM 虚拟反演 | 之前真实图编辑先做 DDIM 反演或 Null-text Inversion 优化空文本嵌入，单图 40–120 秒；之后用特殊方差参数使去噪退化为一致性采样，ReNoise/TurboEdit 等少步模型直接适配，速度达数秒或亚秒 |
| 2024 H1 | 生成骨干从 UNet cross-attention 转向 MM-DiT token 共享注意力，条件 token 化 | SD3-RectifiedFlow | 之前 ControlNet/IP-Adapter 用特征加法或独立 cross-attention 注入条件，受 UNet 架构限制；之后 FLUX-Kontext、Qwen-Image 用序列拼接或双编码把参考图/文本直接放进同一序列，生成与编辑统一到同一 token 化底座 |
| 2025 H1 | 强化学习进入生成/编辑轨迹，推理步骤成为可训练策略 | Flow-GRPO、DanceGRPO | 之前 GoT 等只把显式推理链作为静态文本条件输入扩散模型；之后用 SDE 给确定性 ODE/流匹配采样注入随机探索，GRPO 组内优势训练生成模型，T2I-R1、Meta-CoT 等把规划/生成步骤作为策略优化 |
| 2025 H2–2026 H1 | 评估器自身可信度被质疑，评测从整体打分转向局部锚点/物理真值核对 | EdiVal-Agent 换 OWL-ViT 一致率暴跌；banana100 传统 NR-IQA 反向 | 之前用整图 VLM 开放打分或传统 NR-IQA 度量编辑质量；之后引入检测框 ROI 二值判断、HDR 开/关灯真值、场景图事实网格等可验证锚点，把“真伪”与“好不好”分开测量 |

这些转折之间不是单一因果链。Prompt-to-Prompt 建立的注意力控制被 InstructPix2Pix 直接用作合成配对图的编辑工具，后者把指令编辑从单图反演推进到可训练条件扩散；InfEdit 与少步骨干共同推动真实图编辑向免反演和实时化；SD3-RectifiedFlow 让生成与编辑共享 token 化底座，是 Flow-GRPO/DanceGRPO 在同一骨架上做 SDE 策略探索的前提。评估转折没有由上述任一转折直接触发，而是上游方法大量产出“看起来对”的结果后，评测端自身暴露出检测器替换和 NR-IQA 反向等不可信问题。证据最薄的是 InstructPix2Pix 这一条：素材对指令编辑线明确的后续转折是真实数据与 MLLM 编码器替代，而把它本身列为全局转折主要依赖后续多篇工作沿用其条件扩散与合成数据范式。

哪些算「转折」是判断题，不是算出来的。这里的标准是「之后大部分工作都改了做法」，而不是「这篇有影响力」——所以表里只有 6 行，第 3 节里更多有名的工作没进来。表末那段自己点出了证据最薄的一条。另外前两列的年份是我按素材里的论文日期改过的：模型原本给的是「早期/中期/后期」，评测那一行原写 2025 H2，但它引的 banana100 是 2026/04，所以改成 2025 H2–2026 H1。

#### 论文密度（库内 160 篇按半年）

| 半年 | 篇数 | |
| --- | --- | --- |
| 2021 H2 |  2 | ██ |
| 2022 H1 |  1 | █ |
| 2022 H2 | 13 | █████████████ |
| 2023 H1 | 11 | ███████████ |
| 2023 H2 | 16 | ████████████████ |
| 2024 H1 | 12 | ████████████ |
| 2024 H2 | 16 | ████████████████ |
| 2025 H1 | 26 | ██████████████████████████ |
| 2025 H2 | 25 | █████████████████████████ |
| 2026 H1 | 33 | █████████████████████████████████ |
| 2026 H2 |  5 | █████ |

⚠️ **这是库内密度，不是领域热度。**2026 前八个月的 38 篇是照着 2025 的月均密度（51 篇 / 12 个月）反推出来的配额，
不是「2026 就产出了这么多值得读的工作」。2022 那一头偏少则是另一个原因：早期工作被后续综述反复引用，容易识别，
所以收得准但收得少。怎么筛的、漏了什么，见第 5 节。

### 2.3 全领域还没解决的六条

| 问题 | 具体表现（点名论文和现象） | 为什么难 |
|---|---|---|
| 多轮编辑累积退化与长期一致性无法保证 | MagicBrush 显示多轮误差累积；implicit-preservation 的 OCCUR-Bench 遮挡恢复绝对一致性低；FLUX-Kontext 六轮后身份漂移和 artifacts；InstructX 复杂视频编辑中段崩溃；banana100 100轮复制后持续退化，Qwen-Image-Edit 多轮暴露偏差从 78.36 跌到 41.93 | 每轮编辑条件泄漏、误差累积，缺少自动权衡机制；模型难以跨轮追踪未编辑区域与身份 |
| 高频细节、文字渲染与身份保持受 VAE/潜空间限制 | NTI/EDICT/DirectEdit 指出重建无法超过 VAE 上界；SD3 16 通道 VAE 重建 FID 1.06；tuna-2 像素空间 rFID 差 FLUX VAE 一个量级；Chameleon tokenizer 重建上限；Janus-Pro 384×384 限制 OCR；Meta-CoT 文本编辑退化，CoCo LongText-Bench 落后 GPT-4o | 潜空间编码丢失稠密高频信息，离散/连续表示都难以精确绑定字符和身份；底层 token 容量限制 |
| 空间推理、计数、组合关系与精确几何编辑弱 | 脉络1空间移动/计数失败，Prompt-to-Prompt 无法两点换位；Imagen Editor、AnyDoor 细粒度计数/形状弱；DreamO 复杂空间关系低；FLUX-Kontext 把“移动咖啡”执行成加奶泡，HiDream GenEval Position 仅 0.60；GoT position 0.34、attribute binding 0.27；Z-Image 物体计数 0.78 | 文本-图像扩散难绑定位置/数量，缺乏显式空间或计数监督；单图 3D 理解不足，底模能力上限 |
| 自动指标/奖励模型/评估器与人类偏好错位，且可被 hack | HQ-Edit 方向相似度与人类偏好负相关；ICEdit 发现 CLIP 判据反而降低 GPT 分；PhotoMaker CLIP-T 与用户研究相反；T2I-R1 单一 VQA 奖励被 hack；DanceGRPO 只用 HPS 产出油腻图像；banana100 传统 NR-IQA 给后轮退化图更好分数；EdiVal-Agent 换 OWL-ViT 后一致率 53.67% | 全局标量无法表达细粒度跨图比较与像素级身份保持；奖励/评估模型自身盲区与策略同源，区域级信用分配缺失 |
| 训练/推理成本与保真度/延迟冲突，效率口径不统一 | Null-text Inversion 单图 40–120 秒；Imagic 每图 7–8 分钟；DragDiffusion 36–57 秒；EasyControl 1024×1024 25 步 16.3 秒；EditVerse 110,822 token 50 步约 349 秒；ThinkRL-Edit 编辑时间几乎翻倍；decompose-subject 两阶段 2 倍延迟 | 高保真需要多步/大模型，实时/端侧需要少步/小模型；VAE 和大 MLLM 延迟无法简单压缩，统一硬件口径缺失 |
| 合成数据/伪标签偏差与闭源教师模型锁死上限 | InstructPix2Pix 合成域偏差真实图泛化有限；GEdit-EN 仍低于 GPT-4o；OpenGPT-4o-Image 明确蒸馏上限；Pico-Banana 不能超过 Nano-Banana；NoHumansRequired 全合成分布风格偏差；MimicBrush 外 ID DINO-I 低于有参考掩码的 AnyDoor | 高质量成对编辑监督依赖闭源模型，自动生成有分布偏置，验证不可靠；下游最好只能逼近教师，难以超越 |

这六条里，**空间推理**和**评估错位**是被最多脉络同时点名的两条。前者决定编辑能不能可靠执行，后者决定你有没有办法知道它可靠——一个模型在自动指标上变好，可能只是学会了少改一点。

---

## 3. 仓库长什么样

```
image_edit_paper/
├── README.md                       ← 本文件。全部结论和 186 项全量清单都在这一页
├── LICENSE                         ← CC BY 4.0
│
├── papers/                         ← 186 个论文目录，名字就是 YYYY-MM_简称，按时间自然排序
│   ├── 2021-08_SDEdit/
│   │   ├── 解读.md                  ← 中文笔记（唯一正文）
│   │   ├── meta.json                ← arXiv ID、日期、标题、字数、venue、引用量
│   │   └── paper.pdf                ← 不在仓库里，跑 scripts/fetch_pdfs.py 下载
│   ├── ...
│   └── 2026-08_CPI-Bench/
│
├── docs/
│   ├── INDEX.md                     ← 总索引：15 条脉络 + 按时间全量清单
│   ├── 总结分析.md                   ← 跨论文结论：转折点、脉络咬合、未解问题
│   ├── 主线.html                     ← 五年主线的可视化时间轴（下载后本地浏览器打开）
│   ├── PLAN.md                       ← 建库规划与五个阶段
│   ├── prompt.md                     ← 11 节深读的写作规范（原样作为 system prompt）
│   ├── LARK论文短版解读_PROMPT.md      ← 短版解读的写作规范
│   ├── LARK清单_核验索引.md            ← 2026-08-29 那轮核验的总入口
│   ├── LARK清单_权威性与影响力.md       ← venue / 首发时间 / 引用量的口径与高引条目
│   └── review/                       ← 那轮核验的产出：4 份逐项 manifest + 4 份错误报告
│
├── scripts/
│   ├── pdf_sources.py               ← 直链推导规则 + 3 条例外（默认规则会取错的）
│   ├── fetch_pdfs.py                ← 按 meta.json 把 arXiv / CVF 原文拉回本地
│   └── verify_pdf_links.py          ← 核验附二那 182 条直链，逐条比对远端与本地字节数
│
└── _work/                          ← 生产管线脚本（只留 .py 和 pdf_link_check.json，日志和中间产物没进仓库）
```

---

## 4. 两批笔记，格式和验收口径都不一样

| | 第一批 | 第二批 |
| --- | --- | --- |
| 数量 | 160 篇 | 26 项 |
| 完成时间 | 2026-08-28 | 2026-08-29 |
| 标题形如 | `# 大白话深读《XXX》` | `# XXX：决策型详细阅读笔记` / `# XXX 官方资料核验笔记` |
| 结构 | 固定 11 个二级标题，机器校验齐全 | 8～9 节，覆盖决策信息即可，不追字数 |
| 中文正文长度 | 6502 – 8943 字 | 2510 – 7049 字（4 项无论文的核验笔记 330 – 732 字） |
| 收在哪 | [INDEX.md](docs/INDEX.md) §1 按脉络 + §3 按时间 | [INDEX.md](docs/INDEX.md) §4，以及 [`docs/review/`](docs/review/) 四份 manifest |
| 为什么这么定 | 目标是替代首次泛读，所以要求完整数据流和公式推导 | 目标是给具体方案做选型，[LARK清单_核验索引.md](docs/LARK清单_核验索引.md) 明确「不再机械追求 6500–8500 字」 |

第二批里有 4 项**没有独立论文**，笔记刻意只写官方资料和核验边界，目录里也不放 `paper.pdf`：

| 条目 | 一手来源 | 为什么单列 |
| --- | --- | --- |
| [FLUX.1](papers/2024-08_FLUX.1/解读.md) | Black Forest Labs 发布博客 / model card | 基础 FLUX.1 没有技术报告，只有 FLUX.1 Kontext 有（那篇在第一批里） |
| [Grok / Aurora](papers/2024-12_Grok-Aurora/解读.md) | [xAI 模型目录](https://docs.x.ai/developers/models) | 本轮没找到可核验的独立论文，应当作产品名而非研究条目 |
| [Qwen-Image-Edit-2511](papers/2025-12_Qwen-Image-Edit-2511/解读.md) | [Qwen 官方 model card](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | 2511 是 checkpoint 版本声明，没有独立论文、训练细节或消融 |
| [GPT Image 2](papers/2026-04_GPT-Image-2/解读.md) | [OpenAI 模型文档](https://developers.openai.com/api/docs/models/gpt-image-2) | 同上，产品文档不能替代可复核的架构与训练证据 |

⚠️ **不要拿这 4 项的产品说明去反推架构、训练数据或身份保持机制**。要纳入选型就在自有数据上实测，并单独记录调用版本和日期。

---

## 5. 把原文批量拉回本地

```bash
python3 scripts/fetch_pdfs.py            # 补齐所有缺的，约 182 份 / 3.3 GB / 10 分钟
python3 scripts/fetch_pdfs.py --list     # 只列缺什么，不下载
python3 scripts/fetch_pdfs.py 2024-11_OmniEdit   # 只下一篇
```

只用标准库，不需要装依赖。按 arXiv 要求节流到每 3 秒一份；断了重跑会只补没下成的。
Inter-Edit 只有 CVPR 2026 proceedings 版没有 arXiv 版，脚本从 `meta.json` 的 `url` 推出 CVF 的 PDF 直链。
下载到的 `paper.pdf` 被 `.gitignore` 挡住，不会误提交。

要重新核验[附二](#附二全量清单186-项每项一条核验过的原文直链)那批直链（口径见那一节）：

```bash
python3 scripts/verify_pdf_links.py                    # 全量，约 9 分钟，明细写 _work/pdf_link_check.json
python3 scripts/verify_pdf_links.py 2023-02_ControlNet # 只核一条
```

它只取每篇的前 1 KB（HTTP Range），不会把 3.3 GB 再下一遍。

---

## 6. 可信度边界：什么能当依据，什么不能

### 做过的校验

| 环节 | 怎么验的 | 结果 |
| --- | --- | --- |
| arXiv ID | 逐个实抓 `arxiv.org/abs`，比对 `citation_title` 与 `citation_date` | 第一批 160/160 吻合；2026 筛选轮 111/111 命中 |
| 结构完整 | 机器检查 H1、11 个二级标题、结尾 `<!-- COMPLETE -->` | 第一批 160/160 通过（第二批不适用这套检查） |
| PDF 可解析 | 大小 + pypdf 解析 | 182/182 存在且可解析 |
| 数字溯源 | 笔记里每个数字回 PDF 抽取文本比对 | 9214 个数字中 485 个未直接匹配（5.3%），逐篇看只有 2 篇超过 25%，两篇手工核过全是脚本误报 |
| venue / 引用量 | 55 个载体（对应 43 个目录）逐项查官方 proceedings、作者项目页、OpenAlex | 结果在 [`docs/review/`](docs/review/) 四份 manifest；其中 29 个目录的 `meta.json` 内联了这份记录 |

那 5.3% 未匹配是怎么回事：pypdf 会把表格单元格粘成一串（原文 `6.696.932.17` 实为 6.69 / 6.93 / 2.17），或把 `110K` 当成一个 token，正则匹配不上。累计手工抽查 8 篇没发现编造的数字，**但没有全量核完**。

### ⚠️ 已知会出错的地方

| 局限 | 说明 |
| --- | --- |
| 只读得到文字 | 图表、示意图、定性对比图没有进入模型，纯图里的信息解读不到 |
| 公式符号会丢 | PDF 抽取常丢下标、希腊字母和矩阵记号，**公式细节一律以 PDF 为准** |
| 枝节描述可能出错 | 已发现一例：Imagic 那篇把 Imagen/SD 说成「ImageNet 预训练模型基础」，不准确。数字溯源查不出这类错 |
| 未做交叉复核 | 每篇只生成一次（偏短的做过扩写），没有第二个模型独立复核结论 |
| 不含论文外信息 | 按 [prompt.md](docs/prompt.md) 刻意不写后续工作、社区评价。引用量只在 `meta.json` 和 `docs/review/` 里，不进正文 |
| 2026 的选题是模型判断 | 2026 那 38 篇里 33 篇是 DeepSeek 从 1123 篇检索结果里筛的，人工只定了标准和配额。**只由 2026 论文支撑的结论，用之前先看 [总结分析.md](docs/总结分析.md) §5** |

### 已知的三处对不上（2026-08-30 核）

| 现象 | 实际情况 |
| --- | --- |
| 14 个目录的 `meta.json` 里 `cn_chars` 比 `解读.md` 实际字数少 88～141 字 | 这 14 篇在 2026-08-29 那轮被追加了 `## 本轮决策核验补充（2026-08-29）` 一节，`cn_chars` 没跟着更新。正文没被改写，只是多了追加节 |
| [INDEX.md](docs/INDEX.md) §2 写「160 篇字数落在 6502–8830」 | 受上一条影响，实际上限已是 8943（MGIE）。区间没被截断，只是统计口径早于追加节 |
| [总结分析.md](docs/总结分析.md) §4 正文写「这七条里」，但表里只有 6 行 | 计数写错，**已于 2026-08-30 改成「这六条里」**。表格内容没动，六条未解问题本身是对的 |

---

## 7. 这批解读是怎么产出的

下载 PDF → pypdf 抽正文 → 整篇喂给 DeepSeek v4 Pro（[prompt.md](docs/prompt.md) 原样作为 system prompt）→ 机器校验结构和篇幅 → 不过就回传失败原因重生成，最多 4 次。
单篇约 15k token 输入、8k token 输出，6 路并发。选题、arXiv ID 核实和索引由人做。

管线脚本在 [`_work/`](_work/)：`pipeline.py` 编排，`synth.py` 生成，`factcheck.py` 做数字溯源，`make_index.py` 生成索引，`_work/2026/judge.py` 是 2026 那轮的逐篇打分。
建库的完整规划见 [PLAN.md](docs/PLAN.md)。日志和中间产物（PDF 抽取文本、批次日志、候选清单、被拒草稿）没有进仓库。

---

## 附一：速查表

**按脉络找论文**——[INDEX.md](docs/INDEX.md) §1 的 15 条：

训练-free 扩散编辑 · 反演精度 · 指令式编辑 · 条件控制 · 个性化与主体保持 · 局部与对象级 · 拖拽与点控编辑 · 统一多模态 · 生成骨干 · 推理/RL/评测 · 奖励模型与在线 RL · think-then-edit · 编辑数据工程 · 2025H2–2026 编辑与统一模型 · 新一代评测

**常见问题**

| 情况 | 怎么办 |
| --- | --- |
| `解读.md` 里的公式看着不对 | 以 PDF 为准。pypdf 抽取会丢下标和希腊字母，这是已知问题 |
| 想引用某个数字做决策 | 先看该数字后面的 § / Table / Figure 锚点，回 PDF 对一遍。规范要求每个数字带锚点 |
| 笔记里没提某个实验 | 可能是图里的信息。模型只读到了文字 |
| 想知道某篇是不是真发表了 | 查 `meta.json` 的 `publication.venue`；没有这个字段就查 [`docs/review/`](docs/review/) 四份 manifest；都没有就是本轮没核过 |
| 某篇 `解读.md` 只有 300～700 字 | 那是 4 项无独立论文的核验笔记，见 [§3](#4-两批笔记格式和验收口径都不一样) |
| `fetch_pdfs.py` 有几份下不下来 | 直接重跑，它只补缺的。arXiv 偶发 503，隔几分钟再试 |

**参考**

- [arXiv](https://arxiv.org/) — 所有 PDF 的来源
- [OpenAlex](https://openalex.org/) — `docs/review/` 里引用量的 provider（Semantic Scholar 返回 429 后统一回退到它）
- [CVF Open Access](https://openaccess.thecvf.com/) — CVPR / ICCV 正式 proceedings

---

## 附二：全量清单——186 项，每项一条核验过的原文直链

**「核验过」在这里是什么意思。**PDF 直链不是从 `meta.json` 的 arXiv ID 拼出来就算数的——
拼对了格式也可能指向另一篇。[`scripts/verify_pdf_links.py`](scripts/verify_pdf_links.py) 给每条链接发一个
1 KB 的 HTTP Range 请求，下面四项**全部**通过才标 `PDF`：

| 检查 | 排除掉的情况 |
| --- | --- |
| HTTP 206 | 链接失效、404、拿不到 |
| `Content-Type: application/pdf` | 返回的是 HTML 错误页或摘要页 |
| 前 4 字节是 `%PDF` | Content-Type 骗人，或重定向到了登录页 |
| **远端总字节数 == 本地 `paper.pdf` 字节数** | **链接能打开，但打开的不是本库读的那一篇** |

第四项才是关键：前三项只能证明链接活着，只有和本地那份对上字节数，才能证明它就是写出这篇 `解读.md` 的那个 PDF。

**2026-08-30 全量跑下来的结果**：186 项里 **181 条四项全过**，4 项没有独立论文（给官方来源），1 项存疑。
这轮核验实际揪出了 3 条错链，全部已修：

| 条目 | 原来的链接错在哪 | 现在给的 | 怎么确认的 |
| --- | --- | --- | --- |
| [FlowChef](papers/2024-12_FlowChef/解读.md) | arXiv `2412.00100` 已改题为 *Steering Rectified Flow Models in the Vector Field for Controlled Image Generation* 并大幅改写（13.9 MB），和本库读的不是一份 | ICCV 2025 proceedings 版 | sha256 与本地一致，且与 `meta.json` 里记的 `paper_sha256` 一致 |
| [ug-fight-dpo](papers/2026-03_ug-fight-dpo/解读.md) | 裸链 `arxiv.org/pdf/2603.17044` 稳定 404（复测 2 次） | 带版本号的 `…/2603.17044v1` | sha256 与本地一致 |
| [DICE](papers/2025-05_DICE/解读.md) ⚠️ | —— | arXiv v1，**但标了 ⚠️** | 见下 |

⚠️ **DICE 这一条要单独说。**arXiv 上只有 v1，标题、作者、日期都和本库对得上，链接指向的论文没错；
但 arXiv 版是 15 页 4,016,508 字节，而本库解读所依据的本地副本是 10 页 1,739,117 字节，少了附录、也没有 arXiv 页边戳。
**本地那份从哪来的已经追不到了（未验证）**，两者逐页文字无一页相同（排版不同）。读这篇请以 arXiv 版为准，
并注意解读可能没覆盖到 arXiv 版多出来的那 5 页。

表里的**解读字数**是 2026-08-30 当场从 `解读.md` 数的（口径与 `meta.json` 的 `cn_chars` 相同：U+4E00–U+9FFF），
所以不受 [§6](#6-可信度边界什么能当依据什么不能) 里那 14 个 `cn_chars` 过期的影响。要复算：`python3 scripts/verify_pdf_links.py`。

| 时间 | 简称（→ 解读） | 论文标题 | 原文 | 解读字数 |
| --- | --- | --- | --- | ---: |
| 2021-08-02 | [SDEdit](papers/2021-08_SDEdit/解读.md) | SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations | [PDF](https://arxiv.org/pdf/2108.01073) | 7249 |
| 2021-12-20 | [Latent-Diffusion](papers/2021-12_Latent-Diffusion/解读.md) | High-Resolution Image Synthesis with Latent Diffusion Models | [PDF](https://arxiv.org/pdf/2112.10752) | 7160 |
| 2022-06-06 | [Blended-Latent-Diffusion](papers/2022-06_Blended-Latent-Diffusion/解读.md) | Blended Latent Diffusion | [PDF](https://arxiv.org/pdf/2206.02779) | 6702 |
| 2022-07-26 | [Classifier-Free-Guidance](papers/2022-07_Classifier-Free-Guidance/解读.md) | Classifier-Free Diffusion Guidance | [PDF](https://arxiv.org/pdf/2207.12598) | 6581 |
| 2022-08-25 | [DreamBooth](papers/2022-08_DreamBooth/解读.md) | DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | [PDF](https://arxiv.org/pdf/2208.12242) | 6553 |
| 2022-08-02 | [Prompt-to-Prompt](papers/2022-08_Prompt-to-Prompt/解读.md) | Prompt-to-Prompt Image Editing with Cross Attention Control | [PDF](https://arxiv.org/pdf/2208.01626) | 7138 |
| 2022-08-02 | [Textual-Inversion](papers/2022-08_Textual-Inversion/解读.md) | An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion | [PDF](https://arxiv.org/pdf/2208.01618) | 6900 |
| 2022-10-20 | [DiffEdit](papers/2022-10_DiffEdit/解读.md) | DiffEdit: Diffusion-based semantic image editing with mask guidance | [PDF](https://arxiv.org/pdf/2210.11427) | 7215 |
| 2022-10-17 | [Imagic](papers/2022-10_Imagic/解读.md) | Imagic: Text-Based Real Image Editing with Diffusion Models | [PDF](https://arxiv.org/pdf/2210.09276) | 7049 |
| 2022-11-22 | [EDICT](papers/2022-11_EDICT/解读.md) | EDICT: Exact Diffusion Inversion via Coupled Transformations | [PDF](https://arxiv.org/pdf/2211.12446) | 6614 |
| 2022-11-17 | [InstructPix2Pix](papers/2022-11_InstructPix2Pix/解读.md) | InstructPix2Pix: Learning to Follow Image Editing Instructions | [PDF](https://arxiv.org/pdf/2211.09800) | 7603 |
| 2022-11-17 | [Null-text-Inversion](papers/2022-11_Null-text-Inversion/解读.md) | Null-text Inversion for Editing Real Images using Guided Diffusion Models | [PDF](https://arxiv.org/pdf/2211.09794) | 7202 |
| 2022-11-23 | [Paint-by-Example](papers/2022-11_Paint-by-Example/解读.md) | Paint by Example: Exemplar-based Image Editing with Diffusion Models | [PDF](https://arxiv.org/pdf/2211.13227) | 7577 |
| 2022-11-22 | [Plug-and-Play](papers/2022-11_Plug-and-Play/解读.md) | Plug-and-Play Diffusion Features for Text-Driven Image-to-Image Translation | [PDF](https://arxiv.org/pdf/2211.12572) | 7284 |
| 2022-12-08 | [Custom-Diffusion](papers/2022-12_Custom-Diffusion/解读.md) | Multi-Concept Customization of Text-to-Image Diffusion | [PDF](https://arxiv.org/pdf/2212.04488) | 7128 |
| 2022-12-13 | [Imagen-Editor-EditBench](papers/2022-12_Imagen-Editor-EditBench/解读.md) | Imagen Editor and EditBench: Advancing and Evaluating Text-Guided Image Inpainting | [PDF](https://arxiv.org/pdf/2212.06909) | 8394 |
| 2023-02-10 | [ControlNet](papers/2023-02_ControlNet/解读.md) | Adding Conditional Control to Text-to-Image Diffusion Models | [PDF](https://arxiv.org/pdf/2302.05543) | 7943 |
| 2023-02-16 | [T2I-Adapter](papers/2023-02_T2I-Adapter/解读.md) | T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | [PDF](https://arxiv.org/pdf/2302.08453) | 7127 |
| 2023-02-06 | [pix2pix-zero](papers/2023-02_pix2pix-zero/解读.md) | Zero-shot Image-to-Image Translation | [PDF](https://arxiv.org/pdf/2302.03027) | 6692 |
| 2023-03-16 | [HIVE](papers/2023-03_HIVE/解读.md) | HIVE: Harnessing Human Feedback for Instructional Visual Editing | [PDF](https://arxiv.org/pdf/2303.09618) | 7788 |
| 2023-04-13 | [Inpaint-Anything](papers/2023-04_Inpaint-Anything/解读.md) | Inpaint Anything: Segment Anything Meets Image Inpainting | [PDF](https://arxiv.org/pdf/2304.06790) | 8149 |
| 2023-04-17 | [MasaCtrl](papers/2023-04_MasaCtrl/解读.md) | MasaCtrl: Tuning-Free Mutual Self-Attention Control for Consistent Image Synthesis and Editing | [PDF](https://arxiv.org/pdf/2304.08465) | 6562 |
| 2023-04-13 | [Rich-Text](papers/2023-04_Rich-Text/解读.md) | Expressive Text-to-Image Generation with Rich Text | [PDF](https://arxiv.org/pdf/2304.06720) | 6817 |
| 2023-04-05 | [SAM](papers/2023-04_SAM/解读.md) | Segment Anything | [PDF](https://arxiv.org/pdf/2304.02643) | 6768 |
| 2023-05-18 | [DragGAN](papers/2023-05_DragGAN/解读.md) | Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold | [PDF](https://arxiv.org/pdf/2305.10973) | 7007 |
| 2023-05-29 | [InstructEdit](papers/2023-05_InstructEdit/解读.md) | InstructEdit: Improving Automatic Masks for Diffusion-based Image Editing With User Instructions | [PDF](https://arxiv.org/pdf/2305.18047) | 6897 |
| 2023-06-26 | [DragDiffusion](papers/2023-06_DragDiffusion/解读.md) | DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | [PDF](https://arxiv.org/pdf/2306.14435) | 7065 |
| 2023-06-16 | [MagicBrush](papers/2023-06_MagicBrush/解读.md) | MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | [PDF](https://arxiv.org/pdf/2306.10012) | 7080 |
| 2023-06-01 | [Self-Guidance](papers/2023-06_Self-Guidance/解读.md) | Diffusion Self-Guidance for Controllable Image Generation | [PDF](https://arxiv.org/pdf/2306.00986) | 7259 |
| 2023-07-18 | [AnyDoor](papers/2023-07_AnyDoor/解读.md) | AnyDoor: Zero-shot Object-level Image Customization | [PDF](https://arxiv.org/pdf/2307.09481) | 7129 |
| 2023-07-05 | [DragonDiffusion](papers/2023-07_DragonDiffusion/解读.md) | DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models | [PDF](https://arxiv.org/pdf/2307.02421) | 7518 |
| 2023-08-13 | [IP-Adapter](papers/2023-08_IP-Adapter/解读.md) | IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | [PDF](https://arxiv.org/pdf/2308.06721) | 7379 |
| 2023-09-07 | [InstructDiffusion](papers/2023-09_InstructDiffusion/解读.md) | InstructDiffusion: A Generalist Modeling Interface for Vision Tasks | [PDF](https://arxiv.org/pdf/2309.03895) | 6804 |
| 2023-09-29 | [MGIE](papers/2023-09_MGIE/解读.md) | Guiding Instruction-based Image Editing via Multimodal Large Language Models | [PDF](https://arxiv.org/pdf/2309.17102) | 8943 |
| 2023-09-30 | [PixArt-alpha](papers/2023-09_PixArt-alpha/解读.md) | PixArt-$alpha$: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis | [PDF](https://arxiv.org/pdf/2310.00426) | 6861 |
| 2023-11-20 | [Concept-Sliders](papers/2023-11_Concept-Sliders/解读.md) | Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models | [PDF](https://arxiv.org/pdf/2311.12092) | 7827 |
| 2023-11-06 | [Cross-Image-Attention](papers/2023-11_Cross-Image-Attention/解读.md) | Cross-Image Attention for Zero-Shot Appearance Transfer | [PDF](https://arxiv.org/pdf/2311.03335) | 7423 |
| 2023-11-16 | [Emu-Edit](papers/2023-11_Emu-Edit/解读.md) | Emu Edit: Precise Image Editing via Recognition and Generation Tasks | [PDF](https://arxiv.org/pdf/2311.10089) | 6854 |
| 2023-11-28 | [LEDITSpp](papers/2023-11_LEDITSpp/解读.md) | LEDITS++: Limitless Image Editing using Text-to-Image Models | [PDF](https://arxiv.org/pdf/2311.16711) | 6869 |
| 2023-12-20 | [Emu2](papers/2023-12_Emu2/解读.md) | Generative Multimodal Models are In-Context Learners | [PDF](https://arxiv.org/pdf/2312.13286) | 6701 |
| 2023-12-07 | [InfEdit](papers/2023-12_InfEdit/解读.md) | Inversion-Free Image Editing with Natural Language | [PDF](https://arxiv.org/pdf/2312.04965) | 6814 |
| 2023-12-07 | [PhotoMaker](papers/2023-12_PhotoMaker/解读.md) | PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | [PDF](https://arxiv.org/pdf/2312.04461) | 7001 |
| 2023-12-06 | [PowerPaint](papers/2023-12_PowerPaint/解读.md) | A Task is Worth One Word: Learning with Task Prompts for High-Quality Versatile Image Inpainting | [PDF](https://arxiv.org/pdf/2312.03594) | 7204 |
| 2023-12-11 | [SmartEdit](papers/2023-12_SmartEdit/解读.md) | SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models | [PDF](https://arxiv.org/pdf/2312.06739) | 6742 |
| 2023-12-04 | [StyleAligned](papers/2023-12_StyleAligned/解读.md) | Style Aligned Image Generation via Shared Attention | [PDF](https://arxiv.org/pdf/2312.02133) | 7216 |
| 2024-01-15 | [InstantID](papers/2024-01_InstantID/解读.md) | InstantID: Zero-shot Identity-Preserving Generation in Seconds | [PDF](https://arxiv.org/pdf/2401.07519) | 6825 |
| 2024-01-03 | [Instruct-Imagen](papers/2024-01_Instruct-Imagen/解读.md) | Instruct-Imagen: Image Generation with Multi-modal Instruction | [PDF](https://arxiv.org/pdf/2401.01952) | 7210 |
| 2024-02-04 | [DiffEditor](papers/2024-02_DiffEditor/解读.md) | DiffEditor: Boosting Accuracy and Flexibility on Diffusion-based Image Editing | [PDF](https://arxiv.org/pdf/2402.02583) | 7254 |
| 2024-03-11 | [BrushNet](papers/2024-03_BrushNet/解读.md) | BrushNet: A Plug-and-Play Image Inpainting Model with Decomposed Dual-Branch Diffusion | [PDF](https://arxiv.org/pdf/2403.06976) | 6745 |
| 2024-03-21 | [ReNoise](papers/2024-03_ReNoise/解读.md) | ReNoise: Real Image Inversion Through Iterative Noising | [PDF](https://arxiv.org/pdf/2403.14602) | 6706 |
| 2024-03-05 | [SD3-RectifiedFlow](papers/2024-03_SD3-RectifiedFlow/解读.md) | Scaling Rectified Flow Transformers for High-Resolution Image Synthesis | [PDF](https://arxiv.org/pdf/2403.03206) | 6564 |
| 2024-04-15 | [HQ-Edit](papers/2024-04_HQ-Edit/解读.md) | HQ-Edit: A High-Quality Dataset for Instruction-based Image Editing | [PDF](https://arxiv.org/pdf/2404.09990) | 7232 |
| 2024-04-22 | [SEED-X](papers/2024-04_SEED-X/解读.md) | SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation | [PDF](https://arxiv.org/pdf/2404.14396) | 6648 |
| 2024-04-03 | [VAR](papers/2024-04_VAR/解读.md) | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | [PDF](https://arxiv.org/pdf/2404.02905) | 8136 |
| 2024-05-16 | [Chameleon](papers/2024-05_Chameleon/解读.md) | Chameleon: Mixed-Modal Early-Fusion Foundation Models | [PDF](https://arxiv.org/pdf/2405.09818) | 8109 |
| 2024-05-07 | [SEED-Data-Edit](papers/2024-05_SEED-Data-Edit/解读.md) | SEED-Data-Edit Technical Report: A Hybrid Dataset for Instructional Image Editing | [PDF](https://arxiv.org/pdf/2405.04007) | 6626 |
| 2024-06-11 | [MimicBrush](papers/2024-06_MimicBrush/解读.md) | Zero-shot Image Editing with Reference Imitation | [PDF](https://arxiv.org/pdf/2406.07547) | 8536 |
| 2024-07-07 | [UltraEdit](papers/2024-07_UltraEdit/解读.md) | UltraEdit: Instruction-based Fine-Grained Image Editing at Scale | [PDF](https://arxiv.org/pdf/2407.05282) | 7074 |
| 2024-08-01 | [FLUX.1](papers/2024-08_FLUX.1/解读.md) | FLUX.1 Model Family | [官方来源](https://bfl.ai/blog/24-08-01-bfl) | 634 |
| 2024-08-26 | [I2EBench](papers/2024-08_I2EBench/解读.md) | I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing | [PDF](https://arxiv.org/pdf/2408.14180) | 2518 |
| 2024-08-22 | [Show-o](papers/2024-08_Show-o/解读.md) | Show-o: One Single Transformer to Unify Multimodal Understanding and Generation | [PDF](https://arxiv.org/pdf/2408.12528) | 7514 |
| 2024-08-20 | [Transfusion](papers/2024-08_Transfusion/解读.md) | Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model | [PDF](https://arxiv.org/pdf/2408.11039) | 7019 |
| 2024-08-01 | [TurboEdit](papers/2024-08_TurboEdit/解读.md) | TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models | [PDF](https://arxiv.org/pdf/2408.00735) | 6973 |
| 2024-09-27 | [Emu3](papers/2024-09_Emu3/解读.md) | Emu3: Next-Token Prediction is All You Need | [PDF](https://arxiv.org/pdf/2409.18869) | 7382 |
| 2024-09-17 | [OmniGen](papers/2024-09_OmniGen/解读.md) | OmniGen: Unified Image Generation | [PDF](https://arxiv.org/pdf/2409.11340) | 8139 |
| 2024-10-31 | [In-Context-LoRA](papers/2024-10_In-Context-LoRA/解读.md) | In-Context LoRA for Diffusion Transformers | [PDF](https://arxiv.org/pdf/2410.23775) | 6951 |
| 2024-10-14 | [RF-Inversion](papers/2024-10_RF-Inversion/解读.md) | Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations | [PDF](https://arxiv.org/pdf/2410.10792) | 7312 |
| 2024-11-11 | [Add-it](papers/2024-11_Add-it/解读.md) | Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models | [PDF](https://arxiv.org/pdf/2411.07232) | 7033 |
| 2024-11-24 | [AnyEdit](papers/2024-11_AnyEdit/解读.md) | AnyEdit: Mastering Unified High-Quality Image Editing for Any Idea | [PDF](https://arxiv.org/pdf/2411.15738) | 7500 |
| 2024-11-14 | [MagicQuill](papers/2024-11_MagicQuill/解读.md) | MagicQuill: An Intelligent Interactive Image Editing System | [PDF](https://arxiv.org/pdf/2411.09703) | 7389 |
| 2024-11-22 | [OminiControl](papers/2024-11_OminiControl/解读.md) | OminiControl: Minimal and Universal Control for Diffusion Transformer | [PDF](https://arxiv.org/pdf/2411.15098) | 6543 |
| 2024-11-11 | [OmniEdit](papers/2024-11_OmniEdit/解读.md) | OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision | [PDF](https://arxiv.org/pdf/2411.07199) | 7402 |
| 2024-11-07 | [RF-Solver-Edit](papers/2024-11_RF-Solver-Edit/解读.md) | Taming Rectified Flow for Inversion and Editing | [PDF](https://arxiv.org/pdf/2411.04746) | 7204 |
| 2024-11-11 | [SeedEdit](papers/2024-11_SeedEdit/解读.md) | SeedEdit: Align Image Re-Generation to Image Editing | [PDF](https://arxiv.org/pdf/2411.06686) | 7623 |
| 2024-11-27 | [FlowChef](papers/2024-12_FlowChef/解读.md) | FlowChef: Steering of Rectified Flow Models for Controlled Generations | [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Patel_FlowChef_Steering_of_Rectified_Flow_Models_for_Controlled_Generations_ICCV_2025_paper.pdf) | 4314 |
| 2024-12 | [Grok-Aurora](papers/2024-12_Grok-Aurora/解读.md) | Grok (Aurora) | [官方来源](https://docs.x.ai/developers/models) | 330 |
| 2024-12-10 | [UniReal](papers/2024-12_UniReal/解读.md) | UniReal: Universal Image Generation and Editing via Learning Real-world Dynamics | [PDF](https://arxiv.org/pdf/2412.07774) | 6953 |
| 2025-01-05 | [ACEpp](papers/2025-01_ACEpp/解读.md) | ACE++: Instruction-Based Image Creation and Editing via Context-Aware Content Filling | [PDF](https://arxiv.org/pdf/2501.02487) | 7487 |
| 2025-01-29 | [Janus-Pro](papers/2025-01_Janus-Pro/解读.md) | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | [PDF](https://arxiv.org/pdf/2501.17811) | 8116 |
| 2025-03-10 | [EasyControl](papers/2025-03_EasyControl/解读.md) | EasyControl: Adding Efficient and Flexible Control for Diffusion Transformer | [PDF](https://arxiv.org/pdf/2503.07027) | 7188 |
| 2025-03-13 | [GoT](papers/2025-03_GoT/解读.md) | GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing | [PDF](https://arxiv.org/pdf/2503.10639) | 7356 |
| 2025-04-17 | [Complex-Edit](papers/2025-04_Complex-Edit/解读.md) | $texttt{Complex-Edit}$: CoT-Like Instruction Generation for Complexity-Controllable Image Editing Benchmark | [PDF](https://arxiv.org/pdf/2504.13143) | 8329 |
| 2025-04-23 | [DreamO](papers/2025-04_DreamO/解读.md) | DreamO: A Unified Framework for Image Customization | [PDF](https://arxiv.org/pdf/2504.16915) | 7727 |
| 2025-04-29 | [ICEdit](papers/2025-04_ICEdit/解读.md) | In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer | [PDF](https://arxiv.org/pdf/2504.20690) | 6865 |
| 2025-04-21 | [Insert-Anything](papers/2025-04_Insert-Anything/解读.md) | Insert Anything: Image Insertion via In-Context Editing in DiT | [PDF](https://arxiv.org/pdf/2504.15009) | 6580 |
| 2025-04-08 | [MetaQuery](papers/2025-04_MetaQuery/解读.md) | Transfer between Modalities with MetaQueries | [PDF](https://arxiv.org/pdf/2504.06256) | 7502 |
| 2025-04-03 | [RISEBench](papers/2025-04_RISEBench/解读.md) | Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing | [PDF](https://arxiv.org/pdf/2504.02826) | 7847 |
| 2025-04-24 | [Step1X-Edit](papers/2025-04_Step1X-Edit/解读.md) | Step1X-Edit: A Practical Framework for General Image Editing | [PDF](https://arxiv.org/pdf/2504.17761) | 7396 |
| 2025-04-02 | [UNO](papers/2025-04_UNO/解读.md) | Less-to-More Generalization: Unlocking More Controllability by In-Context Generation | [PDF](https://arxiv.org/pdf/2504.02160) | 7202 |
| 2025-05-20 | [BAGEL](papers/2025-05_BAGEL/解读.md) | Emerging Properties in Unified Multimodal Pretraining | [PDF](https://arxiv.org/pdf/2505.14683) | 7170 |
| 2025-05-14 | [BLIP3-o](papers/2025-05_BLIP3-o/解读.md) | BLIP3-o: A Family of Fully Open Unified Multimodal Models-Architecture, Training and Dataset | [PDF](https://arxiv.org/pdf/2505.09568) | 6887 |
| 2025-05-26 | [DICE](papers/2025-05_DICE/解读.md) | What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models | [PDF](https://arxiv.org/pdf/2505.20405) ⚠️ | 3306 |
| 2025-05-12 | [DanceGRPO](papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | [PDF](https://arxiv.org/pdf/2505.07818) | 7294 |
| 2025-05-22 | [Everyday-Image-Editing](papers/2025-05_Everyday-Image-Editing/解读.md) | Understanding Generative AI Capabilities in Everyday Image Editing Tasks | [PDF](https://arxiv.org/pdf/2505.16181) | 2986 |
| 2025-05-08 | [Flow-GRPO](papers/2025-05_Flow-GRPO/解读.md) | Flow-GRPO: Training Flow Matching Models via Online RL | [PDF](https://arxiv.org/pdf/2505.05470) | 6502 |
| 2025-05-16 | [GIE-Bench](papers/2025-05_GIE-Bench/解读.md) | GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing | [PDF](https://arxiv.org/pdf/2505.11493) | 2670 |
| 2025-05-01 | [HATIE](papers/2025-05_HATIE/解读.md) | Towards Scalable Human-aligned Benchmark for Text-guided Image Editing | [PDF](https://arxiv.org/pdf/2505.00502) | 6842 |
| 2025-05-28 | [HiDream-I1](papers/2025-05_HiDream-I1/解读.md) | HiDream-I1: A High-Efficient Image Generative Foundation Model with Sparse Diffusion Transformer | [PDF](https://arxiv.org/pdf/2505.22705) | 7337 |
| 2025-05-26 | [ImgEdit](papers/2025-05_ImgEdit/解读.md) | ImgEdit: A Unified Image Editing Dataset and Benchmark | [PDF](https://arxiv.org/pdf/2505.20275) | 7451 |
| 2025-05-22 | [KRIS-Bench](papers/2025-05_KRIS-Bench/解读.md) | KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models | [PDF](https://arxiv.org/pdf/2505.16707) | 7494 |
| 2025-05-01 | [T2I-R1](papers/2025-05_T2I-R1/解读.md) | T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT | [PDF](https://arxiv.org/pdf/2505.00703) | 6876 |
| 2025-06-15 | [BPM](papers/2025-06_BPM/解读.md) | Balancing Preservation and Modification: A Region and Semantic Aware Metric for Instruction-Based Image Editing | [PDF](https://arxiv.org/pdf/2506.13827) | 2528 |
| 2025-06-15 | [ComplexBench-Edit](papers/2025-06_ComplexBench-Edit/解读.md) | ComplexBench-Edit: Benchmarking Complex Instruction-Driven Image Editing via Compositional Dependencies | [PDF](https://arxiv.org/pdf/2506.12830) | 2534 |
| 2025-06-17 | [FLUX-Kontext](papers/2025-06_FLUX-Kontext/解读.md) | FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space | [PDF](https://arxiv.org/pdf/2506.15742) | 8679 |
| 2025-06-23 | [OmniGen2](papers/2025-06_OmniGen2/解读.md) | OmniGen2: Towards Instruction-Aligned Multimodal Generation | [PDF](https://arxiv.org/pdf/2506.18871) | 6695 |
| 2025-06-29 | [Ovis-U1](papers/2025-06_Ovis-U1/解读.md) | Ovis-U1 Technical Report | [PDF](https://arxiv.org/pdf/2506.23044) | 6716 |
| 2025-06-03 | [RefEdit](papers/2025-06_RefEdit/解读.md) | RefEdit: A Benchmark and Method for Improving Instruction-based Image Editing Model on Referring Expressions | [PDF](https://arxiv.org/pdf/2506.03448) | 2516 |
| 2025-06-05 | [SeedEdit3](papers/2025-06_SeedEdit3/解读.md) | SeedEdit 3.0: Fast and High-Quality Generative Image Editing | [PDF](https://arxiv.org/pdf/2506.05083) | 7643 |
| 2025-06-18 | [Show-o2](papers/2025-06_Show-o2/解读.md) | Show-o2: Improved Native Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2506.15564) | 6918 |
| 2025-06-03 | [UniWorld-V1](papers/2025-06_UniWorld-V1/解读.md) | UniWorld-V1: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation | [PDF](https://arxiv.org/pdf/2506.03147) | 6657 |
| 2025-07-28 | [GPT-Image-Edit-1.5M](papers/2025-07_GPT-Image-Edit-1.5M/解读.md) | GPT-IMAGE-EDIT-1.5M: A Million-Scale, GPT-Generated Image Dataset | [PDF](https://arxiv.org/pdf/2507.21033) | 6615 |
| 2025-07-22 | [LMM4Edit](papers/2025-07_LMM4Edit/解读.md) | LMM4Edit: Benchmarking and Evaluating Multimodal Image Editing with LMMs | [PDF](https://arxiv.org/pdf/2507.16193) | 2544 |
| 2025-07-18 | [NoHumansRequired](papers/2025-07_NoHumansRequired/解读.md) | NoHumansRequired: Autonomous High-Quality Image Editing Triplet Mining | [PDF](https://arxiv.org/pdf/2507.14119) | 6730 |
| 2025-08-04 | [Qwen-Image](papers/2025-08_Qwen-Image/解读.md) | Qwen-Image Technical Report | [PDF](https://arxiv.org/pdf/2508.02324) | 7310 |
| 2025-08-21 | [VAREdit](papers/2025-08_VAREdit/解读.md) | Visual Autoregressive Modeling for Instruction-Guided Image Editing | [PDF](https://arxiv.org/pdf/2508.15772) | 7076 |
| 2025-08-11 | [X2Edit](papers/2025-08_X2Edit/解读.md) | X2Edit: Revisiting Arbitrary-Instruction Image Editing through Self-Constructed Data and Task-Aware Representation Learning | [PDF](https://arxiv.org/pdf/2508.07607) | 6789 |
| 2025-09-16 | [EdiVal-Agent](papers/2025-09_EdiVal-Agent/解读.md) | EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing | [PDF](https://arxiv.org/pdf/2509.13399) | 6599 |
| 2025-09-30 | [EditReward](papers/2025-09_EditReward/解读.md) | EditReward: A Human-Aligned Reward Model for Instruction-Guided Image Editing | [PDF](https://arxiv.org/pdf/2509.26346) | 7572 |
| 2025-09-28 | [EditScore](papers/2025-09_EditScore/解读.md) | EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling | [PDF](https://arxiv.org/pdf/2509.23909) | 6719 |
| 2025-09-24 | [EditVerse](papers/2025-09_EditVerse/解读.md) | EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning | [PDF](https://arxiv.org/pdf/2509.20360) | 7231 |
| 2025-09-28 | [HunyuanImage3](papers/2025-09_HunyuanImage3/解读.md) | HunyuanImage 3.0 Technical Report | [PDF](https://arxiv.org/pdf/2509.23951) | 6546 |
| 2025-09-29 | [OpenGPT-4o-Image](papers/2025-09_OpenGPT-4o-Image/解读.md) | OpenGPT-4o-Image: A Comprehensive Dataset for Advanced Image Generation and Editing | [PDF](https://arxiv.org/pdf/2509.24900) | 7651 |
| 2025-09-24 | [Seedream4](papers/2025-09_Seedream4/解读.md) | Seedream 4.0: Toward Next-generation Multimodal Image Generation | [PDF](https://arxiv.org/pdf/2509.20427) | 6611 |
| 2025-10-05 | [ChronoEdit](papers/2025-10_ChronoEdit/解读.md) | ChronoEdit: Towards Temporal Reasoning for Image Editing and World Simulation | [PDF](https://arxiv.org/pdf/2510.04290) | 6825 |
| 2025-10-08 | [DreamOmni2](papers/2025-10_DreamOmni2/解读.md) | DreamOmni2: Multimodal Instruction-based Editing and Generation | [PDF](https://arxiv.org/pdf/2510.06679) | 6564 |
| 2025-10-19 | [Edit-R1-UniWorld-V2](papers/2025-10_Edit-R1-UniWorld-V2/解读.md) | Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback | [PDF](https://arxiv.org/pdf/2510.16888) | 6542 |
| 2025-10-30 | [Emu3.5](papers/2025-10_Emu3.5/解读.md) | Emu3.5: Native Multimodal Models are World Learners | [PDF](https://arxiv.org/pdf/2510.26583) | 7580 |
| 2025-10-09 | [InstructX](papers/2025-10_InstructX/解读.md) | InstructX: Towards Unified Visual Editing with MLLM Guidance | [PDF](https://arxiv.org/pdf/2510.08485) | 6671 |
| 2025-10-09 | [Kontinuous-Kontext](papers/2025-10_Kontinuous-Kontext/解读.md) | Kontinuous Kontext: Continuous Strength Control for Instruction-based Image Editing | [PDF](https://arxiv.org/pdf/2510.08532) | 8551 |
| 2025-10-07 | [Lumina-DiMOO](papers/2025-10_Lumina-DiMOO/解读.md) | Lumina-DiMOO: An Omni Diffusion Large Language Model for Multi-Modal Generation and Understanding | [PDF](https://arxiv.org/pdf/2510.06308) | 7291 |
| 2025-10-20 | [PICABench](papers/2025-10_PICABench/解读.md) | PICABench: How Far Are We from Physically Realistic Image Editing? | [PDF](https://arxiv.org/pdf/2510.17681) | 7739 |
| 2025-10-22 | [Pico-Banana-400K](papers/2025-10_Pico-Banana-400K/解读.md) | Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing | [PDF](https://arxiv.org/pdf/2510.19808) | 7750 |
| 2025-11-27 | [ReasonEdit](papers/2025-11_ReasonEdit/解读.md) | ReasonEdit: Towards Reasoning-Enhanced Image Editing Models | [PDF](https://arxiv.org/pdf/2511.22625) | 7349 |
| 2025-11-03 | [UniREditBench](papers/2025-11_UniREditBench/解读.md) | UniREditBench: A Unified Reasoning-based Image Editing Benchmark | [PDF](https://arxiv.org/pdf/2511.01295) | 7321 |
| 2025-11-27 | [Z-Image](papers/2025-11_Z-Image/解读.md) | Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer | [PDF](https://arxiv.org/pdf/2511.22699) | 6667 |
| 2025-12-04 | [I2I-Bench](papers/2025-12_I2I-Bench/解读.md) | I2I-Bench: A Comprehensive Benchmark Suite for Image-to-Image Editing Models | [PDF](https://arxiv.org/pdf/2512.04660) | 7049 |
| 2025-12-17 | [Qwen-Image-Edit-2511](papers/2025-12_Qwen-Image-Edit-2511/解读.md) | Qwen-Image-Edit-2511 | [官方来源](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | 666 |
| 2025-12-17 | [Qwen-Image-Layered](papers/2025-12_Qwen-Image-Layered/解读.md) | Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition | [PDF](https://arxiv.org/pdf/2512.15603) | 7109 |
| 2025-11-29 | [WiseEdit](papers/2025-12_WiseEdit/解读.md) | WiseEdit: Benchmarking Cognition- and Creativity-Informed Image Editing | [PDF](https://arxiv.org/pdf/2512.00387) | 2593 |
| 2026-01-06 | [ThinkRL-Edit](papers/2026-01_ThinkRL-Edit/解读.md) | ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing | [PDF](https://arxiv.org/pdf/2601.03467) | 7196 |
| 2026-01-05 | [nextflow](papers/2026-01_nextflow/解读.md) | NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation | [PDF](https://arxiv.org/pdf/2601.02204) | 7320 |
| 2026-01-06 | [reward-hacking-t2i](papers/2026-01_reward-hacking-t2i/解读.md) | Understanding Reward Hacking in Text-to-Image Reinforcement Learning | [PDF](https://arxiv.org/pdf/2601.03468) | 7524 |
| 2026-02-22 | [ChordEdit](papers/2026-02_ChordEdit/解读.md) | ChordEdit: One-Step Low-Energy Transport for Image Editing | [PDF](https://arxiv.org/pdf/2602.19083) | 7579 |
| 2026-02-12 | [FireRed-Image-Edit](papers/2026-02_FireRed-Image-Edit/解读.md) | FireRed-Image-Edit-1.0 Technical Report | [PDF](https://arxiv.org/pdf/2602.13344) | 7109 |
| 2026-02-02 | [VIBE](papers/2026-02_VIBE/解读.md) | How Well Do Models Follow Visual Instructions? VIBE: A Systematic Benchmark for Visual Instruction-Driven Image Editing | [PDF](https://arxiv.org/pdf/2602.01851) | 2564 |
| 2026-02-09 | [reasoning-to-pixels](papers/2026-02_reasoning-to-pixels/解读.md) | From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2602.08336) | 6985 |
| 2026-02-09 | [rethink-global-text](papers/2026-02_rethink-global-text/解读.md) | Rethinking Global Text Conditioning in Diffusion Transformers | [PDF](https://arxiv.org/pdf/2602.09268) | 7486 |
| 2026-02-07 | [spatialreward-edit](papers/2026-02_spatialreward-edit/解读.md) | SpatialReward: Bridging the Perception Gap in Online RL for Image Editing via Explicit Spatial Reasoning | [PDF](https://arxiv.org/pdf/2602.07458) | 7019 |
| 2026-02-02 | [unireason](papers/2026-02_unireason/解读.md) | UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing | [PDF](https://arxiv.org/pdf/2602.02437) | 7070 |
| 2026-03-30 | [GEditBench-v2](papers/2026-03_GEditBench-v2/解读.md) | GEditBench v2: A Human-Aligned Benchmark for General Image Editing | [PDF](https://arxiv.org/pdf/2603.28547) | 3755 |
| 2026-03-16 | [Omni-IIE-Bench](papers/2026-03_Omni-IIE-Bench/解读.md) | Omni IIE Bench: Benchmarking the Practical Capabilities of Image Editing Models | [PDF](https://arxiv.org/pdf/2603.16944) | 3225 |
| 2026-03-20 | [TIEdit-EditProbe](papers/2026-03_TIEdit-EditProbe/解读.md) | Evaluating Image Editing with LLMs: A Comprehensive Benchmark and Intermediate-Layer Probing Approach | [PDF](https://arxiv.org/pdf/2603.19775) | 2864 |
| 2026-03-09 | [care-edit](papers/2026-03_care-edit/解读.md) | CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing | [PDF](https://arxiv.org/pdf/2603.08589) | 6830 |
| 2026-03-09 | [coco-code-cot](papers/2026-03_coco-code-cot/解读.md) | CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation | [PDF](https://arxiv.org/pdf/2603.08652) | 6950 |
| 2026-03-31 | [editing-manifold](papers/2026-03_editing-manifold/解读.md) | Editing on the Generative Manifold: A Theoretical and Empirical Study of General Diffusion-Based Image Editing Trade-offs | [PDF](https://arxiv.org/pdf/2603.29736) | 7110 |
| 2026-03-10 | [internvl-u](papers/2026-03_internvl-u/解读.md) | InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing | [PDF](https://arxiv.org/pdf/2603.09877) | 6642 |
| 2026-03-17 | [ug-fight-dpo](papers/2026-03_ug-fight-dpo/解读.md) | Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2603.17044v1) | 6969 |
| 2026-04-21 | [GPT-Image-2](papers/2026-04_GPT-Image-2/解读.md) | GPT Image 2 | [官方来源](https://developers.openai.com/api/docs/models/gpt-image-2) | 732 |
| 2026-04-22 | [GSI-Bench](papers/2026-04_GSI-Bench/解读.md) | Exploring Spatial Intelligence from a Generative Perspective | [PDF](https://arxiv.org/pdf/2604.20570) | 2510 |
| 2026-04-03 | [banana100](papers/2026-04_banana100/解读.md) | Banana100: Breaking NR-IQA Metrics by 100 Iterative Image Replications with Nano Banana Pro | [PDF](https://arxiv.org/pdf/2604.03400) | 8186 |
| 2026-04-27 | [beyond-accuracy](papers/2026-04_beyond-accuracy/解读.md) | Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2604.25072) | 7280 |
| 2026-04-26 | [edit-where-you-mean](papers/2026-04_edit-where-you-mean/解读.md) | Edit Where You Mean: Region-Aware Adapter Injection for Mask-Free Local Image Editing | [PDF](https://arxiv.org/pdf/2604.23763) | 6989 |
| 2026-04-27 | [meta-cot](papers/2026-04_meta-cot/解读.md) | Meta-CoT: Enhancing Granularity and Generalization in Image Editing | [PDF](https://arxiv.org/pdf/2604.24625) | 6900 |
| 2026-04-29 | [spatialfusion](papers/2026-04_spatialfusion/解读.md) | SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness | [PDF](https://arxiv.org/pdf/2604.26341) | 6812 |
| 2026-04-27 | [tuna-2](papers/2026-04_tuna-2/解读.md) | Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation | [PDF](https://arxiv.org/pdf/2604.24763) | 6618 |
| 2026-05-29 | [PaintBench](papers/2026-05_PaintBench/解读.md) | PaintBench: Deterministic Evaluation of Precise Visual Editing | [PDF](https://arxiv.org/pdf/2606.00188) | 3038 |
| 2026-05-11 | [Qwen-Image-2.0](papers/2026-05_Qwen-Image-2.0/解读.md) | Qwen-Image-2.0 Technical Report | [PDF](https://arxiv.org/pdf/2605.10730) | 8086 |
| 2026-05-20 | [decompose-subject](papers/2026-05_decompose-subject/解读.md) | Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction | [PDF](https://arxiv.org/pdf/2605.20807) | 7064 |
| 2026-05-04 | [directedit](papers/2026-05_directedit/解读.md) | DirectEdit: Step-Level Accurate Inversion for Flow-Based Image Editing | [PDF](https://arxiv.org/pdf/2605.02417) | 7200 |
| 2026-05-13 | [edit-compass](papers/2026-05_edit-compass/解读.md) | Edit-Compass &amp; EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling | [PDF](https://arxiv.org/pdf/2605.13062) | 6567 |
| 2026-05-11 | [masked-gen-transformer](papers/2026-05_masked-gen-transformer/解读.md) | Masked Generative Transformer Is What You Need for Image Editing | [PDF](https://arxiv.org/pdf/2605.10859) | 6797 |
| 2026-05-12 | [sensenova-u1](papers/2026-05_sensenova-u1/解读.md) | SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture | [PDF](https://arxiv.org/pdf/2605.12500) | 6907 |
| 2026-06-01 | [Inter-Edit](papers/2026-06_Inter-Edit/解读.md) | Inter-Edit: First Benchmark for Interactive Instruction-Based Image Editing | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Inter-Edit_First_Benchmark_for_Interactive_Instruction-Based_Image_Editing_CVPR_2026_paper.pdf) | 2661 |
| 2026-06-09 | [arm-unified](papers/2026-06_arm-unified/解读.md) | ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations | [PDF](https://arxiv.org/pdf/2606.11188) | 7433 |
| 2026-06-02 | [bootstrap-generator](papers/2026-06_bootstrap-generator/解读.md) | Bootstrap Your Generator: Unpaired Visual Editing with Flow Matching | [PDF](https://arxiv.org/pdf/2606.03911) | 7686 |
| 2026-06-11 | [hydra-x](papers/2026-06_hydra-x/解读.md) | HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers | [PDF](https://arxiv.org/pdf/2606.13289) | 6583 |
| 2026-06-25 | [lighting-edit-bench](papers/2026-06_lighting-edit-bench/解读.md) | Do Image Editing Models Understand Lighting? | [PDF](https://arxiv.org/pdf/2606.26738) | 6897 |
| 2026-06-14 | [mind-the-gap](papers/2026-06_mind-the-gap/解读.md) | Mind the Gap: Diagnosing Constraint Discovery Failures in Text-in-Image Editing | [PDF](https://arxiv.org/pdf/2606.15982) | 6741 |
| 2026-06-17 | [moebius-inpainting](papers/2026-06_moebius-inpainting/解读.md) | Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance | [PDF](https://arxiv.org/pdf/2606.19195) | 6843 |
| 2026-06-25 | [qwen-image-rl](papers/2026-06_qwen-image-rl/解读.md) | Qwen-Image-2.0-RL Technical Report | [PDF](https://arxiv.org/pdf/2606.27608) | 8108 |
| 2026-07-28 | [IIE-Survey](papers/2026-07_IIE-Survey/解读.md) | Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications | [PDF](https://arxiv.org/pdf/2607.25642) | 8309 |
| 2026-07-06 | [cfg-inversion-fail](papers/2026-07_cfg-inversion-fail/解读.md) | When Does High-CFG Diffusion Inversion Fail? A Controlled Study of Prompt--Latent Interactions | [PDF](https://arxiv.org/pdf/2607.04731) | 6682 |
| 2026-07-08 | [implicit-preservation](papers/2026-07_implicit-preservation/解读.md) | Making Implicit Preservation Intent Explicit in Conversational Image Editing | [PDF](https://arxiv.org/pdf/2607.07051) | 6823 |
| 2026-07-13 | [read-it-back](papers/2026-07_read-it-back/解读.md) | Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation | [PDF](https://arxiv.org/pdf/2607.11886) | 6611 |
| 2026-08-14 | [CPI-Bench](papers/2026-08_CPI-Bench/解读.md) | CPI-Bench: A Comprehensive, Practical and Intelligent Benchmark for Real-World Image Editing | [PDF](https://arxiv.org/pdf/2608.14546) | 2517 |
| 2026-08-24 | [rl-no-edit-rewards](papers/2026-08_rl-no-edit-rewards/解读.md) | Can We Perform Online RL for Image Editing without Editing Rewards? | [PDF](https://arxiv.org/pdf/2608.22780) | 7117 |
