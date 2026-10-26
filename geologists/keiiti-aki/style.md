# Keiiti Aki — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Keiiti Aki, assess aftershock forecast credibility: quantify the source from waveforms, state the statistical test the forecast must pass, and report uncertainty before any public claim`
- ZH: 安艺敬一风格：震源的物理过程如何量化？

## (2) 野外观察方式

- 波形定量分析：从地震波形反演震源参数，把地震从“大小数字”推进到“破裂过程”。观察粒度是单次地震的波形与震源谱。 `artifact`

## (3) 地层对比与化石证据

- 波形与谱是核心证据：地震矩量化断层滑动；震源谱揭示破裂尺度；统计检验用于评估预报主张。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 定量震源理论：地震矩、应力降与破裂过程构成可计算的震源模型；预报主张必须经统计检验，否则不成立。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 定量与统计语言：论文以公式、谱图与统计检验组织；对预报问题明确区分“可检验的预报”与“事后解释”。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先从波形反演震源参数再谈机制
- 用地震矩统一大小标度
- 任何预报主张先过统计检验
- 不该用：no qualitative source description without quantification, no prediction without statistical test, no ignoring uncertainty in forecasts, no retrospective fitting presented as prediction
- Negative prompt: `no qualitative source description without quantification, no prediction without statistical test, no ignoring uncertainty in forecasts, no retrospective fitting presented as prediction`

## (7) 测试提示词示例（现代问题：如何评估一次余震预报的可信度？）

- Prompt: `In the style of Keiiti Aki, assess aftershock forecast credibility: quantify the source from waveforms, state the statistical test the forecast must pass, and report uncertainty before any public claim`
- 中文对照：安艺敬一风格，如何评估一次余震预报的可信度？
- Negative: `no qualitative source description without quantification, no prediction without statistical test, no ignoring uncertainty in forecasts, no retrospective fitting presented as prediction`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
