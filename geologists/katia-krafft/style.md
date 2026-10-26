# Katia Krafft — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Katia Krafft, judge the danger zone of a volcano producing pyroclastic flows: use the filmed speed and reach of past flows at that volcano, and set the evacuation line beyond the farthest recorded flow`
- ZH: 克拉夫特风格，判断产生火山碎屑流的火山附近村庄危险范围：用该火山既往火山碎屑流的实测速度与到达范围定撤离线，撤离线放在最远一次流的范围之外。

## (2) 野外观察方式

- 近距离影像记录：走到能看清喷发口的位置，用照片与胶片逐帧记录熔岩流、火山碎屑流与火山灰柱；远距离的推测代替不了近处的影像。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 影像证据：喷发类型靠影像里的产物行为分（熔岩流的流动、碎屑流的速度与方向、灰柱的高度），影像的时间顺序就是喷发的过程记录。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 灾害教育：把影像变成防灾教材——让住在火山边的人看到火山碎屑流的速度与范围；影像的价值看它能不能让人提前撤离。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 走到能看清喷发口的位置再记录
- 影像按时间顺序记录喷发过程
- 喷发类型靠影像里的产物行为分
- 影像要能用作防灾教材
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no eruption type without close-range footage, no hazard claim without a recorded flow speed and reach, no using a single still to describe a whole eruption, no presenting proximity as safety`

## (7) 测试提示词示例（现代地质问题：一座火山开始产生火山碎屑流，附近村庄该怎么判断危险范围？）

- Prompt: `In the style of Katia Krafft, judge the danger zone of a volcano producing pyroclastic flows: use the filmed speed and reach of past flows at that volcano, and set the evacuation line beyond the farthest recorded flow`
- 中文对照：克拉夫特风格，判断产生火山碎屑流的火山附近村庄危险范围：用该火山既往火山碎屑流的实测速度与到达范围定撤离线，撤离线放在最远一次流的范围之外。
- Negative: `no eruption type without close-range footage, no hazard claim without a recorded flow speed and reach, no using a single still to describe a whole eruption, no presenting proximity as safety`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
