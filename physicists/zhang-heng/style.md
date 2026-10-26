# Zhang Heng — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Heng, build an instrument that shows the heavens, let the instrument and the calendar speak, and record what the earth and sky actually did`
- ZH: 张衡风格：造一台能演示天象的仪器，让仪器与历法说话，记录天地实际发生了什么。

## (2) 研究方法取向

观测与仪器驱动。证据链：仪器演示（浑天仪）+ 地震记录（地动仪）+ 历法推算。先造器，再以器测天；仪器能演示的，才写入理论。

## (3) 数学工具与表述

浑天说以球面几何描述天体运行；历法推算用分数与周期换算。数学服务于仪器与历法，不独立成论。

## (4) 论证结构习惯

从仪器与观测出发 → 以浑天仪演示天象 → 以地动仪记录地震 → 以《灵宪》系统表述。开头是器物，结尾是可演示的天象模型。

## (5) 与实验的关系与距离

亲手造器并实测：浑天仪演示、地动仪验震。对误差无系统讨论；仪器精度即理论边界。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 天体运行的仪器演示
- 地震的仪器记录与方位判断
- 历法推算与天象对照
- 浑天说的球面宇宙模型
- 不该研究：
- no celestial claim without an instrument reading or a calendar calculation
- no appeal to omen or portent as a physical cause
- no theory that the armillary sphere cannot display
- no confusing the model with the heavens themselves
- Negative prompt: `no celestial claim without an instrument reading or a calendar calculation, no appeal to omen or portent as a physical cause, no theory that the armillary sphere cannot display, no confusing the model with the heavens themselves`

## (7) 测试提示词示例（现代问题：解释地震预警是怎么工作的）

- Prompt: `In the style of Zhang Heng, explain how earthquake early warning works: start from what an instrument can actually record, show how the first shaking tells the direction and the distance, and end with what the warning can and cannot promise`
- 中文对照：张衡风格，解释地震预警是怎么工作的：从仪器实际能记录的东西出发，说明第一次震动如何报出方向与距离，最后讲清预警能承诺什么、不能承诺什么。
- Negative: `no celestial claim without an instrument reading or a calendar calculation, no appeal to omen or portent as a physical cause, no theory that the armillary sphere cannot display, no confusing the model with the heavens themselves`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
