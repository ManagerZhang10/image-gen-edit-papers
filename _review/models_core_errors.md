# Lark 基础模型/方法组：需要人工 review 的关键错误

核对日期：2026-08-29。这里只列会影响技术方案判断的错误或证据等级混淆，不纠结措辞和无关细节。

## 1. ControlNet 小节混入了另一类轻量 DiT 控制方法（严重）

### Lark 中的问题

ControlNet 标题下，前半段“冻结大模型、复制编码层、零卷积、输入 Canny/pose/depth/segmentation”等基本是原论文；但后半段又写成：

- “ControlNet 是过去老方案”；
- 新方法“一个模型同时搞定空间对齐和主体参考”；
- “只增加 0.1% 参数”；
- 有类似 MoE 的调度器，自动区分文字、mask、参考图的重要性。

这不是 2023 ControlNet 论文的架构或实验结论，至少混入了后来的 DiT 轻量统一控制器内容。

### 正确事实

原始 ControlNet 冻结 Stable Diffusion U-Net 主干，复制 U-Net encoder/middle block 作为可训练分支，并通过 zero convolution 注入。它不是 0.1% 参数级的小插件；论文为 Canny、depth、pose、segmentation 等不同条件训练 ControlNet，并展示多个条件相加，但没有“单一 MoE 路由器统一空间与主体参考”的设计。主体外观参考更接近 IP-Adapter/后续统一控制方法的议题。

### 为什么影响决策

这会直接误判参数量、显存、训练权重数量、条件能力与 FLUX/DiT 可迁移性。若按 Lark 描述选型，可能错误地把原始 ControlNet 当作极轻、单权重、多任务、同时保身份的模块。

### 建议替换

把原始 ControlNet 内容保留到“零卷积 + 冻结主干 + 每类空间条件训练控制分支”为止；从“过去老方案”开始的统一 0.1%/MoE 内容整体移出，先查明对应论文再单列。

一手依据：[ICCV 2023 正式论文](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html)。

## 2. “Rectified Flow 最大优势就是步数少、速度快”是错误归因（严重）

### Lark 中的问题

FlowChef 小节把 FLUX、InstaFlow 归为 rectified flow 后，直接说它相对传统扩散的最大优势是“生成步骤少、速度快，轨迹接近直线”。

### 正确事实

“学习更直的传输轨迹”是 rectified flow 的目标/直觉，但少步和速度取决于训练质量、求解器、蒸馏与硬件，不是范式定义自动带来的结果：

- InstaFlow 的一步/少步能力来自蒸馏；
- FLUX.1 [dev] 官方模型卡明确写了 guidance distillation；
- FlowChef 的论文/代码仍使用多步采样与任务超参；官方 FLUX 编辑示例约 30 steps，代码页给出约 30 秒/A100；
- FlowChef 论文还明确观察到 FLUX 速度场非线性导致的颜色退化与失败。

FlowChef 自身的效率主要来自跳过反演和对完整 ODE 求解器的反传，而不是证明“整流流天然快”。

### 为什么影响决策

错误归因会把“是否采用 rectified flow”“是否需要蒸馏”“编辑算法是否低延迟”三个独立问题混成一个，导致错误的 latency 预算和骨干选型。

一手依据：[FlowChef ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Patel_FlowChef_Steering_of_Rectified_Flow_Models_for_Controlled_Generations_ICCV_2025_paper.html)、[FLUX.1 [dev] 官方模型卡](https://huggingface.co/black-forest-labs/FLUX.1-dev)。

## 3. FlowChef 的“无梯度”容易被理解成完全不算梯度（严重）

FlowChef 的贡献是 gradient skipping：不穿过完整 ODE 求解过程和生成模型做昂贵反向传播。算法仍利用任务损失关于估计干净样本的梯度；像素空间损失作用到潜变量时还可能经过 VAE decoder。编辑还依赖自动/人工 mask 和 guidance 超参。

若把它理解成“完全无梯度、无 mask、零调参编辑”，会严重低估工程复杂度。建议 Lark 改成：“training-free、inversion-free，并跳过对 ODE solver 的重反传；仍需要样本空间损失梯度、mask 与任务超参。”

一手依据：[FlowChef arXiv/论文](https://arxiv.org/abs/2412.00100)、[官方代码](https://github.com/FlowChef/FlowChef)。

## 证据等级需要降级，但不属于纯事实错误

### Qwen-Image-Edit-2511

“mitigate image drift、improved character consistency”与官方模型卡一致，不算错误；但这是 2511 checkpoint 的官方版本说明和定性展示，不是 arXiv:2508.02324 对 2511 的量化结论。2511 没有独立论文、数据或消融，技术决策时必须在自有集验证。

### MGIE 在某 benchmark 中“几乎没改图”

可以写成该 benchmark/样本上的观察，不能上升为 MGIE 的普遍属性。MGIE 原论文在多项指令编辑任务上报告有效改动；它的真实短板是缺少显式 mask/local grounding、组合指令和数值理解困难。单一 benchmark 失败不能替代方法级判断。
