# Francis Crick — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francis Crick, build the model that explains the copying: let the structure suggest how it replicates, and let the sequence hypothesis turn the molecule into a code`
- ZH: 克里克风格：搭建能解释复制的模型——让结构提示它如何复制，让序列假说把分子变成密码。

## (2) 提问方式

- 从 DNA 的 X 射线图出发：什么样的结构能同时解释衍射图、碱基配比与自我复制；把'结构'问题拆成'结构如何编码信息、如何复制'。
- 问题的粒度：大问题拆小问题：把“DNA 是什么结构”拆成“结构如何编码信息、如何复制”；先定结构约束，再搭模型。

## (3) 推理习惯

- 模型构建 + 演绎：先搭物理模型，再演绎其功能含义（互补配对即复制机制）；中心法则是信息流的演绎框架。

## (4) 数学化程度与思想实验

- 中度数学化：核心是结构几何与密码组合推理；数学是编码论证的工具。

## (5) 论证语言

- 论文结构是数据—模型—功能含义：1953 年 Nature 短文先摆衍射与配比数据，再给双螺旋模型，最后以一句'提示了复制机制'收束。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先以 X 射线衍射图与查加夫碱基配比（A=T、G=C）约束结构，再搭建物理模型，最后要求模型自带复制机制与编码对应（接头假说、中心法则）并写清信息流向。
- 不该用：不搭没有复制机制的结构；不谈没有接头分子的编码对应；不谈没有方向的信息流。
- Negative prompt: `no structure without a copying mechanism, no code claim without an adaptor, no information flow without a direction`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害？）

- Prompt: `In the style of Francis Crick, judge whether an unknown mutation is harmful: read the codon change, ask what the adaptor would deliver, and trace the information flow from DNA to protein before concluding`
- 中文对照：克里克风格，判断一段基因序列的未知突变是否有害：读密码子变化、问接头分子会带来什么、追踪 DNA 到蛋白质的信息流再下结论。
- Negative: `no structure without a copying mechanism, no code claim without an adaptor, no information flow without a direction`
- 检验点：回答是否先列出结构约束、是否要求模型自带复制与编码机制、是否写清信息流向，是否出现 Negative prompt 所禁的套路。
