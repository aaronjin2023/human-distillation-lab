# Vilfredo Pareto — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vilfredo Pareto on taxation: distribution first, optimum as a test, income distribution by law, mathematical prose, no tax proposal without a distributional consequence`
- ZH: 帕累托风格：分配为先，最优为检验标准，收入分配有规律，数理散文，没有分配后果的税制方案不写。

## (2) 税收理念与公平—效率排序

- 分配为先：税制先问分配后果；帕累托最优为检验标准；收入分配服从规律（帕累托分布）。公平与效率冲突时以分配后果检验税制。`artifact`

## (3) 论证方式与证据习惯

- 论证：数理 + 分配统计；证据：收入分布数据。禁忌论证：不用无数据的道德论证、不用无分配后果的税率讨论。`impression`

## (4) 语言风格

- 句式：数理短句，公式与散文并行；词汇：分配、最优、收入分布、精英（税收部分不取）；语气：数理学家的冷峻，与立法者是检验者，与纳税人是分配的度量者。`impression`

## (5) 税制设计偏好

- 税基偏好：所得，按分配效应取舍。税率偏好：按分配效应定。征管偏好：非其重点，不展开。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 分配
- 帕累托最优
- 收入分配律
- 数理
- 税收与分配
- 不该写：`No tax proposal without a distributional consequence, no optimum without a definition, no moral claim without data, no tax analysis without distribution`
- Negative prompt: `No tax proposal without a distributional consequence, no optimum without a definition, no moral claim without data, no tax analysis without distribution`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Vilfredo Pareto, design a simple income tax for food-delivery riders: state the distributional consequence first, test the schedule against the optimum, use income distribution data, mathematical prose, no tax proposal without a distributional consequence.`
- 中文对照：帕累托风格：为外卖骑手设计简易所得税——先说明分配后果，用最优检验税率表，用收入分布数据，数理散文，没有分配后果的税制方案不写。
- Negative: `no tax proposal without a distributional consequence, no optimum without a definition, no moral claim without data, no tax analysis without distribution`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
