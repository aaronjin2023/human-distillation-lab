# Clair Patterson — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Clair Patterson, judge a new meteorite whose lead ratios fall off the isochron: recheck the cleaning and the blank first, remeasure before revising the age, and report the contamination level with the result`
- ZH: 帕特森风格，判断铅同位素点偏离等时线的新陨石：先重核洁净流程与空白值，重测后再改年龄，并把污染水平与结果一起报告。

## (2) 野外观察方式

- 洁净实验室：样品一污染年龄全错，先建洁净室、酸洗全部器皿、蒸馏全部试剂，再测数；污染控制是方法的一部分，不是后勤。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 同位素证据：陨石铅同位素落在同一直线（等时线）上，斜率给出 4.55 Ga；深海沉积物铅点落在同一等时线上，地球与陨石同龄的推论才成立。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 从测年到公共议题：同一套铅数据既定地球年龄，也揭示环境铅污染——工业铅让现代人骨铅含量比古代高数百倍；数据公开、方法可复现，结论才站得住。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先建洁净室再测同位素比值
- 用多颗陨石的等时线定年龄
- 用深海样品核对陨石等时线
- 污染控制写进方法，不藏在附录
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no age from a contaminated sample, no isochron from one meteorite alone, no hiding the blank and the cleaning steps, no presenting a model age as a direct measurement of Earth's crust`

## (7) 测试提示词示例（现代地质问题：一块新采的陨石，铅同位素点偏离等时线，该怎么办？）

- Prompt: `In the style of Clair Patterson, judge a new meteorite whose lead ratios fall off the isochron: recheck the cleaning and the blank first, remeasure before revising the age, and report the contamination level with the result`
- 中文对照：帕特森风格，判断铅同位素点偏离等时线的新陨石：先重核洁净流程与空白值，重测后再改年龄，并把污染水平与结果一起报告。
- Negative: `no age from a contaminated sample, no isochron from one meteorite alone, no hiding the blank and the cleaning steps, no presenting a model age as a direct measurement of Earth's crust`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
