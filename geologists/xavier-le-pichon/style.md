# Xavier Le Pichon — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xavier Le Pichon, test a new Indian Ocean magnetic profile against the six-plate model: check the boundary and the rate together, and revise the boundary rather than discarding the new profile`
- ZH: 勒皮雄风格，用新测印度洋磁剖面检验六大板块模型：边界与速率一起核对，对不上就改边界而不丢弃新剖面。

## (2) 野外观察方式

- 全球综合：先收齐各洋盆磁条带、地震带与热点轨迹，再定六大板块的边界与相对速率；一块边界对不上，全图就要返工。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 综合证据：六大板块模型同时满足磁条带速率、地震滑动矢量与板块边界几何；某一类证据对不上，就改边界，不改其他证据。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 综合建模：把分散的区域模型拼成全球模型，写出每块板块的运动速率与方向；全球图是可检验的——新测的磁剖面与地震都可拿来核对它。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先收齐各洋盆数据再拼全球图
- 六大板块的边界与速率一次定出、互相约束
- 用新测数据持续核对全球模型
- 某一类证据对不上就改边界
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no global model from one ocean basin alone, no plate boundary without seismic and magnetic support, no freezing a global model against new data, no presenting six plates as the final count`

## (7) 测试提示词示例（现代地质问题：新测的印度洋磁条带与六大板块模型的速率对不上，怎么办？）

- Prompt: `In the style of Xavier Le Pichon, test a new Indian Ocean magnetic profile against the six-plate model: check the boundary and the rate together, and revise the boundary rather than discarding the new profile`
- 中文对照：勒皮雄风格，用新测印度洋磁剖面检验六大板块模型：边界与速率一起核对，对不上就改边界而不丢弃新剖面。
- Negative: `no global model from one ocean basin alone, no plate boundary without seismic and magnetic support, no freezing a global model against new data, no presenting six plates as the final count`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
