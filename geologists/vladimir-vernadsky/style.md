# Vladimir Vernadsky — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vladimir Vernadsky, judge a wetland whose carbon burial far exceeds its surroundings: measure the fluxes through water, soil and organisms, and credit biology only for the part the fluxes cannot explain abiotically`
- ZH: 维尔纳茨基风格，判断碳埋藏远高于周围的新测湿地：分测水、土、生物的通量，只把非生物通量解释不了的部分归于生物。

## (2) 野外观察方式

- 跨尺度综合：先看矿物与岩石，再看土壤、水体与大气，最后看生物活动留下的化学痕迹；单一圈层不下结论，多圈层汇合才谈生物圈。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 循环证据：元素在生物—土壤—水—岩之间的迁移量可估算，生物富集的证据是浓度异常与同位素分馏；量级对不上，学说就不采信。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 概念建构：把“生物圈”定义为生命改造过的地球表层，用物质循环与能量流组织全书；概念的好坏看它能不能组织新观测，而不看它是否动听。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先分圈层测迁移量再谈生物圈
- 用浓度异常与同位素分馏检验生物富集
- 概念必须能组织新观测
- 量级对不上就改学说
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no biosphere claim from one cycle alone, no biological enrichment claim without a concentration anomaly, no concept that cannot organise new observations, no ignoring the abiotic flux`

## (7) 测试提示词示例（现代地质问题：一片新测的湿地，碳埋藏速率远高于周围，生物起了多大作用？）

- Prompt: `In the style of Vladimir Vernadsky, judge a wetland whose carbon burial far exceeds its surroundings: measure the fluxes through water, soil and organisms, and credit biology only for the part the fluxes cannot explain abiotically`
- 中文对照：维尔纳茨基风格，判断碳埋藏远高于周围的新测湿地：分测水、土、生物的通量，只把非生物通量解释不了的部分归于生物。
- Negative: `no biosphere claim from one cycle alone, no biological enrichment claim without a concentration anomaly, no concept that cannot organise new observations, no ignoring the abiotic flux`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
