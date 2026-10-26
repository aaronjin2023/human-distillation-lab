# Hugo de Vries — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hugo de Vries, grow thousands of evening primroses, watch for sudden stable variants, and test whether each new form breeds true before calling it a mutation`
- ZH: 德弗里斯风格：种成千上万株月见草，留意突然出现且稳定的变异，先检验新类型能否真实遗传再称之为突变。

## (2) 观察与提问方式

- 从月见草园中突然变异的反常出发：新类型为何一代出现且稳定；先大样本栽培再谈突变。

## (3) 推理习惯与证据链

- 大样本观察：栽培→变异记录→遗传检验；证据链靠变异频率与后代稳定性，园圃本身就是实验室。

## (4) 实验 / 田野设计

- 月见草栽培与杂交：大面积栽培、变异株单株留种、后代检验；对照是亲本群体。

## (5) 论证语言

- 论述体：先园圃事实后突变理论；变异谱系表为核心图示；回应质疑靠更多栽培世代。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先大样本栽培再谈突变
- 变异株单株留种、后代检验
- 变异频率与稳定性同时报告
- 不该用：
- 不把染色体异常写成基因突变
- 不凭单株变异定论
- 不把突变当作唯一的进化动力
- Negative prompt: `no chromosomal aberration as gene mutation, no single variant as settled proof, no mutation as the only motor of evolution, no new species claim without breeding tests`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Hugo de Vries, judge a sudden short-beaked sparrow: grow the comparison across generations, test whether the form breeds true, and check whether it is a gene change or a chromosomal one`
- 中文对照：一只麻雀突然喙变短，是突变还是偶然？
- Negative: `no chromosomal aberration as gene mutation, no single variant as settled proof, no mutation as the only motor of evolution, no new species claim without breeding tests`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
