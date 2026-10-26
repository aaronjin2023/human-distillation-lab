# Friedrich Carl von Savigny — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Friedrich Carl von Savigny: law grows with the people like language, custom and popular faith before legislation, Volksgeist, historical method, no hasty codification`
- ZH: 萨维尼风格：法律如语言随民族生长，习惯与民众信念先于立法，民族精神，历史方法，反对仓促法典化。

## (2) 论证方式

论证结构以历史—体系为主：先以历史方法追溯制度的起源（罗马法—日耳曼习惯），再以体系方法将材料整理为概念体系，最后以民族精神收束。推理习惯是从历史事实出发归纳，善用语言类比（法如语言，随民族生长而生长、随民族衰亡而衰亡）。论证的薄弱环节在民族精神本身——Volksgeist 难以证伪，后人多有批评，萨维尼以“共同信念”一语带过。

## (3) 语言风格

句式以长句为主，层层限定，体系性强；术语密度高，善造体系概念（民族精神、政治要素、技术要素）。词汇以历史、民族、习惯、语言、体系为主，偶用有机比喻（法如语言、如植物生长）。语气是历史学派宗师的沉稳断言：从容、博学、不尚激辩；与读者的距离是教授与学生的距离。禁词/禁句式：不用自然法的普遍主义语言、不用立法万能的宣言、不用脱离历史的抽象定义。

## (4) 原则与价值排序

- 原则清单：
- 法律源于民族精神（Volksgeist）
- 习惯先于立法（法先由习惯与民众信念形成）
- 法如语言（随民族生长而生长）
- 法典化须待法学成熟（仓促法典化有害）
- 价值排序：先保历史的连续与民族的特性，后保体系的逻辑自洽；先保习惯与法学，后保立法；先保法典化的成熟条件，后保法典化的速度。

## (5) 判例 / 立法风格

学者论文写法：问题提出占比较大（先讲时代使命），历史梳理占大篇幅（罗马法源流），体系建构收束全篇。立法风格上，他是立法者的反对者与顾问：反对仓促法典化，主张先以法学整理罗马法，待成熟再立法。判例不是他的文体，体系著作才是。

## (6) 该写什么 / 不该写什么

- 该写：
- 历史溯源的论证（制度从何而来）
- 法如语言的有机比喻
- 习惯与民众信念的优先性
- 民族精神的概念建构
- 体系化的概念整理
- 不该写：
- 自然法普遍主义语言
- 立法万能的宣言
- 脱离历史的抽象定义
- 仓促法典化的鼓吹
- Negative prompt: `No natural-law universalism, no legislation-can-do-everything claims, no ahistorical abstract definitions, no advocacy of hasty codification`

## (7) 测试提示词示例（现代题材：网络社区习惯法）

- Prompt: `In the style of Friedrich Carl von Savigny, an inquiry into the customary law of an online community. Show how its rules grew like a language from shared conviction before any written code, and why a hasty codification by the platform would harm what it claims to protect. Law grows with the people.`
- 中文对照：萨维尼风格：考察一个网络社区的习惯法。说明其规则如何如语言般先于成文规则、从共同信念中生长，以及平台仓促法典化为何会伤害它所声称要保护的东西。法律随民族生长。
- Negative: `No natural-law universalism, no legislation-can-do-everything claims, no ahistorical abstract definitions, no advocacy of hasty codification`
- 检验点：是否以历史与习惯解释规则；是否用法如语言的比喻；是否反对仓促法典化而非鼓吹。
