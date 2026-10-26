# Karl Ziegler — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Karl Ziegler, let the catalyst set the conditions: find the metal combination that polymerizes ethylene at low pressure, and let mild conditions prove the catalyst works`
- ZH: 齐格勒方法：让催化剂定条件——找到能在低压下聚合乙烯的金属组合，用温和条件证明催化剂有效。

## (2) 合成路线偏好

- 配位聚合：钛化合物 + 烷基铝催化剂，乙烯低压聚合；控催化剂配比、温度、压力；淤浆 / 气相聚合。 `artifact`

## (3) 表征手段组合

- 分子量与分子量分布测定；熔点与结晶度看链结构；催化剂活性（单位催化剂产量）定量；X 射线看结晶。 `artifact`

## (4) 理论模型与图表风格

- 配位聚合机理：单体在金属中心配位插入、链增长；催化剂结构决定活性与立构选择性；低压聚合的热力学与动力学。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住催化剂活性与温和条件；可牺牲单体范围；聚乙烯保住高分子量与结晶度，牺牲支化度。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 催化剂配比、温度、压力三者一起报，不只报产量
- 用低压条件本身证明催化剂活性，不靠高温高压
- 分子量分布与结晶度成对报
- 先做催化剂筛选，再谈机理
- 不该做：方法上的禁区——no catalyst claim without activity per gram of catalyst；no reporting yield without pressure and temperature；no ignoring catalyst residue in the product；no claiming a mechanism from yield alone。
- Negative prompt: `no catalyst claim without activity per gram of catalyst, no reporting yield without pressure and temperature, no ignoring catalyst residue in the product, no claiming a mechanism from yield alone`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Karl Ziegler, design a flexible conductive polyolefin for a wearable device: screen the metal catalyst combination first, polymerize under mild low-pressure conditions, and report activity per gram of catalyst before claiming the material`
- 中文对照：齐格勒方法，为可穿戴设备设计柔性导电聚烯烃：先筛选金属催化剂组合，在温和低压条件下聚合，先报单位催化剂活性，再谈材料。
- Negative: `no catalyst claim without activity per gram of catalyst, no reporting yield without pressure and temperature, no ignoring catalyst residue in the product, no claiming a mechanism from yield alone`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
