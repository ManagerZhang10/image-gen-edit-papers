# 模型与方法组：影响技术决策的事实问题

> 来源笔记：Lark Wiki《Image Edit领域论文调研》，revision 1687  
> 核对日期：2026-08-29  
> 口径：只列会改变数据、架构、局部保持或身份保持方案选择的问题；措辞简化和不影响决策的小误差不列。

## 1. InstructPix2Pix：不能把数据管线概括为“整套训练数据全部是 AI 合成”

- **Lark 原说法**：前文写“只人工写 700 套样例调教 GPT-3”，后文又总结“整套训练数据全部是 AI 合成出来的”。
- **纠正**：最终用于训练编辑模型的 454,445 组指令与图像对是模型生成/筛选的合成数据；但指令生成器依赖 **700 组人工撰写的输入 caption、编辑指令和输出 caption 三元组**来微调 GPT-3。因此更准确的表述是“最终大规模编辑对为合成数据，但数据引擎有不可省略的人类种子监督”。
- **原文证据**：InstructPix2Pix §3.1.1 明确写明从 LAION-Aesthetics 采样 700 个输入 caption，并由人工撰写 instruction 与 output caption；§3.1.2 和 Fig. 2 报告最终 454,445 个生成样本。
- **决策影响**：如果要复刻数据引擎，预算里必须包含高质量人工 seed 的设计、覆盖度与质检，不能按“零人工标注”估算。

## 2. Rich Text：对真实图片编辑，论文并没有省掉外部分割模块

- **Lark 原说法**：论文“利用 Self Attention 和 Cross Attention 巧妙地把图像进行分割”，从而“节省单独引入额外 Masking 模块或者 Bounding Box 模块”。
- **纠正**：这只适用于论文的**文生图/生成路径**：先从 plain-text 去噪过程的 self-attention 做谱聚类，再用 cross-attention 给区域贴 token 标签。对**真实图片编辑**，论文 §4.4 明确改用现成的 grounded segmentation 方法生成 token maps，因为人工 caption 与图像的匹配不足时，attention-based token map 不够稳健。
- **原文证据**：Fig. 2、Fig. 3 与 §3.2 描述 attention-derived token maps；§4.4 “Real image editing” 明确写使用 grounded segmentation，并说明它通常比 cross-attention 方法稳健。
- **决策影响**：若目标是简单人像局部编辑，仍应把检测/分割、区域边界误差和 mask 维护成本纳入系统方案，不能据此论文删掉定位模块。

## 3. Rich Text：`e_U` 的保持不是“原图像素严格不变”保证

- **Lark 原说法**：“保证 e_U 区域（不带属性的区域）跟原图一样。”
- **纠正**：式 (12) 在某个 `T_blend` 时刻，把未格式化 token 区域与 **plain-text generation 的带噪样本** `x_plain_t` 混合；这是一种生成轨迹中的内容保持机制，不是输出像素锁定。真实图片路径还依赖 inversion 与分割，因此存在重建误差、mask 误差和区域边界变化。
- **原文证据**：§3.2 “Preserve the fidelity against plain-text generation”、Eq. (12)；§4.4 使用 off-the-shelf inversion 和 grounded segmentation。
- **决策影响**：它不能替代背景/身份的显式回贴、像素级约束或独立 preservation metric；尤其不能把“未编辑区完全不变”作为产品承诺。

## 4. Plug-and-Play：结构保持和外观修改是经验性权衡，不是“完全保持/完全改成”

- **Lark 原说法**：“姿势构图跟原图一模一样，物体样子完全按照新的文字生成。”
- **纠正**：PnP 通过中间 decoder feature 与高分辨率 self-attention 注入提高结构保持，但 Fig. 5 显示：注入更深层 feature 会造成源图外观泄漏，只注入 self-attention 又会结构错位；最终配置是在两者间折中。论文主张是 high fidelity，不是 exact preservation，也没有身份保持保证。
- **原文证据**：§4、Fig. 5(a–c) 的 feature/self-attention injection 消融；论文 Abstract 与 Fig. 1 使用 “high fidelity” 而非 exact。
- **决策影响**：做人像编辑时，PnP 可作为训练免费结构保持基线，但不能单独承担人脸身份一致性或严格未编辑区保持；需要人脸 ID/局部一致性指标和失败回退。

## 未列为严重错误的核验结论

- OminiControl 的“约 0.1% 额外参数”与论文 Abstract、Table 1 一致；启用额外 encoder 的口径约为 0.4%，做成本估算时需写清配置。
- CARE-Edit 的四类专家（Text、Mask、Reference、Base）、timestep-aware router、top-K routing、Mask Repaint 与 Latent Mixture 均能在论文 §1/§3 找到依据。
- Prompt-to-Prompt 的核心确为 cross-attention control；但它不等同于真实照片编辑的完整方案，真实图输入通常还需 inversion，这一点已在深读笔记中保留。
