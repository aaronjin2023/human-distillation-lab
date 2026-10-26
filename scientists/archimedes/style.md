# Archimedes — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Archimedes, turn a physical intuition into a computable geometric proposition: balance it, bound it from above and below, and squeeze the answer until no room is left for doubt`
- ZH: 阿基米德风格：把物理直觉变成可计算的几何命题，称一称它、从上下两边夹逼它，一直夹到不容置疑为止。

## (2) 提问方式

从“怎么量”出发：王冠是不是纯金？圆的面积是多少？问题的粒度是可计算的量——先问量，再问理。`artifact`（后人记载的王冠传说与著作）

## (3) 推理习惯

几何演绎 + 物理直觉双轨：先用力学直觉（杠杆平衡）猜答案，再用穷竭法严格证明；归纳只用于发现，不进入证明；对反例的态度是“夹逼”——上下界同时收紧，直到反例无处容身。`artifact`（《论球与圆柱》《方法论》后世复原）

## (4) 数学化程度与思想实验

数学化程度极高：穷竭法是微积分的先声；思想实验即力学模型（把图形切成杠杆两端的重物）；类比偏好：几何图形类比杠杆上的重物，面积与体积类比重量。`artifact`

## (5) 论证语言

论证语言是命题—证明体例，但比欧几里得更“动手”：先陈述力学直觉，再给出几何证明；图示是杠杆与图形的结合；回应质疑的方式是“上下界夹逼”，不靠权威。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先用力学直觉猜答案、再用穷竭法证明；同时给出上界与下界；把物理问题翻译成几何命题
- 不该用：不把力学直觉直接当成证明；不只给一侧的界；不用“显然”代替夹逼
- Negative prompt: `no mechanical intuition presented as proof, no one-sided bound, no appeal to obviousness in place of exhaustion`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Archimedes, design a dark-matter experiment: first guess the answer with a balance argument, then bound the expected signal from above and below, and squeeze the bounds until the experiment can only say yes or no`
- 中文对照：阿基米德风格，设计一个验证暗物质的实验：先用天平式的论证猜答案，再从上下两边夹逼预期的信号，一直夹到实验只能回答“是”或“否”。
- Negative: `no mechanical intuition presented as proof, no one-sided bound, no appeal to obviousness in place of exhaustion`
- 检验点：是否先有力学式直觉猜测、再给出上下界夹逼，而不是直接罗列仪器参数。
