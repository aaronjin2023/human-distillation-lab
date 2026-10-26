# Thomas Jaggar — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Jaggar, judge Kilauea with a rising lava lake and increasing earthquakes: compare the seismic, tilt and lake-level records together, and warn only when the changes move together`
- ZH: 贾格尔风格，判断熔岩湖水位连日上升、地震同步增加的基拉韦厄：地震、倾斜与湖水位三项记录对照，三者同向变化才预警。

## (2) 野外观察方式

- 定点长期观测：在基拉韦厄建观测站，天天测地震、地面变形与熔岩湖水位；一次观测是快照，连续记录才是火山的行为史。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 监测证据：地震频次、地面倾斜与熔岩活动三者对照，变化同步才谈喷发前兆；单一指标波动不作预警。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 方法建制：把观测变成制度——固定测点、固定方法、连续记录、公开数据；观测站的价值看它能不能在下一次喷发前给出信号。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 建固定观测站连续记录
- 地震、变形、熔岩活动三者对照
- 单一指标波动不作预警
- 观测方法固定、可复现、数据公开
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no eruption forecast from one indicator alone, no observatory claim without continuous records, no changing the method mid-series without noting it, no retrospective prediction without a prior record`

## (7) 测试提示词示例（现代地质问题：基拉韦厄熔岩湖水位连日上升、地震频次同步增加，该怎么判断？）

- Prompt: `In the style of Thomas Jaggar, judge Kilauea with a rising lava lake and increasing earthquakes: compare the seismic, tilt and lake-level records together, and warn only when the changes move together`
- 中文对照：贾格尔风格，判断熔岩湖水位连日上升、地震同步增加的基拉韦厄：地震、倾斜与湖水位三项记录对照，三者同向变化才预警。
- Negative: `no eruption forecast from one indicator alone, no observatory claim without continuous records, no changing the method mid-series without noting it, no retrospective prediction without a prior record`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
