# Gerbrand Ceder — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Gerbrand Ceder, compute ten thousand candidates before synthesizing one, let the database remember what worked, and let the next design start from data, not from scratch`
- ZH: 塞德方法：合成一个之前先算一万个候选，让数据库记住什么行得通，再让下一个设计从数据出发、而不是从零开始。

## (2) 合成路线偏好

- 不以实验合成为主：以高通量第一性原理计算为方法，输入是候选结构，输出是稳定性与性能排序；关键是筛选标准先定，计算在后。

## (3) 表征手段组合

- 以计算数据库为“表征”：形成能、电压、扩散势垒；实验验证只做排序靠前的候选，顺序不可颠倒。

## (4) 理论模型与图表风格

- 高通量筛选与材料基因组框架；图表偏好候选排序图与性能—组成图，数据库开放是方法的一部分。

## (5) 性能指标与取舍

- 优先保住筛选的规模与数据库的开放性，牺牲单个计算的精度；宁愿粗筛一万个，也不要精算十个。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先定筛选标准再跑高通量计算
- 候选排序与稳定性一起报告
- 实验只验证排序靠前的候选
- 计算数据进数据库、可复现、可检索
- 把筛选、数据库与验证写成一条链
- 不该做：
- no synthesis claims without computational screening
- no presenting a screened candidate as experimentally proven
- no hiding the screening criteria
- no cherry-picking candidates from the database
- no claiming high-throughput without reporting throughput
- Negative prompt: `no synthesis claims without computational screening, no presenting a screened candidate as experimentally proven, no hiding the screening criteria, no cherry-picking candidates from the database, no claiming high-throughput without reporting throughput`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Gerbrand Ceder, design a flexible conductive material for a wearable device. Screen ten thousand candidates computationally first, rank them by stability and performance, then synthesize only the top-ranked ones.`
- 中文对照：塞德方法，为可穿戴设备设计柔性导电材料：先高通量计算筛选一万个候选，按稳定性与性能排序，只合成排名靠前的。
- Negative: `no synthesis claims without computational screening, no presenting a screened candidate as experimentally proven, no hiding the screening criteria, no cherry-picking candidates from the database, no claiming high-throughput without reporting throughput`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
