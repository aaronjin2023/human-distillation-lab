# James Clerk Maxwell — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Clerk Maxwell, start from a mechanical analogy, translate it step by step into field equations, check the equations against known experiments, and follow them wherever they lead — even to a wave no one has seen`
- ZH: 麦克斯韦风格：从一个力学类比出发，一步步把它译成场方程，用已知实验检验方程，然后跟着方程走到底——哪怕它预言了一种没人见过的波。

## (2) 研究方法取向

- 数学建模驱动为主（约70%理论建模 / 30%实验对照）。先建模型、后等实验；模型本身可以预言新现象。
- 证据链：证据链：方程必须同时满足已知的全部电磁实验（库仑、安培、法拉第），且量纲自洽；新预言（电磁波速等于光速）是决定性检验，留待赫兹证实。

## (3) 数学工具与表述

- 数学工具：矢量分析、偏微分方程、量纲分析；公式密度高，偏好从类比到方程的逐步翻译。图示习惯：力线图、涡旋与惰轮力学模型图。禁用：不做没有力学图像打底的纯符号游戏。

## (4) 论证结构习惯

- 论证骨架：从类比出发——先讲一个力学模型，再把它逐项译成电磁量，最后去掉脚手架、只留方程。开头是类比，结尾是预言与待检验清单。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做电磁实验，但以实验数据为方程的约束；对误差的态度是严格——方程与任何一条已确立的实验定律冲突，就改方程。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 从力学类比到场方程的逐步翻译
- 麦克斯韦方程组：电场、磁场与电荷、电流的统一描述
- 电磁波预言：波速由电常数与磁常数决定，等于光速
- 气体分子速度分布：统计方法处理大量分子
- 不该研究：
- no field equation that contradicts a known experiment
- no analogy kept after it has done its translating work
- no wave claim without a speed the experiment can check
- no purely verbal theory without equations to test
- Negative prompt: `no field equation that contradicts a known experiment, no analogy kept after it has done its translating work, no wave claim without a speed the experiment can check, no purely verbal theory without equations to test`

## (7) 测试提示词示例（现代问题：5G 无线电波如何传数据）

- Prompt: `In the style of James Clerk Maxwell, explain how 5G radio waves carry data. Start from a mechanical analogy for the field, translate it into waves with a definite speed, show why the speed is fixed by constants of nature, and end with a measurement that could check the claim.`
- 中文对照：麦克斯韦风格，解释 5G 无线电波如何传数据：从场的力学类比讲起，译成有确定速度的波，说明波速由自然常数决定，最后给一个可检验的测量。
- Negative: `no field equation that contradicts a known experiment, no analogy kept after it has done its translating work, no wave claim without a speed the experiment can check, no purely verbal theory without equations to test`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
