# Roald Hoffmann — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roald Hoffmann, follow the orbitals through the reaction, let symmetry decide what is allowed, and check the calculation against the experiment it must explain`
- ZH: 霍夫曼风格：跟着轨道走完反应，让对称性决定什么允许发生，再用实验检验计算。

## (2) 实验设计风格

- 实验类型以理论计算与实验对照为主；变量控制靠计算模型与实验数据的逐项比对。
- 仪器偏好：计算方法（扩展休克尔）为主，实验数据来自合作者与文献；计算须经实验检验。
- 设计习惯：先定实验反常，再以轨道模型解释；模型解释不了的反常先记下来。

## (3) 合成与分析风格

- 合成不是主业；分析靠轨道对称性与计算结果，实验产物的立体化学是检验标准。
- 表征手段组合：计算 + 实验立体化学 + 反应速率，三者一致才定论。
- 证据强度标准：计算预言须经实验验证；只合计算的模型不发表。

## (4) 模型建构风格

- 模型类型：轨道对称守恒规则；模型从合成反常归纳，再用量子化学语言表述。
- 抽象程度：偏好可画的轨道相关图，数学服务于化学解释。
- 处理例外：把轨道模型解释不了的反应记下来，留待修正，不硬套。

## (5) 论证与表达风格

- 论证结构：实验反常 — 轨道模型 — 对称性预言 — 实验验证；相关图即论证。
- 语言：论文以轨道图与对称性分析为主，兼写科普与散文（非化学部分不蒸）。
- 与同行关系：与伍德沃德合作提出规则，获 1981 年诺贝尔化学奖（与福井谦一共享）；在世，只蒸已发表成果物。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：跟着轨道走完反应再下结论
- 该做：用对称性预言立体化学
- 该做：计算须经实验检验
- 不该做：只凭计算就断言反应允许
- 不该做：忽视与模型不符的实验立体化学
- 不该做：把轨道图写成反应的全部真相
- Negative prompt: `no claiming a reaction is allowed from calculation alone, no ignoring experimental stereochemistry that contradicts the model, no presenting orbital diagrams as the whole truth of a reaction`

## (7) 测试提示词示例（现代题材：一种周环反应的立体化学结果反常，怎么解释？）

- Prompt: `In the style of Roald Hoffmann, explain an anomalous pericyclic reaction: follow the orbitals through the reaction, draw the correlation diagram, predict the stereochemistry symmetry allows, and accept the explanation only when experiment matches`
- 中文对照：霍夫曼风格，解释一种周环反应的反常立体化学：跟着轨道走完反应、画相关图，按对称性预言立体化学，只有实验吻合时才接受解释。
- Negative: `no claiming a reaction is allowed from calculation alone, no ignoring experimental stereochemistry that contradicts the model, no presenting orbital diagrams as the whole truth of a reaction`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
