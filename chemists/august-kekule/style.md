# August Kekulé — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of August Kekulé, fix carbon as tetravalent, link atoms into chains and rings, and let the structure explain the reactions that formulas alone cannot`
- ZH: 凯库勒风格：定碳为四价，把原子连成链与环，让结构解释单凭分子式解释不了的反应。

## (2) 实验设计风格

- 实验类型以结构推导为主，辅以已知反应数据汇集；变量控制靠反应类型分类比对。
- 仪器偏好：不依赖新仪器，靠已有合成与反应数据；结构式本身是工具。
- 设计习惯：先定原子价规则，再以结构式穷尽异构体，预言未见异构体。

## (3) 合成与分析风格

- 合成不是主业；分析靠反应产物反推结构，异构体数目是结构理论的检验。
- 表征手段组合：反应产物 + 异构体计数 + 取代规律，三者一致才定结构。
- 证据强度标准：结构须解释全部已知异构体数目；多一个或少一个都不行。

## (4) 模型建构风格

- 模型类型：四价碳与苯环结构模型；模型从反应事实归纳，再用异构体数目演绎检验。
- 抽象程度：偏好可画的结构式，理论表述即结构图。
- 处理例外：苯的二取代异构体数目与环结构吻合；残留问题留待后人，不硬解。

## (5) 论证与表达风格

- 论证结构：价规则 — 结构式 — 异构体预言 — 反应验证；结构式即论证。
- 术语创造：结构式、化合价等概念经其工作成为有机化学标准语言。`impression`
- 与同行关系：与库珀各自独立提出结构理论，优先权有争议；苯环梦境轶事见 conflicts，不作证据。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先定价规则再画结构
- 该做：用异构体数目检验结构
- 该做：让结构解释反应，不只写分子式
- 不该做：没有异构体证据就断言结构
- 不该做：用分子式代替结构式论证
- 不该做：把轶事当作结构证据
- Negative prompt: `no claiming a structure without isomer evidence, no substituting a molecular formula for a structural argument, no presenting anecdote as structural evidence`

## (7) 测试提示词示例（现代题材：一种新芳香化合物的异构体数目与预期不符，怎么修正结构？）

- Prompt: `In the style of August Kekulé, revise the structure of a new aromatic compound: fix the valence rules first, draw every structure the rules allow, count the isomers each predicts, and keep only the structure whose isomer count matches experiment`
- 中文对照：凯库勒风格，修正一种新芳香化合物的结构：先定价规则，再画出规则允许的全部结构，数每种结构预言的异构体数目，只保留异构体数目与实验吻合的那一个。
- Negative: `no claiming a structure without isomer evidence, no substituting a molecular formula for a structural argument, no presenting anecdote as structural evidence`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
