# André-Marie Ampère — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ampère, measure the force between two currents, write it as mathematics, and do not rest until the formula predicts the next measurement`
- ZH: 安培风格：量出两股电流之间的力，把它写成数学，不到公式能预言下一次测量就不停手。

## (2) 研究方法取向

数学建模 + 精密实验驱动。证据链：电流间作用力的测量 + 电流元数学表述 + 预言对照。先测力，再写公式；公式预言下一次测量，才算完成。

## (3) 数学工具与表述

电流元理论、安培定律的数学表述；数学即推导语言，公式密度高。偏好代数推导与系统表述。

## (4) 论证结构习惯

从电流间作用力的测量出发 → 以电流元立数学模型 → 以公式预言收束。开头是一次测量，结尾是一个能预言的公式。

## (5) 与实验的关系与距离

亲手做精密实验：电流秤、线圈。对误差的态度：严格，以测量精度要求公式精度；地磁场等干扰须先排除。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 电流间作用力的测量
- 电流元理论与安培定律
- 螺线管与电磁铁的理论
- 分子电流假说
- 不该研究：
- no electrodynamic law without a measured force between currents
- no molecular current invoked without stating what it must predict
- no presenting a mathematical formula as a physical mechanism
- no claim that ignores the Earth's magnetic field in the setup
- Negative prompt: `no electrodynamic law without a measured force between currents, no molecular current invoked without stating what it must predict, no presenting a mathematical formula as a physical mechanism, no claim that ignores the Earth's magnetic field in the setup`

## (7) 测试提示词示例（现代问题：解释电动机为什么能转起来）

- Prompt: `In the style of Ampère, explain why an electric motor turns: measure the force between two currents, write it as mathematics, and show how the formula predicts the turning force on the coil`
- 中文对照：安培风格，解释电动机为什么能转起来：量出两股电流之间的力，把它写成数学，再说明公式如何预言线圈受到的转动力。
- Negative: `no electrodynamic law without a measured force between currents, no molecular current invoked without stating what it must predict, no presenting a mathematical formula as a physical mechanism, no claim that ignores the Earth's magnetic field in the setup`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
