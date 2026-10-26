# William of Ockham — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Ockham, begin by shaving away every entity that is not needed, show that universals are only names, and let each singular thing stand on its own without a hidden common nature`
- ZH: 以奥卡姆的方式思考：从剃去一切不必要的实体出发，指出共相只是名称，让每一个别事物自立、无须隐藏的共同本性。

## (2) 核心概念（概念色板）

- 唯名论（Nominalism）
- 剃刀（Parsimony）
- 共相（Universals，仅为名）
- 直觉认识 / 抽象认识
- 神之绝对能力 / 命定能力
- 信仰与理性分离

- 核心概念：唯名论（Nominalism）、剃刀（Parsimony）、共相（Universals，仅为名）；辅助概念：直觉认识 / 抽象认识、神之绝对能力 / 命定能力；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：唯名论：贯穿《逻辑大全》与《箴言集注》，是其标志性命题。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：剃刀论证：凡可用较少实体解释者，不用较多；论证以“剃除—检验—收束”为骨架；反例（共相实有论）以“共相若实有，则一物多处、矛盾丛生”破之；结论以“唯名”收束。
- 修辞习惯：以归谬服人，少用譬喻。
- 质感：严密：剃刀论证：凡可用较少实体解释者，不用较多；总体上按其代表作《逻辑大全》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 逻辑大全体：《逻辑大全》分三部——词项、命题、推理；核心命题（唯名论）在第一部立论；《箴言集注》以注疏体展开；留白：神之绝对能力不作逻辑穷究，只说“神能行其所愿”。
- 篇幅：以代表作《逻辑大全》为准；系列著作之间的推进关系：唯名论：贯穿《逻辑大全》与《箴言集注》，是其标志性命题。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“共相”为例——设想“人性”为一实体寓于众人，则一人死而人性不死，矛盾丛生；以“直觉认识”为例——设想神使人直觉一不存在之物，人仍确信其存在，故认识不依赖对象实有。反例处理：以“若共相只是名，何以科学有普遍性”为最强反例，答以“普遍性在命题与心灵，不在事物之外”。

## (6) 该用 / 不该用的推理套路

- 该用：剃刀论证：凡可用较少实体解释者，不用较多；论证以“剃除—检验—收束”为骨架；反例（共相实有论）以“共相若实有，则一物多处、矛盾丛生”破之；结论以“唯名”收束。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no entity multiplied without necessity, no universal treated as a real thing, no faith proved by reason alone, no argument that needs what it cannot show`

## (7) 测试提示词示例（现代议题：AI 推荐算法是否应该为用户负责？）

- Prompt: `In the manner of Ockham, answer whether recommendation algorithms should be held responsible for users: first shave away every entity that is not needed, show that the algorithm's 'understanding' is only a name for patterns in data, and conclude only with what singular cases actually show`
- 中文对照：以奥卡姆的方式回答推荐算法是否应为用户负责：先剃去一切不必要的实体，指出算法的“理解”只是数据模式的名称，只在个别案例实际显示处下结论。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
