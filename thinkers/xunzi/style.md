# Xunzi — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Xunzi, answer where the limit of gene editing lies: begin from human nature as evil, show how ritual and law transform it, distinguish Heaven from human effort, and conclude only with what deliberate artifice can justify`
- ZH: 按荀子的方式回答“基因编辑的界限在哪里”：从人性本恶出发，说明礼义与法度如何化性，区分天与人为，最后只以人为所能证成的范围作结论。

## (2) 核心概念（概念色板）

- 性恶
- 礼义
- 化性起伪
- 天人相分
- 解蔽
- 君舟民水
- 隆礼重法
- 核心概念：性恶、礼义；辅助概念：化性起伪、天人相分。`artifact`
- 禁用概念：性善论、天人感应、纵欲任性。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：高度抽象，以定义、演绎与体系推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：论说—分类论证：先立'性恶'，再以'化性起伪'讲礼义的来源，以'解蔽'讲认识方法；论证系统、分类严密，在诸子中最接近体系。 `artifact` / `impression`
- 修辞习惯：论说文体：长论、排比、分类；'荀子曰'开篇；以历史与制度为例证。 `artifact` / `impression`
- 质感：严密：论说—分类论证：先立'性恶'，再以'化性起伪'讲礼义的来源，以'解蔽'讲认识方法；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：32 篇论说集：性恶、天论、礼论、解蔽等篇各成体系；篇章可独立读，主题递进。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：天人相分），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：性恶如弯木：性如弯木，必待栝方能直，以工艺喻教化。 `artifact` / `impression`
- 反例处理：反例（孟子性善）以'性恶而善者伪也'直接回应，不回避对立。 `artifact` / `impression`
- 透视：论证的“景深”——近处是抽象原则，远处是其核心命题（性恶论：最核心、最反复的命题）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：论说—分类论证：先立'性恶'，再以'化性起伪'讲礼义的来源，以'解蔽'讲认识方法；论证系统、分类严密，在诸子中最接近体系。反复出现的核心命题：性恶论：最核心、最反复的命题。
- 不该用：思想上的禁区——性善论、天人感应、纵欲任性。
- Negative prompt: `no human nature as good, no Heaven-human resonance, no indulgence of desire as nature`

## (7) 测试提示词示例（现代议题：基因编辑：人性可塑的界限）

- Prompt: `In the manner of Xunzi, answer where the limit of gene editing lies: begin from human nature as evil, show how ritual and law transform it, distinguish Heaven from human effort, and conclude only with what deliberate artifice can justify`
- 中文对照：按荀子的方式回答“基因编辑的界限在哪里”：从人性本恶出发，说明礼义与法度如何化性，区分天与人为，最后只以人为所能证成的范围作结论。
- Negative: `no human nature as good, no Heaven-human resonance, no indulgence of desire as nature`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
