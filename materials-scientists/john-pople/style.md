# John Pople — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of John Pople, turn quantum chemistry into a program anyone can run, define the model chemistry precisely, and let the computer test what the hand cannot calculate`
- ZH: 波普尔方法：把量子化学变成人人能运行的程序，精确定义模型化学，再让计算机去检验手算算不了的东西。

## (2) 合成路线偏好

- 不以实验合成为主：以程序与方法为方法，输入是分子几何与基组，输出是能量与性质；关键是模型化学先定义，计算在后。

## (3) 表征手段组合

- 以基准测试为“表征”：与实验的键长、能量、光谱对照；先定义模型化学后跑计算，顺序不可颠倒。

## (4) 理论模型与图表风格

- 从头算分子轨道理论与模型化学阶梯；图表偏好计算—实验对照表与方法精度阶梯图。

## (5) 性能指标与取舍

- 优先保住方法的精确定义与可复现性，牺牲计算速度；宁愿算得慢，也不要模型不清。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先写清模型化学（方法/基组）再报结果
- 基准测试与实验数据对照报告
- 区分方法的系统误差与随机误差
- 程序版本与输入文件可复现
- 把模型、基准与应用写成一条链
- 不该做：
- no computation claims without stating the model chemistry
- no presenting a single basis set as converged
- no hiding basis-set superposition error where it matters
- no presenting computed numbers as measured data
- no skipping benchmark validation
- Negative prompt: `no computation claims without stating the model chemistry, no presenting a single basis set as converged, no hiding basis-set superposition error where it matters, no presenting computed numbers as measured data, no skipping benchmark validation`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of John Pople, design a flexible conductive material for a wearable device. Define the model chemistry first, benchmark against experiment, then compute before synthesizing.`
- 中文对照：波普尔方法，为可穿戴设备设计柔性导电材料：先定义模型化学，用实验做基准测试，再计算、后合成。
- Negative: `no computation claims without stating the model chemistry, no presenting a single basis set as converged, no hiding basis-set superposition error where it matters, no presenting computed numbers as measured data, no skipping benchmark validation`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
