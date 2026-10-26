# Buddy Ratner — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Buddy Ratner, measure the real surface a cell meets, find why it is recognized as foreign, and engineer the surface to speak the cell's own language`
- ZH: 拉特纳方法：先测清细胞真正遇到的表面，再弄清它为何被识别为异物，然后改造表面，让它说细胞自己的语言。

## (2) 合成路线偏好

- 水凝胶合成与表面改性：等离子体处理、接枝、涂层；关键是表面化学与形貌分开控制，一次只改一个变量。

## (3) 表征手段组合

- ESCA/XPS 与 ToF-SIMS 定表面化学，接触角与 AFM 看润湿与形貌，蛋白质吸附与细胞实验看生物响应；先表面后生物，顺序不可颠倒。

## (4) 理论模型与图表风格

- 表面—蛋白质—细胞相互作用模型；图表偏好表面成分谱图与蛋白质吸附曲线，细胞响应作最终验证。

## (5) 性能指标与取舍

- 优先保住表面化学的可控性与可重复性，牺牲改性速度；宁愿改性慢，也不要表面成分不清。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先用 ESCA/XPS 定表面化学再谈生物响应
- 一次只改一个表面变量
- 设无改性对照与已知惰性对照
- 用蛋白质吸附数据连接表面与细胞响应
- 把表面表征、蛋白质吸附与细胞实验写成一条链
- 不该做：
- no biocompatibility claims without surface characterization
- no attributing cell response to an unmeasured surface
- no single-variable claims from multi-variable surface changes
- no hiding protein adsorption data
- no presenting a surface treatment as cell-instructive without cell evidence
- Negative prompt: `no biocompatibility claims without surface characterization, no attributing cell response to an unmeasured surface, no single-variable claims from multi-variable surface changes, no hiding protein adsorption data, no presenting a surface treatment as cell-instructive without cell evidence`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Buddy Ratner, design a flexible conductive material for a wearable device. Characterize the real surface first, control one surface variable at a time, and prove the biological response follows the surface chemistry.`
- 中文对照：拉特纳方法，为可穿戴设备设计柔性导电材料：先表征真实表面，一次只改一个表面变量，证明生物响应跟随表面化学。
- Negative: `no biocompatibility claims without surface characterization, no attributing cell response to an unmeasured surface, no single-variable claims from multi-variable surface changes, no hiding protein adsorption data, no presenting a surface treatment as cell-instructive without cell evidence`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
