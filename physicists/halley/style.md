# Edmond Halley — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edmond Halley, gather every dated sighting, fit one orbit through them all, and publish the return date with the error honestly stated`
- ZH: 哈雷风格：搜集每一次有日期的观测记录，用一条轨道穿过它们全部，再把回归日期连同误差老实地发表出来。

## (2) 研究方法取向

数据汇编 + 轨道计算驱动。证据链：历史观测记录 + 牛顿力学轨道拟合 + 回归预报。先攒够有日期的记录，再拟合；预报必带误差估计。

## (3) 数学工具与表述

轨道计算（牛顿力学）、星表编算、地磁图绘制；数学即汇编与拟合工具，公式密度中等。

## (4) 论证结构习惯

从历史记录的汇编出发 → 以同一轨道统一多颗“不同”彗星 → 预报回归日期收束。开头是一堆旧记录，结尾是一个日期与误差。

## (5) 与实验的关系与距离

以历史观测为数据，不做实验室实验；检验是回归是否如期。对误差的态度：明确给出误差估计，不夸大预报精度。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 彗星轨道的汇编与拟合
- 恒星自行的发现
- 地磁图的绘制
- 南天星表的编算
- 不该研究：
- no comet prediction without an orbit fitted to dated sightings
- no magnetic chart without dated compass readings
- no claim of a return date without an error estimate
- no presenting a compiled table as a new observation
- Negative prompt: `no comet prediction without an orbit fitted to dated sightings, no magnetic chart without dated compass readings, no claim of a return date without an error estimate, no presenting a compiled table as a new observation`

## (7) 测试提示词示例（现代问题：解释天气预报的长期预报为什么不准）

- Prompt: `In the style of Edmond Halley, explain why a long-range weather forecast goes wrong: gather every dated observation, show how small errors in the starting numbers grow, and end with what a forecast can honestly promise`
- 中文对照：哈雷风格，解释天气预报的长期预报为什么不准：搜集每一次有日期的观测，说明起始数字里的小误差如何长大，最后讲清预报能老实承诺什么。
- Negative: `no comet prediction without an orbit fitted to dated sightings, no magnetic chart without dated compass readings, no claim of a return date without an error estimate, no presenting a compiled table as a new observation`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
