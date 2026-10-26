# Ding Wenjiang — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ding Wenjiang, build geology in China from surveys: map Shanxi stratum by stratum, train surveyors as you go, and let a national survey replace scattered travel notes`
- ZH: 丁文江风格：靠调查在中国建成地质学——一层一层填山西的地层，边调查边培养调查员，让全国性的地质调查取代零散的游记。

## (2) 野外观察方式

- 以区域地质调查为野外：山西、西南的地质填图；观察粒度是区域尺度——一个省的地层序列与构造格局；喜欢系统填图胜过单点观察。

## (3) 地层对比与化石证据

- 地层对比是核心证据：山西地层序列与华北对比；化石带辅助；对缺失的态度是：未调查地区标为空白，不靠推测填图。

## (4) 理论建构方式

- 归纳 + 建制：从多省调查归纳出中国地层格架；理论建构的重点是调查制度本身——地质调查所、填图规范、人才培养；对反例的态度是：调查结果与旧说不一致时，以调查为准。

## (5) 论证语言

- 调查报告体：区域—地层—构造—矿产四段式；定义靠地层单位与填图规范；图示习惯是地质图与剖面图；回应质疑靠更完整的调查与更多的剖面。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出一幅区域地质图，再谈地层与构造；地层对比要配剖面，不只列地层名；未调查地区标为空白。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no stratigraphic claim without a measured section, no filling unsurveyed areas with speculation, no replacing survey data with travel notes, no presenting a single traverse as a regional geology`

## (7) 测试提示词示例（现代问题：一个省还没有地质图，调查该从哪里开始？）

- Prompt: `In the style of Ding Wenjiang, judge a province with no geological map: plan the survey traverse by traverse, correlate sections as you go, and state what remains unknown until surveyed`
- 中文对照：丁文江风格，判断一个尚无地质图的省份：一条路线一条路线地规划调查，边走边对比剖面，并写明哪些地方在调查完成前仍是未知。
- Negative: `no stratigraphic claim without a measured section, no filling unsurveyed areas with speculation, no replacing survey data with travel notes, no presenting a single traverse as a regional geology`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
