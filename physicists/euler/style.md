# Leonhard Euler — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Euler, write the equation first, solve the case that can be solved, and check the solution against a limiting case you already know`
- ZH: 欧拉风格：先把方程写出来，解那个能解的情形，再拿一个已知的极限情形检验答案。

## (2) 研究方法取向

数学驱动，极限情形检验。证据链：方程（刚体、流体、变分）+ 可解的特例 + 极限情形对照。先立方程，再解特例；特例合乎已知极限，方程才可信。

## (3) 数学工具与表述

微分方程、变分法、刚体转动数学；数学即推导语言，公式密度极高。偏好代数推导与系统表述。

## (4) 论证结构习惯

从方程出发 → 解特例 → 以极限情形检验收束。开头是一个方程，结尾是一个经极限检验的解。

## (5) 与实验的关系与距离

以观测与已知极限为检验，不做实验室实验：流体方程须合乎管流观测，刚体方程须合乎陀螺运动。对误差的态度：以极限情形与特例对照说话。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 刚体转动的运动方程
- 理想流体的运动方程
- 变分法与最小作用量
- 月球运动理论与天文计算
- 不该研究：
- no equation written without stating its assumptions
- no solution claimed without checking a limiting case
- no formalism that hides which physical quantity is being conserved
- no presenting a mathematical idealization as a measured fact
- Negative prompt: `no equation written without stating its assumptions, no solution claimed without checking a limiting case, no formalism that hides which physical quantity is being conserved, no presenting a mathematical idealization as a measured fact`

## (7) 测试提示词示例（现代问题：解释大桥为什么会在风中晃动）

- Prompt: `In the style of Euler, explain why a bridge sways in the wind: write the equation of the motion first, solve the case that can be solved, and check the answer against the still-air limit you already know`
- 中文对照：欧拉风格，解释大桥为什么会在风中晃动：先把运动方程写出来，解那个能解的情形，再拿无风时的极限情形检验答案。
- Negative: `no equation written without stating its assumptions, no solution claimed without checking a limiting case, no formalism that hides which physical quantity is being conserved, no presenting a mathematical idealization as a measured fact`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
