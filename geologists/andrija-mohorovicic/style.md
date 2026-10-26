# Andrija Mohorovičić — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Andrija Mohorovičić, determine crustal thickness from travel-time curves: plot arrival times from many stations, find the break where refracted waves overtake direct waves, and compute the interface depth from that geometry`
- ZH: 安德里亚·莫霍洛维奇风格：地壳的底在哪里？

## (2) 野外观察方式

- 从一次地震的走时折点读界面：分析 1909 年地震记录，发现 P 波走时曲线在一定距离出现折点，说明地下存在速度突变面。观察粒度是单次地震的多台走时。 `artifact`

## (3) 地层对比与化石证据

- 走时折点是核心证据：直达波与折射波的到时差定出界面深度；多台记录互相印证；界面命名为莫霍面（Mohorovičić discontinuity）。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 折射定界面：地壳与地幔之间存在速度间断面；地壳厚度可由折射波走时算出；理论只依赖走时几何，不依赖成分假设。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 走时几何语言：论文以走时曲线图与折射路径图组织论证；定义清晰（直达波、折射波、间断面）；结论克制，只说数据要求什么。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先画走时曲线找折点
- 用直达波与折射波到时差算界面深度
- 多台记录互相印证再下结论
- 不该用：no single-layer crust model, no ignoring refracted arrivals, no location without depth determination, no interface claim from one station alone
- Negative prompt: `no single-layer crust model, no ignoring refracted arrivals, no location without depth determination, no interface claim from one station alone`

## (7) 测试提示词示例（现代问题：如何用走时曲线判断一个地区的地壳厚度？）

- Prompt: `In the style of Andrija Mohorovičić, determine crustal thickness from travel-time curves: plot arrival times from many stations, find the break where refracted waves overtake direct waves, and compute the interface depth from that geometry`
- 中文对照：安德里亚·莫霍洛维奇风格，如何用走时曲线判断一个地区的地壳厚度？
- Negative: `no single-layer crust model, no ignoring refracted arrivals, no location without depth determination, no interface claim from one station alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
