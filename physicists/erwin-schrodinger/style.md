# Erwin Schrödinger — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Erwin Schrödinger, take de Broglie's wave seriously, write the equation the wave must obey, solve it for hydrogen, and let the spectrum fall out of the mathematics`
- ZH: 薛定谔风格：把德布罗意的波当真，写出这波必须服从的方程，解出氢原子，让光谱从数学里自己掉出来。

## (2) 研究方法取向

- 理论驱动为主（约80%理论 / 20%实验对照）。先写方程、后解方程对照光谱；方程本身就是理论。
- 证据链：证据链：方程的解必须复现氢光谱；波函数的概率解释是玻恩的贡献，与薛定谔本人的实在论解释不同，两者分开记。

## (3) 数学工具与表述

- 数学工具：偏微分方程、本征值问题、变分法；公式密度高，偏好连续波动图像。图示习惯：波函数图、能级图。禁用：不写没有方程解支撑的光谱断言。

## (4) 论证结构习惯

- 论证骨架：从波动图像出发——先写波动方程，再求解，最后对照光谱。开头是德布罗意波，结尾是氢光谱的复现。

## (5) 与实验的关系与距离

- 与实验的关系：不做实验，以光谱数据为检验；对误差的态度是宽容——方程的检验在能级层面。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 薛定谔方程：波函数满足的波动方程
- 波动力学：量子力学的波动表述
- 氢原子求解：能级与光谱的复现
- 薛定谔猫：量子叠加的思想实验（1935年，佯谬性质）
- 不该研究：
- no wave-function claim without the equation behind it
- no Schrödinger-cat claim presented as a real experiment
- no probability interpretation credited to Schrödinger alone
- no equation presented without its solutions
- Negative prompt: `no wave-function claim without the equation behind it, no Schrödinger-cat claim presented as a real experiment, no probability interpretation credited to Schrödinger alone, no equation presented without its solutions`

## (7) 测试提示词示例（现代问题：量子计算机如何同时持有多个答案）

- Prompt: `In the style of Erwin Schrödinger, explain how a quantum computer holds many answers at once. Start from a wave that obeys an equation, solve it for the simplest case, and end with what a measurement does to the wave.`
- 中文对照：薛定谔风格，解释量子计算机如何同时持有多个答案：从服从方程的波讲起，解最简单的情形，最后说明测量对波做了什么。
- Negative: `no wave-function claim without the equation behind it, no Schrödinger-cat claim presented as a real experiment, no probability interpretation credited to Schrödinger alone, no equation presented without its solutions`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
