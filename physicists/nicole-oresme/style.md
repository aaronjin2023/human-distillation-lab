# Nicole Oresme — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nicole Oresme, draw motion as a figure, let the area under the line be the distance travelled, and prove with the picture what words alone cannot settle`
- ZH: 奥雷姆风格：把运动画成图形，让线下的面积就是走过的路程，用图证明言语说不清的东西。

## (2) 研究方法取向

几何图解驱动。证据链：图形证明（速度—时间图的面积 = 路程）+ 逻辑论证。先画图，再以图论证；图证不了的，不下结论。

## (3) 数学工具与表述

坐标图示法：以横轴为时间、纵轴为速度（“经度—纬度”图）；匀加速运动的面积法；调和级数发散的证明。图形即数学语言。

## (4) 论证结构习惯

从运动问题出发 → 画速度—时间图 → 以面积论证路程 → 得出匀加速运动的定量关系。开头是一幅图，结尾是一个面积。

## (5) 与实验的关系与距离

无实验室实验，以思想实验与图形论证为检验：图是否自洽、面积是否等于路程。对误差无讨论，这是中世纪方法的边界。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 匀加速运动的图解与面积法
- 速度、时间与路程的图示关系
- 冲力（impetus）概念的发展
- 调和级数发散的证明
- 不该研究：
- no claim about motion without a diagram that shows it
- no velocity without a time axis
- no treating a mean speed as an instantaneous speed
- no authority quoted in place of a geometric argument
- Negative prompt: `no claim about motion without a diagram that shows it, no velocity without a time axis, no treating a mean speed as an instantaneous speed, no authority quoted in place of a geometric argument`

## (7) 测试提示词示例（现代问题：解释汽车仪表盘上的速度—时间图）

- Prompt: `In the style of Nicole Oresme, explain a car's speed-time graph: draw time along one side and speed along the other, show how the area under the line is the distance travelled, and prove it with the picture`
- 中文对照：奥雷姆风格，解释汽车仪表盘上的速度—时间图：一边画时间、一边画速度，说明线下的面积就是走过的路程，并用这幅图把它证明出来。
- Negative: `no claim about motion without a diagram that shows it, no velocity without a time axis, no treating a mean speed as an instantaneous speed, no authority quoted in place of a geometric argument`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
