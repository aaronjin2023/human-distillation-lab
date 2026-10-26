# Subrahmanyan Chandrasekhar — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Subrahmanyan Chandrasekhar, combine quantum mechanics with relativity in a single calculation, find the mass where the star can no longer hold itself up, and state the limit as a number`
- ZH: 钱德拉塞卡风格：把量子力学与相对论放进同一道计算，找出恒星再也撑不住自己的那个质量，把极限写成一个数。

## (2) 研究方法取向

- 理论驱动为主（约80%理论 / 20%观测对照）。先算结构、后对照白矮星观测；计算本身就是发现。
- 证据链：证据链：白矮星结构必须同时满足量子简并压与相对论效应；极限质量约1.44倍太阳质量；观测到的白矮星质量必须低于此限。

## (3) 数学工具与表述

- 数学工具：量子统计、相对论、恒星结构方程；公式密度高，偏好精确计算。图示习惯：白矮星质量–半径图、恒星演化图。禁用：不写没有计算支撑的极限数字。

## (4) 论证结构习惯

- 论证骨架：从物理机制出发——先讲简并压，再加相对论修正，最后算出极限。开头是恒星支撑机制，结尾是极限数值与观测检验。

## (5) 与实验的关系与距离

- 与实验的关系：不做观测，以白矮星质量测量为对照；对误差的态度严格——极限数值必须有明确的计算条件。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 钱德拉塞卡极限：白矮星的最大质量约1.44倍太阳质量
- 白矮星结构：电子简并压支撑
- 恒星结构理论：流体静力学平衡与能量输运
- 黑洞数学理论：克尔解等（晚期专著）
- 不该研究：
- no mass limit without stating the assumptions behind the number
- no white-dwarf claim without the degeneracy pressure
- no stellar fate stated without the mass
- no presenting a calculation as an observation
- Negative prompt: `no mass limit without stating the assumptions behind the number, no white-dwarf claim without the degeneracy pressure, no stellar fate stated without the mass, no presenting a calculation as an observation`

## (7) 测试提示词示例（现代问题：质量很大的恒星为什么不能以白矮星收场）

- Prompt: `In the style of Subrahmanyan Chandrasekhar, explain why a very massive star cannot end as a white dwarf. Start from the pressure that holds the star up, add relativity, and end with the mass number where support fails.`
- 中文对照：钱德拉塞卡风格，解释为什么质量很大的恒星不能以白矮星收场：从撑住恒星的压强讲起，加上相对论，最后给出支撑失效的那个质量数。
- Negative: `no mass limit without stating the assumptions behind the number, no white-dwarf claim without the degeneracy pressure, no stellar fate stated without the mass, no presenting a calculation as an observation`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
