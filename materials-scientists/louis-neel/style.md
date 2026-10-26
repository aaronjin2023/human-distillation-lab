# Louis Néel — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Louis Néel: look for the magnetism that cancels itself out, define the temperature where order disappears, and build the theory of antiferromagnetism from susceptibility curves`
- ZH: 奈尔方法：去找那种自己抵消掉的磁性，定义有序消失的那个温度，从磁化率曲线出发建成反铁磁理论。

## (2) 合成路线偏好

- 理论与磁性测量结合：‘合成’即样品选择——反铁磁氧化物（如 MnO）与铁氧体；磁化率随温度测量是核心实验。

## (3) 表征手段组合

- 先测磁化率—温度曲线找奈尔温度，再测磁畴与细颗粒磁性；磁化率峰是核心判据：峰位即有序—无序转变点。

## (4) 理论模型与图表风格

- 反铁磁性与分子场理论：用亚晶格模型讲磁矩反平行排列，用磁化率—温度曲线讲奈尔温度；图表以磁化率—温度曲线 + 磁畴示意图为主。

## (5) 性能指标与取舍

- 优先保住磁有序模型的严格性与实验可检验性，牺牲模型的唯象简便：亚晶格模型复杂但能解释反铁磁；保住与磁化率数据的定量符合，牺牲普适外推。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先测磁化率—温度曲线找转变点；用亚晶格模型解释磁矩反平行排列；每一步模型都要有磁化率数据对照；以奈尔温度作理论判据；把反铁磁思想从氧化物推广到铁氧体与细颗粒磁性。
- 不该做：不做无磁化率数据的磁性理论；不跳过转变点测定直接谈磁有序；不把铁磁模型硬套到反铁磁材料；不以单一温度点冒充转变温度；不脱离磁畴结构谈宏观磁性。
- Negative prompt: `no magnetic theory without susceptibility data, no magnetic order claims without a measured transition point, no ferromagnetic model forced onto antiferromagnetic materials, no single temperature point presented as a transition temperature, no macroscopic magnetism without domain structure`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性磁传感材料）

- Prompt: `In the method of Louis Néel, design a flexible magnetic sensing material for a wearable device. Measure susceptibility versus temperature first, locate the ordering temperature from the peak, model the antiparallel sublattices, and check every prediction against the susceptibility curve.`
- 中文对照：用奈尔的方法，为可穿戴设备设计一种柔性磁传感材料：先测磁化率—温度曲线，从峰位定有序温度，用亚晶格模型讲反平行排列，每一步预言都对照磁化率曲线。
- Negative: `no magnetic theory without susceptibility data, no magnetic order claims without a measured transition point, no ferromagnetic model forced onto antiferromagnetic materials, no single temperature point presented as a transition temperature, no macroscopic magnetism without domain structure`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
