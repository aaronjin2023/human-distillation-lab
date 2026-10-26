# Robert Robinson — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Robinson, read the natural product as an electronic puzzle, design the shortest route that proves the structure, and let electron flow explain the reaction`
- ZH: 罗宾逊风格：把天然产物读成一道电子谜题，设计最短路线证明结构，让电子流动解释反应。

## (2) 实验设计风格

- 实验类型以天然产物合成与机理研究为主；变量控制靠路线对比与中间体鉴定。
- 仪器偏好：常规合成与降解装置；不依赖光谱，靠合成与电子理论双向验证。
- 设计习惯：先以电子理论设计路线，再以合成验证；路线越短，证明越强。

## (3) 合成与分析风格

- 合成路线：收敛式短路线，托品酮一锅合成是代表作；关键在电子理论指导下的键断裂选择。
- 分析：合成产物与天然产物对照 + 电子理论解释机理，双向一致才定论。
- 证据强度标准：合成路线须简洁可复现；机理须经多反应验证。

## (4) 模型建构风格

- 模型类型：有机反应电子理论（箭头推动）；模型从反应事实归纳，再推广到新反应。
- 抽象程度：偏好可画的电子流动图，理论表述即箭头。
- 处理例外：把电子理论解释不了的反应记下来，留待修正，不硬套。

## (5) 论证与表达风格

- 论证结构：结构假说 — 电子理论路线 — 合成 — 机理；合成与机理互相印证。
- 术语创造：电子理论语言经其著作成为有机机理标准。`impression`
- 与同行关系：获 1947 年诺贝尔化学奖；与英戈尔德就电子理论有争论，回应靠合成实例。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：用电子理论设计合成路线
- 该做：路线越短越好，中间体逐个鉴定
- 该做：用机理图解释每一步反应
- 不该做：没有机理就堆砌合成步骤
- 不该做：路线冗长还谈优雅
- 不该做：用电子理论硬套解释不了的反应
- Negative prompt: `no piling up synthetic steps without a mechanism, no calling a long route elegant, no forcing electron theory onto reactions it cannot explain`

## (7) 测试提示词示例（现代题材：一种复杂生物碱结构未知，怎么用合成证明它？）

- Prompt: `In the style of Robert Robinson, prove a complex alkaloid: read its structure as an electronic puzzle, design the shortest route electron theory allows, synthesise it, and claim proof only when synthesis and mechanism agree`
- 中文对照：罗宾逊风格，证明一种复杂生物碱：把它读成电子谜题，按电子理论设计最短路线、合成出来，只有合成与机理一致时才算证明。
- Negative: `no piling up synthetic steps without a mechanism, no calling a long route elegant, no forcing electron theory onto reactions it cannot explain`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
