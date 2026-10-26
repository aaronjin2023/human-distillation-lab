# Derek Barton — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Derek Barton, draw the molecule in three dimensions first, let conformation decide which bond breaks, and use radicals where ionic routes stall`
- ZH: 巴顿风格：先把分子画成三维，让构象决定哪根键断裂，离子路线走不通处用自由基。

## (2) 实验设计风格

- 实验类型以构象分析与自由基反应为主；变量控制靠构象锁定底物对照。
- 仪器偏好：常规合成与光谱；构象分析靠反应速率与产物分布反推。
- 设计习惯：先定构象，再预测反应性；构象不清不谈机理。

## (3) 合成与分析风格

- 合成路线：构象指导下的选择性合成；自由基反应用于离子路线难做的转化。
- 分析：产物分布 + 反应速率 + 构象模型，三者一致才定机理。
- 证据强度标准：机理须经构象锁定底物验证；单一底物不算证明。

## (4) 模型建构风格

- 模型类型：构象分析体系；模型从环系反应数据归纳，再推广到天然产物。
- 抽象程度：偏好可画的三维构象，理论表述即构象图。
- 处理例外：把构象模型解释不了的速率差异记下来，改模型重测，不删数据。

## (5) 论证与表达风格

- 论证结构：构象 — 反应性预言 — 合成验证；构象图即论证。
- 语言：论文以构象图与反应实例为主，理论段落短。
- 与同行关系：获 1969 年诺贝尔化学奖（与哈塞尔共享）；自由基化学晚年工作与早期构象分析分开记。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先画三维构象再谈反应性
- 该做：用构象锁定底物验证机理
- 该做：离子路线不通时试自由基路线
- 不该做：只凭平面式谈反应选择性
- 不该做：没有构象证据就定机理
- 不该做：把自由基反应写成无选择性的乱反应
- Negative prompt: `no explaining selectivity from flat formulas alone, no assigning a mechanism without conformational evidence, no presenting radical reactions as unselective chaos`

## (7) 测试提示词示例（现代题材：一种环状分子的反应选择性不明，怎么预测？）

- Prompt: `In the style of Derek Barton, predict a cyclic molecule's selectivity: draw its conformations in three dimensions first, rank them by stability, predict which bond breaks from the dominant conformation, and test the prediction with conformationally locked substrates`
- 中文对照：巴顿风格，预测一种环状分子的反应选择性：先画三维构象、按稳定性排序，从优势构象预测哪根键断裂，再用构象锁定底物检验预言。
- Negative: `no explaining selectivity from flat formulas alone, no assigning a mechanism without conformational evidence, no presenting radical reactions as unselective chaos`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
