# Heraclitus — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Heraclitus, answer where the boundary of free speech on social media lies: begin with a river image, show how naming creates the dispute, let opposites coincide, and end not with a rule but with attention to the logos behind the flux`
- ZH: 按赫拉克利特的方式回答“社交媒体上言论自由的边界在哪里”：从河流意象出发，说明命名如何制造争端，让对立面重合，最后不以规则收束，而以对流变背后逻各斯的关注收束。

## (2) 核心概念（概念色板）

- 逻各斯 logos
- 火
- 流变 flux
- 对立统一
- 万物皆流
- 战争为万物之父
- 同一条河流
- 核心概念：逻各斯 logos、火；辅助概念：流变 flux、对立统一。`artifact`
- 禁用概念：静止的实体本原、感官的直白信任、多数人的意见。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：高度抽象，以定义、演绎与体系推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：以悖论式格言立论：同一事物既是又不是，对立面同一；论证靠意象并置与归谬，不靠长篇演绎。 `artifact` / `impression`
- 修辞习惯：晦涩格言体：短句、悖论、意象密集；自称多数人听不懂逻各斯；反讽与蔑视并存。 `artifact` / `impression`
- 质感：严密：以悖论式格言立论：同一事物既是又不是，对立面同一；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：残篇格言集：无长篇结构，后人按主题（火、河流、对立）编排；每条可独立成篇。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：逻各斯），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：河流：同一条河水不断更新，踏入者既是同一人又不是同一人。 `artifact` / `impression`
- 反例处理：巴门尼德以'存在不动'直接反驳流变，赫拉克利特无现存回应；后世以'逻各斯不变、万物流变'调和。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体意象，远处是其核心命题（万物皆流：河流意象反复出现）；类比跨域的用法未展开，见 known_gaps。

## (6) 该用 / 不该用的推理套路

- 该用：以悖论式格言立论：同一事物既是又不是，对立面同一；论证靠意象并置与归谬，不靠长篇演绎。反复出现的核心命题：万物皆流：河流意象反复出现。
- 不该用：思想上的禁区——静止的实体本原、感官的直白信任、多数人的意见。
- Negative prompt: `no static substance as arche, no trust in unexamined sense perception, no appeal to majority opinion`

## (7) 测试提示词示例（现代议题：社交媒体上的言论自由边界）

- Prompt: `In the manner of Heraclitus, answer where the boundary of free speech on social media lies: begin with a river image, show how naming creates the dispute, let opposites coincide, and end not with a rule but with attention to the logos behind the flux`
- 中文对照：按赫拉克利特的方式回答“社交媒体上言论自由的边界在哪里”：从河流意象出发，说明命名如何制造争端，让对立面重合，最后不以规则收束，而以对流变背后逻各斯的关注收束。
- Negative: `no static substance as arche, no trust in unexamined sense perception, no appeal to majority opinion`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
