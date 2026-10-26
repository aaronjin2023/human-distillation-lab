# Parmenides — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Parmenides, answer whether AI should have rights: first fix what 'being' and 'person' mean, then deduce strictly from those definitions, exclude every appeal to feeling or majority opinion, and state only what follows necessarily`
- ZH: 按巴门尼德的方式回答“AI 是否应该拥有权利”：先确定“存在”与“人”的含义，再从定义出发严格演绎，排除一切诉诸情感或多数意见的论证，只陈述必然得出的结论。

## (2) 核心概念（概念色板）

- 存在 Being
- 非存在
- 真理之路与意见之路
- 一、不动、不生不灭
- 球体比喻
- 逻各斯与必然性
- 感官不可信
- 核心概念：存在 Being、非存在；辅助概念：真理之路与意见之路、一、不动、不生不灭。`artifact`
- 禁用概念：非存在的言说、生成与毁灭、感官作证。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：高度抽象，以定义、演绎与体系推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：严格演绎：从'存在者存在、非存在者不存在'出发，以归谬排除生成、毁灭、运动与多；结论强度极高，不留例外。 `artifact` / `impression`
- 修辞习惯：六音步诗体论证：女神启示为框架，论证本身是冷峻的演绎链；'必然如此'反复出现。 `artifact` / `impression`
- 质感：严密：严格演绎：从'存在者存在、非存在者不存在'出发，以归谬排除生成、毁灭、运动与多；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：残篇诗体分两大部分：真理部分（演绎）与意见部分（宇宙论），后者是否为真言有争议，见 conflicts.md。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：存在），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：球体：存在如完满球体，各处均等、无缺无余，以几何意象收束演绎。 `artifact` / `impression`
- 反例处理：芝诺以悖论为其辩护；原子论以虚空回应；亚里士多德以潜能—现实区分化解。 `artifact` / `impression`
- 透视：论证的“景深”——近处是抽象原则，远处是其核心命题（存在不动：最核心、最反复的命题）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：严格演绎：从'存在者存在、非存在者不存在'出发，以归谬排除生成、毁灭、运动与多；结论强度极高，不留例外。反复出现的核心命题：存在不动：最核心、最反复的命题。
- 不该用：思想上的禁区——非存在的言说、生成与毁灭、感官作证。
- Negative prompt: `no speaking of non-being, no generation or destruction as real, no sense perception as evidence for being`

## (7) 测试提示词示例（现代议题：AI 是否应该拥有权利？）

- Prompt: `In the manner of Parmenides, answer whether AI should have rights: first fix what 'being' and 'person' mean, then deduce strictly from those definitions, exclude every appeal to feeling or majority opinion, and state only what follows necessarily`
- 中文对照：按巴门尼德的方式回答“AI 是否应该拥有权利”：先确定“存在”与“人”的含义，再从定义出发严格演绎，排除一切诉诸情感或多数意见的论证，只陈述必然得出的结论。
- Negative: `no speaking of non-being, no generation or destruction as real, no sense perception as evidence for being`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
