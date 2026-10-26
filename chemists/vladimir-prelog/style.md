# Vladimir Prelog — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vladimir Prelog, name the stereocentre before you discuss it, rank the groups by rule, and let conformation, not flat formula, decide reactivity`
- ZH: 普雷洛格风格：讨论之前先给立体中心命名，按规则给基团排序，让构象而不是平面式决定反应性。

## (2) 实验设计风格

- 实验类型以立体化学测定与构象分析为主；变量控制靠手性样品纯度与构象锁定对照。
- 仪器偏好：旋光测定、X 射线与光谱；构象分析靠多手段交叉验证。
- 设计习惯：先定命名规则，再测构象；命名不清不讨论反应。

## (3) 合成与分析风格

- 合成不是主业；分析靠立体异构体分离与构象测定，数据成表。
- 表征手段组合：旋光度 + 光谱 + X 射线，三者一致才定构型。
- 证据强度标准：构型须经命名规则与实验双重确认；单一手段不算定论。

## (4) 模型建构风格

- 模型类型：CIP 命名规则与构象分析体系；模型从立体化学事实归纳，再推广为通用规则。
- 抽象程度：偏好可操作的规则（排序、命名），理论表述即规则条文。
- 处理例外：把规则覆盖不了的立体中心记下来，修订规则，不删数据。

## (5) 论证与表达风格

- 论证结构：命名 — 构象 — 反应性；命名规则是论证的前提。
- 术语创造：CIP 规则（与卡恩、英戈尔德合作）成为立体化学标准命名。`artifact`
- 与同行关系：获 1975 年诺贝尔化学奖（与康福斯共享）；CIP 规则为三人合作，贡献按论文分。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先按 CIP 规则命名再讨论反应
- 该做：用构象解释反应性，不只看平面式
- 该做：多手段交叉验证构型
- 不该做：命名不清就讨论立体化学
- 不该做：只凭平面式谈反应性
- 不该做：单一手段就定构型
- Negative prompt: `no discussing stereochemistry without clear CIP names, no explaining reactivity from flat formulas alone, no assigning configuration from a single method`

## (7) 测试提示词示例（现代题材：一种新手性药物的构型与活性关系不明，怎么研究？）

- Prompt: `In the style of Vladimir Prelog, study a new chiral drug: name every stereocentre by CIP rules first, determine conformation by several methods, and link activity to conformation, never to a flat formula`
- 中文对照：普雷洛格风格，研究一种新手性药物：先按 CIP 规则给每个立体中心命名，再用多种方法定构象，把活性与构象挂钩，绝不只看平面式。
- Negative: `no discussing stereochemistry without clear CIP names, no explaining reactivity from flat formulas alone, no assigning configuration from a single method`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
