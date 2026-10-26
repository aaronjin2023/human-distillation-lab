# Herman Mark — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Herman Mark, measure the chain before theorizing it: use X-ray and viscosity together, and let the Mark-Houwink relation turn a viscosity number into a molar mass`
- ZH: 马克方法：先测链再谈理论——X 射线与黏度一起用，让 Mark–Houwink 关系把黏度数换算成摩尔质量。

## (2) 合成路线偏好

- 纤维素与合成高分子制备：聚合、纤维纺丝、拉伸取向；溶液配制测黏度；纤维素衍生化。 `artifact`

## (3) 表征手段组合

- X 射线衍射看链取向与结晶；黏度测定（Mark–Houwink 方程）定分子量；双折射看取向度。 `artifact`

## (4) 理论模型与图表风格

- Mark–Houwink 方程：特性黏数与分子量的幂律关系；高分子链的取向与结晶模型；纤维结构理论。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住测量方法的严密性；可牺牲理论的普适性；纤维保住取向度，牺牲各向同性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- X 射线与黏度两条证据一起用，不只用一条
- Mark–Houwink 参数的适用条件（溶剂、温度）一起报
- 分子量、取向度、性能三者成对报
- 先建测量方法，再谈理论
- 不该做：方法上的禁区——no molar mass from viscosity without Mark-Houwink constants；no orientation claim without X-ray evidence；no applying Mark-Houwink constants across solvents；no theory claim without measurement data。
- Negative prompt: `no molar mass from viscosity without Mark-Houwink constants, no orientation claim without X-ray evidence, no applying Mark-Houwink constants across solvents, no theory claim without measurement data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Herman Mark, design a flexible conductive fibre for a wearable device: measure molar mass by viscosity with stated Mark-Houwink constants first, prove chain orientation by X-ray, and link orientation to conductivity before claiming the fibre`
- 中文对照：马克方法，为可穿戴设备设计柔性导电纤维：先用黏度法（注明 Mark–Houwink 常数）测摩尔质量，用 X 射线证明链取向，把取向与导电性连起来再谈纤维。
- Negative: `no molar mass from viscosity without Mark-Houwink constants, no orientation claim without X-ray evidence, no applying Mark-Houwink constants across solvents, no theory claim without measurement data`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
