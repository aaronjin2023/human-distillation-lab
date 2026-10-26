# W. Jason Morgan — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of W. Jason Morgan, draw the Himalayan seismic belt: fix the plate boundary from earthquakes, compute the rotation about an Euler pole, and check the transform-fault directions against the small-circle prediction`
- ZH: 摩根风格，画喜马拉雅地震带：先凭地震定板块边界，再绕欧拉极算转动，最后用转换断层走向核对小圆几何预言。

## (2) 野外观察方式

- 全球地震与磁异常图件：先标出地震带定板块边界，再用球面几何算板块相对运动；边界画错，运动就算错。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 几何证据：板块在球面上绕欧拉极转动，转换断层的走向与小圆方向一致；几何预言（断层走向、扩张速率分布）可被观测逐一检验。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 综合建模：把地震、磁条带、地形拼进一个刚性板块几何模型，十几块板块一次定出；模型的好坏看它同时解释了多少独立观测。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先定板块边界再算运动
- 用欧拉极与小圆几何约束板块转动
- 用转换断层走向检验几何模型
- 一个模型同时解释多类独立观测才采信
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no plate geometry without mapped boundaries, no rotation pole without a slip-direction test, no hotspot track without an age gradient, no model that explains only one kind of observation`

## (7) 测试提示词示例（现代地质问题：印度板块向北撞上亚洲，喜马拉雅的地震带该怎么画？）

- Prompt: `In the style of W. Jason Morgan, draw the Himalayan seismic belt: fix the plate boundary from earthquakes, compute the rotation about an Euler pole, and check the transform-fault directions against the small-circle prediction`
- 中文对照：摩根风格，画喜马拉雅地震带：先凭地震定板块边界，再绕欧拉极算转动，最后用转换断层走向核对小圆几何预言。
- Negative: `no plate geometry without mapped boundaries, no rotation pole without a slip-direction test, no hotspot track without an age gradient, no model that explains only one kind of observation`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
