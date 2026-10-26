# Lucien Febvre — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lucien Febvre, refuse the single cause: take one region through its long history, weigh every possibility the land offered, and show how people chose among them`
- ZH: 费弗尔风格：拒绝单一原因——带一个区域走过它的长历史，权衡土地提供的每种可能，说明人们如何在其中选择。

## (2) 考察方法

- 田野方式：以历史文献与区域档案为田野：地方史、档案、地图的长时段梳理；最依赖长时段的文献对照。
- 证据偏好：历史文献为主：地方志、档案、旧地图；野外观察为辅；几乎不用单一时点的证据，结论必有长时段。
- 尺度偏好：以区域为基本尺度，论证上收至人地关系的一般理论；尺度转换靠“长时段”——同一区域的不同时代叠加即演进。

## (3) 制图与空间表达

- 历史地图对比为主：同一区域不同时代的地图并置；符号是时代标记；地图是演进的证据。

## (4) 理论建构习惯

- 论述结构：区域长时段梳理 → 可能性列举 → 选择机制分析 → 可能论命题。核心概念：可能论、长时段、选择、历史地理、环境。概念衔接：环境提供可能，历史呈现选择，选择累积成区域。论证落点：理论命题——可能论。

## (5) 空间观与时间观

- 空间观：可能空间——空间是一组可能性，不是决定因素。时间观：长时段——以百年计的演进。人地关系：可能论——环境设限，人选择。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 区域的长时段历史梳理
- 环境可能性的列举与权衡
- 人类选择的机制分析
- 可能论的论证
- 不该研究：no single-cause explanation of a region, no judging a past choice by present conditions, no determinism dressed as history, no region described at one moment only
- Negative prompt: `no single-cause explanation of a region, no judging a past choice by present conditions, no determinism dressed as history, no region described at one moment only`

## (7) 测试提示词示例（现代题材：一座新城区的土地提供了哪些可能，人们在历史上如何选择？）

- Prompt: `In the style of Lucien Febvre, survey a new city district through its long history: weigh every possibility the land offered, and show how people chose among them`
- 中文对照：费弗尔风格，带一座新城区走过它的长历史：权衡土地提供的每种可能，说明人们如何选择。
- Negative: `no single-cause explanation of a region, no judging a past choice by present conditions, no determinism dressed as history, no region described at one moment only`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
