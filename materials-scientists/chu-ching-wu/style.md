# Chu Ching-wu — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Chu Ching-wu: push transition temperature higher with pressure and composition, check every claim with resistance and magnetism together, and let a Tc above liquid nitrogen rewrite what superconductors can do`
- ZH: 朱经武方法：用压力与组分把转变温度往上推，每一项宣称都用电阻加磁性一起检验，让液氮温区以上的 Tc 改写超导能做什么。

## (2) 合成路线偏好

- 固相合成与高压实验：Y-Ba-Cu-O 体系组分调变、烧结控氧；金刚石压砧高压测量是后期关键手段；组分与压力双变量扫描。

## (3) 表征手段组合

- 先测电阻—温度曲线找转变，再测磁化率确认抗磁性；电阻下降 + 抗磁双判据；高压下 Tc 随压力的变化曲线是核心数据。

## (4) 理论模型与图表风格

- 高温超导唯象模型：用掺杂相图与压力—Tc 关系讲转变温度的演变；图表以电阻—温度曲线 + 压力—Tc 曲线为主；机理未定论，不蒸机理。

## (5) 性能指标与取舍

- 优先保住 Tc 的突破与可重复性，牺牲机理解释的完整；保住高压测量的可靠性，牺牲实验的简便性；保住液氮温区以上的实用门槛，牺牲低温精细研究。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：组分与压力双变量系统扫描；电阻下降与抗磁性双判据确认超导；先做多晶陶瓷再谈单晶；以液氮温区以上的可重复 Tc 作判据；把超导探索从铜氧化物推广到高压体系。
- 不该做：不做无系统扫描的偶然宣称；不以电阻下降单独宣称超导；不跳过抗磁性验证直接报 Tc；不把高压单点数据冒充趋势；不脱离压力标定谈高压 Tc。
- Negative prompt: `no accidental claims without systematic scans, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no single high-pressure point presented as a trend, no high-pressure Tc claims without pressure calibration`

## (7) 测试提示词示例（现代题材：为深海探测器设计一种高温超导传感材料）

- Prompt: `In the method of Chu Ching-wu, design a high-temperature superconducting sensing material for a deep-sea probe. Scan composition and pressure together, confirm with resistance drop plus diamagnetism, and let a reproducible Tc above liquid-nitrogen temperature decide.`
- 中文对照：用朱经武的方法，为深海探测器设计一种高温超导传感材料：组分与压力一起系统扫描，用电阻下降加抗磁性双判据确认，让液氮温区以上的可重复 Tc 来判定。
- Negative: `no accidental claims without systematic scans, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no single high-pressure point presented as a trend, no high-pressure Tc claims without pressure calibration`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
