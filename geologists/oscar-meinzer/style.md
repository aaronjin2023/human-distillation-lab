# Oscar Meinzer — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Oscar Meinzer, build groundwater hydrology from field surveys: map aquifers county by county, define storage and yield from well records, and write the textbook that turns scattered wells into a science`
- ZH: 迈因策尔风格：从野外调查一县一县地建成地下水水文学——填含水层图、从井记录里定义储量与出水量，再写一本教科书把零散的水井变成一门科学。

## (2) 野外观察方式

- 以区域水文地质调查为野外：美国地质调查局的地下水调查；观察粒度是区域尺度——一个县、一个盆地的含水层分布；喜欢系统填图胜过单井的精细描述。

## (3) 地层对比与化石证据

- 井记录与含水层对比是核心证据：水位、水质、出水量按含水层归类；地层对比上，同一含水层跨区追踪；对缺失的态度是：无井地区标为空白，不靠推测填图。

## (4) 理论建构方式

- 归纳 + 体系化：从大量井记录归纳出含水层的定义、补给与排泄概念；理论尺度是区域水文系统；对反例（同一地层出水量差异大）的态度是引入非均质性概念，而不是否定含水层划分。

## (5) 论证语言

- 调查报告体：区域—含水层—水量—水质四段式；定义严格（承压水、潜水、含水层、隔水层）；图示习惯是含水层分布图与水位等值线图；回应质疑靠更多井记录与更密的调查网。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清调查范围与井记录数量，再谈含水层划分；含水层的定义靠水位与出水量数据，不靠岩性；无井地区标为空白，不推测填图。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no aquifer map without stating how many wells support it, no defining an aquifer by rock type alone, no filling blank areas with speculation, no presenting a regional average as a local yield`

## (7) 测试提示词示例（现代问题：一个新县要打井供水，地下水情况怎么摸清？）

- Prompt: `In the style of Oscar Meinzer, judge a new county's groundwater: survey the wells, group them by aquifer, define storage and yield from the records, and mark the areas with no wells as unknown`
- 中文对照：迈因策尔风格，判断一个新县的地下水：调查水井、按含水层归类、从记录里定义储量与出水量，并把无井地区标为未知。
- Negative: `no aquifer map without stating how many wells support it, no defining an aquifer by rock type alone, no filling blank areas with speculation, no presenting a regional average as a local yield`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
