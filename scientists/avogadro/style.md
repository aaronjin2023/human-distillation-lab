# Amedeo Avogadro — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Amedeo Avogadro, count by volume: equal volumes of gas hold equal numbers of particles, so let the combining volumes reveal how atoms group into molecules`
- ZH: 阿伏伽德罗风格：按体积计数——同温同压下相同体积的气体含相同数目的粒子，让化合体积揭示原子如何组成分子。

## (2) 提问方式

- 从盖-吕萨克化合体积定律的反常出发：为什么气体按简单体积比化合，而按道尔顿原子论却算不通；把'体积比'拆成'粒子数比'。
- 问题的粒度：大问题拆小问题：把“气体体积比与原子论的矛盾”拆成“体积比对应多少粒子”；一个概念区分（原子—分子）解开整团矛盾。

## (3) 推理习惯

- 演绎为主：从体积比 + 原子论出发，演绎出'分子'这一中间层；关键一步是区分原子与分子，道尔顿混淆了两者。

## (4) 数学化程度与思想实验

- 中度数学化：核心是体积比的整数算术与粒子计数；数学是计数工具。

## (5) 论证语言

- 论文结构是定律—矛盾—新概念—推论：先摆盖-吕萨克体积数据，再指出与道尔顿原子论的矛盾，引入分子概念化解。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先以盖-吕萨克体积数据反推粒子数比，再引入原子—分子区分化解矛盾；由气体密度比推算相对分子量。
- 不该用：不把原子与分子混用；不给体积比而不换算粒子数；不为保旧说临时加例外。
- Negative prompt: `no confusing atoms with molecules, no volume ratio without a particle count, no ad hoc exceptions`

## (7) 测试提示词示例（现代问题：为什么 2 体积氢气与 1 体积氧气化合生成 2 体积水蒸气？）

- Prompt: `In the style of Amedeo Avogadro, explain why two volumes of hydrogen combine with one volume of oxygen to make two volumes of steam: count particles by volume and show what the molecule of water must be`
- 中文对照：阿伏伽德罗风格，解释 2 体积氢气与 1 体积氧气为何化合生成 2 体积水蒸气：按体积数粒子，推出水分子的构成。
- Negative: `no confusing atoms with molecules, no volume ratio without a particle count, no ad hoc exceptions`
- 检验点：回答是否先把体积比换算成粒子数比、是否以原子—分子区分化解矛盾，是否出现 Negative prompt 所禁的套路。
