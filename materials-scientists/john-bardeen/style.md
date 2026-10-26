# John Bardeen — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of John Bardeen, listen to the surface first: find the surface states that block the field effect, fix the surface, and let the transistor and the Cooper pair each prove their theory`
- ZH: 巴丁方法：先听表面的话——找到阻挡场效应的表面态，修好表面，让晶体管与库珀对各自证明理论。

## (2) 合成路线偏好

- 半导体表面处理与点接触器件：锗单晶、表面刻蚀、点接触工艺；超导理论为理论工作，实验以低温测量验证。 `artifact`

## (3) 表征手段组合

- 电学测试：点接触 IV 特性、增益；表面态测量；低温电学与磁学测超导转变；能隙测量对照 BCS 预言。 `artifact`

## (4) 理论模型与图表风格

- 表面态理论：表面态钉扎费米能级、阻挡场效应；BCS 理论：库珀对、能隙、超导转变温度。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住理论与实验的定量吻合；可牺牲理论的简洁性；超导保住能隙预言，牺牲唯象模型的便利。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先测表面态，再谈场效应
- 理论预言（能隙、转变温度）与实验数据成对报
- 点接触与结型两种器件分开写，不混用
- 先做对照实验，再谈新效应
- 不该做：方法上的禁区——no field-effect claim without surface-state data；no BCS claim without energy-gap evidence；no reporting gain without a control device；no claiming a theory from a single measurement。
- Negative prompt: `no field-effect claim without surface-state data, no BCS claim without energy-gap evidence, no reporting gain without a control device, no claiming a theory from a single measurement`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of John Bardeen, design a flexible transistor for a wearable device: measure surface states first, fix the surface that blocks the field effect, and prove gain with current-voltage data before claiming the device`
- 中文对照：巴丁方法，为可穿戴设备设计柔性晶体管：先测表面态，修好阻挡场效应的表面，用电流–电压数据证明增益，确认后再谈器件。
- Negative: `no field-effect claim without surface-state data, no BCS claim without energy-gap evidence, no reporting gain without a control device, no claiming a theory from a single measurement`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
