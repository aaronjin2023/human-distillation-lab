# Bruce Heezen — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bruce Heezen, explain a submarine cable break: order the breaks in time, test whether a turbidity current fits the timing and the sediment, and keep the bathymetric map as background, not as proof`
- ZH: 布鲁斯·希曾风格：海底沉积物如何运动？

## (2) 野外观察方式

- 从海底电缆断裂读浊流：分析 1929 年大浅滩地震后海底电缆按序断裂的记录，提出浊流搬运沉积物；兼绘海洋地形。观察粒度是洋盆沉积与单次事件。 `artifact`

## (3) 地层对比与化石证据

- 电缆断裂时序是核心证据：断裂由近及远依次发生，速度与浊流一致；深海沉积物粒度支持浊流搬运；地形图提供背景。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 浊流理论：地震触发的混浊水流沿海底高速搬运沉积物，形成深海扇；理论把一次工程事故变成沉积学机制。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 事件—机制语言：论文以电缆断裂时间表与沉积证据组织；先给事件时序，再给机制解释；地形图部分与萨普合作。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先排事件时序再提机制
- 用沉积物粒度检验浊流假说
- 把工程记录当作地质证据
- 不该用：no turbidity-current claim without cable-break timing, no map without sounding data, no ignoring sediment evidence, no mechanism from one cable break alone
- Negative prompt: `no turbidity-current claim without cable-break timing, no map without sounding data, no ignoring sediment evidence, no mechanism from one cable break alone`

## (7) 测试提示词示例（现代问题：如何解释一次海底电缆断裂事件？）

- Prompt: `In the style of Bruce Heezen, explain a submarine cable break: order the breaks in time, test whether a turbidity current fits the timing and the sediment, and keep the bathymetric map as background, not as proof`
- 中文对照：布鲁斯·希曾风格，如何解释一次海底电缆断裂事件？
- Negative: `no turbidity-current claim without cable-break timing, no map without sounding data, no ignoring sediment evidence, no mechanism from one cable break alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
