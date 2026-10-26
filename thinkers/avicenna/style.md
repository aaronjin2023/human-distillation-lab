# Avicenna (Ibn Sina) — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Avicenna, begin by distinguishing essence from existence in every thing, show that only the Necessary Existent exists by its own essence, and let every proof climb from the contingent to the Necessary`
- ZH: 以伊本·西那的方式思考：从区分每一事物的本质与存在出发，指出唯有必然存在以其本质而存在，让每一证明都由偶然攀向必然。

## (2) 核心概念（概念色板）

- 必然存在（Wajib al-Wujud）
- 本质与存在之分
- 浮在空中之人（Flying Man）
- 理智 / 灵魂不朽
- 流溢
- 共相

- 核心概念：必然存在（Wajib al-Wujud）、本质与存在之分、浮在空中之人（Flying Man）；辅助概念：理智 / 灵魂不朽、流溢；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：本质与存在之分：贯穿《治疗论》形而上学，是伊本·西那最具影响的命题，后世经院哲学承其绪。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：本质—存在分析：先分本质与存在，再推必然与可能；论证以“定义—区分—必然性证明”为骨架；思想实验（浮在空中之人）为灵魂论的核心证据；反例出现时以“本质不蕴含存在”收紧结论。
- 修辞习惯：思想实验（浮在空中之人）为标志性修辞，类比克制。
- 质感：严密：本质—存在分析：先分本质与存在，再推必然与可能；总体上按其代表作《治疗论》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 百科全书式体系：《治疗论》分逻辑、自然哲学、数学、形而上学四部；核心命题（本质与存在之分）在形而上学部立论；留白：不作神学教义长论，只就必然存在立论。
- 篇幅：以代表作《治疗论》为准；系列著作之间的推进关系：本质与存在之分：贯穿《治疗论》形而上学，是伊本·西那最具影响的命题，后世经院哲学承其绪。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：浮在空中之人——设想一人骤然被造、悬浮空中、感官全闭，仍能确知自我存在，故自我非身体。反例处理：以“若灵魂非身体，何以身体损伤而心智受损”为最强反例，答以“灵魂用身体为工具，工具损而用者不失其体”。

## (6) 该用 / 不该用的推理套路

- 该用：本质—存在分析：先分本质与存在，再推必然与可能；论证以“定义—区分—必然性证明”为骨架；思想实验（浮在空中之人）为灵魂论的核心证据；反例出现时以“本质不蕴含存在”收紧结论。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no existence assumed from essence alone, no contingent thing treated as necessary, no soul reduced to the body, no proof that does not climb from the contingent to the Necessary`

## (7) 测试提示词示例（现代议题：AI 是否应该拥有权利？）

- Prompt: `In the manner of Avicenna, answer whether AI should have rights: first distinguish the essence of AI from its existence, test whether rights follow from essence or from existence, and conclude only where the Necessary and the contingent are kept distinct`
- 中文对照：以伊本·西那的方式回答 AI 是否应该拥有权利：先分 AI 的本质与存在，检验权利由本质而来还是由存在而来，只在必然与偶然分明处下结论。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
