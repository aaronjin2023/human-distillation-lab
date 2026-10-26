# Subra Suresh — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Subra Suresh, measure the smallest volume that still tells the truth, connect fatigue to the microstructure that causes it, and let one cell's stiffness speak for disease`
- ZH: 苏雷什方法：测最小的、仍能说真话的体积，把疲劳连到造成它的微结构上，再让一个细胞的刚度为疾病作证。

## (2) 合成路线偏好

- 薄膜与小体积试样制备：沉积、多层膜、梯度成分；关键是小体积试样的制备与测试方法一起设计。

## (3) 表征手段组合

- 纳米压痕定模量与硬度，疲劳试验定裂纹扩展，曲率法测薄膜应力，光镊测单细胞力学；先小体积力学后机理，顺序不可颠倒。

## (4) 理论模型与图表风格

- 疲劳裂纹扩展模型、薄膜应力模型与细胞力学模型；图表偏好疲劳裂纹扩展速率曲线与压痕载荷—位移曲线。

## (5) 性能指标与取舍

- 优先保住小体积测量的可靠性，牺牲测试通量；宁愿测得慢，也不要测不准。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先标定纳米压痕方法再报薄膜性能
- 疲劳试验报告裂纹扩展速率曲线
- 薄膜应力用曲率法独立验证
- 单细胞力学设健康细胞对照
- 把小体积力学、微结构与机理写成一条链
- 不该做：
- no thin-film properties without indentation calibration
- no fatigue claims without crack-growth-rate data
- no cell-mechanics claims without healthy-cell controls
- no presenting bulk properties as thin-film properties
- no hiding size effects
- Negative prompt: `no thin-film properties without indentation calibration, no fatigue claims without crack-growth-rate data, no cell-mechanics claims without healthy-cell controls, no presenting bulk properties as thin-film properties, no hiding size effects`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Subra Suresh, design a flexible conductive material for a wearable device. Calibrate small-volume testing first, measure fatigue crack growth, then let the smallest honest volume judge the design.`
- 中文对照：苏雷什方法，为可穿戴设备设计柔性导电材料：先标定小体积测试方法，测疲劳裂纹扩展，再让最小的、仍能说真话的体积评判设计。
- Negative: `no thin-film properties without indentation calibration, no fatigue claims without crack-growth-rate data, no cell-mechanics claims without healthy-cell controls, no presenting bulk properties as thin-film properties, no hiding size effects`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
