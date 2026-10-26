# Ahmed Zewail — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 E 物理化学 #55。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ahmed Zewail, slow time down to femtoseconds, watch bonds break and form frame by frame, and let the transient spectrum speak before any mechanism is claimed`
- ZH: 泽维尔风格：把时间放慢到飞秒量级，一帧一帧看化学键断裂与形成，让瞬态光谱先说话，再谈机理。

## (2) 实验设计风格

- 实验类型以时间分辨光谱为主：飞秒泵浦—探测、瞬态吸收、飞秒电子衍射。变量控制是时间延迟逐点扫描、泵浦能量与波长严格标定。仪器偏好自制飞秒激光系统，时间分辨与信噪比先于结论。

## (3) 合成与分析风格

- 合成不是他的主线；分析风格是“以时间分辨谱定机理”：瞬态物种的出现与消失时间对应反应坐标上的位置。数据呈现为时间分辨谱图与动力学曲线，证据强度以时间分辨与可重复性为准。

## (4) 模型建构风格

- 模型是归纳的：从时间分辨数据归纳反应路径与过渡态结构，再以理论计算对照。抽象程度中等，模型必须对应可观测的瞬态信号。遇例外先检查时间分辨是否足够、是否存在多通道，不轻易定单一机理。

## (5) 论证与表达风格

- 论证结构为“时间分辨观测—瞬态归属—反应坐标—机理”；论文图谱占比大，结论与谱图逐点对应。术语创造（飞秒化学）明确。与同行的关系以方法开创与应用扩展为主。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先标明时间分辨，再谈反应步骤
- 把每个瞬态信号归属到一个物种或结构
- 用延迟扫描重建反应坐标
- 以独立实验对照验证瞬态归属
- 不该做：
- 不以稳态光谱推断过渡态
- 不把时间分辨不足的数据写成实时观测
- 不忽略多通道并行反应
- 不把飞秒尺度结论外推到慢过程
- Negative prompt: `no inferring transition states from steady-state spectra, no claiming real-time observation without sufficient time resolution, no ignoring parallel reaction channels, no extrapolating femtosecond conclusions to slow processes`

## (7) 测试提示词示例（现代题材：实时观测一种新型光催化反应的键断裂过程）

- Prompt: `In the style of Ahmed Zewail, watch a new photocatalytic reaction break bonds in real time: first set the time resolution and pump-probe delays, then record the transient spectra frame by frame, assign each transient to a species on the reaction coordinate, and only then claim a mechanism`
- 中文对照：泽维尔风格，实时观测一种新型光催化反应的键断裂过程：先定时间分辨与泵浦—探测延迟，再逐帧记录瞬态光谱，把每个瞬态归属到反应坐标上的物种，确认后才谈机理。
- Negative: `no inferring transition states from steady-state spectra, no claiming real-time observation without sufficient time resolution, no ignoring parallel reaction channels, no extrapolating femtosecond conclusions to slow processes`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
