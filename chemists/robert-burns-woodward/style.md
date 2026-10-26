# Robert Burns Woodward — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Burns Woodward, plan the whole synthesis before making the first bond, characterise every intermediate, and let stereochemistry rule the route`
- ZH: 伍德沃德风格：动第一根键之前先规划整条路线，每个中间体都表征，让立体化学统治路线。

## (2) 实验设计风格

- 实验类型以长路线全合成为主；变量控制靠路线分段验证与中间体表征，逐段推进。
- 仪器偏好：常规合成、色谱分离与光谱鉴定；新方法随路线需要而开发。
- 设计习惯：先画完整逆合成路线，再分段执行；一段不通即回头改路线，不硬推。

## (3) 合成与分析风格

- 合成路线：收敛式长路线，B12 合成近百步、与埃舍莫泽合作；关键在立体化学控制。
- 分析：中间体逐个表征（光谱、结晶），产物与天然产物对照。
- 证据强度标准：每步产率与结构须写清；跳过表征的步骤不进入路线。

## (4) 模型建构风格

- 模型类型：伍德沃德—霍夫曼规则（轨道对称）；模型从合成中的立体化学反常归纳。
- 抽象程度：偏好具体合成事实，理论由合成问题倒逼出来。
- 处理例外：把电环化反常先记下来，再以轨道对称解释，不改数据迁就旧规则。

## (5) 论证与表达风格

- 论证结构：目标 — 逆合成 — 分段执行 — 表征 — 机理；路线图即论证。
- 语言：论文以路线图与实验步骤为主，立体化学表述极严密。
- 与同行关系：获 1965 年诺贝尔化学奖；与霍夫曼合作提出规则，霍夫曼 1981 年因此获奖时伍德沃德已去世。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先画完整逆合成路线再动手
- 该做：中间体逐个表征，不跳步
- 该做：让立体化学决定路线选择
- 不该做：没有路线图就开始合成
- 不该做：跳过中间体表征推进下一步
- 不该做：为路线简短牺牲立体化学严密
- Negative prompt: `no starting a synthesis without a full retrosynthetic plan, no advancing past an uncharacterised intermediate, no sacrificing stereochemical rigour for a shorter route`

## (7) 测试提示词示例（现代题材：一种结构极复杂的新药，怎么规划全合成？）

- Prompt: `In the style of Robert Burns Woodward, plan a total synthesis of a complex new drug: draw the full retrosynthetic route first, divide it into characterised segments, let stereochemistry choose each disconnection, and advance only when every intermediate is proven`
- 中文对照：伍德沃德风格，规划一种复杂新药的全合成：先画完整逆合成路线，分段执行、每段表征，让立体化学决定每处断键，只有每个中间体都证实了才推进。
- Negative: `no starting a synthesis without a full retrosynthetic plan, no advancing past an uncharacterised intermediate, no sacrificing stereochemical rigour for a shorter route`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
