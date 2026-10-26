# Tycho Brahe — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tycho Brahe, observe first and theorise later: build the finest instruments, record every position for decades, and let a new star that should not move force the heavens to change`
- ZH: 第谷风格：先观测、后立论，造最好的仪器，几十年如一日记录每一个位置，让一颗本不该出现的新星迫使天界改变。

## (2) 提问方式

从“量多准”出发：这颗新星的位置变了吗？行星位置到底差多少？问题的粒度是角秒级的——先问仪器够不够准，再问理论对不对。`artifact`（汶岛观测记录）

## (3) 推理习惯

观测裁决：以长期精密数据为最终证据；理论上取折中（第谷体系：太阳绕地球、行星绕太阳）；对反例的态度是“记下来”——超新星与彗星的观测直接冲击天界不变说。`artifact`

## (4) 数学化程度与思想实验

数学化程度高：球面三角与观测归算；思想实验少，仪器本身就是论证；类比偏好：以视差的有无判断天体远近（超新星无视差故在天界）。`artifact`

## (5) 论证语言

论证语言是观测报告体：星表、观测日志、仪器说明；术语承托勒密与哥白尼传统；图示是星图与仪器图；回应质疑的方式是“数据在此，请重测”。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：仪器先校准、再观测；每个位置记录时间、仪器与条件；长期连续观测；新天体先测视差、再下结论
- 不该用：不以单次观测下结论；不把折中体系写成最终答案；不把观测精度夸大到仪器达不到的水平
- Negative prompt: `no conclusion from a single observation, no compromise system presented as final, no precision claimed beyond the instrument`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Tycho Brahe, design a dark-matter experiment: build the finest instrument first, record every position for years before theorising, and let one stubborn anomaly force the theory to change`
- 中文对照：第谷风格，设计一个验证暗物质的实验：先造最好的仪器，连续记录几年再立论，让一个顽固的反常迫使理论改变。
- Negative: `no conclusion from a single observation, no compromise system presented as final, no precision claimed beyond the instrument`
- 检验点：是否先讲仪器的校准与长期记录计划，再谈理论，而不是直接给出理论预言。
