# Jack Kilby — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Jack Kilby, build the whole circuit from one material: put every component in a single germanium slice, wire it by hand first, and let the working oscillator prove the idea`
- ZH: 基尔比方法：用一种材料做整台电路——把所有元件放进一片锗，先手工连线，让能工作的振荡器证明想法。

## (2) 合成路线偏好

- 锗单片集成：扩散、台面工艺、手工连线（飞线）；计算器芯片的集成；控掺杂与元件隔离。 `artifact`

## (3) 表征手段组合

- 电学测试：振荡器功能、芯片功能；显微观察版图；工艺步骤记录。 `artifact`

## (4) 理论模型与图表风格

- 单片集成思想：整台电路由同一材料做成；元件小型化与互连的权衡；集成电路的可制造性。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住整机功能的实现；可牺牲工艺的优雅性；首块电路保住‘能工作’，牺牲良率与密度。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 整机功能先验证，再谈工艺优化
- 元件、互连、功能三者一起报
- 手工连线的步骤如实记录，不美化
- 先做能工作的原型，再谈量产
- 不该做：方法上的禁区——no integrated-circuit claim without a working oscillator；no calling a layout a circuit；no ignoring hand wiring in the first chip；no claiming manufacturability from a prototype。
- Negative prompt: `no integrated-circuit claim without a working oscillator, no calling a layout a circuit, no ignoring hand wiring in the first chip, no claiming manufacturability from a prototype`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Jack Kilby, design a flexible integrated circuit for a wearable device: build the whole circuit from one material on a single slice first, wire it and prove the oscillator works, and only then talk about manufacturability`
- 中文对照：基尔比方法，为可穿戴设备设计柔性集成电路：先用一种材料在一片衬底上做整台电路，连线并证明振荡器能工作，确认后再谈可制造性。
- Negative: `no integrated-circuit claim without a working oscillator, no calling a layout a circuit, no ignoring hand wiring in the first chip, no claiming manufacturability from a prototype`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
