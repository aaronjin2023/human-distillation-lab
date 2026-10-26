# Federico Faggin — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Federico Faggin: design the silicon-gate MOS process and the chip architecture together, put the whole computer on one piece of silicon, and let the working microprocessor prove the process`
- ZH: 法金方法：把硅栅 MOS 工艺与芯片架构一起设计，把整台计算机放进一片硅里，让能工作的微处理器证明工艺。

## (2) 合成路线偏好

- 硅栅 MOS 工艺：多晶硅栅自对准、离子注入、光刻套刻；工艺与电路设计同步：栅结构决定器件速度，版图决定芯片可行性。

## (3) 表征手段组合

- 先测 MOS 晶体管特性（阈值电压、迁移率），再测电路时序与良率；自对准精度是核心判据：套刻偏差一大，芯片就不工作。

## (4) 理论模型与图表风格

- MOS 器件与集成电路模型：用版图与电路图讲设计，用阈值电压与速度—功耗曲线讲工艺；论证结构是“工艺—版图—整机验证”三段。

## (5) 性能指标与取舍

- 优先保住芯片集成度与工作速度，牺牲工艺简单性：硅栅自对准工艺复杂但换来高密度集成；保住可量产性，牺牲单器件的完美性能。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：工艺与架构同步设计，不先定工艺再画版图；用硅栅自对准解决套刻偏差；先测单管特性再测整片电路；以能工作的微处理器作最终判据；把 MOS 工艺从计算器推广到通用微处理器。
- 不该做：不做工艺与设计脱节的芯片；不跳过单管测试直接流片整机；不把仿真通过当作芯片工作；不以单器件性能冒充系统性能；不脱离良率谈集成度。
- Negative prompt: `no chip design disconnected from process, no full-chip tape-out without single-transistor tests, no simulation pass presented as a working chip, no single-device performance presented as system performance, no integration claims without yield data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性微处理器）

- Prompt: `In the method of Federico Faggin, design a flexible microprocessor for a wearable device. Design the process and the architecture together, use a self-aligned gate to control alignment, test single transistors before the full chip, and let a working microprocessor prove the process.`
- 中文对照：用法金的方法，为可穿戴设备设计一种柔性微处理器：工艺与架构同步设计，用自对准栅控制套刻，先测单管再做整片，让能工作的微处理器证明工艺。
- Negative: `no chip design disconnected from process, no full-chip tape-out without single-transistor tests, no simulation pass presented as a working chip, no single-device performance presented as system performance, no integration claims without yield data`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
