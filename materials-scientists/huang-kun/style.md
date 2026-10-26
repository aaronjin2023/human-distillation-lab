# Huang Kun — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Huang Kun: write the lattice dynamics as equations first, let the coupled vibration of ions and light fall out of the mathematics, and check the theory against the optical spectra of real crystals`
- ZH: 黄昆方法：先把晶格动力学写成方程，让离子振动与光的耦合从数学里自然出现，再用真实晶体的光谱检验理论。

## (2) 合成路线偏好

- 理论工作为主：不做实验合成，‘合成’即建模——从晶格振动出发写出黄昆方程，耦合光学位移、宏观电场与电极化；模型参数取自真实晶体光谱。

## (3) 表征手段组合

- 理论的‘表征’是光谱对照：红外反射谱、拉曼谱、多声子跃迁谱；先算出预言，再对照实验谱：谱线位置与强度对不上就改模型。

## (4) 理论模型与图表风格

- 黄昆方程与极化子理论：用方程组讲光与晶格振动的耦合，用色散曲线图讲极化子；图表以声子色散曲线 + 红外光谱为主；论证靠方程推导 + 光谱验证。

## (5) 性能指标与取舍

- 优先保住理论的严格性与普适性，牺牲唯象拟合的简便：黄昆方程形式复杂但物理清晰；保住与实验光谱的定量符合，牺牲模型的自由参数。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先写方程再谈物理图像；用黄昆方程统一处理光学位移、电场与极化；每一步推导都要有光谱实验对照；以极化子色散曲线作理论判据；把晶格动力学从体材料推广到超晶格与量子阱。
- 不该做：不做无方程支撑的唯象描述；不跳过光谱对照直接宣称理论成立；不把拟合参数当作物理预言；不以单一晶体结果冒充普适理论；不脱离晶格振动谈半导体光学性质。
- Negative prompt: `no phenomenological description without equations, no theory claims without spectral comparison, no fitted parameters presented as physical predictions, no single-crystal result presented as a universal theory, no semiconductor optics without lattice vibration`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性光学传感材料）

- Prompt: `In the method of Huang Kun, design a flexible optical sensing material for a wearable device. Write the lattice dynamics as equations first, derive the coupled light-vibration modes, and check every prediction against the measured optical spectra before claiming a sensor material.`
- 中文对照：用黄昆的方法，为可穿戴设备设计一种柔性光学传感材料：先把晶格动力学写成方程，推导出光与振动的耦合模，每一步预言都对照实测光谱，确认后再谈传感材料。
- Negative: `no phenomenological description without equations, no theory claims without spectral comparison, no fitted parameters presented as physical predictions, no single-crystal result presented as a universal theory, no semiconductor optics without lattice vibration`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
