# K. Barry Sharpless — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of K. Barry Sharpless, find a reaction that always works, make it selective with a catalyst, and let reliability, not novelty, be the standard`
- ZH: 夏普莱斯风格：找一个总能奏效的反应，用催化剂让它有选择性，让可靠而不是新奇成为标准。

## (2) 实验设计风格

- 实验类型以催化方法开发为主；变量控制靠底物谱系统筛选与对映选择性测定。
- 仪器偏好：常规合成、手性色谱与光谱；对映体过量值是核心数据。
- 设计习惯：先定反应的可靠性标准，再优化选择性；不可靠的反应不推广。

## (3) 合成与分析风格

- 合成路线：催化不对称合成，环氧化与双羟基化是代表作；关键在催化剂与底物匹配。
- 分析：产物对映选择性 + 产率成表，底物谱越广方法价值越高。
- 证据强度标准：方法须经宽底物谱验证；单一底物高选择性不算方法。

## (4) 模型建构风格

- 模型类型：点击化学标准（模块化、高产率、立体专一）；模型从反应可靠性归纳。
- 抽象程度：偏好可操作的反应标准，理论表述即标准清单。
- 处理例外：把不符合点击标准的反应排除在外，不放宽标准迁就。

## (5) 论证与表达风格

- 论证结构：反应 — 催化剂 — 底物谱 — 选择性表；底物谱的广度即论证。
- 术语创造：“点击化学”一词经其 2001 年论文成为标准概念。`artifact`
- 与同行关系：获 2001 年与 2022 年两届诺贝尔化学奖；在世，只蒸已发表成果物。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先定可靠性标准再优化选择性
- 该做：一种方法测遍底物谱，对映选择性成表
- 该做：只推广可靠、可重复的反应
- 不该做：只用一个底物就宣称通用方法
- 不该做：为新奇牺牲可靠性
- 不该做：放宽标准迁就不符合的反应
- Negative prompt: `no claiming a general method from one substrate, no sacrificing reliability for novelty, no loosening the standard to fit a reaction that fails it`

## (7) 测试提示词示例（现代题材：需要一种可靠的连接反应来组装药物分子，怎么开发？）

- Prompt: `In the style of K. Barry Sharpless, develop a reliable ligation for drug assembly: set the reliability standard first, screen catalysts across a broad substrate scope, tabulate yields and selectivity, and promote the reaction only when it works every time`
- 中文对照：夏普莱斯风格，开发一种可靠的药物组装连接反应：先定可靠性标准，再宽底物谱筛选催化剂，产率与选择性成表，只有每次都奏效时才推广。
- Negative: `no claiming a general method from one substrate, no sacrificing reliability for novelty, no loosening the standard to fit a reaction that fails it`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
