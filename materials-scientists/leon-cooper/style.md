# Leon Cooper — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Leon Cooper: find the one instability that changes everything, show that two electrons can attract through the lattice, and let that single pair unlock the whole theory of superconductivity`
- ZH: 库珀方法：找到那个改变一切的不稳定性，证明两个电子能通过晶格相互吸引，让这一对电子解锁整个超导理论。

## (2) 合成路线偏好

- 理论工作为主：‘合成’即建模——在费米海背景上加一对电子，算出束缚态；模型参数取自真实超导体的能隙与临界温度。

## (3) 表征手段组合

- 理论的‘表征’是与实验对照：能隙、临界温度、同位素效应；先算出库珀对束缚能，再对照 BCS 理论的实验预言：对不上就改模型。

## (4) 理论模型与图表风格

- 库珀对与 BCS 理论：用费米面与声子媒介吸引讲电子配对，用能隙方程讲超导态；图表以能隙—温度曲线 + 配对示意图为主；论证靠数学推导 + 实验验证。

## (5) 性能指标与取舍

- 优先保住理论的数学严格性与实验可检验性，牺牲模型的普适外推：库珀对只在费米面附近成立，但这一点足够解锁 BCS；保住与实验的定量符合，牺牲唯象描述。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先找到费米海的不稳定性再建模型；用一对电子的束缚态讲清配对机制；每一步推导都要有实验可检验的预言；以能隙与临界温度作理论判据；把配对思想从超导推广到其他凝聚态体系。
- 不该做：不做无数学推导的唯象超导解释；不跳过实验对照直接宣称理论成立；不把库珀对推广到不适用的温区；不以单一实验符合冒充理论证明；不脱离费米面谈电子配对。
- Negative prompt: `no phenomenological superconductivity without mathematics, no theory claims without experimental comparison, no Cooper pairs extended beyond their valid temperature range, no single experiment presented as proof of a theory, no electron pairing without the Fermi surface`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性超导传感材料）

- Prompt: `In the method of Leon Cooper, design a flexible superconducting sensing material for a wearable device. Find the instability first, show how two electrons pair through the lattice, derive a testable gap prediction, and check it against measured critical temperature before claiming superconductivity.`
- 中文对照：用库珀的方法，为可穿戴设备设计一种柔性超导传感材料：先找到不稳定性，证明两个电子如何通过晶格配对，推导出可检验的能隙预言，对照实测临界温度，确认后再谈超导。
- Negative: `no phenomenological superconductivity without mathematics, no theory claims without experimental comparison, no Cooper pairs extended beyond their valid temperature range, no single experiment presented as proof of a theory, no electron pairing without the Fermi surface`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
