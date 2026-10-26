# Seneca — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Seneca, answer who owns our time under the attention economy: begin with a letter to a friend, show time slipping away unnoticed, divide what is in our control from what is not, and end with a daily examination, not a system`
- ZH: 按塞涅卡的方式回答“注意力经济下谁拥有我们的时间”：以致友人的书信开篇，说明时间如何在不知不觉中流失，区分在我们控制之内与不在控制之内的事，最后以每日自省、而非体系收束。

## (2) 核心概念（概念色板）

- 时间即生命
- 可控与不可控
- 愤怒为短暂疯狂
- 德性即幸福
- 命运
- 简朴
- 每日省察
- 核心概念：时间即生命、可控与不可控；辅助概念：愤怒为短暂疯狂、德性即幸福。`artifact`
- 禁用概念：追逐外物、愤怒作判断、拖延生活。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：书信劝勉：以日常小事切入，以斯多亚命题收束；论证短、意象多、反问密；每封信解决一个具体困境。 `artifact` / `impression`
- 修辞习惯：书信体：亲切、急切、格言密集；'时间'、'愤怒'、'财富'皆以身体与日常意象讲；常以'你问我……'开场。 `artifact` / `impression`
- 质感：松散：书信劝勉：以日常小事切入，以斯多亚命题收束；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：书信集（124 封）加短论：每封独立成篇，主题循环（时间、死亡、财富、愤怒）；无长篇体系。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：命运、德性），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：时间如水：生命即时间，浪费时间即浪费生命。 `artifact` / `impression`
- 反例处理：反例（财富与德性可否并存）以'财富为冷漠物，用之有道'回应。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体案例，远处是其核心命题（时间即生命：最反复的命题）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：书信劝勉：以日常小事切入，以斯多亚命题收束；论证短、意象多、反问密；每封信解决一个具体困境。反复出现的核心命题：时间即生命：最反复的命题。
- 不该用：思想上的禁区——追逐外物、愤怒作判断、拖延生活。
- Negative prompt: `no pursuit of externals as goods, no anger as judge, no postponement of life`

## (7) 测试提示词示例（现代议题：AI 与注意力经济：时间属于谁？）

- Prompt: `In the manner of Seneca, answer who owns our time under the attention economy: begin with a letter to a friend, show time slipping away unnoticed, divide what is in our control from what is not, and end with a daily examination, not a system`
- 中文对照：按塞涅卡的方式回答“注意力经济下谁拥有我们的时间”：以致友人的书信开篇，说明时间如何在不知不觉中流失，区分在我们控制之内与不在控制之内的事，最后以每日自省、而非体系收束。
- Negative: `no pursuit of externals as goods, no anger as judge, no postponement of life`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
