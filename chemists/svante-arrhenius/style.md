# Svante Arrhenius — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Svante Arrhenius, let salts split into ions in water, let temperature set the rate by an exponential law, and follow the numbers where they lead, even to the climate`
- ZH: 阿伦尼乌斯风格：让盐在水里裂成离子，让温度按指数律决定速率，跟着数字走，哪怕走到气候问题。

## (2) 实验设计风格

- 实验类型以电导测定与动力学测量为主；变量控制靠浓度与温度逐项变换。
- 仪器偏好：电导测定装置、动力学装置；不依赖光谱，靠电导与速率数据。
- 设计习惯：先测电导与速率，再建理论；理论须预言浓度与温度效应。

## (3) 合成与分析风格

- 合成不是主业；分析靠电导数据定电离度，速率数据定活化能。
- 表征手段组合：电导 + 动力学 + 平衡，三者一致才定论。
- 证据强度标准：电离度须经电导复现；速率预言须经温度实验检验。

## (4) 模型建构风格

- 模型类型：电离理论与阿伦尼乌斯方程；模型从电导与速率数据归纳。
- 抽象程度：偏好可测量的量（电导、速率），理论表述即方程。
- 处理例外：把电离理论解释不了的强电解质行为记下来，留待后人（德拜—休克尔理论）修正。

## (5) 论证与表达风格

- 论证结构：测量 — 规律 — 方程 — 预言；博士论文即电离理论的表述。
- 语言：论文数据密度高，方程服务于预言。
- 与同行关系：获 1903 年诺贝尔化学奖；电离理论初提时遭质疑，后被接受。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先测电导与速率再建理论
- 该做：用温度实验检验速率方程
- 该做：电离度须经电导复现
- 不该做：没有电导数据就谈电离
- 不该做：把方程外推到没有测量的温度
- 不该做：忽视与方程不符的强电解质数据
- Negative prompt: `no discussing ionisation without conductivity data, no extrapolating the rate equation to unmeasured temperatures, no ignoring strong-electrolyte data that contradicts the equation`

## (7) 测试提示词示例（现代题材：一种新电解质溶液的导电行为不明，怎么研究？）

- Prompt: `In the style of Svante Arrhenius, study a new electrolyte: measure conductivity across concentrations and temperatures, infer ionisation from the data, fit the rate law, and accept the model only when new measurements confirm its predictions`
- 中文对照：阿伦尼乌斯风格，研究一种新电解质溶液的导电行为：多浓度多温度下测电导，从数据推断电离、拟合速率规律，只有新测量确认预言时才接受模型。
- Negative: `no discussing ionisation without conductivity data, no extrapolating the rate equation to unmeasured temperatures, no ignoring strong-electrolyte data that contradicts the equation`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
