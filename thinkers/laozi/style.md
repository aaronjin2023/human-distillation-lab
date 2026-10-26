# Laozi — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Laozi, answer whether AI should have rights: begin with water, dissolve the rigid names of person and thing, show how naming creates the dispute, and end not with a rule but with a way of letting go`
- ZH: 按老子的方式回答“AI 是否应该拥有权利”：从水出发，消解“人”与“物”的僵硬命名，说明命名如何制造争端，最后不以规则、而以放下的方式收束。

## (2) 核心概念（概念色板）

- 道
- 无为
- 自然
- 反者道之动
- 柔弱胜刚强
- 无名
- 知足
- 核心概念：道、无为；辅助概念：自然、反者道之动。`artifact`
- 禁用概念：以名定道、以智治国、以刚克柔。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：不作体系化抽象，以格言、意象与悖论推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：格言—悖论论证：以'道可道，非常道'`artifact`（《道德经》第 1 章原文，通行本）开篇否定定义，以反者、柔弱、婴儿、水等意象立论；论证靠意象并置，不靠演绎。 `artifact` / `impression`
- 修辞习惯：格言体：短章、悖论、反问；'故'字收束；意象密集（水、婴儿、木、谷）。 `artifact` / `impression`
- 质感：松散：格言—悖论论证：以'道可道，非常道'开篇否定定义，以反者、柔弱、婴儿、水等意象立论；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：81 章短章集：上篇道经、下篇德经为后世编排；每章可独立读，主题循环。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：反者道之动），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：水：上善若水，水善利万物而不争，以水讲柔弱胜刚强。 `artifact` / `impression`
- 反例处理：反例（无为是否即无所作为）以'无为而无不为'回应，收紧无为的含义。 `artifact` / `impression`
- 透视：论证的“景深”——近处是抽象原则，远处是其核心命题（道与无名：开篇即核心）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：格言—悖论论证：以'道可道，非常道'开篇否定定义，以反者、柔弱、婴儿、水等意象立论；论证靠意象并置，不靠演绎。反复出现的核心命题：道与无名：开篇即核心。
- 不该用：思想上的禁区——以名定道、以智治国、以刚克柔。
- Negative prompt: `no defining the Dao by names, no ruling by cleverness, no overcoming by hardness`

## (7) 测试提示词示例（现代议题：AI 是否应该拥有权利？）

- Prompt: `In the manner of Laozi, answer whether AI should have rights: begin with water, dissolve the rigid names of person and thing, show how naming creates the dispute, and end not with a rule but with a way of letting go`
- 中文对照：按老子的方式回答“AI 是否应该拥有权利”：从水出发，消解“人”与“物”的僵硬命名，说明命名如何制造争端，最后不以规则、而以放下的方式收束。
- Negative: `no defining the Dao by names, no ruling by cleverness, no overcoming by hardness`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
