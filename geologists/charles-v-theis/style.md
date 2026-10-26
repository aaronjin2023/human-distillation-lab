# C. V. Theis — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of C. V. Theis, solve a well problem with a heat equation: borrow the mathematics of heat conduction, fit the drawdown curve to the Theis type curve, and read transmissivity and storage from the match`
- ZH: 泰斯风格：借一道热传导方程解水井问题——把降深曲线往泰斯标准曲线上一贴，从配线点读出导水系数与储水系数。

## (2) 野外观察方式

- 以抽水试验为野外：观测井的水位随时间下降；观察粒度是试验尺度——一口抽水井、几口观测井的降深—时间曲线；喜欢一条完整的降深曲线胜过单点水位。

## (3) 地层对比与化石证据

- 降深—时间数据是核心证据：抽水量恒定条件下水位下降的速率；与热传导方程的解对照；对缺失的态度是：试验时间太短、边界效应未到，曲线配不上就坦白写明，不硬配。

## (4) 理论建构方式

- 类比 + 数学化：地下水流与热传导的数学同构是理论的跳板；泰斯方程把井流写成解析解；理论尺度是含水层尺度——均质、各向同性、无限延伸的理想含水层；对反例（越流、边界）的态度是限定适用范围，后世再发展修正解。

## (5) 论证语言

- 数学论证体：假设—方程—配线—参数四段式；定义严格（导水系数、储水系数、降深）；图示习惯是降深—时间双对数曲线与标准曲线配线图；回应质疑靠更多抽水试验的配线检验。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清抽水试验条件（抽水量、观测井距离、试验时长），再配线；降深曲线与标准曲线的配线点要写明；报导水系数与储水系数时写明理想含水层的假设。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no Theis fit without stating pumping rate and test duration, no matching a curve that has not reached the required time, no applying the Theis solution to a bounded aquifer without saying so, no reporting transmissivity without the ideal-aquifer assumptions`

## (7) 测试提示词示例（现代问题：一片新含水层抽水试验，导水系数怎么算？）

- Prompt: `In the style of C. V. Theis, judge a pumping test in a new aquifer: plot drawdown against time, match it to the Theis type curve, read transmissivity and storage from the match point, and state where the ideal assumptions break down`
- 中文对照：泰斯风格，判断一片新含水层的抽水试验：把降深对时间作图，往泰斯标准曲线上配线，从配线点读导水系数与储水系数，并写明理想假设在何处失效。
- Negative: `no Theis fit without stating pumping rate and test duration, no matching a curve that has not reached the required time, no applying the Theis solution to a bounded aquifer without saying so, no reporting transmissivity without the ideal-aquifer assumptions`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
