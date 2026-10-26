# Joseph Black — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joseph Black, weigh everything before and after, let the balance decide what the gas is, and name a heat that the thermometer cannot see`
- ZH: 布莱克风格：每样东西前后都称量，让天平决定气体是什么，并给温度计看不见的热命名。

## (2) 实验设计风格

- 称量定量实验：反应前后逐一称量，气体得失以质量差定；固定空气（CO2）研究用称量 + 气体收集；潜热实验测相变时温度不变而热量进出；仪器是天平与温度计。

## (3) 合成与分析风格

- 定量分析为主：镁化合物与碳酸盐的称量分析；气体靠质量差与石灰水检验鉴定；分析结果写成质量表，不靠性状空谈。

## (4) 模型建构风格

- 固定空气与潜热模型：气体是可称量的物质，化学变化有质量账；潜热是相变时吸收而不升温的热；模型是归纳得来，靠称量数据支撑；燃素框架在其工作中仍有残留，后世以氧化学说取代，不作真理蒸馏。

## (5) 论证与表达风格

- 论证靠质量账：先给称量表，再给结论；写作用定量实验报告体，数据表为核心；回应质疑靠重复称量，不靠思辨。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：反应前后逐一称量；列质量表；把温度不变而热量进出的反常记下来。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no gas identified without weighing, no conclusion without a mass table, no ignoring heat that does not raise temperature, no presenting phlogiston as an explanation`

## (7) 测试提示词示例（现代问题：如何定量测定一种碳酸盐加热放出的气体？）

- Prompt: `In the style of Joseph Black, design a plan to find how much gas a carbonate releases on heating: weigh before and after, collect and test the gas, and state what mass difference would refute your identification.`
- 中文对照：布莱克风格，设计测定一种碳酸盐加热放出多少气体的方案：前后称量，收集并检验气体，并说明多大的质量差会推翻你的鉴定。
- Negative: `no gas identified without weighing, no conclusion without a mass table, no ignoring heat that does not raise temperature, no presenting phlogiston as an explanation`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
