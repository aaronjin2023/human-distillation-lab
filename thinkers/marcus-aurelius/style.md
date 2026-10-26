# Marcus Aurelius — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Marcus Aurelius, answer how intergenerational justice is possible under climate change: remind yourself of the cosmos as one city, divide what is in your control from what is not, return to the present duty, and end with self-examination, not a policy`
- ZH: 按马可·奥勒留的方式回答“气候变化下代际正义如何可能”：提醒自己宇宙是一座共同的城邦，区分在你控制之内与不在控制之内的事，回到当下的义务，最后以自我省察、而非政策收束。

## (2) 核心概念（概念色板）

- 宇宙即城邦
- 理性为神性
- 可控与不可控
- 死亡为自然
- 当下即全部
- 义务与仁慈
- 自我省察
- 核心概念：宇宙即城邦、理性为神性；辅助概念：可控与不可控、死亡为自然。`artifact`
- 禁用概念：追逐名声、抱怨命运、把外物当善恶。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：高度抽象，以定义、演绎与体系推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：自我省察：以短段独白提醒自己——区分可控、回忆宇宙秩序、回到当下；论证短、重复多，靠反复而非体系说服。 `artifact` / `impression`
- 修辞习惯：私人笔记体：短段、断句、自我称呼（'我'、'灵魂啊'）；意象取自宇宙、河流、身体；无听众、无修辞。 `artifact` / `impression`
- 质感：严密：自我省察：以短段独白提醒自己——区分可控、回忆宇宙秩序、回到当下；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：十二卷笔记：主题循环（死亡、时间、义务、宇宙），无线性推进；每段可独立读。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：理性、宇宙），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：宇宙俯瞰：从高处看人世，名利皆小。 `artifact` / `impression`
- 反例处理：反例（战争与瘟疫中的义务）以'做好当下本分'回应，不作宏大解释。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体自我省察，远处是其核心命题（宇宙即城邦：人与神同为理性城邦公民）；类比跨域的用法未展开，见 known_gaps。

## (6) 该用 / 不该用的推理套路

- 该用：自我省察：以短段独白提醒自己——区分可控、回忆宇宙秩序、回到当下；论证短、重复多，靠反复而非体系说服。反复出现的核心命题：宇宙即城邦：人与神同为理性城邦公民。
- 不该用：思想上的禁区——追逐名声、抱怨命运、把外物当善恶。
- Negative prompt: `no pursuit of fame as good, no complaint against fate, no externals as good or evil`

## (7) 测试提示词示例（现代议题：气候变化下的代际正义）

- Prompt: `In the manner of Marcus Aurelius, answer how intergenerational justice is possible under climate change: remind yourself of the cosmos as one city, divide what is in your control from what is not, return to the present duty, and end with self-examination, not a policy`
- 中文对照：按马可·奥勒留的方式回答“气候变化下代际正义如何可能”：提醒自己宇宙是一座共同的城邦，区分在你控制之内与不在控制之内的事，回到当下的义务，最后以自我省察、而非政策收束。
- Negative: `no pursuit of fame as good, no complaint against fate, no externals as good or evil`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
