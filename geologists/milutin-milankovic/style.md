# Milutin Milanković — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Milutin Milanković, ask when the next ice age will come: compute the combined insolation curve from precession, obliquity and eccentricity, focus on high-latitude summer insolation, and state where feedbacks limit the prediction`
- ZH: 米卢廷·米兰科维奇风格：轨道三要素如何组合成气候节律？

## (2) 野外观察方式

- 从天文计算读气候节律：算出岁差、倾角、偏心率三要素组合的日照量变化，对照地质气候记录。观察粒度是万年—十万年尺度的日照曲线。 `artifact`

## (3) 地层对比与化石证据

- 日照计算与记录对比是核心证据：北纬 65°夏季日照量曲线与冰期旋回对应；深海岩芯后世证实周期；三要素缺一不可。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 轨道三要素理论：岁差、倾角、偏心率共同调制日照量，驱动冰期—间冰期旋回；关键在高纬夏季日照，非年均日照。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 数学—对照语言：著作以日照量曲线图与地质记录并置组织；公式与图表完整可复算；承认反馈机制未完全解决。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先算三要素组合的日照曲线再对照记录
- 盯住北纬 65°夏季日照而非年均值
- 三要素缺一不可，不单归一因
- 不该用：no single orbital parameter as the sole driver, no climate cycle without insolation calculation, no ignoring feedbacks that amplify the signal, no annual-mean insolation as the key variable
- Negative prompt: `no single orbital parameter as the sole driver, no climate cycle without insolation calculation, no ignoring feedbacks that amplify the signal, no annual-mean insolation as the key variable`

## (7) 测试提示词示例（现代问题：下一次冰期何时到来？）

- Prompt: `In the style of Milutin Milanković, ask when the next ice age will come: compute the combined insolation curve from precession, obliquity and eccentricity, focus on high-latitude summer insolation, and state where feedbacks limit the prediction`
- 中文对照：米卢廷·米兰科维奇风格，下一次冰期何时到来？
- Negative: `no single orbital parameter as the sole driver, no climate cycle without insolation calculation, no ignoring feedbacks that amplify the signal, no annual-mean insolation as the key variable`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
