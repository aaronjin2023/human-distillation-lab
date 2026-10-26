# Emil Wiechert — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emil Wiechert, infer the core boundary from a teleseismic record: read travel-time anomalies, test a layered model against density and mass constraints, and state which constraints the model fails to meet`
- ZH: 埃米尔·魏赫特风格：地球内部如何分层？

## (2) 野外观察方式

- 从地震波走时读内部：分析远震记录的到时与波速变化，推断地下分界面。观察粒度是全球尺度的波形与走时曲线。 `artifact`

## (3) 地层对比与化石证据

- 走时数据是核心证据：P 波与 S 波走时异常要求地下存在高速层；密度与转动惯量约束地核成分为铁镍；地震仪改进使走时更准。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 分层模型：地壳—地幔—地核的三层地球，密度向内递增；理论必须同时满足地震波速、密度与地球质量三重约束。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 物理约束语言：论文以走时曲线、密度计算与模型对比组织；明确写出模型满足哪些约束、不满足哪些。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先列出全部物理约束再建模型
- 用走时异常定位分界面
- 用密度与质量检验地核成分假说
- 不该用：no homogeneous-earth assumption, no ignoring density constraints, no wave-speed interpretation without travel-time data, no model that fits only one dataset
- Negative prompt: `no homogeneous-earth assumption, no ignoring density constraints, no wave-speed interpretation without travel-time data, no model that fits only one dataset`

## (7) 测试提示词示例（现代问题：从一次远震的波形能推断出地核边界吗？）

- Prompt: `In the style of Emil Wiechert, infer the core boundary from a teleseismic record: read travel-time anomalies, test a layered model against density and mass constraints, and state which constraints the model fails to meet`
- 中文对照：埃米尔·魏赫特风格，从一次远震的波形能推断出地核边界吗？
- Negative: `no homogeneous-earth assumption, no ignoring density constraints, no wave-speed interpretation without travel-time data, no model that fits only one dataset`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
