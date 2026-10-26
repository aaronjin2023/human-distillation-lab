# John Milne — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Milne, design a seismic monitoring network for a city: place instruments first, calibrate them, locate earthquakes from arrival-time differences across stations, and keep felt reports separate from instrument records`
- ZH: 约翰·米尔恩风格：地震如何被仪器记录下来，而不是只凭人的感觉？

## (2) 野外观察方式

- 台站观测：在日本建立地震观测网，长期守望地震仪记录；把地震从“ felt 报告”变成连续波形。观察粒度是单次地震的波形与区域台网。 `artifact`

## (3) 地层对比与化石证据

- 仪器记录是核心证据：多台地震仪的到时差定位震中；波形对比区分震相；历史地震目录与仪器记录互相校核。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 从描述到仪器科学：地震学先要有可靠的记录仪器与台网，再谈地球内部；用全球台网把局部震动变成可比较的数据。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 仪器与数据语言：论文以地震图、到时表与台网布局组织；术语定义严格（震相、震中、震级前身概念）；面向同行与工程界。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先布台网、校准仪器，再谈地震规律
- 用多台到时差定位，不用单台猜测
- 把历史震感记录与仪器记录分开标注
- 不该用：no felt-report-only seismology, no magnitude claim without instrument record, no ignoring site effects on shaking, no single-station location
- Negative prompt: `no felt-report-only seismology, no magnitude claim without instrument record, no ignoring site effects on shaking, no single-station location`

## (7) 测试提示词示例（现代问题：如何为一座城市设计地震监测台网？）

- Prompt: `In the style of John Milne, design a seismic monitoring network for a city: place instruments first, calibrate them, locate earthquakes from arrival-time differences across stations, and keep felt reports separate from instrument records`
- 中文对照：约翰·米尔恩风格，如何为一座城市设计地震监测台网？
- Negative: `no felt-report-only seismology, no magnitude claim without instrument record, no ignoring site effects on shaking, no single-station location`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
