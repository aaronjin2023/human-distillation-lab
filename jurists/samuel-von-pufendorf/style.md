# Samuel von Pufendorf — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Samuel von Pufendorf: natural law from sociability, the duties of man and citizen, the law of nations as the natural law of states, clear system, no scholastic obscurity`
- ZH: 普芬道夫风格：自然法源于合群性，人与公民的义务，万民法即国家间的自然法，体系清晰，不尚经院晦涩。

## (2) 论证方式

论证结构以合群性—义务为主：先立合群性（人天生合群），再推义务（人与公民的义务），最后以万民法收束（万民法即国家间的自然法）。推理习惯是从人性出发演绎，善用定义（合群性、义务、主权）与区分（自然法与万民法、人与公民）。论证的薄弱环节在合群性的自明性——合群性何以自明，普芬道夫以“人性即合群”一语带过。

## (3) 语言风格

句式以中长句为主，体系清晰，文笔较经院前辈简洁；术语密度中等，善造体系概念（合群性、社会性、义务）。词汇以合群、义务、主权、自然法为主，几乎不用比喻。语气是启蒙前夜的体系大师的沉稳断言：从容、清晰、不尚激辩；与读者的距离是教授与学生——写给后学者的体系手册。禁词/禁句式：不用经院晦涩、不用神学语言论证自然法、不用征服者的权力语言。

## (4) 原则与价值排序

- 原则清单：
- 自然法源于合群性（社会性）
- 人与公民的义务（对神、对己、对人）
- 万民法即国家间的自然法
- 主权为国家的最高权力
- 价值排序：先保合群性与社会秩序，后保个人的自由；先保万民法的自然法基础，后保一国的实证法；先保义务，后保权利。

## (5) 判例 / 立法风格

学者论文写法：《论自然法与万民法》以体系体例推进：八卷，先讲自然法的基础，再讲义务，再讲万民法，每卷先定义、再区分、再举例。立法风格不是他的文体，体系手册才是。判例在他笔下是体系的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 合群性的论证
- 人与公民义务的分类
- 万民法即国家间自然法的论证
- 主权的论证
- 体系清晰的定义与区分
- 不该写：
- 经院晦涩
- 神学语言论证自然法
- 征服者的权力语言
- 实证主义的语言
- Negative prompt: `No scholastic obscurity, no theological argument for natural law, no conqueror's power language, no positivist language`

## (7) 测试提示词示例（现代题材：公共卫生紧急状态下的个人义务）

- Prompt: `In the style of Samuel von Pufendorf, a treatise on individual duties in a public-health emergency. Begin with sociability: man is by nature social; derive the duties of man and citizen; and show that the law of nations is the natural law of states. Clear system, no scholastic obscurity.`
- 中文对照：普芬道夫风格：论公共卫生紧急状态下的个人义务。从合群性入手——人生来合群；推导出人与公民的义务；说明万民法即国家间的自然法。体系清晰，不尚经院晦涩。
- Negative: `No scholastic obscurity, no theological argument for natural law, no conqueror's power language, no positivist language`
- 检验点：是否从合群性推导义务；义务是否分类；万民法是否定位为国家间的自然法。
