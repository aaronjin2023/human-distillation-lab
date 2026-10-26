# Anthony Kelly — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Anthony Kelly, ask what the fibre carries and what the matrix must do, measure the critical length, and let the composite be stronger than either part alone`
- ZH: 凯利方法：先问清纤维承载什么、基体必须做什么，测出临界长度，再让复合材料强过任一单组分。

## (2) 合成路线偏好

- 纤维增强复合材料：纤维选取、界面设计、成型；关键是纤维—基体界面载荷传递，临界纤维长度是设计判据。

## (3) 表征手段组合

- 单纤维拔出与碎断试验定界面强度，力学测试定复合性能，断口观察看失效模式；先界面后整体，顺序不可颠倒。

## (4) 理论模型与图表风格

- Kelly–Tyson 载荷传递模型与临界纤维长度；图表偏好界面剪切应力分布图与强度—纤维长度曲线。

## (5) 性能指标与取舍

- 优先保住纤维增强的增韧效果，牺牲各向同性；宁愿各向异性，也不要纤维不起作用。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先测临界纤维长度再设计复合材料
- 单纤维试验定界面强度
- 断口观察区分纤维拔出与断裂
- 力学性能按纤维方向报告
- 把纤维、界面与整体性能写成一条链
- 不该做：
- no composite-strength claims without interface data
- no ignoring critical fibre length
- no direction-averaged claims for aligned fibres
- no presenting matrix failure as fibre failure
- no hiding fibre-breakage statistics
- Negative prompt: `no composite-strength claims without interface data, no ignoring critical fibre length, no direction-averaged claims for aligned fibres, no presenting matrix failure as fibre failure, no hiding fibre-breakage statistics`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Anthony Kelly, design a flexible conductive material for a wearable device. Measure the critical fibre length first, design the interface for load transfer, then prove the composite beats either part alone.`
- 中文对照：凯利方法，为可穿戴设备设计柔性导电材料：先测临界纤维长度，为载荷传递设计界面，再证明复合材料强过任一单组分。
- Negative: `no composite-strength claims without interface data, no ignoring critical fibre length, no direction-averaged claims for aligned fibres, no presenting matrix failure as fibre failure, no hiding fibre-breakage statistics`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
