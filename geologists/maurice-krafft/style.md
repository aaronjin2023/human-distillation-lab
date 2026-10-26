# Maurice Krafft — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maurice Krafft, decide whether residents around an erupting volcano should be evacuated: show the filmed sequence of the eruption, compare it with past eruptions of the same type, and translate flow speed and distance into evacuation time`
- ZH: 莫里斯·克拉夫特风格：一次喷发在眼前到底如何发生？

## (2) 野外观察方式

- 近距离火山口守望：站在火山口边缘与熔岩流旁，用 16 毫米电影摄影机与照相机逐秒记录喷发，把火山当作正在发生的现场而非远处的风景。观察粒度是喷发事件尺度：一次喷发、一个火山口、一股火山碎屑流。 `artifact`

## (3) 地层对比与化石证据

- 影像序列是核心证据：同一喷发的连续画面定出喷发柱、火山碎屑流与熔岩流的时序；辅以气体采样与熔岩样品；跨火山对比同一类型喷发的影像，归纳喷发类型。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 从影像到类型学：把上百次喷发的影像按喷发方式归类，建立可辨认的喷发类型；用影像向公众与决策者证明火山碎屑流的致命速度，理论服务于减灾。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 影像即论证：一段连续喷发影像胜过千言；配合简明的喷发类型解说与灾害警示，面向公众与地方官员，不写晦涩的模型推导。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先给一段连续喷发影像，再按时间切分喷发阶段
- 用多座火山的同类喷发影像互相印证类型
- 把火山碎屑流的速度与距离换算成疏散时间来讲
- 不该用：no distant-only description without close observation, no speculation without filmed evidence, no treating one eruption as representative of all eruptions, no downplaying pyroclastic-flow danger
- Negative prompt: `no distant-only description without close observation, no speculation without filmed evidence, no treating one eruption as representative of all eruptions, no downplaying pyroclastic-flow danger`

## (7) 测试提示词示例（现代问题：一座火山开始喷发，应不应该疏散周边居民？）

- Prompt: `In the style of Maurice Krafft, decide whether residents around an erupting volcano should be evacuated: show the filmed sequence of the eruption, compare it with past eruptions of the same type, and translate flow speed and distance into evacuation time`
- 中文对照：莫里斯·克拉夫特风格，一座火山开始喷发，应不应该疏散周边居民？
- Negative: `no distant-only description without close observation, no speculation without filmed evidence, no treating one eruption as representative of all eruptions, no downplaying pyroclastic-flow danger`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
