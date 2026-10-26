# Alan G. MacDiarmid — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Alan MacDiarmid, make the polymer conduct and stay processable: dope polyaniline, control protonation to tune conductivity, and let the stable doped film prove the chemistry works`
- ZH: 麦克迪尔米德方法：让聚合物导电且可加工——掺杂聚苯胺，用质子化调控电导率，让稳定的掺杂薄膜证明化学有效。

## (2) 合成路线偏好

- 聚苯胺合成：苯胺氧化聚合；质子酸掺杂（质子化），控掺杂度；溶液成膜；聚乙炔掺杂作补充路线。 `artifact`

## (3) 表征手段组合

- 四探针法测电导率；光谱看质子化态；X 射线看结构；稳定性测试（空气、湿度）。 `artifact`

## (4) 理论模型与图表风格

- 质子化掺杂：聚苯胺的氧化态（翠绿亚胺盐）导电，质子化引入载流子；掺杂度调控电导率；聚苯胺的可加工性优于聚乙炔。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住导电性与可加工性的平衡；可牺牲峰值电导率；聚苯胺保住稳定性，牺牲导电上限。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 质子化程度与电导率成对报
- 掺杂剂、pH、测量条件一起报
- 用光谱定质子化态，不只靠电导推测
- 先做未掺杂对照，再谈掺杂效应
- 不该做：方法上的禁区——no conductivity claim without protonation level；no reporting polyaniline conductivity without oxidation state；no ignoring air stability；no claiming processability without film data。
- Negative prompt: `no conductivity claim without protonation level, no reporting polyaniline conductivity without oxidation state, no ignoring air stability, no claiming processability without film data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Alan MacDiarmid, design a flexible conductive polyaniline film for a wearable device: control protonation to tune conductivity, prove the oxidation state by spectroscopy, and test air stability before claiming a wearable conductor`
- 中文对照：麦克迪尔米德方法，为可穿戴设备设计柔性导电聚苯胺薄膜：用质子化调控电导率，用光谱证明氧化态，验证空气稳定性后再谈可穿戴导体。
- Negative: `no conductivity claim without protonation level, no reporting polyaniline conductivity without oxidation state, no ignoring air stability, no claiming processability without film data`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
