# Walter Brattain — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Walter Brattain, work the surface with your hands: etch, contact, and measure the germanium surface until the point contact amplifies, and let the gain prove the surface is right`
- ZH: 布拉顿方法：用手做出表面——刻蚀、接触、测量锗表面，直到点接触放大，让增益证明表面是对的。

## (2) 合成路线偏好

- 锗单晶表面处理：刻蚀、清洗、点接触制备；控表面氧化与污染；金触点工艺。 `artifact`

## (3) 表征手段组合

- 电学测试：点接触 IV 特性、增益、频率响应；表面电势与光电测量；显微观察表面。 `artifact`

## (4) 理论模型与图表风格

- 表面态与点接触注入：表面态影响场效应，点接触注入少数载流子实现放大；实验先于理论，测量驱动理解。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住实验的可重复性与增益的实测；可牺牲理论的完备性；点接触保住增益，牺牲稳定性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 表面处理步骤逐项报，不只报结果
- 点接触的几何与压力条件一起报
- 增益、频率、稳定性三者成对报
- 先做对照器件，再谈新效应
- 不该做：方法上的禁区——no gain claim without point-contact geometry；no reporting a transistor without surface treatment steps；no ignoring surface contamination；no claiming stability from a short test。
- Negative prompt: `no gain claim without point-contact geometry, no reporting a transistor without surface treatment steps, no ignoring surface contamination, no claiming stability from a short test`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Walter Brattain, design a flexible point-contact device for a wearable device: etch and prepare the semiconductor surface first, set the point contact carefully, and measure gain before claiming the device works`
- 中文对照：布拉顿方法，为可穿戴设备设计柔性点接触器件：先刻蚀制备半导体表面，仔细设定点接触，测增益后再谈器件有效。
- Negative: `no gain claim without point-contact geometry, no reporting a transistor without surface treatment steps, no ignoring surface contamination, no claiming stability from a short test`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
