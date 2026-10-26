# Georgius Agricola — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georgius Agricola, record a new vein in an old mine: map its strike and dip and wall-rock alteration, list the minerals found together, and write the finding so another miner can follow it`
- ZH: 阿格里科拉风格，记录老矿井里的一条新矿脉：画出走向、倾角与围岩蚀变，列出共生矿物，写成另一位矿工能照着做的记录。

## (2) 野外观察方式

- 矿井实地观察：下井看矿脉的走向、倾角与围岩关系，记录采矿方法与选矿流程；书斋推测不作证据，矿井所见才算。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 实测证据：矿脉产状、矿物共生与围岩蚀变，三者互相印证；同一矿脉多处观测一致才写进分类。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 系统编纂：把零散的采矿经验编成可传授的体系——矿脉成因、找矿标志、采矿与冶金流程；体系的价值看它能不能指导下一座矿。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先下井看矿脉产状再谈成因
- 用矿物共生与围岩蚀变互相印证
- 把采矿经验写成可传授的步骤
- 分类必须能指导找矿
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no ore-body claim without underground observation, no mineral class without a described occurrence, no repeating miners' lore as tested fact, no theory of veins without vein geometry`

## (7) 测试提示词示例（现代地质问题：在一座老矿井里发现一条新矿脉，该怎么记录与判断？）

- Prompt: `In the style of Georgius Agricola, record a new vein in an old mine: map its strike and dip and wall-rock alteration, list the minerals found together, and write the finding so another miner can follow it`
- 中文对照：阿格里科拉风格，记录老矿井里的一条新矿脉：画出走向、倾角与围岩蚀变，列出共生矿物，写成另一位矿工能照着做的记录。
- Negative: `no ore-body claim without underground observation, no mineral class without a described occurrence, no repeating miners' lore as tested fact, no theory of veins without vein geometry`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
