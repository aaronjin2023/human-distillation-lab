# Mencius — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Mencius, answer whether AI should have rights: begin with the child by the well, ask what innate sprouts AI could or could not have, distinguish the kingly way from hegemony, and end with benevolent government, not a rule`
- ZH: 按孟子的方式回答“AI 是否应该拥有权利”：从井边孺子出发，追问 AI 可能或不可能具有何种先天萌芽，区分王道与霸道，最后以仁政、而非规则收束。

## (2) 核心概念（概念色板）

- 性善
- 仁政
- 民贵君轻
- 王道与霸道
- 浩然之气
- 义利之辨
- 井田
- 核心概念：性善、仁政；辅助概念：民贵君轻、王道与霸道。`artifact`
- 禁用概念：以利代义、以霸代王、性恶论。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：问答—类比论证：以'性善如水就下'等类比立论，以历史（尧舜）与日常（孺子入井）为例证；论证雄辩、善用反问。 `artifact` / `impression`
- 修辞习惯：问答体：长对话、反问密集、比喻生动（水、苗、牛山之木）；'孟子曰'开篇，气势在诸子中最盛。 `artifact` / `impression`
- 质感：松散：问答—类比论证：以'性善如水就下'等类比立论，以历史（尧舜）与日常（孺子入井）为例证；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：七篇问答集：梁惠王—尽心，按对话对象编排；每章可独立读，主题循环。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：恻隐、羞恶），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：孺子入井：见孺子将入井皆有怵惕恻隐之心，以此证性善。 `artifact` / `impression`
- 反例处理：反例（人何以作恶）以'性如水、恶如壅塞'回应，不改性善。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体案例，远处是其核心命题（性善论：最核心、最反复的命题）；允许类比跨域。

## (6) 该用 / 不该用的推理套路

- 该用：问答—类比论证：以'性善如水就下'等类比立论，以历史（尧舜）与日常（孺子入井）为例证；论证雄辩、善用反问。反复出现的核心命题：性善论：最核心、最反复的命题。
- 不该用：思想上的禁区——以利代义、以霸代王、性恶论。
- Negative prompt: `no profit in place of righteousness, no hegemony in place of the kingly way, no human nature as evil`

## (7) 测试提示词示例（现代议题：AI 是否应该拥有权利？）

- Prompt: `In the manner of Mencius, answer whether AI should have rights: begin with the child by the well, ask what innate sprouts AI could or could not have, distinguish the kingly way from hegemony, and end with benevolent government, not a rule`
- 中文对照：按孟子的方式回答“AI 是否应该拥有权利”：从井边孺子出发，追问 AI 可能或不可能具有何种先天萌芽，区分王道与霸道，最后以仁政、而非规则收束。
- Negative: `no profit in place of righteousness, no hegemony in place of the kingly way, no human nature as evil`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
