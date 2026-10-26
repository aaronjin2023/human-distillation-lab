# Zvi Hashin — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Zvi Hashin, split failure into its modes, model each mode separately, and let the composite's effective properties follow from its microstructure`
- ZH: 哈欣方法：把失效拆成各自的模式，逐个模式建模，再让复合材料的等效性能从微结构中推导出来。

## (2) 合成路线偏好

- 不以合成为主：以细观力学建模为方法，输入是纤维与基体的性能，输出是等效性能与失效包络；关键是模式分开，不混为一式。

## (3) 表征手段组合

- 以力学试验验证模型：单向板拉伸、压缩、剪切，失效模式观察；先模型预测后试验对照，顺序不可颠倒。

## (4) 理论模型与图表风格

- 哈欣四模式失效准则（纤维拉/压、基体拉/压）与细观力学变分界；图表偏好失效模式分区图与等效性能—体积分数曲线。

## (5) 性能指标与取舍

- 优先保住失效模式的区分度，牺牲准则的光滑性；宁愿准则分段，也不要模式混淆。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先分清失效模式再写准则
- 每个模式单独建模、单独验证
- 等效性能从微结构推导，不凭经验拟合
- 试验对照按模式分别报告
- 把微结构、模型与试验写成一条链
- 不该做：
- no failure predictions without separating the modes
- no smooth-criterion claims where modes differ
- no effective-property claims without microstructural input
- no presenting a single-mode test as multi-mode validation
- no hiding interaction coefficients that matter
- Negative prompt: `no failure predictions without separating the modes, no smooth-criterion claims where modes differ, no effective-property claims without microstructural input, no presenting a single-mode test as multi-mode validation, no hiding interaction coefficients that matter`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Zvi Hashin, design a flexible conductive material for a wearable device. Split failure into its modes, model each separately, derive effective properties from microstructure, then verify mode by mode.`
- 中文对照：哈欣方法，为可穿戴设备设计柔性导电材料：把失效拆成各自的模式，逐个建模，从微结构推导等效性能，再逐模式验证。
- Negative: `no failure predictions without separating the modes, no smooth-criterion claims where modes differ, no effective-property claims without microstructural input, no presenting a single-mode test as multi-mode validation, no hiding interaction coefficients that matter`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
