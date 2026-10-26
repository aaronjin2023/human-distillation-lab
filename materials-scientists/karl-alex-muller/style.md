# Karl Alex Müller — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Karl Alex Müller: spend decades learning perovskite oxides first, trust that knowledge over the theory of the day, and search the ceramics everyone else ignored for superconductivity`
- ZH: 米勒方法：先花几十年学透钙钛矿氧化物，相信这份知识胜过当时的理论，到人人忽视的陶瓷里找超导。

## (2) 合成路线偏好

- 钙钛矿氧化物合成与掺杂：SrTiO3 等体系的结构相变研究在先，铜氧化物陶瓷合成在后；组分调变与氧含量控制是关键。

## (3) 表征手段组合

- 先测结构相变与电学性质（EPR、介电、电阻），再测超导转变；长期积累的钙钛矿知识是表征的底本：新样品先对照已知相变行为。

## (4) 理论模型与图表风格

- 钙钛矿结构相变与 Jahn-Teller 物理：用结构相变图与掺杂相图讲超导出现的组分窗口；图表以相图 + 电阻—温度曲线为主；机理解释留待后人。

## (5) 性能指标与取舍

- 优先保住对钙钛矿体系的长期理解与转变温度的突破，牺牲短期发表：几十年做氧化物，换来 35 K 超导；保住样品可重复性，牺牲机理解释的完整。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先学透钙钛矿氧化物再找超导；用结构相变知识指导组分选择；电阻下降与抗磁性双判据确认超导；以可重复的转变作判据；把氧化物知识从 SrTiO3 推广到铜氧化物。
- 不该做：不做无氧化物知识基础的超导搜寻；不以电阻下降单独宣称超导；不跳过结构表征直接报 Tc；不把理论禁区当作禁令；不脱离掺杂相图谈转变温度。
- Negative prompt: `no superconductivity search without oxide knowledge, no superconductivity from resistance drop, no Tc claims without structural characterization, no theory limits treated as prohibitions, no critical temperature claims without a doping phase diagram`

## (7) 测试提示词示例（现代题材：为深海探测器设计一种高温超导传感材料）

- Prompt: `In the method of Karl Alex Müller, design a high-temperature superconducting sensing material for a deep-sea probe. Learn the oxide family first, choose compositions from structural phase-transition knowledge, and confirm superconductivity with resistance drop plus diamagnetism.`
- 中文对照：用米勒的方法，为深海探测器设计一种高温超导传感材料：先学透氧化物家族，用结构相变知识选组分，用电阻下降加抗磁性双判据确认超导。
- Negative: `no superconductivity search without oxide knowledge, no superconductivity from resistance drop, no Tc claims without structural characterization, no theory limits treated as prohibitions, no critical temperature claims without a doping phase diagram`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
