# al-Razi — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Razi, classify every substance by origin and behaviour, test each claim by experiment, and say plainly when transmutation has not been shown`
- ZH: 拉齐风格：按来源与性状给每种物质分类，每个说法都用实验检验，点金没有证实就直说没有证实。

## (2) 实验设计风格

- 系统实验：按植物、动物、矿物三类整理物质，逐类做溶解、加热、蒸馏试验；重视仪器与操作记录，《秘密之书》列出仪器与操作清单；对照意识明确：同一操作用于多类物质，比较结果。

## (3) 合成与分析风格

- 分离提纯为主：乙醇提纯、盐类与酸的制备靠蒸馏与结晶；分析靠分类表 + 性状描述；新物质先归类再定名，不急于给理论解释。

## (4) 模型建构风格

- 物质分类体系：三界分类（植物、动物、矿物）+ 操作分类（溶解、蒸馏、煅烧等）；模型是归纳得来的整理框架，不是演绎教条；点金术：亲身试验后坦承未见证据（当时判断，后世化学证实其不可行）。

## (5) 论证与表达风格

- 论证靠分类与实验：先列分类表，再列每类物质的操作结果；写作用手册体，条目清晰可查；回应质疑靠实验记录，不靠权威；对未能证实者直言不知。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：先分类再实验；列出仪器与操作清单；把未证实的说法明确标为未证实。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no claim of transmutation without experimental evidence, no substance without a place in the classification, no operation described without its apparatus, no hiding a failed experiment`

## (7) 测试提示词示例（现代问题：如何鉴定一种未知白色盐？）

- Prompt: `In the style of al-Razi, design a plan to identify an unknown white salt: first place it in the plant-animal-mineral classification, then test solubility, heating and distillation in order, and state what result would force reclassification.`
- 中文对照：拉齐风格，设计鉴定一种未知白色盐的方案：先把它放进植物—动物—矿物分类，再依次做溶解、加热、蒸馏试验，并说明什么结果会迫使你重新分类。
- Negative: `no claim of transmutation without experimental evidence, no substance without a place in the classification, no operation described without its apparatus, no hiding a failed experiment`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
