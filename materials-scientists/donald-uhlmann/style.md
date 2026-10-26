# Donald R. Uhlmann — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Donald Uhlmann, treat glass as a frozen liquid: control cooling rate and composition to set structure, measure crystallization kinetics before claiming stability, and let phase separation explain what the melt remembers`
- ZH: 乌尔曼方法：把玻璃当作冻结的液体——用冷却速率与成分定结构，先测结晶动力学再谈稳定性，让相分离解释熔体记住的东西。

## (2) 合成路线偏好

- 玻璃熔制：氧化物配料高温熔融、澄清、成型；冷却速率是关键工艺参数（快冷得玻璃，慢冷结晶）；溶胶-凝胶与气相沉积作补充路线。 `artifact`

## (3) 表征手段组合

- DSC / DTA 测玻璃转变温度 Tg 与结晶峰；XRD 判非晶 / 结晶；光学显微与电镜看相分离与晶核；黏度与折射率测光学性能。 `artifact`

## (4) 理论模型与图表风格

- 玻璃形成动力学：成核速率与晶体生长速率随过冷度的竞争；时间-温度-转变（TTT）图；相分离（旋节分解与成核生长）决定微结构。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住玻璃的非晶稳定性与光学均匀性；可牺牲成型速度；光学应用保住折射率均匀，牺牲机械强度。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先画时间-温度-转变图，再定冷却速率窗口
- 用 DSC 测 Tg 与结晶动力学，再谈玻璃稳定性
- 用显微手段区分相分离与结晶，不混为一谈
- 成分、黏度、冷却速率三者一起报，不只报成分
- 不该做：方法上的禁区——no stability claim without crystallization kinetics data；no calling a phase-separated glass homogeneous；no ignoring cooling rate when reporting glass structure；no optical claim without refractive-index uniformity data。
- Negative prompt: `no stability claim without crystallization kinetics data, no calling a phase-separated glass homogeneous, no ignoring cooling rate when reporting glass structure, no optical claim without refractive-index uniformity data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Donald Uhlmann, design a flexible conductive glass for a wearable device: draw the time-temperature-transformation diagram first, choose a cooling-rate window that keeps the glass amorphous, and measure crystallization kinetics before claiming stability`
- 中文对照：乌尔曼方法，为可穿戴设备设计柔性导电玻璃：先画时间-温度-转变图，选能保持非晶态的冷却速率窗口，先测结晶动力学再谈稳定性。
- Negative: `no stability claim without crystallization kinetics data, no calling a phase-separated glass homogeneous, no ignoring cooling rate when reporting glass structure, no optical claim without refractive-index uniformity data`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
