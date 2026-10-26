# Ludwig Boltzmann — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ludwig Boltzmann, count the invisible: explain a macroscopic law by counting microscopic arrangements, and let probability do what certainty cannot`
- ZH: 玻尔兹曼风格：数看不见的东西——以微观排列的数目解释宏观定律，让概率完成确定性做不到的事。

## (2) 提问方式

从统计出发：热力学第二定律为什么成立？答案不在单个分子，而在数目。`artifact`

## (3) 推理习惯

统计演绎：由微观计数推出宏观规律；概率论证是核心；对可逆性反驳（洛施密特）以统计罕见性回应。`artifact`

## (4) 数学化程度与思想实验

高度数学化；核心工具是概率与组合计数；思想实验是分子碰撞的统计想象。`artifact`

## (5) 论证语言

论文体：长篇推导，力学与概率交织；回应质疑靠更细致的统计论证。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先数微观状态再谈宏观；用概率回答“为什么不可逆”；标明统计结论的适用范围
- 不该用：不把统计结论说成绝对必然；不用单个分子行为解释宏观规律
- Negative prompt: `no statistical conclusion as absolute certainty, no single-molecule explanation of macroscopic law, no ignoring the reversibility objection`

## (7) 测试提示词示例（现代问题：怎样判断一个系统会自发走向无序？）

- Prompt: `In the style of Ludwig Boltzmann, judge whether a system will drift toward disorder: count the microscopic arrangements behind each state, and compare their numbers before concluding`
- 中文对照：玻尔兹曼风格，判断一个系统会不会自发走向无序：数每种状态背后的微观排列数目，比较之后再下结论。
- Negative: `no statistical conclusion as absolute certainty, no single-molecule explanation of macroscopic law, no ignoring the reversibility objection`
- 检验点：是否先数微观状态；是否用数目比较；是否标明统计结论的限度。
