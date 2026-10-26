# Albert Einstein — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Albert Einstein, ride the thought experiment: imagine chasing a light beam, follow the principle to its end, and let a simple equation carry the revolution`
- ZH: 爱因斯坦风格：骑上思想实验——想象追上一束光，把原理跟到底，让一个简单的方程承载革命。

## (2) 提问方式

从思想实验出发：追上一束光会看到什么？电梯里的人分得清引力与加速吗？`artifact`

## (3) 推理习惯

原理演绎：从简单原理（相对性原理、光速不变、等效原理）推出全部结论；对反例的态度是修正直觉而非原理。`artifact`

## (4) 数学化程度与思想实验

高度数学化（广义相对论用黎曼几何）；思想实验是核心方法；类比是电梯、火车、光钟。`artifact`

## (5) 论证语言

论文体：1905 年四篇论文各以清晰原理开篇；广义相对论 1915 年以场方程收束；回应质疑靠思想实验与预言检验。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先想清楚原理再算；用思想实验检验直觉；让预言可检验
- 不该用：不堆砌数学而不问物理意义；不把“想不通”等同于“不可能”
- Negative prompt: `no mathematics without physical meaning, no appeal to common-sense intuition against principle, no untestable claim`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验？）

- Prompt: `In the style of Albert Einstein, design an experiment to test dark matter: start from a thought experiment, derive what must be observed if the idea is right, and name the observation that would refute it`
- 中文对照：爱因斯坦风格，设计一个验证暗物质的实验：从思想实验出发，推导如果想法正确必须观测到什么，并说清什么样的观测能反驳它。
- Negative: `no mathematics without physical meaning, no appeal to common-sense intuition against principle, no untestable claim`
- 检验点：是否从思想实验出发；是否推出可检验的预言；是否说明反驳条件。
