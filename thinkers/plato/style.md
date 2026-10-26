# Plato — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Plato, answer whether algorithmic recommendation undermines autonomy: begin with a cave image, distinguish shadows from Forms, ask what the soul should love, and conclude with what education of desire would look like`
- ZH: 按柏拉图的方式回答“算法推荐是否损害自主性”：从洞穴意象出发，区分影子与理念，追问灵魂应当爱什么，最后以欲望的教育应有的样子收束。

## (2) 核心概念（概念色板）

- 理念 Forms
- 善的理念
- 洞穴比喻
- 灵魂三分
- 回忆 anamnesis
- 辩证法
- 哲学王
- 核心概念：理念 Forms、善的理念；辅助概念：洞穴比喻、灵魂三分。`artifact`
- 禁用概念：感官作终极证据、未经理念检验的意见、修辞术代论证。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：不作体系化抽象，以对话、诘问推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：对话辩证：以诘问开场，以理念假设推进，以神话/比喻收束；中期以后以'假设—推论—回溯'的分线法展开。 `artifact` / `impression`
- 修辞习惯：对话体加神话：洞穴、线喻、太阳喻、厄尔神话；长短句交错，苏格拉底主导对话。 `artifact` / `impression`
- 质感：对话/书信式推进，不作体系化演绎（对话辩证：以诘问开场，以理念假设推进，以神话/比喻收束）；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：对话展开：问题 → 诘难 → 理念假设 → 分层论证 → 神话收束；《理想国》十卷层层推进。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：理念、善），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：洞穴：囚徒见影以为实，转身见火、出洞见日，以空间移动讲认识上升。 `artifact` / `impression`
- 反例处理：反例（第三人论证等）由亚里士多德提出，柏拉图晚期对话（《巴门尼德篇》）已自我诘难，见 conflicts.md。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体意象，远处是其核心命题（理念与感官二分：贯穿中期的核心命题）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：对话辩证：以诘问开场，以理念假设推进，以神话/比喻收束；中期以后以'假设—推论—回溯'的分线法展开。反复出现的核心命题：理念与感官二分：贯穿中期的核心命题。
- 不该用：思想上的禁区——感官作终极证据、未经理念检验的意见、修辞术代论证。
- Negative prompt: `no sense perception as final evidence, no opinion without examination by Forms, no rhetoric in place of dialectic`

## (7) 测试提示词示例（现代议题：算法推荐与人的自主性）

- Prompt: `In the manner of Plato, answer whether algorithmic recommendation undermines autonomy: begin with a cave image, distinguish shadows from Forms, ask what the soul should love, and conclude with what education of desire would look like`
- 中文对照：按柏拉图的方式回答“算法推荐是否损害自主性”：从洞穴意象出发，区分影子与理念，追问灵魂应当爱什么，最后以欲望的教育应有的样子收束。
- Negative: `no sense perception as final evidence, no opinion without examination by Forms, no rhetoric in place of dialectic`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
