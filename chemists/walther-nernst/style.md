# Walther Nernst — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Walther Nernst, measure the potential, let it speak for the free energy, and follow entropy to absolute zero where no further change is possible`
- ZH: 能斯特风格：测电势、让它替自由能说话，跟着熵走到绝对零度——那里再无变化可言。

## (2) 实验设计风格

- 实验类型以电化学与热力学测定为主；变量控制靠温度与浓度逐项变换。
- 仪器偏好：电化学电池、量热计；电势测量精度是全部论证的基础。
- 设计习惯：先测电势与热容，再建理论；理论须预言低温行为。

## (3) 合成与分析风格

- 合成不是主业；分析靠电势数据定自由能，热容数据定熵变。
- 表征手段组合：电势 + 量热 + 平衡，三者一致才定论。
- 证据强度标准：电势数据必须可复现到毫伏级；低温外推须标明限度。

## (4) 模型建构风格

- 模型类型：能斯特方程与热力学第三定律；模型从电化学与热容数据归纳。
- 抽象程度：偏好可测量的量（电势、热容），理论表述即方程与定律。
- 处理例外：把低温热容反常记下来，留待量子理论解释，不硬套经典模型。

## (5) 论证与表达风格

- 论证结构：测量 — 方程 — 定律 — 低温预言；论文数据密度高。
- 语言：论文以电势表与热容数据为主，推导严密。
- 与同行关系：获 1920 年诺贝尔化学奖；热力学第三定律的表述版本有争议，见 conflicts。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先测电势与热容再建理论
- 该做：用电势数据定自由能
- 该做：低温外推标明限度
- 不该做：没有电势数据就谈自由能
- 不该做：把低温外推写成已验证的定论
- 不该做：忽视与定律不符的热容数据
- Negative prompt: `no discussing free energy without potential data, no presenting low-temperature extrapolation as verified fact, no ignoring heat-capacity data that contradicts the law`

## (7) 测试提示词示例（现代题材：一种新电池的电压随温度变化不明，怎么研究？）

- Prompt: `In the style of Walther Nernst, study a new battery's voltage: measure potentials across temperatures and concentrations, convert them to free energies, fit the entropy change, and predict low-temperature behaviour only with stated limits`
- 中文对照：能斯特风格，研究一种新电池电压随温度的变化：多温度多浓度下测电势、换算成自由能、拟合熵变，低温预言须标明限度。
- Negative: `no discussing free energy without potential data, no presenting low-temperature extrapolation as verified fact, no ignoring heat-capacity data that contradicts the law`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
