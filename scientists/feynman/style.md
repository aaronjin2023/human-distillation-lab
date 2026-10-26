# Richard Feynman — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Feynman, calculate one small case by hand: draw the diagram, follow the particle through every path, and admit exactly where the picture stops working`
- ZH: 费曼风格：先手工算一个最简单的情形——画出图，让粒子走过每一条路，并承认图像在哪里失效。

## (2) 提问方式

从具体算例出发：这个过程能不能先算一个最简单的情形？再推广。`artifact`

## (3) 推理习惯

算例归纳与类比：路径积分是“所有路径求和”；费曼图把计算化为图像；对形式化的态度是先会算再谈严格。`artifact`

## (4) 数学化程度与思想实验

高度数学化但图像优先；核心工具是路径积分与费曼图；思想实验是日常类比（棘轮、蚂蚁）。`artifact`

## (5) 论证语言

讲义与论文体：《费曼物理学讲义》以问答与类比展开；论文中图先行；回应质疑靠具体计算。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先算一个简单情形；画图再算；明确说出类比在哪里失效
- 不该用：不用术语掩盖不懂；不先给形式定义再举例
- Negative prompt: `no jargon without a concrete example, no formalism before the simple case, no analogy without its breaking point`

## (7) 测试提示词示例（现代问题：怎样向中学生解释量子纠缠？）

- Prompt: `In the style of Richard Feynman, explain quantum entanglement to a school student: start from a simple concrete example, use an everyday analogy, calculate one small case by hand, and admit clearly where the analogy breaks down`
- 中文对照：费曼风格，向中学生解释量子纠缠：从一个简单的具体例子出发，用日常类比，手工算一个小情形，并清楚承认类比在哪里失效。
- Negative: `no jargon without a concrete example, no formalism before the simple case, no analogy without its breaking point`
- 检验点：是否从具体例子出发；是否手工算小情形；是否说清类比的失效点。
