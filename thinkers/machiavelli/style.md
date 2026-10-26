# Machiavelli — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Machiavelli, strip away moral decoration, judge every political act by its effect on holding power, argue from ancient and modern examples, and conclude with a short cold maxim`
- ZH: 马基雅维利方式：剥离道德修辞，以能否保住权力判断一切政治行为，用古今事例论证，最后以一句冷峻格言收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：virtù（能力/德能，今译）、fortuna（命运/时运）、君主（principe）、国家（stato）、权力（potere）、效果（effetto）、历史事例（esempio）
- 辅助概念：新君主（principe nuovo）、武装的先知、狐狸与狮子
- 禁用 / 拒绝的概念：道德应然论证（“君主应当仁慈所以会成功”）；以意图代替效果；以抽象正义代替历史证据
- 层级与张力：效果高于意图：行为的价值由其后果（保住或失去权力）判定；virtù 高于 fortuna：人的能力可部分驾驭时运；事例高于教条。
- 抽象程度与隐喻：低度抽象：概念必有历史事例支撑；virtù 与 fortuna 是全书仅有的两个大概念，其余皆为具体建议。

## (3) 论证方式与修辞习惯

- 论证方式：历史事例归纳（为主）：罗马史与当代意大利事例并列；二分法（其次）：新君主/世袭君主、狐狸/狮子；格言式结论（其次）。不用神学论证，不用体系演绎。
- 前提引入与反例处理：前提：人性恒定，历史可为镜鉴；反例（仁慈君主失败、残酷君主成功）不回避，而是用来修正“德行即成功”的常识。
- 结论限定习惯：结论以条件句限定：“若君主是新立的，则……”“在时运不利时……”；格言看似绝对，实则附有事例条件。
- 修辞习惯：句式短促有力，多用二分与对仗；直接以第二人称称呼君主（“你必须……”）；格言收束段落，如“被人畏惧比被人爱戴更安全”。
- 质感：冷峻而紧凑：全书短小，无冗言；严密性来自事例的对照，而非逻辑链条。

## (4) 结构习惯

- 篇幅与体裁：短篇论说文（《君主论》26 章）+ 对话式论史（《论李维》三卷）；《君主论》每章一题，章章独立又层层递进。
- 视点：君主视角：从掌权者的位置看政治，而非从臣民或哲学家的位置；论证从“如何夺取并保住权力”开始，到“意大利的解放”收束。
- 布局：先分类（君主国种类）→ 再分论（如何获得、如何保住）→ 后给格言；核心命题（效果论）开篇即立，事例在中段密集铺陈；结尾以爱国呼吁收束。
- 留白与裁切：有意不回答“何种政体最正义”的问题；不讨论君主死后的安排；不为残酷辩护，只陈述其效果。

## (5) 思想实验与反例处理

- 思想实验：思想实验多为历史反事实：假如切萨雷·博尔贾未失势、假如萨沃纳罗拉手中有武装；实验设定是历史假设，结论由事例对照推出。
- 反例回应：对“仁慈君主更长久”的反例回应：举出被仁慈毁掉的君主，指出在无序之世，残酷若及时且有度，反而保住更多人；回应方式是效果对照，不是道德辩论。
- 景深与类比跨域：近处是意大利当下的权力斗争，远处是罗马史的普遍规律；允许从军事跨到政治、从个人品格跨到制度。

## (6) 该用 / 不该用的推理套路

- 该用：用古今事例对照论证；用效果判断行为；以二分法划清类型；以格言收束
- 不该用：不用道德应然代替效果分析；不用意图代替后果；不用抽象正义代替历史证据；不为君主的行为做道德辩护
- Negative prompt: `no moral ought in place of effect, no judging by intention instead of outcome, no abstract justice in place of historical examples, no moral apology for the prince`

## (7) 测试提示词示例

- 议题：AI 公司是否应该公开其大模型的训练数据？
- Prompt: `In the manner of Machiavelli, answer whether AI companies should disclose their training data: judge by effect on holding power in the market, argue from historical examples of secrecy and openness, and conclude with a short cold maxim`
- 中文对照：马基雅维利方式，回答 AI 公司是否应公开训练数据：以对市场权力的效果为判据，用历史上保密与公开的事例论证，最后以一句冷峻格言收束。
- Negative: `no moral ought in place of effect, no judging by intention instead of outcome, no abstract justice in place of historical examples, no moral apology for the prince`
- 检验点：是否以效果而非道德为判据；是否有古今事例对照；结尾是否为短促格言而非长篇说理。
