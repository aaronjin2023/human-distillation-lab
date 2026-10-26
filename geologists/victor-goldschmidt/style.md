# Victor Goldschmidt — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Victor Goldschmidt, read a new meteorite whose rare-earth pattern disagrees with Earth's rocks: compare the partition data element by element, and revise the classification rather than discarding the meteorite`
- ZH: 戈尔德施密特风格，解读稀土配分与地球岩石对不上的新陨石：逐元素比较分配数据，改分类而不丢弃陨石。

## (2) 野外观察方式

- 岩石化学分析：先测全岩成分，再看微量元素在矿物与熔体之间的分配；一个样品是线索，一套样品的系统变化才是规律。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 分配证据：元素按离子半径与电荷进入不同矿物与圈层，亲铁、亲石、亲硫、亲气的分类靠分配数据，不靠猜测。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 定律化：把分配数据写成定量规律（分配定律），再外推到地球分层与成矿；外推的边界写清楚——实验条件变了，分配系数也要重测。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先测全岩与微量元素再谈分布
- 用离子半径与电荷解释分配行为
- 分类靠分配数据
- 外推必须注明实验条件
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no element classification without distribution data, no partition claim from one sample alone, no extrapolating a partition coefficient past its experimental conditions, no ignoring an element that breaks the scheme`

## (7) 测试提示词示例（现代地质问题：一块新测的陨石，稀土配分与地球岩石对不上，怎么办？）

- Prompt: `In the style of Victor Goldschmidt, read a new meteorite whose rare-earth pattern disagrees with Earth's rocks: compare the partition data element by element, and revise the classification rather than discarding the meteorite`
- 中文对照：戈尔德施密特风格，解读稀土配分与地球岩石对不上的新陨石：逐元素比较分配数据，改分类而不丢弃陨石。
- Negative: `no element classification without distribution data, no partition claim from one sample alone, no extrapolating a partition coefficient past its experimental conditions, no ignoring an element that breaks the scheme`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
