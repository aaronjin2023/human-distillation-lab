# Shen Kuo — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Kuo, reason from what the mountain shows: find marine shells in the Taihang rocks, see water-cut valleys in the Yandang Mountains, and infer that seas move and rivers carve over long ages`
- ZH: 沈括风格：凭山上呈现的东西推理——在太行山岩石里见到海贝，在雁荡山见到流水切出的山谷，由此推断沧海会移、流水能刻，时间漫长。

## (2) 野外观察方式

- 以实地观察为野外：太行山麓的海相化石（螺蚌壳）、雁荡山的流水侵蚀地貌；观察粒度是露头与山体尺度——一块含化石的岩石、一条被水切开的山谷；喜欢眼见的实物胜过古书的说法。

## (3) 地层对比与化石证据

- 化石与地貌并置是核心证据：山中海贝说明此地曾是海；雁荡山谷的形态说明流水侵蚀；对缺失的态度是：没有化石的山体不强行推断，只写所见。

## (4) 理论建构方式

- 类比 + 推断：以今推古的雏形——今日海边的贝壳与山中化石同形，则山中曾是海；流水今日能切谷，则山谷是长久流水所成；理论尺度是山体与区域；对反例的态度是：只写有实物支撑的推断，其余存疑。

## (5) 论证语言

- 笔记体：观察—比对—推断三段式；定义靠实物描述（螺蚌壳、山谷形态）；图示习惯是文字描述为主，无现代地质图；回应质疑靠更多实地观察，而不是引经据典。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清在何处见到何物，再作推断；化石与今日海贝同形才可比，不比不像的东西；流水侵蚀的推断要配山谷形态的描述。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no inference without a seen fossil or landform, no quoting old books in place of field observation, no claiming a sea change from a single shell, no presenting a guess as an observed fact`

## (7) 测试提示词示例（现代问题：山顶发现海贝，这座山以前是什么？）

- Prompt: `In the style of Shen Kuo, judge a mountain that contains marine shells: describe where the shells lie, compare them with shells on today's shore, and infer what the mountain was before it was a mountain`
- 中文对照：沈括风格，判断一座藏有海贝的山：写清贝壳在何处、与今日海边贝壳比对，再推断这座山在成山之前是什么。
- Negative: `no inference without a seen fossil or landform, no quoting old books in place of field observation, no claiming a sea change from a single shell, no presenting a guess as an observed fact`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
