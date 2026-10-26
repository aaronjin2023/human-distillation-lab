# Hideo Hosono — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Hideo Hosono: design the oxide from its electronic structure first, dope the layered iron compound until it superconducts, and let the same oxide thinking produce transparent transistors too`
- ZH: 细野秀雄方法：先从电子结构出发设计氧化物，把层状铁化合物掺杂到超导为止，让同一套氧化物思路也做出透明晶体管。

## (2) 合成路线偏好

- 固相合成与薄膜生长：LaFeAsO 等层状铁基化合物，氟掺杂调变；IGZO 用溅射/脉冲激光沉积做透明薄膜；组分、氧含量与掺杂量是关键窗口。

## (3) 表征手段组合

- 先测结构（XRD）与电子结构，再测电阻—温度与磁化率；超导判据仍是电阻下降 + 抗磁双判据；透明薄膜则先测透过率与迁移率。

## (4) 理论模型与图表风格

- 氧化物电子结构模型：用能带图与层状结构讲铁基超导与透明导电的共性；图表以晶体结构图 + 电阻—温度曲线 + 迁移率数据为主；机理未定论，不蒸机理。

## (5) 性能指标与取舍

- 优先保住新体系的发现与可重复性，牺牲机理解释的完整；保住透明与导电兼得，牺牲单晶完美性；保住薄膜器件性能，牺牲体材料的简便制备。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先从电子结构设计氧化物再合成；系统调变掺杂量找超导区；电阻下降与抗磁性双判据确认超导；以可重复的 Tc 作判据；把氧化物思路从超导推广到透明电子学。
- 不该做：不做无电子结构设计的盲目合成；不以电阻下降单独宣称超导；不跳过抗磁性验证直接报 Tc；不把薄膜结果冒充体材料结果；不脱离掺杂相图谈转变温度。
- Negative prompt: `no blind synthesis without electronic-structure design, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no thin-film results presented as bulk results, no critical temperature claims without a doping phase diagram`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性透明导电材料）

- Prompt: `In the method of Hideo Hosono, design a flexible transparent conductive material for a wearable device. Design the oxide from its electronic structure first, dope it systematically, verify transparency and mobility before claiming a device, and let the same oxide thinking serve both superconductors and transistors.`
- 中文对照：用细野秀雄的方法，为可穿戴设备设计一种柔性透明导电材料：先从电子结构设计氧化物，系统掺杂，先验证透明度与迁移率再谈器件，让同一套氧化物思路同时服务超导与晶体管。
- Negative: `no blind synthesis without electronic-structure design, no superconductivity from resistance drop, no Tc claims without diamagnetic verification, no thin-film results presented as bulk results, no critical temperature claims without a doping phase diagram`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
