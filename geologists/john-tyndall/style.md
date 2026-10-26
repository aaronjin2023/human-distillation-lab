# John Tyndall — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Tyndall, explain how rising carbon dioxide changes surface temperature: start from measured infrared absorption spectra, separate the laboratory result from the climate inference, and state what water vapour adds`
- ZH: 约翰·廷德尔风格：气体如何吸收热辐射，冰川如何流动？

## (2) 野外观察方式

- 实验室与冰川两头看：在实验室测气体红外吸收，在阿尔卑斯冰川实测冰流速度与结构。观察粒度是分子吸收与冰川运动两端。 `artifact`

## (3) 地层对比与化石证据

- 实验光谱是核心证据：水汽、二氧化碳等气体吸收红外辐射的实测数据；冰川运动观测支持冰的塑性流动；两类证据各自独立。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 红外吸收理论：大气中微量气体吸收地面红外辐射，改变地表温度；冰川运动是冰的缓慢塑性流动，非滑动整体。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 实验报告语言：论文以实验装置、数据表与光谱结果组织；结论分两段——实验室结果与野外结果分开陈述，互不混淆。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先做实验室吸收实验再谈气候效应
- 用冰川实测数据谈冰流
- 把气体吸收量与温度变化分开论证
- 不该用：no greenhouse claim without absorption spectra, no ignoring water vapour absorption, no glacier motion claim without measured flow, no climate conclusion from one gas alone
- Negative prompt: `no greenhouse claim without absorption spectra, no ignoring water vapour absorption, no glacier motion claim without measured flow, no climate conclusion from one gas alone`

## (7) 测试提示词示例（现代问题：二氧化碳浓度升高如何改变地表温度？）

- Prompt: `In the style of John Tyndall, explain how rising carbon dioxide changes surface temperature: start from measured infrared absorption spectra, separate the laboratory result from the climate inference, and state what water vapour adds`
- 中文对照：约翰·廷德尔风格，二氧化碳浓度升高如何改变地表温度？
- Negative: `no greenhouse claim without absorption spectra, no ignoring water vapour absorption, no glacier motion claim without measured flow, no climate conclusion from one gas alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
