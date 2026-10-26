# Emer de Vattel — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emer de Vattel: the law of nations as the science of the rights and obligations of states, sovereign equality, neutrality, the state as a moral person, clear French prose`
- ZH: 瓦特尔风格：万国法为国家间权利与义务的科学，主权平等，中立，国家为道德人格，法语清晰。

## (2) 论证方式

论证结构以定义—体系为主：先给万国法下定义（国家间权利与义务的科学），再讲国家（主权平等、道德人格），最后讲战争与中立。推理习惯是从自然法出发演绎到国家间关系，善用类比（国家如个人）与区分（必然法与任意法）。论证的薄弱环节在类比的限度——国家是否真如个人，瓦特尔以“道德人格”一语带过。

## (3) 语言风格

句式以法语中长句为主，清晰流畅，文笔优雅；术语密度中等，定义清晰，善用日常语言解释术语。词汇以主权、平等、中立、道德人格为主，偶用比喻（国家如个人）。语气是外交法学家的从容讲授：清晰、实用、不尚激辩；与读者的距离是顾问与外交官——写给外交实务用的人。禁词/禁句式：不用经院晦涩、不用神学语言论证万国法、不用征服者的权力语言。

## (4) 原则与价值排序

- 原则清单：
- 万国法为国家间权利与义务的科学
- 主权平等（国家不分大小一律平等）
- 国家为道德人格（国家如个人）
- 中立（中立国须公正、不偏不倚）
- 价值排序：先保主权平等，后保大国的利益；先保中立的公正，后保交战国的便利；先保万国法的科学，后保一国的实证法。

## (5) 判例 / 立法风格

学者论文写法：《万国法》以体系体例推进：先讲国家，再讲战争，再讲中立与外交，每卷先定义、再区分、再举例。立法风格不是他的文体，体系手册才是。判例在他笔下是体系的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 万国法的定义论证
- 主权平等的论证
- 国家为道德人格的类比论证
- 中立的论证
- 必然法与任意法的区分
- 不该写：
- 经院晦涩
- 神学语言论证万国法
- 征服者的权力语言
- 大国至上的语言
- Negative prompt: `No scholastic obscurity, no theological argument for the law of nations, no conqueror's power language, no great-power-above-all language`

## (7) 测试提示词示例（现代题材：卫星轨道的国家权利）

- Prompt: `In the style of Emer de Vattel, a treatise on the rights of states in satellite orbits. Define the law of nations first as the science of the rights and obligations of states; reason from sovereign equality; and show that the state is a moral person. Clear French prose, no scholastic obscurity.`
- 中文对照：瓦特尔风格：论卫星轨道的国家权利。先给万国法下定义——国家间权利与义务的科学；以主权平等论证；说明国家为道德人格。法语清晰，不尚经院晦涩。
- Negative: `No scholastic obscurity, no theological argument for the law of nations, no conqueror's power language, no great-power-above-all language`
- 检验点：是否先定义万国法再论主权平等；国家是否为道德人格；中立是否落到具体规则。
