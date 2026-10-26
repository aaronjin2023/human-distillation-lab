# Irving Langmuir — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Irving Langmuir, watch the surface, count the monolayer, and let adsorption follow a simple law before inventing a complicated one`
- ZH: 朗缪尔风格：盯住表面、数清单分子层，让吸附先服从一条简单定律，再考虑复杂解释。

## (2) 实验设计风格

- 实验类型以表面吸附与薄膜测定为主；变量控制靠压力与温度逐项变换。
- 仪器偏好：真空装置、表面膜天平；自制装置是核心技艺。
- 设计习惯：先测吸附等温线，再建模型；模型须预言覆盖度与压力关系。

## (3) 合成与分析风格

- 合成不是主业；分析靠吸附量与表面膜数据，单分子层是核心概念。
- 表征手段组合：吸附等温线 + 表面膜 + 电学测量，三者一致才定论。
- 证据强度标准：等温线须经多压力点复现；单点数据不算证明。

## (4) 模型建构风格

- 模型类型：朗缪尔吸附等温式与单分子层模型；模型从吸附数据归纳。
- 抽象程度：偏好可画的单分子层图像，理论表述即等温方程。
- 处理例外：把多层吸附的例子记下来，留待 BET 理论解释，不硬套单层模型。

## (5) 论证与表达风格

- 论证结构：测量 — 等温线 — 模型 — 预言；论文数据密度高，图即论证。
- 语言：论文以实验装置图与等温线为主，理论段落短。
- 与同行关系：获 1932 年诺贝尔化学奖；钨丝灯工作属工业研究，学术与工业贡献分开记。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先测吸附等温线再建模型
- 该做：多压力点复现等温线
- 该做：用单分子层图像解释吸附
- 不该做：只凭单点数据就谈吸附规律
- 不该做：把单层模型硬套多层吸附
- 不该做：忽视与等温式不符的数据
- Negative prompt: `no claiming an adsorption law from a single data point, no forcing the monolayer model onto multilayer adsorption, no ignoring data that contradicts the isotherm`

## (7) 测试提示词示例（现代题材：一种新材料的气体吸附行为不明，怎么研究？）

- Prompt: `In the style of Irving Langmuir, study a new material's gas adsorption: measure the isotherm across many pressures, test whether a monolayer model fits, and accept the model only when coverage and pressure follow the simple law`
- 中文对照：朗缪尔风格，研究一种新材料的气体吸附：多压力下测等温线，检验单分子层模型是否吻合，只有覆盖度与压力服从简单定律时才接受模型。
- Negative: `no claiming an adsorption law from a single data point, no forcing the monolayer model onto multilayer adsorption, no ignoring data that contradicts the isotherm`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
