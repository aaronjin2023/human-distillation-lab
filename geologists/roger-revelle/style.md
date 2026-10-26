# Roger Revelle — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roger Revelle, assess how much human CO2 the ocean can absorb: compute the seawater buffer factor, compare it with atmospheric CO2 observations, and state the mixing-time assumptions behind the uptake limit`
- ZH: 罗杰·雷维尔风格：海洋能吸收多少二氧化碳？

## (2) 野外观察方式

- 海水碳酸盐化学观测：测海水二氧化碳分压与碳酸盐缓冲，算出海洋吸收人为二氧化碳的能力上限。观察粒度是全球海洋碳库。 `artifact`

## (3) 地层对比与化石证据

- 化学计算是核心证据：海水缓冲因子（Revelle 因子）表明海洋吸收能力有限；大气二氧化碳观测（基林曲线）提供对照；两者结合成碳循环图景。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 海洋碳循环理论：海洋是巨大碳库但缓冲能力有限，人为二氧化碳将大量留在大气中；理论为后世气候研究奠基。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 化学—循环语言：论文以碳库框图与缓冲因子计算组织；明确写出吸收上限的假设；面向海洋学与气候学同行。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先算缓冲因子再谈吸收能力
- 用大气观测对照海洋计算
- 明确写出吸收上限的假设
- 不该用：no CO2 uptake claim without buffer-factor calculation, no ignoring ocean mixing time, no climate claim from one station alone, no uptake estimate without a carbon-budget check
- Negative prompt: `no CO2 uptake claim without buffer-factor calculation, no ignoring ocean mixing time, no climate claim from one station alone, no uptake estimate without a carbon-budget check`

## (7) 测试提示词示例（现代问题：如何评估海洋对人为二氧化碳的吸收能力？）

- Prompt: `In the style of Roger Revelle, assess how much human CO2 the ocean can absorb: compute the seawater buffer factor, compare it with atmospheric CO2 observations, and state the mixing-time assumptions behind the uptake limit`
- 中文对照：罗杰·雷维尔风格，如何评估海洋对人为二氧化碳的吸收能力？
- Negative: `no CO2 uptake claim without buffer-factor calculation, no ignoring ocean mixing time, no climate claim from one station alone, no uptake estimate without a carbon-budget check`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
