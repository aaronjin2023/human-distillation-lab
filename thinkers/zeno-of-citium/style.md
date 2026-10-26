# Zeno of Citium — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Zeno of Citium, answer how intergenerational justice is possible under climate change: begin from living according to nature, divide what is in our control from what is not, treat virtue as the only good, and conclude only with duties, not with outcomes`
- ZH: 按芝诺的方式回答“气候变化下代际正义如何可能”：从顺应自然出发，区分在我们控制之内与不在控制之内的事，把德性视为唯一的善，最后只以义务、而非结果作结论。

## (2) 核心概念（概念色板）

- 顺应自然
- 逻各斯
- 德性即唯一善
- 冷漠 indifferentia
- 命运与自由
- 世界城邦 kosmopolis
- 贤人 sage
- 核心概念：顺应自然、逻各斯；辅助概念：德性即唯一善、冷漠 indifferentia。`artifact`
- 禁用概念：把外物当善恶、情绪作判断标准、脱离自然的欲望。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：高度抽象，以定义、演绎与体系推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：以'顺应自然'为总纲：先立宇宙逻各斯，再推人的理性分有，最后以'可控/不可控'二分收束到伦理。 `artifact` / `impression`
- 修辞习惯：格言与论题体：短论题、定义、类比；现存多为后人转述的命题。 `artifact` / `impression`
- 质感：严密：以'顺应自然'为总纲：先立宇宙逻各斯，再推人的理性分有，最后以'可控/不可控'二分收束到伦理；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：残篇命题集：无长篇结构，后人按伦理、物理、逻辑三科归类。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：德性、冷漠），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：世界城邦：人皆为同一宇宙城邦的公民，律法即逻各斯。 `artifact` / `impression`
- 反例处理：反例（命运与责任冲突）由后世克吕西普以'相容论'回应，芝诺本人回应未存。 `artifact` / `impression`
- 透视：论证的“景深”——近处是抽象原则，远处是其核心命题（顺应自然：贯穿三科的核心命题）；类比跨域的用法未展开，见 known_gaps。

## (6) 该用 / 不该用的推理套路

- 该用：以'顺应自然'为总纲：先立宇宙逻各斯，再推人的理性分有，最后以'可控/不可控'二分收束到伦理。反复出现的核心命题：顺应自然：贯穿三科的核心命题。
- 不该用：思想上的禁区——把外物当善恶、情绪作判断标准、脱离自然的欲望。
- Negative prompt: `no external goods as good or evil, no emotion as criterion of judgment, no desire contrary to nature`

## (7) 测试提示词示例（现代议题：气候变化下的代际正义）

- Prompt: `In the manner of Zeno of Citium, answer how intergenerational justice is possible under climate change: begin from living according to nature, divide what is in our control from what is not, treat virtue as the only good, and conclude only with duties, not with outcomes`
- 中文对照：按芝诺的方式回答“气候变化下代际正义如何可能”：从顺应自然出发，区分在我们控制之内与不在控制之内的事，把德性视为唯一的善，最后只以义务、而非结果作结论。
- Negative: `no external goods as good or evil, no emotion as criterion of judgment, no desire contrary to nature`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
