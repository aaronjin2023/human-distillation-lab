# Alan J. Heeger — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Alan Heeger, dope the polymer to make it conduct: oxidize or reduce the conjugated chain, measure conductivity across doping levels, and let the metal-like conductivity prove the doping works`
- ZH: 黑格方法：掺杂让聚合物导电——氧化或还原共轭链，逐级测掺杂量与电导率，让金属般的导电性证明掺杂有效。

## (2) 合成路线偏好

- 聚乙炔薄膜制备（白川法）+ 掺杂：碘蒸气 / AsF5 等掺杂剂，控掺杂量；薄膜成型与电极制备。 `artifact`

## (3) 表征手段组合

- 四探针法测电导率随掺杂量变化；光谱（吸收、拉曼）看掺杂态；X 射线看链取向；ESR 看自旋。 `artifact`

## (4) 理论模型与图表风格

- 掺杂导电：共轭链的 π 电子离域，掺杂引入孤子 / 极化子载流子；电导率随掺杂量跃升多个数量级；金属–绝缘体转变。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住电导率与掺杂可控性；可牺牲环境稳定性；导电聚合物保住导电性，牺牲加工性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 电导率随掺杂量逐级测，不只报最高值
- 掺杂剂、掺杂量、测量条件一起报
- 用光谱与电导两条证据定掺杂态
- 先做未掺杂对照，再谈掺杂效应
- 不该做：方法上的禁区——no conductivity claim without doping level；no reporting peak conductivity without stability data；no ignoring the undoped control；no claiming metallic conduction from a single temperature。
- Negative prompt: `no conductivity claim without doping level, no reporting peak conductivity without stability data, no ignoring the undoped control, no claiming metallic conduction from a single temperature`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Alan Heeger, design a flexible conductive polymer for a wearable device: dope the conjugated chain stepwise, measure conductivity across doping levels with four-probe method, and prove stability before claiming a wearable conductor`
- 中文对照：黑格方法，为可穿戴设备设计柔性导电聚合物：逐级掺杂共轭链，用四探针法测电导率随掺杂量的变化，验证稳定性后再谈可穿戴导体。
- Negative: `no conductivity claim without doping level, no reporting peak conductivity without stability data, no ignoring the undoped control, no claiming metallic conduction from a single temperature`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
