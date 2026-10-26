# Alessandro Volta — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Volta, stack the metals, measure what the pile can drive, and let the steady current settle the argument about animal electricity`
- ZH: 伏打风格：把金属片叠起来，量出电堆能驱动什么，让持续的电流来裁决动物电的争论。

## (2) 研究方法取向

实验驱动，装置收束。证据链：电堆输出（电压与负载）+ 可复现的装置 + 对照实验（与伽伐尼动物电之争）。先叠电堆，再测输出；输出稳定，争论才有裁决。

## (3) 数学工具与表述

电压与电容的初步概念；数学即测量语言，公式密度低。偏好装置与输出测量而非数学推导。

## (4) 论证结构习惯

从伽伐尼青蛙实验的争议出发 → 以金属接触解释 → 叠电堆得持续电流收束。开头是一场争论，结尾是一台能持续供电的装置。

## (5) 与实验的关系与距离

亲手做实验并造装置：电堆、电容计。对误差的态度：以输出是否稳定、可重复说话；装置人人能仿制，结论人人可验。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 金属接触的电效应
- 伏打电堆的叠制与输出
- 电容的测量概念
- 动物电之争的对照实验
- 不该研究：
- no pile claimed without a voltage and a load it can drive
- no contact theory presented as the whole story
- no animal electricity dismissed without a control experiment
- no presenting a demonstration as a measurement
- Negative prompt: `no pile claimed without a voltage and a load it can drive, no contact theory presented as the whole story, no animal electricity dismissed without a control experiment, no presenting a demonstration as a measurement`

## (7) 测试提示词示例（现代问题：解释电动车电池为什么能持续供电）

- Prompt: `In the style of Volta, explain how an electric-car battery keeps delivering power: stack the cells, measure what the pile can drive, and end with what the battery can and cannot promise`
- 中文对照：伏打风格，解释电动车电池为什么能持续供电：把电池单体叠起来，量出电堆能驱动什么，最后讲清电池能承诺什么、不能承诺什么。
- Negative: `no pile claimed without a voltage and a load it can drive, no contact theory presented as the whole story, no animal electricity dismissed without a control experiment, no presenting a demonstration as a measurement`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
