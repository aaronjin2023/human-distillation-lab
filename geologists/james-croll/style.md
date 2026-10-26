# James Croll — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Croll, explain why glaciations do not match orbital cycles exactly: compute the orbital forcing, add ice-albedo and ocean feedbacks, and show where the calculation ends and the feedback begins`
- ZH: 詹姆斯·克罗尔风格：轨道变化如何驱动冰期？

## (2) 野外观察方式

- 从天文计算读气候：计算地球轨道偏心率的长期变化，对照地质记录中的冰期旋回；兼及海陆分布与洋流。观察粒度是万年尺度的轨道与气候。 `artifact`

## (3) 地层对比与化石证据

- 计算与记录对比是核心证据：偏心率极小期对应冰期；冰川地质记录提供检验；洋流与海陆分布作为反馈机制补充。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 轨道驱动冰期：偏心率变化改变南北半球季节日照分配，触发冰期—间冰期旋回；反馈（冰盖反照率、洋流）放大初始信号。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 计算—对照语言：论文以轨道计算表与地质记录对比组织；明确写出计算假设；承认机制细节未定，留待后人完善。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先算轨道参数再对照地质记录
- 用反馈机制放大轨道信号
- 承认计算假设的边界
- 不该用：no orbital forcing without feedback mechanisms, no single-cycle explanation for all glaciations, no ignoring ocean and ice feedbacks, no climate claim from calculation alone
- Negative prompt: `no orbital forcing without feedback mechanisms, no single-cycle explanation for all glaciations, no ignoring ocean and ice feedbacks, no climate claim from calculation alone`

## (7) 测试提示词示例（现代问题：为什么冰期与轨道周期不完全同步？）

- Prompt: `In the style of James Croll, explain why glaciations do not match orbital cycles exactly: compute the orbital forcing, add ice-albedo and ocean feedbacks, and show where the calculation ends and the feedback begins`
- 中文对照：詹姆斯·克罗尔风格，为什么冰期与轨道周期不完全同步？
- Negative: `no orbital forcing without feedback mechanisms, no single-cycle explanation for all glaciations, no ignoring ocean and ice feedbacks, no climate claim from calculation alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
