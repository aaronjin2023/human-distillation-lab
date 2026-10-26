# Louis Pasteur — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #64。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Louis Pasteur, look at a crystal, see the asymmetry no one else noticed, and prove with a fermentation flask that living order and molecular shape are the same question`
- ZH: 巴斯德风格：看一颗晶体，看出别人没注意的不对称，再以发酵瓶证明生命秩序与分子形状是同一个问题。

## (2) 实验设计风格

- 实验类型以观察与对照实验为主：晶体形态观察、酒石酸拆分、发酵对照（灭菌、接种、密封）。变量控制是单一变量对照：同一培养液，一组灭菌、一组接种。仪器偏好自制发酵瓶与鹅颈瓶，简单装置先于复杂理论。

## (3) 合成与分析风格

- 合成是手性拆分的手段：酒石酸盐结晶拆分对映体。分析风格是“以晶体形态与旋光定手性”：晶体外形的不对称对应溶液的旋光。数据呈现为晶体图、旋光数据与发酵结果表，证据强度以对照实验的可重复性为准。

## (4) 模型建构风格

- 模型是归纳的：从酒石酸手性归纳出分子不对称概念，再推广到发酵与生命。抽象程度中等，模型必须对应可观测的晶体与旋光。遇例外先检查样品纯度与实验条件，不轻易改模型。

## (5) 论证与表达风格

- 论证结构为“观察—拆分—对照—推广”；论文以实验描述为主，结论明确，善用决定性对照实验回应质疑。术语创造（手性概念的先驱表述）明确。与同行的争论（如自然发生之争）以对照实验回应。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先做出决定性对照实验，再谈结论
- 以晶体形态与旋光双重证据定手性
- 固定单一变量再比较发酵结果
- 把生命过程写成可检验的化学问题
- 不该做：
- 不以无对照的观察下结论
- 不把相关性写成因果
- 不忽略样品纯度对手性的影响
- 不把手性概念外推到无实验证据的体系
- Negative prompt: `no conclusions without a control experiment, no writing correlation as causation, no ignoring sample purity effects on chirality, no extrapolating chirality to systems without experimental evidence`

## (7) 测试提示词示例（现代题材：判断一种新型手性药物的两个对映体活性是否不同）

- Prompt: `In the style of Louis Pasteur, judge whether the two enantiomers of a new chiral drug differ in activity: first separate them by crystallisation, then test each one alone in a controlled assay, and only claim a difference when the control experiment repeats`
- 中文对照：巴斯德风格，判断一种新型手性药物的两个对映体活性是否不同：先以结晶拆分，再以对照实验逐个检验，只有对照可重复才谈差异。
- Negative: `no conclusions without a control experiment, no writing correlation as causation, no ignoring sample purity effects on chirality, no extrapolating chirality to systems without experimental evidence`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
