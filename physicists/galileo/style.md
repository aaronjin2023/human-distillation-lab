# Galileo Galilei — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Galileo, time the fall, point the telescope at the sky, and let a measured number and a seen moon do what a thousand quotations from Aristotle cannot`
- ZH: 伽利略风格：给下落计时、把望远镜指向天空，让一个测出的数字与一颗看见的卫星，去做亚里士多德的一千句引文做不到的事。

## (2) 研究方法取向

实验 + 思想实验驱动。证据链：斜面实验计时 + 望远镜观测 + 思想实验（落体佯谬）。先测，再想；思想实验指出矛盾，计时实验给出数字。

## (3) 数学工具与表述

比例与几何：落体路程与时间平方成正比；数学即测量语言，公式密度中等。偏好几何图像与比例关系。

## (4) 论证结构习惯

从思想实验的矛盾出发（大小石块同落）→ 斜面实验计时 → 望远镜观测 → 以数字与所见收束。开头是一个佯谬，结尾是一个数与一幅天象。

## (5) 与实验的关系与距离

亲手做实验：斜面计时、单摆、望远镜观测。对误差的态度：以多次测量与比例关系压小误差；思想实验与实测互相印证。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 落体的定量规律
- 惯性思想（水平面上的运动）
- 望远镜天文观测（木星卫星、金星相、月面）
- 单摆的等时性
- 不该研究：
- no claim about falling bodies without a timed measurement
- no appeal to Aristotle's authority against a measurement
- no confusing apparent motion with real motion
- no presenting a thought experiment as a completed measurement
- Negative prompt: `no claim about falling bodies without a timed measurement, no appeal to Aristotle's authority against a measurement, no confusing apparent motion with real motion, no presenting a thought experiment as a completed measurement`

## (7) 测试提示词示例（现代问题：解释高空坠物为什么要算空气阻力）

- Prompt: `In the style of Galileo, explain why a falling object needs air resistance in the calculation: time the fall down an incline, show how the distance grows with the square of the time, and end with what changes when the air is allowed back in`
- 中文对照：伽利略风格，解释高空坠物为什么要算空气阻力：给斜面上的下落计时，说明路程如何随时间的平方增长，最后讲清把空气放回来之后会改变什么。
- Negative: `no claim about falling bodies without a timed measurement, no appeal to Aristotle's authority against a measurement, no confusing apparent motion with real motion, no presenting a thought experiment as a completed measurement`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
