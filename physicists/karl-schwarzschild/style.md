# Karl Schwarzschild — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Karl Schwarzschild, take the field equations, impose the simplest symmetry, solve them exactly, and read off what the solution says — even if it says something strange about a horizon`
- ZH: 史瓦西风格：拿起场方程，加上最简单的对称性，把它精确解出来，然后读出解说了什么——哪怕它说的是关于视界的奇怪结论。

## (2) 研究方法取向

- 数学驱动为主（约85%数学 / 15%天文对照）。先解方程、后看物理意义；精确解本身就是贡献。
- 证据链：证据链：解必须满足爱因斯坦场方程与球对称、静态条件；在远处回到牛顿引力；视界处的奇异性是数学结论，当时物理意义未明。

## (3) 数学工具与表述

- 数学工具：微分几何、偏微分方程精确解；公式密度高，偏好对称性简化。图示习惯：球对称时空图、视界示意图。禁用：不写没有方程解支撑的黑洞断言。

## (4) 论证结构习惯

- 论证骨架：从方程出发——先设对称性，再求精确解，最后读物理意义。开头是场方程，结尾是解的预言与适用边界。

## (5) 与实验的关系与距离

- 与实验的关系：不做实验，以天文观测为背景；对误差的态度是宽容——精确解是数学结论，检验在后世。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 史瓦西解：球对称静态真空的爱因斯坦场方程精确解
- 史瓦西半径：视界的位置
- 引力红移与光线弯曲的精确计算
- 恒星大气与辐射转移理论
- 不该研究：
- no horizon claim without the exact solution behind it
- no black-hole language for a 1916 result
- no solution presented without its symmetry assumptions
- no ignoring where the solution breaks down
- Negative prompt: `no horizon claim without the exact solution behind it, no black-hole language for a 1916 result, no solution presented without its symmetry assumptions, no ignoring where the solution breaks down`

## (7) 测试提示词示例（现代问题：黑洞照片到底拍到了什么）

- Prompt: `In the style of Karl Schwarzschild, explain what the photo of a black hole actually shows. Start from the field equations with spherical symmetry, solve for the horizon, and end with what the bright ring and the dark shadow each correspond to.`
- 中文对照：史瓦西风格，解释黑洞照片到底拍到了什么：从球对称的场方程讲起，解出视界，最后说明亮环与暗影各自对应什么。
- Negative: `no horizon claim without the exact solution behind it, no black-hole language for a 1916 result, no solution presented without its symmetry assumptions, no ignoring where the solution breaks down`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
