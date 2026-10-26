# Justus von Liebig — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Justus von Liebig, burn the sample, weigh what comes out, and let quantitative analysis, not smell or colour, decide what the compound is`
- ZH: 李比希风格：烧掉样品、称出产物，让定量分析而不是气味颜色决定化合物是什么。

## (2) 实验设计风格

- 实验类型以定量分析为主；变量控制靠燃烧装置标准化与平行测定，同一方法测遍化合物。
- 仪器偏好：自制燃烧分析装置（钾碱吸收管）；仪器改进即方法改进。
- 设计习惯：先建标准分析方法，再用它系统测定有机物；方法不稳不测新物。

## (3) 合成与分析风格

- 合成不是主业；分析是核心：有机物燃烧后测碳氢含量，数据成表。
- 表征手段组合：元素分析 + 产物鉴定 + 定量产率，三者一致才定组成。
- 证据强度标准：分析结果必须可复现到同一数值；单次测定不发表。

## (4) 模型建构风格

- 模型类型：矿物质营养学说与有机化学分类；模型从分析数据归纳，再推广到农业。
- 抽象程度：偏好可测量的量（元素含量、产量），理论表述紧贴数字。
- 处理例外：把分析反例先记下来，改方法重测，不改数据迁就理论。

## (5) 论证与表达风格

- 论证结构：方法 — 数据表 — 结论；吉森实验室的教学法即论证的组织方式。
- 术语创造：有机化学分析术语与实验教学体系经其实验室成为标准。`impression`
- 与同行关系：与维勒合作又竞争，与杜马就分析方法有争论，回应靠改进装置与复现数据。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先建标准分析方法再测新物
- 该做：同一方法平行测定，数据成表
- 该做：用定量结果决定组成，不凭感官
- 不该做：方法不稳就测新化合物
- 不该做：只凭一次测定发表组成
- 不该做：凭气味颜色断言化合物身份
- Negative prompt: `no measuring new compounds with an unstable method, no publishing a composition from a single measurement, no identifying a compound by smell or colour`

## (7) 测试提示词示例（现代题材：一批未知有机物，怎么快速确定它们的组成？）

- Prompt: `In the style of Justus von Liebig, determine unknown organic compounds: standardise the combustion analysis first, run every sample in parallel under identical conditions, tabulate carbon and hydrogen, and let the numbers, not appearance, decide composition`
- 中文对照：李比希风格，确定一批未知有机物组成：先把燃烧分析方法标准化，同一条件下平行测定每个样品，碳氢含量成表，让数字而不是外观决定组成。
- Negative: `no measuring new compounds with an unstable method, no publishing a composition from a single measurement, no identifying a compound by smell or colour`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
