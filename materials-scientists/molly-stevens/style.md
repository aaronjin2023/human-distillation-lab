# Molly Stevens — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Molly Stevens, design the interface where material meets biology, read the cell's response at the nanoscale, and turn the same interface into sensing and regeneration`
- ZH: 史蒂文斯方法：设计材料与生物相遇的界面，在纳米尺度上读出细胞的响应，再把同一界面转用于传感与再生。

## (2) 合成路线偏好

- 生物活性支架与纳米粒：肽功能化、纳米针、纳米簇；关键是界面化学定细胞响应，界面设计先于器件设计。

## (3) 表征手段组合

- 单分子力学与光谱看界面相互作用，细胞培养看分化，动物模型看再生，传感测试看检测限；先界面后功能，顺序不可颠倒。

## (4) 理论模型与图表风格

- 生物—材料界面模型；图表偏好界面示意图与细胞响应曲线，传感数据作定量验证。

## (5) 性能指标与取舍

- 优先保住界面设计的可控性与细胞响应的可重复性，牺牲器件通用性；宁愿只做一类界面，也不要界面不清。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先设计界面化学再谈细胞响应
- 单分子与光谱手段验证界面相互作用
- 细胞实验设无功能化对照
- 传感实验报告检测限与特异性
- 把界面、细胞响应与再生/传感写成一条链
- 不该做：
- no cell-response claims without interface characterization
- no sensing claims without limit-of-detection data
- no regeneration claims from cell culture alone
- no hiding non-specific binding
- no presenting a bulk material effect as an interface effect
- Negative prompt: `no cell-response claims without interface characterization, no sensing claims without limit-of-detection data, no regeneration claims from cell culture alone, no hiding non-specific binding, no presenting a bulk material effect as an interface effect`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Molly Stevens, design a flexible conductive material for a wearable device. Design the bio-material interface first, read cell response at the nanoscale, then prove sensing or regeneration function.`
- 中文对照：史蒂文斯方法，为可穿戴设备设计柔性导电材料：先设计生物—材料界面，在纳米尺度上读出细胞响应，再证明传感或再生功能。
- Negative: `no cell-response claims without interface characterization, no sensing claims without limit-of-detection data, no regeneration claims from cell culture alone, no hiding non-specific binding, no presenting a bulk material effect as an interface effect`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
