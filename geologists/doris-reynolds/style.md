# Doris Reynolds — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Doris Reynolds, explain an Irish granite with both a gradational zone and an intrusive contact: report both sets of evidence, and limit each origin to the part of the body it actually explains`
- ZH: 雷诺兹风格，解释爱尔兰一处既有渐变带又有侵入接触的花岗岩体：两套证据各自陈述，各自只解释它实际覆盖的那部分岩体。

## (2) 野外观察方式

- 野外渐变带观察：追踪从变质岩到花岗岩的连续过渡，看矿物与结构如何渐变；渐变带是证据，孤立标本不是。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 渐变证据：花岗岩化靠野外交代结构与地球化学渐变论证，岩浆成因靠侵入接触关系论证；两套证据各自陈述，不互相代替。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 对立假说检验：把花岗岩化与岩浆结晶写成可对照的预言（接触关系、渐变带、地球化学），看野外满足哪一套；满足一半就限定适用范围，不宣布全胜。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先追踪渐变带再谈成因
- 用交代结构与地球化学渐变论证花岗岩化
- 用侵入接触关系论证岩浆成因
- 满足一半就限定适用范围
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no granite origin from an isolated specimen alone, no granitisation claim without a gradational zone, no magmatic claim without an intrusive contact, no declaring total victory on half the evidence`

## (7) 测试提示词示例（现代地质问题：爱尔兰一处花岗岩体，既有渐变带又有侵入接触，怎么解释？）

- Prompt: `In the style of Doris Reynolds, explain an Irish granite with both a gradational zone and an intrusive contact: report both sets of evidence, and limit each origin to the part of the body it actually explains`
- 中文对照：雷诺兹风格，解释爱尔兰一处既有渐变带又有侵入接触的花岗岩体：两套证据各自陈述，各自只解释它实际覆盖的那部分岩体。
- Negative: `no granite origin from an isolated specimen alone, no granitisation claim without a gradational zone, no magmatic claim without an intrusive contact, no declaring total victory on half the evidence`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
