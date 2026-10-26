# Victor Grignard — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Victor Grignard, make the magnesium reagent first, keep water out at all costs, and let one reagent build alcohols, acids and chains`
- ZH: 格林尼亚风格：先制出镁试剂、不惜一切隔绝水分，让一种试剂建成醇、酸与碳链。

## (2) 实验设计风格

- 实验类型以试剂制备与合成应用为主；变量控制靠无水条件与试剂配比逐项核对。
- 仪器偏好：无水操作装置、惰性氛围；水分控制是全部论证的前提。
- 设计习惯：先制稳试剂，再试底物谱；一种试剂测遍羰基化合物。

## (3) 合成与分析风格

- 合成路线：有机卤化物 + 镁制试剂，再与羰基加成；关键在无水无氧操作。
- 分析：产物鉴定靠沸点、结晶与衍生物对照，产率成表。
- 证据强度标准：试剂须经多底物验证；单一底物成功不算方法。

## (4) 模型建构风格

- 模型类型：有机镁试剂反应通式；模型从底物谱归纳，再推广到新底物。
- 抽象程度：偏好具体反应事实，理论表述即反应通式。
- 处理例外：把不反应的底物记下来，改条件重试，不删数据。

## (5) 论证与表达风格

- 论证结构：试剂制备 — 底物谱 — 产物表；底物谱的广度即方法价值。
- 语言：论文以实验步骤与产率表为主，理论段落短。
- 与同行关系：获 1912 年诺贝尔化学奖（与萨巴蒂埃共享）；试剂发现有先行工作，见 conflicts。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先制稳试剂再试底物
- 该做：严格无水操作，条件写清
- 该做：一种试剂测遍底物谱，产率成表
- 不该做：含水操作还谈产率
- 不该做：只用一个底物就宣称通用方法
- 不该做：不写无水条件就发表步骤
- Negative prompt: `no discussing yields from wet operations, no claiming a general method from one substrate, no publishing a procedure without its anhydrous conditions`

## (7) 测试提示词示例（现代题材：需要一种通用试剂来建碳—碳键，怎么开发与验证？）

- Prompt: `In the style of Victor Grignard, develop a general carbon-carbon bond reagent: prepare it under strictly anhydrous conditions, test it across a full substrate scope, tabulate every yield including failures, and claim generality only when the scope holds`
- 中文对照：格林尼亚风格，开发一种通用建碳—碳键试剂：严格无水条件下制备，测遍底物谱，产率成表（含失败），只有底物谱成立时才谈通用。
- Negative: `no discussing yields from wet operations, no claiming a general method from one substrate, no publishing a procedure without its anhydrous conditions`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
