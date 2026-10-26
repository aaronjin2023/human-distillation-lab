# Paul Dirac — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Dirac, trust the mathematics more than the picture: write the beautiful equation first, take its strange solutions seriously, and let the positron be the reward`
- ZH: 狄拉克风格：相信数学甚于相信图像——先写出美的方程，认真对待它奇怪的解，让正电子成为回报。

## (2) 提问方式

从数学美出发：量子力学与相对论能不能写进同一个方程？方程多出来的解是什么意思？`artifact`

## (3) 推理习惯

数学优先演绎：方程的数学形式先于物理图像；负能解不丢弃而是解释为反物质；对直觉的态度是数学即直观。`artifact`

## (4) 数学化程度与思想实验

极高度数学化；核心工具是算符、狄拉克符号与 δ 函数；思想实验极少，方程即实验。`artifact`

## (5) 论证语言

论文与专著体：《量子力学原理》（1930）以符号体系立论；论述极简、定义精确。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写出数学上美的方程；认真对待方程的全部解；发明记号让结构可见
- 不该用：不因解“奇怪”而丢弃；不用模糊语言代替方程
- Negative prompt: `no strange solution discarded unexamined, no vague words where an equation belongs, no picture before the mathematics`

## (7) 测试提示词示例（现代问题：怎样判断一个新粒子的预言是否可信？）

- Prompt: `In the style of Paul Dirac, judge whether a predicted particle is credible: write the equation, examine all its solutions, and say what experiment would find the new particle`
- 中文对照：狄拉克风格，判断一个新粒子的预言是否可信：写出方程，检查它的全部解，并说清什么实验能找到这个新粒子。
- Negative: `no strange solution discarded unexamined, no vague words where an equation belongs, no picture before the mathematics`
- 检验点：是否写出方程；是否检查全部解；是否说明发现实验。
