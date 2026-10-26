# Adolf von Baeyer — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Adolf von Baeyer, pick a natural dye, take it apart step by step, and rebuild it in the flask until synthesis proves the structure`
- ZH: 拜尔风格：挑一种天然染料，一步步拆开，再在烧瓶里重建它，直到合成证明结构。

## (2) 实验设计风格

- 实验类型以天然产物拆解与全合成为主；变量控制靠分步降解与中间体鉴定。
- 仪器偏好：常规合成、蒸馏与结晶装置；不依赖光谱，靠降解产物与合成路线双向验证。
- 设计习惯：先降解定结构，再设计合成路线；结构与合成互相印证。

## (3) 合成与分析风格

- 合成路线：线性长路线，分步推进；靛蓝合成是代表作，关键中间体逐个鉴定。
- 分析：降解产物鉴定 + 合成产物与天然产物对照，双向一致才定论。
- 证据强度标准：合成产物须与天然产物在全部可测性质上一致；中间体须逐个表征。

## (4) 模型建构风格

- 模型类型：张力理论（环大小与稳定性）；模型从环系合成难易归纳。
- 抽象程度：偏好具体合成事实，理论表述紧贴环系数据。
- 处理例外：把难成环的例子记为张力证据，不为理论整齐丢掉反例。

## (5) 论证与表达风格

- 论证结构：降解 — 结构假说 — 合成 — 对照；合成成功即结构证明。
- 语言：论文以实验步骤与产物鉴定为主，理论段落短。
- 与同行关系：获 1905 年诺贝尔化学奖；靛蓝合成的工业化由巴斯夫推进，学术与工业贡献分开记。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先降解定结构再设计合成
- 该做：中间体逐个鉴定，不跳步
- 该做：合成产物与天然产物逐项对照
- 不该做：不鉴定中间体就推进下一步
- 不该做：只凭降解就断言结构
- 不该做：把工业化成果写成学术发现
- Negative prompt: `no advancing without identifying each intermediate, no claiming a structure from degradation alone, no presenting industrial scale-up as academic discovery`

## (7) 测试提示词示例（现代题材：一种天然色素结构未知，怎么用合成证明它？）

- Prompt: `In the style of Adolf von Baeyer, prove a natural pigment's structure by synthesis: degrade it step by step to known fragments, propose a structure, rebuild it in the flask intermediate by intermediate, and claim proof only when synthetic and natural products match in every test`
- 中文对照：拜尔风格，用合成证明一种天然色素的结构：逐步降解到已知碎片、提出结构、逐个中间体在烧瓶里重建，只有合成产物与天然产物在每一项检验中都一致时，才算证明。
- Negative: `no advancing without identifying each intermediate, no claiming a structure from degradation alone, no presenting industrial scale-up as academic discovery`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
