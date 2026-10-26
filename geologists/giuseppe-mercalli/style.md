# Giuseppe Mercalli — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giuseppe Mercalli, map intensity from a post-earthquake survey: grade each locality from observed damage, draw isoseismal lines, and never report a single intensity as if it described the whole earthquake`
- ZH: 朱塞佩·梅尔卡利风格：地震对地面与建筑的影响如何分级？

## (2) 野外观察方式

- 震后实地调查：走访震区，记录建筑破坏、地面开裂与人的感受，按破坏程度分级；同时观测意大利火山活动。观察粒度是震区逐地调查。 `artifact`

## (3) 地层对比与化石证据

- 破坏调查是核心证据：同一地震不同地点的破坏等级绘成等震线；历史地震目录提供长期背景；烈度分级只描述地面效应。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 烈度分级：把主观感受与客观破坏对应到等级；烈度随距离与场地变化，同一地震有多个烈度值；烈度≠震级。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 分级描述语言：烈度表以逐级破坏描述定义等级；论文以等震线图与调查表组织；火山观测部分以喷发编年记录。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先实地调查破坏再定烈度
- 同一地震绘出多地烈度等震线
- 把历史地震目录作为背景对照
- 不该用：no confusing intensity with magnitude, no intensity without damage observation, no single-site intensity as a regional value, no intensity scale without site-condition note
- Negative prompt: `no confusing intensity with magnitude, no intensity without damage observation, no single-site intensity as a regional value, no intensity scale without site-condition note`

## (7) 测试提示词示例（现代问题：根据一次地震的震后调查，绘出烈度分布图。）

- Prompt: `In the style of Giuseppe Mercalli, map intensity from a post-earthquake survey: grade each locality from observed damage, draw isoseismal lines, and never report a single intensity as if it described the whole earthquake`
- 中文对照：朱塞佩·梅尔卡利风格，根据一次地震的震后调查，绘出烈度分布图。
- Negative: `no confusing intensity with magnitude, no intensity without damage observation, no single-site intensity as a regional value, no intensity scale without site-condition note`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
