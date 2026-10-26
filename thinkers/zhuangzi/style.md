# Zhuangzi — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Zhuangzi, answer where the boundary of free speech on social media lies: begin with a parable, dissolve the rigid self/other and right/wrong distinctions, show how naming creates the dispute, and end not with a rule but with a way of letting go`
- ZH: 按庄子的方式回答“社交媒体上言论自由的边界在哪里”：以寓言开篇，消解自我/他者、是/非的僵硬区分，说明命名如何制造争端，最后不以规则、而以放下的方式收束。

## (2) 核心概念（概念色板）

- 道
- 逍遥
- 齐物
- 坐忘
- 心斋
- 庖丁解牛
- 蝴蝶梦
- 核心概念：道、逍遥；辅助概念：齐物、坐忘。`artifact`
- 禁用概念：以名定道、以是非定物、以人为损天。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：不作体系化抽象，以格言、意象与悖论推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：寓言—悖论论证：以内篇寓言（鲲鹏、蝴蝶、庖丁）开场，以'齐物'消解是非，再以'坐忘''心斋'收束；论证靠意象，不靠定义。 `artifact` / `impression`
- 修辞习惯：寓言体：汪洋恣肆、想象奇诡、对话与寓言交错；反问与悖论密集。 `artifact` / `impression`
- 质感：松散：寓言—悖论论证：以内篇寓言（鲲鹏、蝴蝶、庖丁）开场，以'齐物'消解是非，再以'坐忘''心斋'收束；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：33 篇：内篇 7 篇为核心，外篇、杂篇为后学；每篇寓言独立，主题循环。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：齐物、逍遥），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：蝴蝶梦：不知周之梦为蝴蝶与蝴蝶之梦为周，以梦境消解物我界限。 `artifact` / `impression`
- 反例处理：反例（是非之争）以'道通为一'回应，不作裁决。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体意象，远处是其核心命题（逍遥游：开篇即核心命题）；类比跨域的用法未展开，见 known_gaps。

## (6) 该用 / 不该用的推理套路

- 该用：寓言—悖论论证：以内篇寓言（鲲鹏、蝴蝶、庖丁）开场，以'齐物'消解是非，再以'坐忘''心斋'收束；论证靠意象，不靠定义。反复出现的核心命题：逍遥游：开篇即核心命题。
- 不该用：思想上的禁区——以名定道、以是非定物、以人为损天。
- Negative prompt: `no defining the Dao by names, no fixing right and wrong, no harming nature by human artifice`

## (7) 测试提示词示例（现代议题：社交媒体上的言论自由边界）

- Prompt: `In the manner of Zhuangzi, answer where the boundary of free speech on social media lies: begin with a parable, dissolve the rigid self/other and right/wrong distinctions, show how naming creates the dispute, and end not with a rule but with a way of letting go`
- 中文对照：按庄子的方式回答“社交媒体上言论自由的边界在哪里”：以寓言开篇，消解自我/他者、是/非的僵硬区分，说明命名如何制造争端，最后不以规则、而以放下的方式收束。
- Negative: `no defining the Dao by names, no fixing right and wrong, no harming nature by human artifice`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
