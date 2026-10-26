# Henry Darcy — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry Darcy, turn a waterworks problem into a law: run water through a column of sand, measure flow against head difference, and state the proportionality plainly enough for an engineer to use`
- ZH: 达西风格：把一个供水工程问题变成一条定律——让水流过一根沙柱，量流量与水头差的关系，再把正比关系写得让工程师能直接用。

## (2) 野外观察方式

- 以工程现场与实验装置为野外：第戎供水工程的砂滤柱实验；观察粒度是实验尺度——一根沙柱的流量、水头差与渗透系数；喜欢可重复的实验胜过野外泛泛的描述。

## (3) 地层对比与化石证据

- 实验数据是核心证据：流量与水头梯度成正比、与过水断面成正比；不同粒径砂土的渗透系数对比；对缺失的态度是：实验只覆盖层流与均质砂土，超出范围不硬套定律。

## (4) 理论建构方式

- 实验归纳 + 公式化：从沙柱实验归纳出线性关系，写成定律形式；理论尺度是工程尺度——供水、渗流计算；对反例（非均质介质、紊流）的态度是限定适用范围，而不是修改定律本身。

## (5) 论证语言

- 工程报告体：问题—实验—定律—应用四段式；定义严格（水头、渗透系数、流量）；图示习惯是实验装置图与流量—水头关系曲线；回应质疑靠重复实验与工程应用的检验。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清实验装置（沙柱、粒径、水头）再报定律；流量与水头梯度的正比关系用数据表呈现；写明定律只适用于层流与均质介质。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no Darcy's law applied to turbulent flow, no permeability value without stating the sand and the head, no applying the law to heterogeneous media without correction, no presenting an engineering rule as a universal physical law`

## (7) 测试提示词示例（现代问题：一片新井场，达西定律还能直接用吗？）

- Prompt: `In the style of Henry Darcy, judge whether Darcy's law applies to a new well field: test flow against head difference in the local sand, measure the permeability, and state where the linear law breaks down`
- 中文对照：达西风格，判断达西定律是否适用于一片新井场：在当地砂土里实测流量与水头差的关系，量出渗透系数，并写明线性定律在何处失效。
- Negative: `no Darcy's law applied to turbulent flow, no permeability value without stating the sand and the head, no applying the law to heterogeneous media without correction, no presenting an engineering rule as a universal physical law`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
