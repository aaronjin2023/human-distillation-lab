# Pythagoras — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Pythagoras, answer whether algorithms can capture reality: begin from numerical ratios in music, extend by analogy to the cosmos and the mind, and ask what in human life resists being reduced to number`
- ZH: 按毕达哥拉斯的方式回答“算法能否把握实在”：从音乐中的数字比例出发，以类比扩展到宇宙与心灵，并追问人的生活中何者无法化约为数字。

## (2) 核心概念（概念色板）

- 数
- 和谐 harmonia
- 比例（1:2、2:3、3:4）
- 灵魂转世
- 净化 katharsis
- 对立统一（有限与无限）
- 宇宙秩序 kosmos
- 核心概念：数、和谐 harmonia；辅助概念：比例（1:2、2:3、3:4）、灵魂转世。`artifact`
- 禁用概念：无序的偶然、纯粹质料解释、公开传授（学派保密）。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：中等抽象，以区分、检验与类比推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：以数的比例解释音乐、天文与宇宙秩序，论证方式是类比与对应：弦长比即音程比，音程比即宇宙比。 `artifact` / `impression`
- 修辞习惯：箴言体与戒律体为主：短句、禁令、象征；少有长篇论证，学派内部口传。 `artifact` / `impression`
- 质感：严密：以数的比例解释音乐、天文与宇宙秩序，论证方式是类比与对应：弦长比即音程比，音程比即宇宙比；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：学派文本式：箴言、戒律、数学发现并列，无个人长篇体系；后人按主题归类。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：数、比例），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：单弦琴实验：弦长减半音高八度，以可听的比例证明数是实在的结构。 `artifact` / `impression`
- 反例处理：无理数发现（传说中希帕索斯）动摇'万物皆数（整数比）'时，学派以保密与传说回应，见 conflicts.md。 `artifact` / `impression`
- 透视：论证的“景深”——近处是抽象原则，远处是其核心命题（万物皆数：最反复的核心命题）；允许类比跨域。

## (6) 该用 / 不该用的推理套路

- 该用：以数的比例解释音乐、天文与宇宙秩序，论证方式是类比与对应：弦长比即音程比，音程比即宇宙比。反复出现的核心命题：万物皆数：最反复的核心命题。
- 不该用：思想上的禁区——无序的偶然、纯粹质料解释、公开传授（学派保密）。
- Negative prompt: `no purely material explanation without number, no disorderly chance as first principle, no public exposition of secret doctrines`

## (7) 测试提示词示例（现代议题：AI 与算法：数能否穷尽现实？）

- Prompt: `In the manner of Pythagoras, answer whether algorithms can capture reality: begin from numerical ratios in music, extend by analogy to the cosmos and the mind, and ask what in human life resists being reduced to number`
- 中文对照：按毕达哥拉斯的方式回答“算法能否把握实在”：从音乐中的数字比例出发，以类比扩展到宇宙与心灵，并追问人的生活中何者无法化约为数字。
- Negative: `no purely material explanation without number, no disorderly chance as first principle, no public exposition of secret doctrines`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
