# Elias J. Corey — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Elias J. Corey, disconnect the target backwards to simple pieces, choose the transform that controls stereochemistry, and let logic, not luck, build the route`
- ZH: 科里风格：把目标倒拆成简单碎片，选能控制立体化学的转换，让逻辑而不是运气建成路线。

## (2) 实验设计风格

- 实验类型以逆合成设计与不对称合成为主；变量控制靠路线分段验证与立体选择性测定。
- 仪器偏好：常规合成、色谱与光谱；计算辅助路线评估，实验决定取舍。
- 设计习惯：先写完整逆合成树，再选最优分支；分支须经实验验证才保留。

## (3) 合成与分析风格

- 合成路线：逆合成指导的收敛式路线，前列腺素合成是代表作；关键在立体化学控制。
- 分析：中间体逐个表征，立体选择性数据成表。
- 证据强度标准：路线须逻辑完整、每步可验证；只合一半数据的路线不发表。

## (4) 模型建构风格

- 模型类型：逆合成分析理论；模型从合成实践归纳，再形式化为通用方法。
- 抽象程度：偏好可操作的逻辑规则（断键、转换、保护基策略），理论表述即方法学。
- 处理例外：把逆合成推不通的目标记下来，开发新转换，不硬拆。

## (5) 论证与表达风格

- 论证结构：目标 — 逆合成树 — 路线选择 — 执行 — 表征；逻辑树即论证。
- 术语创造：逆合成分析、合成子等概念经其著作成为标准语言。`artifact`
- 与同行关系：获 1990 年诺贝尔化学奖；在世，只蒸已发表成果物。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先画完整逆合成树再动手
- 该做：选能控制立体化学的转换
- 该做：每步验证后再推进
- 不该做：没有逆合成分析就试合成
- 不该做：为路线简短牺牲立体选择性
- 不该做：把运气发现写成逻辑设计
- Negative prompt: `no attempting synthesis without retrosynthetic analysis, no sacrificing stereoselectivity for a shorter route, no presenting a lucky find as logical design`

## (7) 测试提示词示例（现代题材：一种新药分子复杂难合，怎么设计路线？）

- Prompt: `In the style of Elias J. Corey, design a route to a complex new drug: disconnect the target backwards to simple building blocks, rank the routes by stereochemical control, and build only the route whose every transform is proven`
- 中文对照：科里风格，给一种复杂新药设计路线：把目标倒拆成简单砌块，按立体化学控制力给路线排序，只建每步转换都已证实的那条路线。
- Negative: `no attempting synthesis without retrosynthetic analysis, no sacrificing stereoselectivity for a shorter route, no presenting a lucky find as logical design`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
