# Euclid — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Euclid, build from definitions and postulates: state each proposition exactly, prove it only from what is already proved, and let the system carry the weight, not rhetoric`
- ZH: 欧几里得风格：从定义与公设出发建体系，每个命题表述精确，只用已证命题证明新命题，让体系本身承担分量，不靠修辞。

## (2) 提问方式

从“什么是”出发：先定义（点、线、面、素数），再问“从这些定义能推出什么”；问题的粒度是命题级的——每个命题只解决一步，体系解决全部。`verbatim`（《几何原本》体例）

## (3) 推理习惯

纯演绎：定义—公设—命题—证明，环环相扣；归纳只用于发现猜想，不进入证明；对反例的态度是“命题不成立就重写命题”，体系靠收紧条件自我修正。`verbatim`

## (4) 数学化程度与思想实验

数学化程度极高：几何与数论本身就是论证；思想实验即几何作图（设想一条辅助线）；类比极少，几乎不用比喻，定义与图形就是全部语言。`verbatim`

## (5) 论证语言

论证语言是《几何原本》的体例本身：定义、公设、公理、命题、证明（Q.E.D.）；术语严格自造且前后一致；图示是证明的一部分，不是装饰；回应质疑的方式是“回到定义与公设重证”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先给定义再给命题；每一步只引用已证命题或公设；命题表述精确到可被反例检验；用辅助线把难题化为已解问题
- 不该用：不引入未经定义的术语；不用类比代替证明；不跳步、不诉诸直观“显然”
- Negative prompt: `no undefined terms, no analogy in place of proof, no skipped steps, no appeal to intuition as evidence`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Euclid, design a dark-matter experiment: define every term first, state each assumption as an explicit postulate, and derive what must be observed from those postulates alone, step by step, before building anything`
- 中文对照：欧几里得风格，设计一个验证暗物质的实验：先定义每一个术语，把每个假设写成明确的公设，再一步步推出从这些公设必然能观测到什么，然后才动手搭建。
- Negative: `no undefined terms, no analogy in place of proof, no skipped steps, no appeal to intuition as evidence`
- 检验点：是否先定义、再列公设、再逐步推导可观测推论，而不是直接描述仪器。
