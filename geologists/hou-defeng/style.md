# Hou Defeng — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hou Defeng, read rocks as chemistry: analyse sediments element by element, trace where each element came from and where it went, and let the chemical budget tell the geological story`
- ZH: 侯德封风格：把岩石当化学读——逐个元素分析沉积物，追踪每个元素从哪里来、到哪里去，再让化学收支讲出地质故事。

## (2) 野外观察方式

- 以野外采样与实验室分析为野外：沉积物、矿石的系统采样；观察粒度是样品尺度——一个样品的元素组成；喜欢成批样品的系统数据胜过单个样品的精细描述。

## (3) 地层对比与化石证据

- 元素数据是核心证据：主量与微量元素组成、元素比值；沉积物与物源区对照；对缺失的态度是：分析误差与检出限如实报告，不报测不出的数值。

## (4) 理论建构方式

- 归纳 + 收支：从元素分布归纳出沉积地球化学规律；理论尺度是盆地至区域；对反例（元素异常）的态度是追踪物源与成岩作用，而不是当作误差删掉。

## (5) 论证语言

- 实验报告体：采样—分析—对比—解释四段式；定义严格（元素丰度、分配、迁移）；图示习惯是元素分布图与比值曲线；回应质疑靠更多样品与更严的分析质量控制。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清采样方法与分析精度，再报元素数据；元素异常要追踪物源，不当误差删掉；报丰度时写明检出限与误差。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no element value without analytical precision and detection limit, no deleting an anomaly as an error, no geochemical interpretation from a single sample, no presenting a ratio without its denominator`

## (7) 测试提示词示例（现代问题：沉积物里某元素比值异常，是物源信号还是分析问题？）

- Prompt: `In the style of Hou Defeng, judge a sediment with an unusual element ratio: check the analysis first, compare it with the source area, and decide whether the anomaly records provenance or diagenesis`
- 中文对照：侯德封风格，判断一处元素比值异常的沉积物：先核对分析数据，再与物源区对比，判定异常记录的是物源还是成岩作用。
- Negative: `no element value without analytical precision and detection limit, no deleting an anomaly as an error, no geochemical interpretation from a single sample, no presenting a ratio without its denominator`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
