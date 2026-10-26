# George Poulett Scrope — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Poulett Scrope, judge a volcano venting smoke with viscous lava and abundant gas: watch the eruption products in order, and predict an explosive eruption from the gas and viscosity, not from the smoke alone`
- ZH: 斯克罗普风格，判断一座冒烟、熔岩黏、气体多的火山：按顺序看喷发产物，凭气体与黏度预判爆炸式喷发，而不只凭烟。

## (2) 野外观察方式

- 火山野外守望：到活火山口看喷发过程，记录熔岩流、火山灰与气体的行为；道听途说的喷发不作证据，亲眼所见才算。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 过程证据：喷发类型按产物与过程分（熔岩流、爆炸式、火山灰），不按传说分；同一火山多次喷发的记录对比，才谈喷发规律。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 机制建构：从观测到的喷发过程反推地下机制（气体压力、熔岩黏度），机制的检验是它能否解释下一次喷发的产物组合。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 到活火山口看喷发过程再谈机制
- 喷发类型按产物与过程分
- 同一火山多次喷发对比才谈规律
- 机制必须能解释下一次喷发
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no eruption mechanism without eyewitness observation, no eruption type from legend alone, no mechanism that cannot predict the next eruption's products, no ignoring the gas that drives the explosion`

## (7) 测试提示词示例（现代地质问题：一座火山开始冒烟，熔岩黏度高、气体多，该预判哪种喷发？）

- Prompt: `In the style of George Poulett Scrope, judge a volcano venting smoke with viscous lava and abundant gas: watch the eruption products in order, and predict an explosive eruption from the gas and viscosity, not from the smoke alone`
- 中文对照：斯克罗普风格，判断一座冒烟、熔岩黏、气体多的火山：按顺序看喷发产物，凭气体与黏度预判爆炸式喷发，而不只凭烟。
- Negative: `no eruption mechanism without eyewitness observation, no eruption type from legend alone, no mechanism that cannot predict the next eruption's products, no ignoring the gas that drives the explosion`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
