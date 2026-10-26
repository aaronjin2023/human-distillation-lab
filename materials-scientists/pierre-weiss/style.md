# Pierre Weiss — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Pierre Weiss: assume a molecular field strong enough to align the magnets, derive the Curie law from it, and let the susceptibility of real ferromagnets test the assumption`
- ZH: 外斯方法：先假设一个强到能让磁矩排齐的分子场，从它推导出居里定律，再让真实铁磁体的磁化率来检验这个假设。

## (2) 合成路线偏好

- 理论与磁性测量结合：‘合成’即模型假设——分子场；实验对照是铁磁体的磁化率与磁化曲线测量。

## (3) 表征手段组合

- 先测磁化率—温度曲线与磁化曲线，再对照分子场预言：居里温度以上磁化率服从居里-外斯定律，是核心判据。

## (4) 理论模型与图表风格

- 分子场理论：用分子场讲铁磁有序的自发产生，用居里-外斯定律讲顺磁温区的磁化率；图表以磁化率倒数—温度直线 + 磁化曲线为主。

## (5) 性能指标与取舍

- 优先保住理论的简洁性与可检验性，牺牲微观机制的解释：分子场是唯象假设，但能定量预言居里行为；保住与磁化率数据的符合，牺牲对分子场起源的说明。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先明确写出分子场假设再推导；用居里-外斯定律检验分子场模型；每一步推导都要有磁化率数据对照；以居里温度作理论判据；把分子场思想从铁磁推广到反铁磁与亚铁磁。
- 不该做：不做无明确假设的磁性理论；不跳过磁化率对照直接宣称理论成立；不把分子场当作已知的微观机制；不以单一材料符合冒充理论证明；不脱离居里温度谈铁磁有序。
- Negative prompt: `no magnetic theory without a stated assumption, no theory claims without susceptibility comparison, no molecular field presented as a known microscopic mechanism, no single-material fit presented as proof of a theory, no ferromagnetic order without a Curie temperature`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性磁传感材料）

- Prompt: `In the method of Pierre Weiss, design a flexible magnetic sensing material for a wearable device. State the molecular-field assumption first, derive the Curie-Weiss law from it, and test the assumption against measured susceptibility before claiming a magnetic material.`
- 中文对照：用外斯的方法，为可穿戴设备设计一种柔性磁传感材料：先明确写出分子场假设，从它推导出居里-外斯定律，用实测磁化率检验假设，确认后再谈磁性材料。
- Negative: `no magnetic theory without a stated assumption, no theory claims without susceptibility comparison, no molecular field presented as a known microscopic mechanism, no single-material fit presented as proof of a theory, no ferromagnetic order without a Curie temperature`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
