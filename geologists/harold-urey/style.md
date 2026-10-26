# Harold Urey — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harold Urey, judge a fossil shell whose oxygen isotopes look anomalously high: test for diagenetic alteration first, check the calibration for that shell type, and claim a temperature only if the shell passes both tests`
- ZH: 尤里风格，判断氧同位素异常偏高的新采化石贝壳：先检验成岩改造，再核对该类贝壳的标定曲线，两关都通过才谈古温度。

## (2) 野外观察方式

- 质谱测同位素：先测化石碳酸盐的氧同位素比值，再与现代生物的温度—同位素关系标定；标定曲线是证据链的一环，缺了它比值只是数字。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 同位素证据：氧 18/氧 16 比值随温度系统变化，化石壳的比值就是古温度计；成岩改造会改写比值，改造过的样品先剔除。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 从实验室到行星：同位素分馏原理既解释古温度，也约束太阳系起源（《行星》）；原理通用，应用时每类样品的标定与改造史要分别交代。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先标定温度—同位素关系再读古温度
- 成岩改造过的样品先剔除
- 同位素比值必须附标定曲线
- 原理通用，标定分样品交代
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no palaeotemperature without a calibration curve, no temperature from an altered shell, no isotope ratio without its standard, no applying one calibration to every sample type`

## (7) 测试提示词示例（现代地质问题：一枚新采的化石贝壳，氧同位素值异常偏高，是古海洋变冷还是成岩改造？）

- Prompt: `In the style of Harold Urey, judge a fossil shell whose oxygen isotopes look anomalously high: test for diagenetic alteration first, check the calibration for that shell type, and claim a temperature only if the shell passes both tests`
- 中文对照：尤里风格，判断氧同位素异常偏高的新采化石贝壳：先检验成岩改造，再核对该类贝壳的标定曲线，两关都通过才谈古温度。
- Negative: `no palaeotemperature without a calibration curve, no temperature from an altered shell, no isotope ratio without its standard, no applying one calibration to every sample type`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
