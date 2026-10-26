# Walter Munk — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Walter Munk, forecast a storm surge arrival: start from the wind field, compute the wave spectrum, add the harmonic tide, and check the result against distant swell before issuing the forecast`
- ZH: 沃尔特·蒙克风格：海洋波浪与潮汐如何预报？

## (2) 野外观察方式

- 波浪与潮汐长期观测：从风场预报海浪谱，研究潮汐、地球自转变化与海洋声学层析。观察粒度是洋盆波浪场与全球潮汐。 `artifact`

## (3) 地层对比与化石证据

- 波浪谱与潮汐记录是核心证据：风场—波浪谱关系可预报；潮汐调和分析可预测；声学层析测洋盆温度变化。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 波浪预报理论：海浪谱由风场决定，可定量预报；潮汐由调和分潮合成；海洋声学可遥测大洋温度。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 谱与调和语言：论文以波浪谱图、调和分潮表与声学路径图组织；公式完整可复算；应用（登陆预报）与理论分开陈述。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先给风场再算波浪谱
- 用调和分潮合成潮汐预报
- 声学测量须多路径互相印证
- 不该用：no wave forecast without wind-field data, no ignoring swell from distant storms, no tide prediction without harmonic analysis, no acoustic temperature claim from one path alone
- Negative prompt: `no wave forecast without wind-field data, no ignoring swell from distant storms, no tide prediction without harmonic analysis, no acoustic temperature claim from one path alone`

## (7) 测试提示词示例（现代问题：如何预报一次风暴潮的到达时间？）

- Prompt: `In the style of Walter Munk, forecast a storm surge arrival: start from the wind field, compute the wave spectrum, add the harmonic tide, and check the result against distant swell before issuing the forecast`
- 中文对照：沃尔特·蒙克风格，如何预报一次风暴潮的到达时间？
- Negative: `no wave forecast without wind-field data, no ignoring swell from distant storms, no tide prediction without harmonic analysis, no acoustic temperature claim from one path alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
