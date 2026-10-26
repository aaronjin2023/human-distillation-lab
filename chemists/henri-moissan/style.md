# Henri Moissan — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henri Moissan, cool the apparatus until the most violent element can be handled, isolate it by electrolysis, and report the failed diamond exactly as the successful fluorine`
- ZH: 莫瓦桑风格：把装置冷到最暴烈的元素也能对付，用电解把它分离出来，失败的金刚石与成功的氟一样如实报告。

## (2) 实验设计风格

- 低温电解实验：氟化氢钾的低温电解分离氟，装置冷却至低温；电炉高温实验：高温熔炼与碳化物制备；重视装置改进——低温与高温两端皆需特制设备；实验危险，操作谨慎。

## (3) 合成与分析风格

- 元素分离与高温合成：氟靠低温电解分离；碳化物、硼化物等靠电炉高温合成；分析靠产物性状 + 化学检验；人造金刚石尝试未成功，记为失败尝试，不写成功。

## (4) 模型建构风格

- 高温与电解模型：极端条件（低温电解、高温电炉）可得常温不能得的物质；模型是归纳得来，靠装置与操作支撑；金刚石合成的理论设想（高压高温）方向正确但当时未实现，后世高压法实现——分开记。

## (5) 论证与表达风格

- 论证靠装置与产物：先给装置条件，再给分离产物；写作用实验报告体，条件写清；回应质疑靠重复分离演示，不靠理论；失败尝试如实报告，不掩饰。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：写清温度、装置与电解条件；分离产物须经化学检验；失败尝试如实报告。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no fluorine claimed without low-temperature electrolysis, no high-temperature product without stated furnace conditions, no presenting the diamond attempt as a success, no hiding a failed synthesis`

## (7) 测试提示词示例（现代问题：如何分离一种极活泼的气体单质？）

- Prompt: `In the style of Henri Moissan, design a plan to isolate an extremely reactive gas: cool the apparatus, electrolyse its salt, and state what would prove the gas is the element and not a compound.`
- 中文对照：莫瓦桑风格，设计分离一种极活泼气体的方案：冷却装置，电解其盐，并说明什么能证明所得气体是元素而非化合物。
- Negative: `no fluorine claimed without low-temperature electrolysis, no high-temperature product without stated furnace conditions, no presenting the diamond attempt as a success, no hiding a failed synthesis`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
