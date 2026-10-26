# J. Georg Bednorz — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of J. Georg Bednorz: search where theory says not to look, synthesize copper-oxide ceramics systematically, and let a resistance drop at 35 K overturn thirty years of low-temperature limits`
- ZH: 贝德诺兹方法：到理论说不要找的地方去找，系统地合成铜氧化物陶瓷，让电阻在 35 K 的下降推翻三十年的低温极限。

## (2) 合成路线偏好

- 固相合成铜氧化物陶瓷：La-Ba-Cu-O 体系，组分系统调变、烧结温度与氧含量控制；陶瓷粉末混合、压片、烧结是关键工艺。

## (3) 表征手段组合

- 先测电阻—温度曲线找转变，再测磁化率确认迈斯纳效应；电阻下降 + 抗磁性双判据：只有电阻降不算超导，必须有抗磁信号。

## (4) 理论模型与图表风格

- 铜氧化物超导唯象模型：用钙钛矿结构与掺杂相图讲超导区；图表以电阻—温度曲线 + 掺杂—Tc 相图为主；机理解释留给后人，本文件夹只蒸发现方法。

## (5) 性能指标与取舍

- 优先保住转变温度的突破与可重复性，牺牲机理解释的完整：先发现 35 K 超导，再谈机理；保住陶瓷样品的均匀性，牺牲单晶的完美性。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：系统调变组分，不只做一个配方；电阻下降与抗磁性双判据确认超导；先做陶瓷样品再谈单晶；以可重复的 35 K 转变作判据；把铜氧化物体系从 La 系推广到 Y 系等后续体系。
- 不该做：不做无系统组分扫描的偶然发现宣称；不以电阻下降单独宣称超导；不跳过抗磁性验证直接报 Tc；不把单次测量冒充可重复转变；不脱离掺杂相图谈转变温度。
- Negative prompt: `no accidental discovery claims without systematic composition scans, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no single measurement presented as a reproducible transition, no critical temperature claims without a doping phase diagram`

## (7) 测试提示词示例（现代题材：为深海探测器设计一种高温超导传感材料）

- Prompt: `In the method of J. Georg Bednorz, design a high-temperature superconducting sensing material for a deep-sea probe. Scan ceramic compositions systematically, confirm superconductivity with both resistance drop and diamagnetism, and let a reproducible transition temperature decide.`
- 中文对照：用贝德诺兹的方法，为深海探测器设计一种高温超导传感材料：系统扫描陶瓷组分，用电阻下降加抗磁性双判据确认超导，让可重复的转变温度来判定。
- Negative: `no accidental discovery claims without systematic composition scans, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no single measurement presented as a reproducible transition, no critical temperature claims without a doping phase diagram`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
