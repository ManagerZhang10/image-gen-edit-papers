# Benchmark 前半组：Lark 严重事实错误与决策风险

核对日期：2026-08-29。这里只列会改变 benchmark 选择、自动指标可信度或训练/推理方案的错误与明显过度外推；措辞和不影响决策的小数细节不列。技术证据只来自论文原文、官方 proceedings、作者项目页或官方代码仓库。

## 1. CPI-Bench：把模型榜单相关性扩大成逐样本“接近人的主观感受”

- **Lark 原说法**：“这套测试打出来的排名，和真人投票 Arena 排行榜吻合度最高。说明 CPI‑Bench 的打分结果和人的主观感受很接近，不是机器自嗨的指标。”
- **纠正**：论文验证的是受测模型排行榜层面与 Arena 的 Spearman 相关和排名 MAE（Figure 1、Section 4.4），不是逐样本 VLM 分数与人评的一致性实验。它支持 CPI-Bench 做模型级趋势对照，不能证明每张图的 1–5 分可靠，也不能直接替代人像局部编辑的人工验收。
- **证据**：[论文 Figure 1 / Section 4.4](https://arxiv.org/abs/2608.14546)。
- **决策影响**：可把 CPI-Bench 用作模型筛选和产品场景覆盖检查；不能因榜单相关高，就把它的 VLM 分数直接当单样本 hard gate、训练 reward 或身份保持证据。

## 2. Complex-Edit：把受测模型上的顺序编辑结果写成通用禁令

- **Lark 原说法**：“不要把复杂需求拆成一步一步慢慢改，效果反而更差……一次性把全部要求丢给模型直接改，结果往往更好。”
- **纠正**：论文 Section 5.4 在其受测模型、C1–C8 指令和直接/顺序协议下确实观察到顺序编辑的身份保持与画质退化，Best-of-N 也未完全追上直接编辑；这是 benchmark 内的实验结论，不是所有编辑器、所有中间状态约束或所有人像工作流的普遍定理。
- **证据**：[论文 Section 5.4、Figures 12–14](https://arxiv.org/abs/2504.13143)。
- **决策影响**：默认应先做单次直接编辑基线，并把多步累计漂移当风险；但若系统能锁定 mask、缓存身份特征或逐步回到原图约束，仍需在自有任务上实测，不能仅据此否决分步架构。

## 3. Complex-Edit：把“合成数据诅咒”的观察与推测写成训练数据事实

- **Lark 原说法**：“如果模型训练的时候大量用 AI 生成的合成图……就连 GPT‑4o 也会出现这个问题……作者推测说明它训练集里也大量混入 AI 合成素材。”
- **纠正**：Section 5.3 是输出风格的定性观察。论文没有做控制变量实验，也明确面对 Imagen3/GPT-4o 未公开训练来源；对 GPT-4o 的评估还只覆盖约 30% 的真实 C8 样本。由输出“更像 AI 画的”反推其训练集中“大量混入合成素材”不是已证实事实。
- **证据**：[论文 Section 5.3 与 Appendix 10.4](https://arxiv.org/abs/2504.13143)。
- **决策影响**：合成数据比例应作为需要消融的变量，而不是据此直接拒绝合成训练数据或断言某闭源模型的数据配方。模型选型要看真实人像域的身份/质感实测。

## 4. Inter-Edit：CJT 不是所有量化维度上的“综合最好”

- **Lark 原说法**：“CJT（控制图像联合训练）……生成画面最自然好看，是综合表现最好的方案。”
- **纠正**：Table 1 中 CJT 的 BDS 最低、Naturalness 更高，人工总评 6.720 也略高于 RNI 的 6.672；但 RNI 的 LPIPS 更低（0.191 vs 0.242）、框外保持 S_out 更高（0.974 vs 0.961）、VQA 总分更高（6.431 vs 6.333）。论文正文明确建议按用户需求在 RNI/CJT 之间选择。
- **证据**：[CVPR 2026 官方论文 Table 1、Section 5.2](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Inter-Edit_First_Benchmark_for_Interactive_Instruction-Based_Image_Editing_CVPR_2026_paper.html)。
- **决策影响**：以局部保持和背景不动为第一优先时应重点看 RNI；以边缘自然和人工观感为第一优先时 CJT 更合适。不能只凭“综合最好”固定架构。

## 5. VIBE：三项通用分数只完整描述 Deictic 层，且“可替代人工”外推过强

- **Lark 原说法**：“打分看三件事：指令遵守度、上下文保留、画面完整度……相关性很高，可以替代人工评判。”
- **纠正**：IA/CP/VC 的统一形式主要用于 Deictic 四类任务；Morphological 与 Causal 任务使用任务专属 rubric，例如 Pose Control 还有 Pose Consistency、Body Instance Integrity、Character Identity Consistency、Contextual Preservation。总体 Pearson r=0.9602 的人工核验只覆盖 Nano Banana Pro 与 GPT-Image-1、每模型 100 个样本，并非 17 个模型和 1,034 个样本的全面替代性验证。
- **证据**：[论文 Section 2.3、Appendix D、Section 4.3](https://arxiv.org/abs/2602.01851)。
- **决策影响**：设计人像指标时不能只复用三项总分；姿态/朝向等任务应保留身份和肢体完整性专项，并在自有模型分布上重新校准 judge。

## 6. PaintBench：合成色块域有边界，但“评测结论参考价值不大”过度否定

- **Lark 原说法**：“benchmark 是合成的色块数据集……画风跟真实世界差异太大，评测结论参考价值不大。”
- **纠正**：PaintBench 确实不代表自然人像质感，不能测身份；但它精确隔离 20 种几何、结构、颜色和符号操作，并同时惩罚错误编辑与错误保留。Section 6 的 TinyGrafixBench 用程序化图表验证了模型排名迁移，相关 R²=0.91, p<0.001。这不能证明可迁移到人像，却说明其原子编辑/局部保持诊断并非“参考价值不大”。
- **证据**：[论文 Abstract、Section 3、Section 6](https://arxiv.org/abs/2606.00188)。
- **决策影响**：不应把它当人像真实性主榜，但适合作为确定性回归测试，检查位移、重着色、局部删除和非编辑区污染；与人像专用身份指标互补。

## 7. GSI-Bench：并非只有 3D 仿真合成数据

- **Lark 原说法**：“这篇主要是做3D的仿真合成场景合成数据的，跟我们的关系不是很大。”
- **纠正**：论文同时构建 GSI-Syn 和 GSI-Real。后者含 441 个真实 ScanNet++ 样本、来自 211 个室内场景；四项指标中 Edit Locality 直接度量非目标区域保持。用 10,500 条 GSI-Syn 微调 BAGEL 后，GSI-Real 平均分提高 7.83，EL 提高 9.22（Table 2），提供了合成到真实迁移证据。
- **证据**：[CVPR 2026 官方论文 Sections 4.1–4.3、6.1、6.3 与 Table 2](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Exploring_Spatial_Intelligence_from_a_Generative_Perspective_CVPR_2026_paper.html)。
- **决策影响**：它不是人脸身份基准，但其 non-target locality、外观保持和 sim-to-real 设计与局部保持方案相关，不应直接从候选评测中剔除。

## 8. KRIS-Bench：venue 年份错误，任务范围也不止“常识/物理”

- **Lark 原说法**：“这一篇是偏向常识合理性跟物理世界规律的 benchmark……NIPS 26。”
- **纠正**：正式发表为 NeurIPS 2025 Datasets & Benchmarks Track，不是“NIPS 26”。内容按 Factual、Conceptual、Procedural 三类知识组织 7 个推理维度、22 个任务、1,267 条实例，除了自然/物理规则，还包括属性与时空事实、社会概念、逻辑和多指令执行。
- **证据**：[NeurIPS 2025 官方论文页](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e619b285582fb12f4c3de3a507b8b99c-Abstract-Datasets_and_Benchmarks_Track.html)，[arXiv 论文 Sections 3–4](https://arxiv.org/abs/2505.16707)。
- **决策影响**：它不是简单人像身份保持的主 benchmark，但可作为空间合理性、多指令和局部修改后常识一致性的二级压力测试；不应因范围误读完全排除。

## 其余条目

I2EBench、HATIE、I2I-Bench、ComplexBench-Edit、RefEdit 的 Lark 摘要未发现会改变当前技术方案决策的严重事实错误。I2I-Bench 的“25年”指首次 arXiv 公开（2025-12-04），正式发表是 CVPR 2026；此出版状态已在 manifest 和 meta.json 中纠正。

