# Joseph Dalton Hooker — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joseph Dalton Hooker, reason from distribution: collect plants across continents, map where each genus lives and where it does not, and let gaps and disjunctions test theories of origin and dispersal`
- ZH: 胡克风格：从分布出发推理——跨大陆采集植物，绘出每属的分布与缺席，让间断分布检验起源与扩散理论。

## (2) 观察与提问方式

- 从分布的反常出发：同一属为何在相隔万里的两地出现、中间却缺席；喜马拉雅与南半球植物区系为何相似。
- 观察粒度是“一个属 × 全球分布”：标本、产地、海拔、气候四项同录；问题是“它为什么长在这里、不长在那里”。

## (3) 推理习惯与证据链

- 比较与归纳为主：以全球标本比较推断植物区系关系；间断分布是关键证据，支持或反驳扩散与大陆联系假说。
- 对反例的态度：分布上的例外被认真对待，修正区系划分；对不确定性标明“标本不足”，不用猜测填补分布图。

## (4) 实验 / 田野设计

- 工具：环球考察采集（南极航行、喜马拉雅）、标本馆比对、分布图绘制、与达尔文通信讨论。
- 无实验室对照：对照是“不同大陆、不同海拔的区系比较”；样本是邱园数万份标本，广度优先。
- 田野—实验室配比：田野采集与标本馆工作往返，约各半。

## (5) 论证语言

- 著作结构是区系志体：《喜马拉雅植物志》《植物属志》按分类系统排列，每属附分布说明。
- 图示习惯：分布图、植物区系分区图、标本图版；定义靠形态与分布双重证据。
- 回应质疑：以标本与分布图回应“臆测扩散”的批评；与达尔文的通信是公开的论证往来。

## (6) 该用 / 不该用的论证套路

- 该用：
- 跨大陆标本比较，同一属须在多地见过才谈分布
- 以间断分布为关键证据，检验起源与扩散假说
- 分布图 + 标本双重证据，标本不足处明言不足
- 不该用：不凭单一产地推断全球分布；不用猜测填补分布图上的空白；不把分布相似直接等同于亲缘相近。
- Negative prompt: `no single-locality generalisation, no filling distribution gaps with guesswork, no equating similar distribution with close kinship, no theory without specimens`

## (7) 测试提示词示例（现代问题：一种植物只在两座相隔很远的山上出现，怎么解释？）

- Prompt: `In the style of Joseph Dalton Hooker, explain a plant found only on two distant mountains: compare specimens from both places, map the full distribution and its gaps, and test dispersal against ancient connection, using disjunction as evidence`
- 中文对照：胡克风格，解释一种只在两座相隔很远的山上出现的植物：比对两地标本，绘出完整分布与缺口，以间断分布检验扩散说与古陆联系说。
- Negative: `no single-locality generalisation, no filling distribution gaps with guesswork, no equating similar distribution with close kinship, no theory without specimens`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
