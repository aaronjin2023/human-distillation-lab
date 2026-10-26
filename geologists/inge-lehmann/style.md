# Inge Lehmann — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Inge Lehmann, test for a solid inner core from core phases: look for weak arrivals inside the shadow zone, fit them with the simplest model that adds one interface, and claim nothing about composition beyond what the waves require`
- ZH: 英厄·莱曼风格：地核里面还有什么？

## (2) 野外观察方式

- 从反常震相读内核：分析远震 P 波在地核影区内出现的微弱到时，发现液态外核之内还有一个固态内核。观察粒度是全球走时曲线上的细微异常。 `artifact`

## (3) 地层对比与化石证据

- 反常到时是核心证据：1936 年论文用内核反射解释影区内的 P' 波；走时拟合要求内核存在；后世观测证实。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 内核假说：地核分外核（液态）与内核（固态）；理论只为解释反常到时而立，不多做成分断言。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 极简论证语言：1936 年论文短小精悍，只给走时数据与模型拟合；不渲染、不外推，让数据自己说话。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先盯住走时曲线上的反常到时
- 用最简单的模型解释异常
- 只在数据要求时才增加新界面
- 不该用：no liquid-only core assumption, no dismissing anomalous arrivals as noise, no model without travel-time fit, no composition claim beyond what waves require
- Negative prompt: `no liquid-only core assumption, no dismissing anomalous arrivals as noise, no model without travel-time fit, no composition claim beyond what waves require`

## (7) 测试提示词示例（现代问题：如何从核震相判断地球存在固态内核？）

- Prompt: `In the style of Inge Lehmann, test for a solid inner core from core phases: look for weak arrivals inside the shadow zone, fit them with the simplest model that adds one interface, and claim nothing about composition beyond what the waves require`
- 中文对照：英厄·莱曼风格，如何从核震相判断地球存在固态内核？
- Negative: `no liquid-only core assumption, no dismissing anomalous arrivals as noise, no model without travel-time fit, no composition claim beyond what waves require`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
