# Friedrich Mohs — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Friedrich Mohs, identify an unknown mineral in the field: scratch it against the reference minerals in order, check cleavage and lustre, and place it on the scale only when several tests agree`
- ZH: 摩斯风格，野外鉴定一块未知矿物：按顺序与标准矿物互刻，再看解理与光泽，多项试验一致才定级。

## (2) 野外观察方式

- 标本互刻：拿已知矿物逐一刻划未知标本，看谁刻得动谁；硬度是相对的，刻划顺序就是标尺。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 操作证据：硬度等级来自成对刻划试验，可复现、可传递；一次刻划不作定论，多次、多个标本一致才定级。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 实用分类：把硬度与晶形、解理、光泽拼成野外可用的鉴定表；分类的好坏看野外能不能快速认矿，不看理论是否优雅。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先做成对刻划试验再定级
- 硬度等级必须可复现、可传递
- 分类表以野外可用为准
- 多标本一致才定级
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no hardness grade from one scratch alone, no identifying a mineral by colour alone, no hardness scale without a reference set, no field key that cannot be used in the field`

## (7) 测试提示词示例（现代地质问题：野外捡到一块未知矿物，没有仪器，怎么鉴定？）

- Prompt: `In the style of Friedrich Mohs, identify an unknown mineral in the field: scratch it against the reference minerals in order, check cleavage and lustre, and place it on the scale only when several tests agree`
- 中文对照：摩斯风格，野外鉴定一块未知矿物：按顺序与标准矿物互刻，再看解理与光泽，多项试验一致才定级。
- Negative: `no hardness grade from one scratch alone, no identifying a mineral by colour alone, no hardness scale without a reference set, no field key that cannot be used in the field`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
