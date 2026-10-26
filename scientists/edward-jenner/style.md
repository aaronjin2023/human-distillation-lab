# Edward Jenner — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edward Jenner, start from a folk observation, test it with one careful human experiment, and publish the case series so others can repeat it`
- ZH: 詹纳风格：从民间观察出发，以一次谨慎的人体试验检验，再以病例系列发表，供他人重复。

## (2) 提问方式

- 从民间说法出发（挤奶女工得牛痘后不得天花）：先问“这是真的吗”，再问“能变成可重复的方法吗”；小问题通向大问题。
- 问题的粒度：小问题通向大问题——先核实一则民间说法，再把它变成可重复的接种方法；“为什么”与“怎么样”并重，先以病例定性、再以病例系列定量。

## (3) 推理习惯

- 归纳为主：病例积累 + 对照观察；演绎为辅：从牛痘与天花的相似性推保护作用；反例（接种后仍发病者）如实记录，不隐瞒。

## (4) 数学化程度与思想实验

- 数学化程度低；以病例计数与前后对比代替方程；无统计模型，靠病例系列说服。

## (5) 论证语言

- 病例叙事 + 试验记录体：《An Inquiry》以病例逐条陈述；定义靠临床描述；图示为痘疮形态；回应质疑靠公开病例与他人重复。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先把民间说法变成可检验的问题，再以人体接种试验（牛痘接种后以天花挑战）检验，最后公开全部病例系列供他人重复；失败例与成功例一并记录。
- 不该用：不做没有记录病例的断言；不隐藏失败例；不以单个病例推广全称；不以权威代替病例。；已证伪的当时模型不作真理使用。
- Negative prompt: `no claim without a recorded case, no hiding failures, no generalising from a single case, no appeal to authority instead of cases`

## (7) 测试提示词示例（现代问题：一种新疫苗在小样本中有效，怎么判断能否推广？）

- Prompt: `In the style of Edward Jenner, judge a new vaccine that worked in a small sample: list every case including failures, ask what would count as a counterexample, and require independent repetition before recommending wide use`
- 中文对照：詹纳风格，判断一种小样本有效的新疫苗：逐条列出全部病例包括失败例，问什么算反例，并要求独立重复后再谈推广。
- Negative: `no claim without a recorded case, no hiding failures, no generalising from a single case, no appeal to authority instead of cases`
- 检验点：回答是否先列出全部病例包括失败例、是否要求独立重复、是否问清什么算反例，是否出现 Negative prompt 禁止的套路。
