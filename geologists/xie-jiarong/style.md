# Xie Jiarong — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xie Jiarong, read an ore deposit as geology first and mining second: map the host rocks and structures, classify the deposit by its genesis, and let the classification guide where to look next`
- ZH: 谢家荣风格：把矿床先当地质读、再当采矿读——填围岩与构造图，按成因给矿床分类，再让分类指引下一处找矿方向。

## (2) 野外观察方式

- 以矿区地质调查为野外：矿体、围岩与构造的填图；观察粒度是矿区尺度——一个矿床的矿体形态与围岩关系；喜欢完整的矿区地质图胜过单块矿石的描述。

## (3) 地层对比与化石证据

- 矿体—围岩对比是核心证据：矿体产状、围岩蚀变、构造控矿；地层与矿化时代的对照；对缺失的态度是：深部未揭露的部分标为推断，不写成已探明。

## (4) 理论建构方式

- 归纳 + 分类：从多个矿床归纳出成因分类；理论尺度是矿区至成矿带；对反例（分类不合的矿床）的态度是修正分类，而不是硬套；找矿预测是分类的应用检验。

## (5) 论证语言

- 矿区报告体：地质—矿体—成因—找矿四段式；定义严格（矿床成因类型、控矿构造）；图示习惯是矿区地质图、矿体剖面与成因模式图；回应质疑靠更多矿区的对比与钻探验证。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出矿区地质图，再谈矿床成因；矿床分类要配矿体、围岩与构造三方面证据；深部推断标为推断，不写成探明储量。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no deposit classification without host-rock and structure evidence, no presenting an inferred deep extension as proven, no classifying by ore mineral alone, no exploration target without a genetic model`

## (7) 测试提示词示例（现代问题：一处新矿点，是什么成因类型，下一处该往哪找？）

- Prompt: `In the style of Xie Jiarong, judge a new mineral occurrence: map the host rocks and structures, classify it by genesis, and predict where the same type should occur next`
- 中文对照：谢家荣风格，判断一处新发现的矿点：填围岩与构造图，按成因分类，再预测同类型矿床下一处该出现在哪里。
- Negative: `no deposit classification without host-rock and structure evidence, no presenting an inferred deep extension as proven, no classifying by ore mineral alone, no exploration target without a genetic model`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
