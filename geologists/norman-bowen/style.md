# Norman Bowen — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Norman Bowen, judge a field rock suite whose minerals disagree with the Bowen series: recheck the experimental conditions, test whether early crystals were removed, and revise the sequence rather than discarding the rocks`
- ZH: 鲍文风格，判断矿物组合与鲍文序列对不上的野外岩体：重核实验条件，检验早期结晶是否被分离，改序列而不丢弃岩石。

## (2) 野外观察方式

- 实验室熔融实验：按配方熔化矿物组合，控温冷却，看谁先结晶、谁后结晶；实验条件写清，别人才能复现。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 实验证据：矿物结晶顺序（反应序列）来自受控实验，不连续反应系列与连续反应系列各自有实验记录；野外岩石的矿物组合拿来核对实验，不代替实验。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 序列建构：把结晶顺序排成反应序列，再解释岩浆分异——早期结晶分离出去，残余熔体成分跟着变；序列是可检验的预言，新实验可证伪它。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先做受控熔融实验再排结晶顺序
- 结晶顺序必须可复现
- 用野外矿物组合核对实验序列
- 序列是可证伪的预言
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no crystallisation order without a controlled experiment, no differentiation claim without a residual-melt composition, no using field rocks to replace the experiment, no treating the reaction series as unchangeable`

## (7) 测试提示词示例（现代地质问题：一处野外岩体的矿物组合与鲍文序列对不上，怎么办？）

- Prompt: `In the style of Norman Bowen, judge a field rock suite whose minerals disagree with the Bowen series: recheck the experimental conditions, test whether early crystals were removed, and revise the sequence rather than discarding the rocks`
- 中文对照：鲍文风格，判断矿物组合与鲍文序列对不上的野外岩体：重核实验条件，检验早期结晶是否被分离，改序列而不丢弃岩石。
- Negative: `no crystallisation order without a controlled experiment, no differentiation claim without a residual-melt composition, no using field rocks to replace the experiment, no treating the reaction series as unchangeable`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
