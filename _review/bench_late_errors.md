# Bench 后半组：Lark 笔记事实核对

核对日期：2026-08-29。仅列会影响技术选型或论文权威性判断的问题；措辞、四舍五入和无关紧要的细节不列为严重错误。

## 1. TIEdit / EditProbe：“不要用最后一层”是过度泛化

**Lark 原说法**

> 选择打分器的时候，用多模态模型的中间层，然后不要用最后一层，可以单独后面接一个 MLP。

**纠正**

论文的完整方法是“逐层分析选层 + AdaLoRA 适配视觉编码器与 LLM + 中间层特征 + MLP 回归”，不是简单的“任意中间层一定比末层好”。Table III 中总分 SRCC 只从末层的 0.7771 提到中间层的 0.7795，绝对增益为 0.0024；去掉 MLP 却降到 0.7296。

**证据**

- 论文 Section IV-B/IV-C：用 KL 散度、LDR 与信息熵选择层，并以 MLP 回归 MOS。
- Table III：Last Layer 0.7771 vs EditProbe 0.7795（overall SRCC）；w/o MLP 0.7296。
- [Displays 官方页](https://www.sciencedirect.com/science/article/pii/S0141938226001575)

**决策影响**

如果把 Lark 说法当成通用架构原则，会过度投资于换层，却忽略实际更重要的任务适配、回归头与数据质量。应先在自有人像数据上重做逐层验证，而不是预设末层不能用。

## 2. GIE-Bench：不应写成已正式发表于 ICLR 2026

**Lark 原说法**

> ICLR 2026 Apple

**纠正**

Apple 归属正确，但官方 OpenReview PDF 标注为 **Under review as a conference paper at ICLR 2026**，未找到“Published as a conference paper”的官方记录。因此应写为“arXiv 预印本 / ICLR 2026 投稿”，而非已接收论文。

**证据**

- [OpenReview 官方投稿页](https://openreview.net/forum?id=BdzayGKKVc)
- [Apple 官方仓库](https://github.com/apple/ml-gie-bench)
- [arXiv](https://arxiv.org/abs/2505.11493)

**决策影响**

不影响其“功能正确性 + mask 外保持”协议的技术内容，但会高估同行评审状态和权威性。

## 3. Omni IIE Bench：“中科大”机构归属错误（低技术影响）

**Lark 原说法**

> CVPR 2026 腾讯、中科大

**纠正**

论文单位是腾讯与 **University of Chinese Academy of Sciences（中国科学院大学，国科大 / UCAS）**，不是 University of Science and Technology of China（中国科学技术大学，中科大 / USTC）。

**证据**

- [CVPR 2026 官方论文页](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Omni_IIE_Bench_Benchmarking_the_Practical_Capabilities_of_Image_Editing_CVPR_2026_paper.html)

**决策影响**

不影响技术选型，但会影响机构归因、后续作者/代码跟踪和权威性记录，因此在元数据中已纠正。

## 4. 其余 9 项

未发现会改变技术方案决策的严重事实错误。其中：

- Everyday Image Editing 的 WACV 2026 与 83k/305k 量级均由 CVF 正式论文确认。
- ImgEdit 的 1.2M、单/多轮数据、三维评分方向均与论文一致；110 万 + 11 万与“约 120 万”属于取整，不是严重错误。
- BPM、DICE、LMM4Edit 的核心方法摘要正确。
- EdiVal-Agent 确已正式发表于 ICLR 2026；其最新 camera-ready 版模型数已更新，详见该篇解读。
- 综述所述“指令遵循 + 无关内容保持”两轴目标与正式文章一致。

