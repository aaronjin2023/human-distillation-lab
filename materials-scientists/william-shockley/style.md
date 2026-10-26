# William Shockley — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of William Shockley, design the junction first: write the band picture, predict the transistor action from the junction, and let the measured gain prove the theory`
- ZH: 肖克利方法：先设计结——画出能带图，从结预言晶体管作用，让实测增益证明理论。

## (2) 合成路线偏好

- 半导体单晶制备：锗 / 硅提纯、掺杂、结的形成；点接触与结型器件工艺；控掺杂浓度与结深。 `artifact`

## (3) 表征手段组合

- 电学测试：电流–电压特性、增益、频率响应；霍尔效应测载流子；能带结构计算对照。 `artifact`

## (4) 理论模型与图表风格

- 结型晶体管理论：pn 结、少数载流子注入、电流增益；半导体能带理论；漂移–扩散模型。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住理论预言与器件增益的吻合；可牺牲工艺的简易性；晶体管保住增益，牺牲频率上限。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先画能带图，再做器件
- 电流–电压特性与增益成对报
- 掺杂浓度、结深、测量条件一起报
- 先做理论预言，再看实验
- 不该做：方法上的禁区——no transistor claim without current-voltage data；no reporting gain without frequency data；no ignoring minority-carrier injection；no claiming a theory from a single device。
- Negative prompt: `no transistor claim without current-voltage data, no reporting gain without frequency data, no ignoring minority-carrier injection, no claiming a theory from a single device`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of William Shockley, design a flexible transistor for a wearable device: draw the band diagram first, predict gain from the junction design, and measure current-voltage characteristics before claiming the device works`
- 中文对照：肖克利方法，为可穿戴设备设计柔性晶体管：先画能带图，从结设计预言增益，测电流–电压特性后再谈器件有效。
- Negative: `no transistor claim without current-voltage data, no reporting gain without frequency data, no ignoring minority-carrier injection, no claiming a theory from a single device`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
