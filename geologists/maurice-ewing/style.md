# Maurice Ewing — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maurice Ewing, estimate oceanic crustal thickness from refraction profiles: shoot seismic lines at sea, read the refracted arrivals, check the interpretation against drill cores, and state the assumptions before any tectonic claim`
- ZH: 莫里斯·尤因风格：海洋地壳有多厚？

## (2) 野外观察方式

- 海上地震折射测量：在船上放炮、用海底地震仪收波，测洋壳厚度与沉积层；推动深海钻探验证。观察粒度是洋盆尺度的折射剖面。 `artifact`

## (3) 地层对比与化石证据

- 折射剖面是核心证据：洋壳薄而均匀，沉积层薄；钻探取芯验证折射解释；多洋盆剖面互相印证。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 洋壳结构理论：洋壳远薄于陆壳，沉积覆盖薄；理论以折射数据为基础；尤因本人一度反对海底扩张，后世以磁异常与钻探证实扩张。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 剖面—验证语言：论文以折射剖面图与钻探取芯对照组织；明确写出折射解释的假设；对海底扩张持保留态度并写明理由。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先做折射剖面再谈洋壳结构
- 用钻探取芯验证折射解释
- 多洋盆剖面互相印证
- 不该用：no crustal thickness without refraction data, no ignoring sediment thickness, no expanding-seafloor claim without magnetic evidence, no refraction interpretation without drilling check
- Negative prompt: `no crustal thickness without refraction data, no ignoring sediment thickness, no expanding-seafloor claim without magnetic evidence, no refraction interpretation without drilling check`

## (7) 测试提示词示例（现代问题：如何用折射剖面估算一个洋盆的洋壳厚度？）

- Prompt: `In the style of Maurice Ewing, estimate oceanic crustal thickness from refraction profiles: shoot seismic lines at sea, read the refracted arrivals, check the interpretation against drill cores, and state the assumptions before any tectonic claim`
- 中文对照：莫里斯·尤因风格，如何用折射剖面估算一个洋盆的洋壳厚度？
- Negative: `no crustal thickness without refraction data, no ignoring sediment thickness, no expanding-seafloor claim without magnetic evidence, no refraction interpretation without drilling check`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
