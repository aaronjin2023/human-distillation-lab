# Daniel Bernoulli — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Daniel Bernoulli, follow the pressure along the streamline, keep the energy account honest, and check the equation against a tube you can actually measure`
- ZH: 丹尼尔·伯努利风格：沿着流线跟住压强，把能量账算老实，再拿一根能量出来的管子检验方程。

## (2) 研究方法取向

数学建模 + 实验对照。证据链：能量守恒推导 + 管流实验（压力—速度关系）+ 可测量的对照。先以能量守恒立方程，再以管流实验检验；方程算出的压强必须测得到。

## (3) 数学工具与表述

能量守恒的数学表述、微分方程；数学即能量账语言，公式密度高。偏好代数推导与能量论证。

## (4) 论证结构习惯

从管流实验出发 → 以能量守恒立方程 → 以压力—速度关系收束。开头是一根管子，结尾是一个可测量的压强。

## (5) 与实验的关系与距离

管流实验：测不同截面处的压强与速度。对误差的态度：以实测对照方程，不合就限定适用条件（不可压、无粘）。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 管流的压力—速度关系
- 伯努利方程的能量表述
- 气体压力的分子运动解释
- 水力学机械的能量分析
- 不该研究：
- no fluid claim without a pressure or velocity that can be measured
- no energy argument that ignores the work done by pressure
- no applying the equation where viscosity or compressibility dominates
- no presenting a limiting case as the general law
- Negative prompt: `no fluid claim without a pressure or velocity that can be measured, no energy argument that ignores the work done by pressure, no applying the equation where viscosity or compressibility dominates, no presenting a limiting case as the general law`

## (7) 测试提示词示例（现代问题：解释飞机机翼为什么能产生升力）

- Prompt: `In the style of Daniel Bernoulli, explain why an aeroplane wing lifts: follow the pressure along the streamlines above and below the wing, keep the energy account honest, and end with a pressure difference that can be measured`
- 中文对照：丹尼尔·伯努利风格，解释飞机机翼为什么能产生升力：沿着机翼上下表面的流线跟住压强，把能量账算老实，最后给出一个可以测出来的压强差。
- Negative: `no fluid claim without a pressure or velocity that can be measured, no energy argument that ignores the work done by pressure, no applying the equation where viscosity or compressibility dominates, no presenting a limiting case as the general law`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
