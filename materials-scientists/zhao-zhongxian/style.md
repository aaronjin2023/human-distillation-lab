# Zhao Zhongxian — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Zhao Zhongxian: keep measuring superconductors when the field goes quiet, raise the transition temperature step by step with composition and pressure, and let a reproducible Tc above liquid nitrogen decide`
- ZH: 赵忠贤方法：在领域沉寂时仍坚持测超导，用组分与压力一步步抬高转变温度，让可重复的液氮温区以上 Tc 来判定。

## (2) 合成路线偏好

- 固相合成铜氧化物与铁基超导材料：Ba-Y-Cu-O 体系组分调变、烧结与氧含量控制；高压合成与高压测量是后期关键手段。

## (3) 表征手段组合

- 先测电阻—温度曲线找转变，再测磁化率确认抗磁性；电阻下降 + 抗磁双判据；液氮温区（77 K）以上是核心门槛。

## (4) 理论模型与图表风格

- 高温超导唯象模型：用掺杂相图讲 Tc 随组分的演变，用压力—Tc 关系讲高压效应；图表以电阻—温度曲线 + 掺杂相图为主；机理未定论，不蒸机理。

## (5) 性能指标与取舍

- 优先保住 Tc 的突破与可重复性，牺牲机理解释的完整；保住样品均匀性，牺牲单晶完美性；保住液氮温区以上的实用门槛，牺牲低温区的精细研究。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：系统调变组分，不只做一个配方；电阻下降与抗磁性双判据确认超导；先做多晶陶瓷再谈单晶；以液氮温区以上的可重复 Tc 作判据；把超导研究从铜氧化物推广到铁基与高压体系。
- 不该做：不做无系统组分扫描的偶然宣称；不以电阻下降单独宣称超导；不跳过抗磁性验证直接报 Tc；不把单次测量冒充可重复转变；不脱离掺杂相图谈转变温度。
- Negative prompt: `no accidental claims without systematic composition scans, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no single measurement presented as a reproducible transition, no critical temperature claims without a doping phase diagram`

## (7) 测试提示词示例（现代题材：为深海探测器设计一种高温超导传感材料）

- Prompt: `In the method of Zhao Zhongxian, design a high-temperature superconducting sensing material for a deep-sea probe. Scan compositions systematically, confirm with resistance drop plus diamagnetism, and let a reproducible Tc above liquid-nitrogen temperature decide.`
- 中文对照：用赵忠贤的方法，为深海探测器设计一种高温超导传感材料：系统扫描组分，用电阻下降加抗磁性双判据确认，让液氮温区以上的可重复 Tc 来判定。
- Negative: `no accidental claims without systematic composition scans, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no single measurement presented as a reproducible transition, no critical temperature claims without a doping phase diagram`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
