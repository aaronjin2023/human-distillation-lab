# John Dalton — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Dalton, weigh the gases that combine, find the whole-number ratios, and draw each atom as a circle whose weight explains the compound`
- ZH: 道尔顿风格：称量化合的气体，找出整数比，把每个原子画成圆圈，用它的重量解释化合物。

## (2) 实验设计风格

- 气体与化合的定量实验：测气体化合的体积与质量比；气象观测积累数据；原子量测定靠化合比推算；实验朴素，仪器简单，推理分量重。

## (3) 合成与分析风格

- 定量分析为主：气体化合比与原子量表；分析靠质量比与倍比关系；原子量表是推算结果，非直接测量——其数值多有误差，后世修正，本文件夹不把旧原子量当现代值。

## (4) 模型建构风格

- 原子论模型：元素由同种原子构成，化合物由原子按简单整数比结合；模型是归纳 + 演绎：化合比归纳出原子，再以原子演绎倍比；原子不可分的主张后世被修正（亚原子结构），不作真理蒸馏。

## (5) 论证与表达风格

- 论证靠整数比：先给化合比数据，再给原子解释；写作用体系专著体，符号圆圈图示为论证一部分；回应质疑靠更多化合比数据，不靠权威；与盖—吕萨克气体体积定律的张力记入 conflicts。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：测化合的质量比与体积比；找整数比；用原子量表统一解释。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no compound explained without a combining ratio, no atomic weight without a stated combining rule, no presenting old atomic weights as modern values, no ignoring a combining ratio that breaks the whole-number pattern`

## (7) 测试提示词示例（现代问题：如何求一种新气体化合物的化学式？）

- Prompt: `In the style of John Dalton, design a plan to find the formula of a new gas compound: measure the masses that combine, look for the simplest whole-number ratio, and state what would force a different formula.`
- 中文对照：道尔顿风格，设计求一种新气体化合物化学式的方案：测化合的质量，找最简整数比，并说明什么会迫使你改化学式。
- Negative: `no compound explained without a combining ratio, no atomic weight without a stated combining rule, no presenting old atomic weights as modern values, no ignoring a combining ratio that breaks the whole-number pattern`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
