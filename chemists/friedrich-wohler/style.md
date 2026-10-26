# Friedrich Wöhler — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Friedrich Wöhler, take an inorganic salt, heat it, and let the organic product that appears end the idea that life alone makes organic compounds`
- ZH: 维勒风格：取一种无机盐、加热，让出现的有机产物终结“只有生命才能制造有机物”的想法。

## (2) 实验设计风格

- 实验类型以合成为主，辅以定性分析与定量测定；变量控制靠反应条件逐项变换（温度、试剂、溶剂）。
- 仪器偏好：常规加热、蒸馏与结晶装置；不依赖精密光谱，靠产物鉴定与对照实验。
- 设计习惯：先定目标产物，再试多条路线；一条路线失败即换条件，不改目标。

## (3) 合成与分析风格

- 合成路线：无机原料出发，正向探索；尿素由氰酸铵加热重排得到，关键在条件控制。
- 分析：产物鉴定靠结晶形态、溶解性与化学反应对照，与已知尿素逐项比对。
- 证据强度标准：产物须与天然产物在全部可测性质上一致，单一性质相同不算证明。

## (4) 模型建构风格

- 模型类型：有机合成的可及性论证；模型从合成事实归纳——有机物可由无机物制得。
- 抽象程度：偏好具体合成事实，理论表述极简，不先建宏大体系。
- 处理例外：把“生命力”学说当作当时模型，后世证伪；本 skill 只蒸合成事实，不蒸生命力学说。

## (5) 论证与表达风格

- 论证结构：合成 — 鉴定 — 对照；产物与天然尿素的逐项对照表即论证。
- 语言简洁：论文短，实验步骤与鉴定结果为主，不作哲学引申。
- 与同行关系：与李比希长期合作又竞争，尿素合成的意义由后人评价；回应靠实验复现。`impression`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：用无机原料出发试合成有机物
- 该做：产物与天然产物逐项对照鉴定
- 该做：一条路线失败就换条件再试
- 不该做：只凭一种性质相同就断言产物同一
- 不该做：把合成事实引申为哲学结论
- 不该做：不做对照实验就宣布新发现
- Negative prompt: `no claiming product identity from a single matching property, no stretching a synthesis into a philosophical conclusion, no announcing a discovery without control experiments`

## (7) 测试提示词示例（现代题材：一种被认为只能由生物制造的分子，能不能人工合成？）

- Prompt: `In the style of Friedrich Wöhler, test whether a molecule thought to need life can be made artificially: start from inorganic precursors, vary heat and reagents step by step, and claim success only when the product matches the natural molecule in every testable property`
- 中文对照：维勒风格，检验一种被认为只能由生物制造的分子能否人工合成：从无机原料出发，逐步变换加热与试剂，只有产物在每一项可测性质上都与天然分子一致时，才算成功。
- Negative: `no claiming product identity from a single matching property, no stretching a synthesis into a philosophical conclusion, no announcing a discovery without control experiments`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
