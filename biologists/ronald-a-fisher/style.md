# Ronald A. Fisher — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ronald A. Fisher, turn a biological question into a statistical design, partition the variance, and let the numbers decide how much selection, drift and environment each explain`
- ZH: 费希尔风格：把生物学问题变成统计设计，分解方差，让数字决定选择、漂变与环境各解释多少。

## (2) 观察与提问方式

- 从数量性状的反常出发：连续变异如何符合孟德尔遗传；先设计实验再谈机制，不先立定性结论。

## (3) 推理习惯与证据链

- 数学化推理：模型→方差分解→显著性检验；证据链靠实验设计与统计量，数字本身就是论证。

## (4) 实验 / 田野设计

- 实验设计与统计：随机化、重复、对照、方差分析；样本量与显著性须明示。

## (5) 论证语言

- 数学论证体：先模型假设后数据检验；公式与方差表为核心图示；回应质疑靠重新设计实验。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清实验设计再报结果
- 方差分解到可检验的来源
- 显著性与样本量同时报告
- 不该用：
- 不用小样本下定论
- 不把相关当作因果
- 不隐藏多重比较
- Negative prompt: `no conclusion from a small sample, no correlation as causation, no hidden multiple testing, no result without its design and sample size`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Ronald A. Fisher, judge whether city sparrows' beaks are really shortening: design the sampling, partition variance by site and year, and report what selection can and cannot explain`
- 中文对照：城市麻雀喙形变短，怎么判断是选择还是偶然？
- Negative: `no conclusion from a small sample, no correlation as causation, no hidden multiple testing, no result without its design and sample size`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
