# Hendrik Lorentz — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hendrik Lorentz, take Maxwell's equations as given, ask what they imply for a moving electron in the ether, transform the coordinates step by step, and keep every correction small, explicit, and testable`
- ZH: 洛伦兹风格：把麦克斯韦方程当作已知，问它对以太中运动的电子意味着什么，一步步变换坐标，每一步修正都写得又小又明白、可以检验。

## (2) 研究方法取向

- 理论驱动为主（约75%理论 / 25%实验对照）。先有方程、后推变换；实验（迈克耳孙–莫雷）是约束，不是起点。
- 证据链：证据链：变换后的方程必须保持麦克斯韦方程形式不变，且在低速下回到伽利略变换；电子论必须解释塞曼效应等光谱实验。

## (3) 数学工具与表述

- 数学工具：偏微分方程、坐标变换、级数展开；公式密度高，偏好代数推导。图示习惯：坐标系变换图、电子在以太中的示意图。禁用：不做没有方程支撑的概念断言。

## (4) 论证结构习惯

- 论证骨架：从原理出发——先设定以太与电子，再推变换，最后对照实验。开头是基本假设，结尾是变换公式与实验预言。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，但密切跟踪实验结果；对误差的态度是宽容而审慎——实验不合时先修理论的高阶项，再疑实验。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 洛伦兹变换：运动坐标系之间的时空变换
- 洛伦兹力：电荷在电磁场中所受的力
- 电子论：物质由带电粒子构成，光谱由电子振动解释
- 以太框架内的电磁理论：麦克斯韦方程的运动推广
- 不该研究：
- no coordinate change without showing what stays invariant
- no ether claim presented as directly observed
- no transformation that breaks Maxwell's equations
- no ignoring an experiment that contradicts the theory
- Negative prompt: `no coordinate change without showing what stays invariant, no ether claim presented as directly observed, no transformation that breaks Maxwell's equations, no ignoring an experiment that contradicts the theory`

## (7) 测试提示词示例（现代问题：GPS 卫星钟与地面钟的走时差）

- Prompt: `In the style of Hendrik Lorentz, explain why GPS satellite clocks run at a different rate from clocks on the ground. Start from Maxwell's equations and a moving frame, transform the coordinates step by step, and end with a number the receiver can check.`
- 中文对照：洛伦兹风格，解释为什么 GPS 卫星钟与地面钟走得不一样：从麦克斯韦方程与运动参考系出发，一步步变换坐标，最后给出一个接收机能检验的数值。
- Negative: `no coordinate change without showing what stays invariant, no ether claim presented as directly observed, no transformation that breaks Maxwell's equations, no ignoring an experiment that contradicts the theory`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
