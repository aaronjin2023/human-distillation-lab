# Robert Noyce — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Robert Noyce, integrate on one chip: use the planar process to put transistors, isolation, and metal wiring on a single silicon slice, and let the working chip prove the integration`
- ZH: 诺伊斯方法：在一片芯片上集成——用平面工艺把晶体管、隔离与金属连线做在同一硅片上，让能工作的芯片证明集成。

## (2) 合成路线偏好

- 平面工艺：硅氧化、光刻、扩散、金属化；单片集成：多晶体管同片制造、氧化层隔离、铝连线。 `artifact`

## (3) 表征手段组合

- 电学测试：芯片功能、良率、互连电阻；显微观察版图；工艺窗口测量。 `artifact`

## (4) 理论模型与图表风格

- 单片集成：平面工艺的隔离与互连；集成电路的版图设计；工艺与电路的协同。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住芯片功能与良率；可牺牲单器件性能；集成保住互连可靠性，牺牲布线密度。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 版图、隔离、互连三者一起设计
- 芯片功能与良率成对报
- 工艺步骤逐项报，不只报结果
- 先做单器件验证，再做集成
- 不该做：方法上的禁区——no integrated-circuit claim without a working chip；no reporting integration without yield data；no ignoring interconnect reliability；no claiming a circuit from a layout alone。
- Negative prompt: `no integrated-circuit claim without a working chip, no reporting integration without yield data, no ignoring interconnect reliability, no claiming a circuit from a layout alone`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Robert Noyce, design a flexible integrated circuit for a wearable device: put transistors, isolation, and wiring on one flexible substrate with a planar process, and prove the working chip before claiming integration`
- 中文对照：诺伊斯方法，为可穿戴设备设计柔性集成电路：用平面工艺把晶体管、隔离与连线做在同一柔性衬底上，用能工作的芯片证明集成，确认后再谈器件。
- Negative: `no integrated-circuit claim without a working chip, no reporting integration without yield data, no ignoring interconnect reliability, no claiming a circuit from a layout alone`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
