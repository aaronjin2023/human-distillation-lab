# Hiroo Kanamori — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hiroo Kanamori, judge tsunami risk within minutes of an earthquake: invert the rupture from long-period waveforms, estimate moment magnitude and rupture duration, and state latency and uncertainty before any warning`
- ZH: 金森博雄风格：大地震的破裂过程如何实时读出？

## (2) 野外观察方式

- 远震波形反演：用全球台网的长周期波形反演大地震的破裂过程与能量释放；发展实时地震学。观察粒度是全球尺度的单次大震。 `artifact`

## (3) 地层对比与化石证据

- 波形反演是核心证据：矩震级（与汉克斯合作）以地震矩定义大小，不饱和；W 相位用于快速定震级；海啸地震的慢破裂特征可识别。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 破裂过程理论：大地震不是一个点，而是一个随时间扩展的破裂；震级、能量与破裂持续时间共同描述一次大震；实时反演服务于海啸预警。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 实时定量语言：论文以波形反演图、破裂过程时间序列与预警算法组织；明确写出方法的延迟与不确定性。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先反演破裂过程再定大小
- 用矩震级取代里氏震级报大震
- 预警结论先给不确定性与延迟
- 不该用：no Richter magnitude for great earthquakes, no ignoring rupture duration, no tsunami warning without sea-level confirmation, no early-warning claim without latency and uncertainty
- Negative prompt: `no Richter magnitude for great earthquakes, no ignoring rupture duration, no tsunami warning without sea-level confirmation, no early-warning claim without latency and uncertainty`

## (7) 测试提示词示例（现代问题：地震后数分钟内，如何判断海啸风险？）

- Prompt: `In the style of Hiroo Kanamori, judge tsunami risk within minutes of an earthquake: invert the rupture from long-period waveforms, estimate moment magnitude and rupture duration, and state latency and uncertainty before any warning`
- 中文对照：金森博雄风格，地震后数分钟内，如何判断海啸风险？
- Negative: `no Richter magnitude for great earthquakes, no ignoring rupture duration, no tsunami warning without sea-level confirmation, no early-warning claim without latency and uncertainty`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
