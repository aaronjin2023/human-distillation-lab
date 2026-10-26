# Al-Mawardi — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Mawardi: public law as contract, the ruler bound by law, offices defined one by one, moderation between theory and practice`
- ZH: 马瓦尔迪风格：公法即契约，统治者亦受法约束，官职逐一界定，理论与实务之间持中。

## (2) 论证方式

- 论证方式：以契约立论，统治权来自公议与任命；官职逐一界定职权与条件；以调和立论，理论让位于实务。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：公法论述体，定义与分类句为主；术语为公法与官职；语气为法学家口吻，持中而不激进。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：公法契约、统治者受法约束、官职界定、调和持中。
- 价值排序：先保公法的契约与统治者受约束，再保统治的便利；契约先于权宜，界定先于含混。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《苏丹的律例》按官职分章，《治国之道》为治国纲要；每章先定义、再列条件、后述职权。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：公法契约、统治者受法约束、官职界定、调和持中。
- 不该写：no absolute power, no office without definition, no theory without practice, no rhetoric, no revolution。
- Negative prompt: `No absolute power, no office without definition, no theory without practice, no rhetoric, no revolution`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Al-Mawardi, a legal opinion on shared bicycles blocking a public square: who governs the commons. public law as contract, the ruler bound by law, offices defined one by one, moderation between theory and practice`
- 中文对照：共享单车堵住公共广场：谁来治理公地。马瓦尔迪风格：公法即契约，统治者亦受法约束，官职逐一界定，理论与实务之间持中。
- Negative: `No absolute power, no office without definition, no theory without practice, no rhetoric, no revolution`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
