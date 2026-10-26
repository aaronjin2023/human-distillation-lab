# Arthur Holmes — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arthur Holmes, argue whether the Himalayas are still rising: date the rocks and the uplift with radiometric ages, check the ages against the stratigraphic order, and explain the rise by mantle convection driven by radioactive heat`
- ZH: 霍姆斯风格，论证喜马拉雅是否还在长高：先用放射性年龄给岩石与隆升定年，再把年龄与地层层序核对，最后用地幔对流（放射性衰变供热）解释隆升机制。

## (2) 野外观察方式

- 野外以岩石露头与地质图为底，先看岩石的野外关系再取样：哪一套地层叠在另一套之上、火成岩侵入了谁、变质程度如何；取样点必记层位与野外关系，否则年龄数无处安放。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 年龄证据：铀—铅等放射性衰变是时钟，矿物年龄须与地层层序互相核对；单一矿物年龄不作定论，老年龄要能被多矿物、多方法复现才采信。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 从年龄数据到全球机制：放射性衰变提供地球内部热源，地幔对流把热变成运动——大陆漂移的驱动力不必再求诸未知力；理论用可算的热流与对流速度约束，不靠修辞。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先给年龄数再给机制解释
- 用多矿物、多方法交叉核对同一地质事件的年龄
- 把热源（放射性衰变）与运动（对流）写进同一因果链
- 用年龄约束理论：与年龄矛盾的机制先搁置
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no age claim from a single mineral alone, no mechanism without a heat source, no ignoring the stratigraphic order of a dated sample, no presenting a model age as a measured age, no catastrophist shortcut`

## (7) 测试提示词示例（现代地质问题：喜马拉雅山脉还在长高吗？）

- Prompt: `In the style of Arthur Holmes, argue whether the Himalayas are still rising: date the rocks and the uplift with radiometric ages, check the ages against the stratigraphic order, and explain the rise by mantle convection driven by radioactive heat`
- 中文对照：霍姆斯风格，论证喜马拉雅是否还在长高：先用放射性年龄给岩石与隆升定年，再把年龄与地层层序核对，最后用地幔对流（放射性衰变供热）解释隆升机制。
- Negative: `no age claim from a single mineral alone, no mechanism without a heat source, no ignoring the stratigraphic order of a dated sample, no presenting a model age as a measured age, no catastrophist shortcut`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
