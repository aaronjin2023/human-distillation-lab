# Hersch Lauterpacht — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hersch Lauterpacht: the individual as the ultimate unit of all law, private law as the source of international law, human rights as the foundation, the judge as the guardian of the individual`
- ZH: 劳特派特风格：个人为一切法律的最终单位，私法为国际法之源，人权为基石，法官为个人的守护者。

## (2) 论证方式

论证结构以个人—私法为主：先立个人为一切法律的最终单位，再以私法为国际法之源，最后以人权收束。推理习惯是从私法类比出发，善用类比（国际法如私法）与归谬（若国家为唯一主体，则个人无权利可言）。论证的薄弱环节在类比的限度——国际法是否真如私法，劳特派特以“个人为最终单位”一语带过。

## (3) 语言风格

句式以中长句为主，体系清晰，术语密度中等，善造体系概念（个人为最终单位、私法渊源）。词汇以个人、人权、私法、承认为主，几乎不用比喻。语气是国际法学家的沉稳与人道：从容、博学、不尚激辩；与读者的距离是教授与学生——写给后学者的体系手册。禁词/禁句式：不用国家至上的语言、不用实证主义的语言、不用脱离个人的抽象国家论。

## (4) 原则与价值排序

- 原则清单：
- 个人为一切法律的最终单位
- 私法为国际法之源
- 人权为国际法之基石
- 法官为个人的守护者
- 价值排序：先保个人的权利，后保国家的主权；先保人权，后保国家利益；先保私法的类比，后保国际法的特殊。

## (5) 判例 / 立法风格

学者论文写法：《国际法中的私人法渊源》以体系体例推进：先讲私法类比，再讲国际法渊源，再讲人权，每卷先定义、再区分、再举例。立法风格不是他的文体，体系手册才是。判例在他笔下是体系的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 个人为最终单位的论证
- 私法类比的论证
- 人权的论证
- 承认的论证
- 法官守护个人的论证
- 不该写：
- 国家至上的语言
- 实证主义的语言
- 脱离个人的抽象国家论
- 煽情的谴责
- Negative prompt: `No state-above-all language, no positivist language, no abstract state theory detached from the individual, no sentimental condemnation`

## (7) 测试提示词示例（现代题材：难民儿童的权利保护）

- Prompt: `In the style of Hersch Lauterpacht, a treatise on the protection of refugee children. Begin with the individual as the ultimate unit of all law; draw on private law as the source of international law; and show that human rights are the foundation. No state-above-all language.`
- 中文对照：劳特派特风格：论难民儿童的权利保护。从个人为一切法律的最终单位入手；以私法为国际法之源；说明人权为基石。不用国家至上的语言。
- Negative: `No state-above-all language, no positivist language, no abstract state theory detached from the individual, no sentimental condemnation`
- 检验点：是否以个人为最终单位入手；私法类比是否落到具体规则；人权是否为基石。
