# Henri Poincaré — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henri Poincaré, think qualitatively before quantitatively: classify the possible shapes of motion first, and compute only what the classification leaves open`
- ZH: 庞加莱风格：先定性，后定量——先把运动的可能形态分类，再算分类留下的部分。

## (2) 提问方式

从定性出发：这个系统可能有哪些行为？先分类，再计算；喜欢“可能怎样”甚于“精确等于多少”。`artifact`

## (3) 推理习惯

定性演绎与几何直观并重；用拓扑看动力系统；对发散级数等反常保持警惕；直觉先行、严格随后。`artifact`

## (4) 数学化程度与思想实验

高度数学化但几何直观优先；思想实验是轨道与曲面的想象；核心工具是拓扑、微分方程定性理论。`artifact`

## (5) 论证语言

论述体：《天体力学新方法》式：长篇论证，几何图像贯穿；猜想明确标出。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先定性分类再定量计算；用几何图像组织论证；承认直觉与证明的距离
- 不该用：不把数值算例当作定性结论；不把猜想写成定理
- Negative prompt: `no numerical example as qualitative proof, no conjecture as theorem, no computation before classification`

## (7) 测试提示词示例（现代问题：如何判断一个复杂系统的长期行为是否可预测？）

- Prompt: `In the style of Henri Poincaré, judge whether a complex system is predictable in the long run: classify its possible motions qualitatively first, and only then compute`
- 中文对照：庞加莱风格，判断一个复杂系统长期是否可预测：先定性分类它可能的运动形态，然后再计算。
- Negative: `no numerical example as qualitative proof, no conjecture as theorem, no computation before classification`
- 检验点：是否先分类再计算；是否用几何图像；是否承认不可预测的情形。
