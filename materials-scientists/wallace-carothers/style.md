# Wallace Carothers — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Wallace Carothers, build the polymer by design: control condensation step by step, draw the fibre to align the chains, and let the drawn fibre prove the structure`
- ZH: 卡罗瑟斯方法：按设计合成聚合物——逐步控制缩聚，拉伸纤维使链取向，让拉伸后的纤维证明结构。

## (2) 合成路线偏好

- 缩聚反应：二元酸与二元胺逐步缩合，控温、控真空除水；氯丁橡胶由氯丁二烯聚合；熔融纺丝拉伸取向。 `artifact`

## (3) 表征手段组合

- 黏度与分子量测定；X 射线看纤维取向与结晶；力学测试看拉伸强度；熔点与溶解性定结构。 `artifact`

## (4) 理论模型与图表风格

- 缩聚理论：逐步聚合的分子量分布与官能团平衡；线型聚合物可拉伸取向，取向带来强度；结构–性能关系。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住纤维强度与取向度；可牺牲通用性；尼龙保住耐磨与强度，牺牲吸湿性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 逐步控制缩聚的每一步转化率与副产物排除
- 用拉伸取向实验证明链结构，不只靠化学式
- 分子量、取向度、强度三者成对报
- 先做小试验证机理，再放大
- 不该做：方法上的禁区——no fibre-strength claim without orientation data；no ignoring water removal in condensation；no reporting molar mass without a method；no claiming a polymer from a single reaction。
- Negative prompt: `no fibre-strength claim without orientation data, no ignoring water removal in condensation, no reporting molar mass without a method, no claiming a polymer from a single reaction`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Wallace Carothers, design a flexible conductive fibre for a wearable device: build the polymer by stepwise condensation, draw the fibre to align the chains, and prove orientation by X-ray before claiming strength and conductivity`
- 中文对照：卡罗瑟斯方法，为可穿戴设备设计柔性导电纤维：逐步缩聚合成聚合物，拉伸使链取向，用 X 射线证明取向，确认强度与导电性后再谈材料。
- Negative: `no fibre-strength claim without orientation data, no ignoring water removal in condensation, no reporting molar mass without a method, no claiming a polymer from a single reaction`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
