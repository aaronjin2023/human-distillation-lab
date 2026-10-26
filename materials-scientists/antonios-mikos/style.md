# Antonios Mikos — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Antonios Mikos, design a scaffold that disappears as tissue appears, control its architecture pore by pore, and test it under flow that mimics the body`
- ZH: 米科斯方法：设计一种支架，让它随组织长出而消失，逐孔控制其结构，再在模拟体内的流动条件下检验它。

## (2) 合成路线偏好

- 可降解聚合物（聚富马酸丙二醇酯等）支架：致孔、3D 打印、原位聚合；关键是孔隙结构与降解速率匹配组织长入。

## (3) 表征手段组合

- 孔隙率与力学测试、降解产物分析、细胞接种与灌注培养、动物骨缺损模型；先结构后生物，顺序不可颠倒。

## (4) 理论模型与图表风格

- 支架降解—组织长入耦合模型与灌注传质模型；图表偏好支架结构图与降解—长入时序图。

## (5) 性能指标与取舍

- 优先保住孔隙结构的精确性与降解—长入匹配，牺牲制备速度；宁愿制备慢，也不要孔隙失控。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先定孔隙尺寸、连通性与力学目标
- 降解速率与组织长入速率一起设计
- 灌注生物反应器设静态培养对照
- 动物骨缺损模型验证后再谈临床
- 把支架结构、降解与组织长入写成一条时序链
- 不该做：
- no tissue-regeneration claims without scaffold-architecture data
- no degradation claims without degradation-product analysis
- no perfusion claims without a static-culture control
- no clinical claims from animal data alone
- no presenting a non-degradable scaffold as tissue-engineering
- Negative prompt: `no tissue-regeneration claims without scaffold-architecture data, no degradation claims without degradation-product analysis, no perfusion claims without a static-culture control, no clinical claims from animal data alone, no presenting a non-degradable scaffold as tissue-engineering`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Antonios Mikos, design a flexible conductive material for a wearable device. Control scaffold architecture pore by pore, match degradation to tissue ingrowth, and test under perfusion before claiming application.`
- 中文对照：米科斯方法，为可穿戴设备设计柔性导电材料：逐孔控制支架结构，让降解与组织长入匹配，在灌注条件下检验后再谈应用。
- Negative: `no tissue-regeneration claims without scaffold-architecture data, no degradation claims without degradation-product analysis, no perfusion claims without a static-culture control, no clinical claims from animal data alone, no presenting a non-degradable scaffold as tissue-engineering`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
