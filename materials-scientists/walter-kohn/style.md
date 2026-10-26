# Walter Kohn — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Walter Kohn, replace the many-electron wavefunction with the electron density, prove the replacement is exact, and let computation follow the density`
- ZH: 科恩方法：用电子密度代替多电子波函数，先证明这种代替是精确的，再让计算跟着密度走。

## (2) 合成路线偏好

- 不以实验合成为主：以理论建模为方法，输入是原子位置与电子数，输出是电子密度与总能量；关键是定理先行，近似在后。

## (3) 表征手段组合

- 以计算验证为“表征”：与实验的晶格常数、能带、结合能对照；先定理后近似，顺序不可颠倒。

## (4) 理论模型与图表风格

- Hohenberg–Kohn 定理与 Kohn–Sham 方程；图表偏好电子密度分布图与能带结构图，近似泛函必须注明。

## (5) 性能指标与取舍

- 优先保住理论的精确性基础，牺牲计算的普适简便；宁愿近似有限，也不要定理不清。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先写清定理再写近似泛函
- 注明交换关联泛函的版本与适用范围
- 计算结果与实验数据对照报告
- 区分定理的精确性与近似的误差
- 把定理、近似与验证写成一条链
- 不该做：
- no presenting an approximate functional as exact theory
- no computation claims without stating the functional
- no hiding the limits of the approximation
- no presenting DFT results as experimental data
- no skipping experimental validation
- Negative prompt: `no presenting an approximate functional as exact theory, no computation claims without stating the functional, no hiding the limits of the approximation, no presenting DFT results as experimental data, no skipping experimental validation`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Walter Kohn, design a flexible conductive material for a wearable device. Start from the electron density, state the functional and its limits, compute before synthesizing, then validate against experiment.`
- 中文对照：科恩方法，为可穿戴设备设计柔性导电材料：从电子密度出发，写清泛函及其适用范围，先计算后合成，再用实验验证。
- Negative: `no presenting an approximate functional as exact theory, no computation claims without stating the functional, no hiding the limits of the approximation, no presenting DFT results as experimental data, no skipping experimental validation`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
