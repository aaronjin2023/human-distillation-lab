# Leo Baekeland — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Leo Baekeland, control the condensation: react phenol with formaldehyde under heat and pressure, stop the reaction at the mouldable stage, and let the hard moulded piece prove the resin`
- ZH: 贝克兰方法：控制缩聚——苯酚与甲醛在热压下反应，在可模塑阶段停住，让硬质模塑件证明树脂。

## (2) 合成路线偏好

- 酚醛缩聚：苯酚 + 甲醛，碱 / 酸催化，控温控压；分阶段：可溶可熔中间体 → 热压成型 → 不溶不熔终产物；控反应程度是关键。 `artifact`

## (3) 表征手段组合

- 硬度与热稳定性测试；电绝缘测试；成型性观察；化学抗性测试；外观与尺寸稳定性。 `artifact`

## (4) 理论模型与图表风格

- 缩聚交联：酚醛树脂由线型中间体交联成三维网络；反应程度决定可模塑性与最终硬度；热固性塑料的成型窗口。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住成型后的硬度与热稳定性；可牺牲可重塑性；电木保住电绝缘与耐热，牺牲韧性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 反应程度、温度、压力三者一起报
- 在可模塑阶段停住反应，不等到完全固化再成型
- 硬度、绝缘、耐热三项成对报
- 先做小样验证成型窗口，再放大
- 不该做：方法上的禁区——no Bakelite claim without heat-and-pressure moulding conditions；no calling the soluble intermediate the final resin；no reporting hardness without a cure schedule；no claiming a plastic from a single reaction。
- Negative prompt: `no Bakelite claim without heat-and-pressure moulding conditions, no calling the soluble intermediate the final resin, no reporting hardness without a cure schedule, no claiming a plastic from a single reaction`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Leo Baekeland, design a flexible conductive thermoset for a wearable device: control the phenol-formaldehyde condensation first, stop at the mouldable stage, and prove hardness and insulation after heat-and-pressure curing before claiming the material`
- 中文对照：贝克兰方法，为可穿戴设备设计柔性导电热固性材料：先控制酚醛缩聚，在可模塑阶段停住，热压固化后验证硬度与绝缘，确认后再谈材料。
- Negative: `no Bakelite claim without heat-and-pressure moulding conditions, no calling the soluble intermediate the final resin, no reporting hardness without a cure schedule, no claiming a plastic from a single reaction`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
