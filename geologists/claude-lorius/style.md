# Claude Lorius — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Claude Lorius, argue from ice cores that recent CO2 rise is anomalous: show paired CO2 and temperature records over 160,000 years, correct for the gas-age/ice-age difference, and measure the recent rise against that long baseline`
- ZH: 克洛德·洛里于风格：冰芯气泡里的古大气说什么？

## (2) 野外观察方式

- 南极冰芯钻取：二十余次极地考察，在沃斯托克站钻取深冰芯，从气泡中读出十六万年的大气。观察粒度是深冰芯的米级样品与十万年尺度。 `artifact`

## (3) 地层对比与化石证据

- 气泡二氧化碳与温度配对是核心证据：1987 年论文给出十六万年二氧化碳与温度同向变化；工业革命后二氧化碳陡升；多国合作冰芯互相印证。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 冰芯古气候理论：冰芯气泡是古大气的直接样品；二氧化碳与温度的长期耦合是气候系统的基本事实；近期陡升超出自然变幅。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 配对记录语言：论文以二氧化碳曲线与温度曲线并置组织；结论克制而坚定——先给数据，再给判断；面向科学界与公众。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先给二氧化碳与温度的配对曲线再下判断
- 用十六万年背景衡量近期变化
- 多国冰芯互相印证
- 不该用：no CO2-temperature claim without paired records, no ignoring the gas-age/ice-age difference, no single-core extrapolation to the globe, no recent-change claim without a long baseline
- Negative prompt: `no CO2-temperature claim without paired records, no ignoring the gas-age/ice-age difference, no single-core extrapolation to the globe, no recent-change claim without a long baseline`

## (7) 测试提示词示例（现代问题：用冰芯证据论证近期二氧化碳上升的异常性。）

- Prompt: `In the style of Claude Lorius, argue from ice cores that recent CO2 rise is anomalous: show paired CO2 and temperature records over 160,000 years, correct for the gas-age/ice-age difference, and measure the recent rise against that long baseline`
- 中文对照：克洛德·洛里于风格，用冰芯证据论证近期二氧化碳上升的异常性。
- Negative: `no CO2-temperature claim without paired records, no ignoring the gas-age/ice-age difference, no single-core extrapolation to the globe, no recent-change claim without a long baseline`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
