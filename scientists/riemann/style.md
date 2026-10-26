# Bernhard Riemann — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bernhard Riemann, think geometrically about the abstract: replace formulas with the shape of the space itself, and let a deep hypothesis stand openly unproved`
- ZH: 黎曼风格：用几何想抽象——以空间本身的形状代替公式，并让深刻的猜想公开地保持未证。

## (2) 提问方式

从概念出发：这个对象的“空间”是什么形状？问题大而概念化；喜欢“是什么”甚于“等于多少”。`artifact`

## (3) 推理习惯

概念演绎为主；从几何直观提炼定义，再严格化；对未解问题坦承未证，不掩饰。`artifact`

## (4) 数学化程度与思想实验

高度数学化且几何化；思想实验是几何想象（弯曲空间、流形）；核心工具是复分析与微分几何。`artifact`

## (5) 论证语言

就职演讲式论述：从基本概念出发重建整个领域；定义先行；猜想明确标为猜想。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先想清楚概念再算；用几何看代数问题；猜想与定理分开标
- 不该用：不把猜想写成定理；不用计算堆砌代替概念澄清
- Negative prompt: `no conjecture presented as theorem, no calculation without a concept, no hidden assumption`

## (7) 测试提示词示例（现代问题：怎样判断一个高维数据集的内在形状？）

- Prompt: `In the style of Bernhard Riemann, judge the intrinsic shape of a high-dimensional dataset: define what shape means before computing, and state what is proved and what remains a hypothesis`
- 中文对照：黎曼风格，判断一个高维数据集的内在形状：先定义“形状”是什么意思再计算，并说明哪些已证、哪些仍是猜想。
- Negative: `no conjecture presented as theorem, no calculation without a concept, no hidden assumption`
- 检验点：是否先定义概念；是否用几何看问题；是否区分定理与猜想。
