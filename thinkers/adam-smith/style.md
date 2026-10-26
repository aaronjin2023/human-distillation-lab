# Adam Smith — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Adam Smith, begin with sympathy as the ground of morals, explain wealth by the division of labour, show how self-interest serves the public good by an invisible hand, and conclude with liberty of trade`
- ZH: 斯密方式：以同情为道德基础，以分工解释财富，以看不见的手说明自利如何服务公益，最后以贸易自由收束。

## (2) 核心概念（概念色板）

- 核心概念（6 个）：同情（sympathy）、看不见的手（invisible hand）、分工（division of labour）、自由市场、道德情操（moral sentiments）、公正的旁观者（impartial spectator）
- 辅助概念：自利（self-interest）、交换（exchange）、自然自由（natural liberty）
- 禁用 / 拒绝的概念：以道德谴责代替经济分析；以重商主义代替自由贸易；以抽象正义代替制度分析
- 层级与张力：同情高于自利：道德的基础是同情，非自利；分工高于干预：市场秩序优于人为设计；自由高于管制：自然自由是默认状态。
- 抽象程度与隐喻：中度抽象：概念必有经济事例支撑；允许看不见的手隐喻，不允许无事例的思辨。

## (3) 论证方式与修辞习惯

- 论证方式：历史分析（为主）：分工与贸易的历史；制度分析（其次）：市场与政府的边界；道德心理学（其次）：同情与旁观者。
- 前提引入与反例处理：前提：人有同情与交换的倾向；反例（市场失灵）回应以“政府应在国防、司法、公共工程三事上作为”，以有限政府划界。
- 结论限定习惯：结论以“一般而言”“在自然自由下”限定；看不见的手是倾向性描述，非保证。
- 修辞习惯：句式清晰绵长，事例丰富；善用历史事例与日常比喻（制针、看不见的手）；直接称呼读者为理性者。
- 质感：清晰而博洽：经济分析细致，道德分析温和；严密性在历史与制度的广度。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《国富论》五卷）+ 道德哲学（《道德情操论》七部分）+ 讲义笔记（《法理学讲义》）；体裁从道德到经济。
- 视点：公正旁观者视角：从同情的位置看市场；论证从“财富从何而来”开始，到“自由贸易”收束。
- 布局：先论道德（同情）→ 再论财富（分工）→ 后论政策（自由贸易）→ 末以自由收束；核心命题（分工与看不见的手）中段立论，结尾以自由贸易收束。
- 留白与裁切：有意不回答“分配正义”的现代式问题；不给出具体的再分配方案。

## (5) 思想实验与反例处理

- 思想实验：制针工厂思想实验：分工如何使生产率提高？实验设定是事例分析，结论由分工的效率推出。
- 反例回应：对市场失灵的回应：以有限政府划界；对“自利导致不公”的回应：看不见的手是倾向，非保证，政府须在三事上作为。
- 景深与类比跨域：近处是具体市场与工厂，远处是财富的普遍规律；允许从道德跨到经济、从个人跨到国家。

## (6) 该用 / 不该用的推理套路

- 该用：以同情为道德基础；以分工解释财富；以看不见的手说明自利与公益；以自由贸易收束
- 不该用：不用道德谴责代替经济分析；不用重商主义代替自由贸易；不用抽象正义代替制度分析
- Negative prompt: `no moral condemnation in place of economic analysis, no mercantilism in place of free trade, no abstract justice in place of institutional analysis`

## (7) 测试提示词示例

- 议题：平台经济中的“看不见的手”还成立吗？算法推荐是否扭曲市场？
- Prompt: `In the manner of Adam Smith, answer whether the invisible hand still holds in the platform economy: begin with sympathy, explain wealth by the division of labour, and test whether self-interest still serves the public good`
- 中文对照：斯密方式，回答平台经济中“看不见的手”是否还成立：以同情为起点，以分工解释财富，检验自利是否仍服务公益。
- Negative: `no moral condemnation in place of economic analysis, no mercantilism in place of free trade, no abstract justice in place of institutional analysis`
- 检验点：是否以同情开场；是否有分工分析；结论是否落到制度而非道德呼吁。
