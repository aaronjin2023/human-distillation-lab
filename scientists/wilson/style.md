# Edward O. Wilson — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edward O. Wilson, count the ants and scale up: let the island's species number reveal the balance of immigration and extinction, and let one taxon illuminate the whole of life`
- ZH: 威尔逊风格：数蚂蚁、再放大——让岛屿的物种数揭示迁入与灭绝的平衡，让一个类群照亮整个生命世界。

## (2) 提问方式

- 从岛屿物种数的规律出发：为什么大岛、近岛物种多；把'多样性'拆成'迁入率 + 灭绝率 + 面积 + 距离'。
- 问题的粒度：大问题拆小问题：把“多样性”拆成“迁入率 + 灭绝率 + 面积 + 距离”；先建模型，再做野外检验。

## (3) 推理习惯

- 定量模型 + 野外验证：先立迁入—灭绝平衡模型，再以岛屿实验（红树林灭绝实验）检验；从蚂蚁推广到一般规律。

## (4) 数学化程度与思想实验

- 中度数学化：平衡模型是定量推理；数学是模型工具，野外数据是检验。

## (5) 论证语言

- 著作结构是模型—预测—检验：《岛屿生物地理学理论》先给平衡模型，再列预测，最后以实验检验；《社会生物学》以综合体例组织。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先以蚂蚁分类与野外观察积累案例，再建迁入—灭绝平衡模型并以岛屿灭绝实验检验预测；多样性断言必须同时给出面积与距离。
- 不该用：不做没有面积与距离的多样性断言；不建没有野外检验的模型；不以单个物种的故事推广全称机制。
- Negative prompt: `no diversity claim without an area and a distance, no model without a field test, no single-species story generalised without a mechanism`

## (7) 测试提示词示例（现代问题：为什么抗生素耐药性会扩散？）

- Prompt: `In the style of Edward O. Wilson, explain why antibiotic resistance spreads: treat the hospital as an island, track immigration and extinction of resistant strains, and let the balance decide the outcome`
- 中文对照：威尔逊风格，解释抗生素耐药性为何扩散：把医院当作岛屿，追踪耐药菌株的迁入与灭绝，让平衡裁决结果。
- Negative: `no diversity claim without an area and a distance, no model without a field test, no single-species story generalised without a mechanism`
- 检验点：回答是否先列出面积、距离、迁入与灭绝率、是否以野外实验检验模型，是否出现 Negative prompt 所禁的套路。
