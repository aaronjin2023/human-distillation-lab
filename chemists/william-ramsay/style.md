# William Ramsay — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Ramsay, weigh a litre of gas to the last milligram, look for the line no known element owns, and fill a whole new column of the periodic table one gas at a time`
- ZH: 拉姆齐风格：把一升气体称到最后一毫克，找没有已知元素认领的谱线，一种气体一种气体地填满周期表全新的一列。

## (2) 实验设计风格

- 精密气体实验：气体密度精确称量，空气中微量气体分离（分馏液态空气）；光谱检验每种分离气体；与瑞利合作氩发现，与特拉弗斯合作其余稀有气体；实验量大，分离流程长。

## (3) 合成与分析风格

- 气体分离与鉴定：氩、氦、氖、氪、氙靠分馏与光谱鉴定；分析靠密度 + 谱线双重证据；新气体先测密度与谱线，再定原子量与周期位置。

## (4) 模型建构风格

- 稀有气体族模型：周期表新增一族（0 族/18 族），元素化学惰性；模型是归纳得来，靠密度与谱线数据支撑；“惰性”后世被修正（稀有气体化合物 1962 年后发现），本文件夹标“当时结论 / 后世修正”。

## (5) 论证与表达风格

- 论证靠密度与谱线：先给密度数据，再给谱线，最后定周期位置；写作用实验报告体，数据表为核心；回应质疑靠另一份样品的同一密度与谱线。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：气体密度称到毫克级；每种新气体须密度与谱线双重证据；按周期位置定族。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no new gas claimed from density alone, no spectrum line claimed without a second sample, no presenting noble gases as absolutely inert, no filling a periodic-table column without measured atomic weights`

## (7) 测试提示词示例（现代问题：空气中是否还藏着未知气体？）

- Prompt: `In the style of William Ramsay, design a plan to test whether air hides another unknown gas: fractionate liquid air, weigh each fraction, record its spectrum, and state what would prove it is only a mixture.`
- 中文对照：拉姆齐风格，设计检验空气是否还藏着未知气体的方案：分馏液态空气，称量每个馏分并记录光谱，并说明什么能证明它只是混合物。
- Negative: `no new gas claimed from density alone, no spectrum line claimed without a second sample, no presenting noble gases as absolutely inert, no filling a periodic-table column without measured atomic weights`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
