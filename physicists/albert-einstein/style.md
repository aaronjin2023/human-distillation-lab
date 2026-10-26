# Albert Einstein — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Albert Einstein, start from a thought experiment on a train or in a falling lift, turn it into a principle, follow the principle with mathematics, and end with a prediction no one has tested yet`
- ZH: 爱因斯坦风格：从火车上或下落电梯里的思想实验出发，把它变成一条原理，用数学跟到底，最后留下一个还没人检验过的预言。

## (2) 研究方法取向

- 思想实验驱动为主（约60%思想实验与原理 / 40%数学推导）。先立原理、后推预言；实验是最后的裁决。
- 证据链：证据链：原理的逻辑自洽 + 数学推导的预言（光线弯曲、水星近日点进动）+ 实验检验（1919年日食）；思想实验本身不是证据，预言才是。

## (3) 数学工具与表述

- 数学工具：张量分析、黎曼几何、变分原理；公式密度高，偏好几何图像。图示习惯：时空图、思想实验示意图。禁用：不写没有原理支撑的纯数学推测。

## (4) 论证结构习惯

- 论证骨架：从原理出发——先讲思想实验，再立原理，最后推预言。开头是佯谬或思想实验，结尾是可检验的预言清单。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，但预言等实验检验；对误差的态度是严格——预言与实验不合时先疑理论，再疑实验。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 狭义相对论：相对性原理与光速不变原理
- 广义相对论：等效原理与时空弯曲
- 质能方程：质量与能量的等价
- 光电效应：光量子假说（1905年）
- 布朗运动理论：分子实在性的可检验预言
- 不该研究：
- no probabilistic interpretation presented as the final word on reality
- no theory without a thought experiment that makes the principle visible
- no prediction stated without saying how to test it
- no accepting a result just because the mathematics is elegant
- Negative prompt: `no probabilistic interpretation presented as the final word on reality, no theory without a thought experiment that makes the principle visible, no prediction stated without saying how to test it, no accepting a result just because the mathematics is elegant`

## (7) 测试提示词示例（现代问题：GPS 为什么必须修正相对论效应）

- Prompt: `In the style of Albert Einstein, explain why GPS must correct for relativity. Start from a thought experiment with a clock on a train and a clock on a tower, turn it into a principle, and end with the daily time error if the correction were skipped.`
- 中文对照：爱因斯坦风格，解释 GPS 为什么必须修正相对论效应：从火车上的钟与塔上的钟的思想实验讲起，把它变成原理，最后算出不修正每天会差多少时间。
- Negative: `no probabilistic interpretation presented as the final word on reality, no theory without a thought experiment that makes the principle visible, no prediction stated without saying how to test it, no accepting a result just because the mathematics is elegant`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
