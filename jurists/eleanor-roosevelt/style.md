# Eleanor Roosevelt — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eleanor Roosevelt: human rights begin in small places close to home, the Universal Declaration as a Magna Carta for all mankind, consensus-builder, plain American prose, dignity in daily life`
- ZH: 埃莉诺·罗斯福风格：人权始于家门口的小地方，世界人权宣言为全人类的自由大宪章，共识的缔造者，朴素的美式散文，日常生活中的尊严。

## (2) 论证方式

论证结构以小处—普世为主：先讲人权始于家门口的小地方（邻里、学校、工厂），再推及普世（宣言为全人类的自由大宪章），最后以共识收束。推理习惯是从日常生活出发，善用归纳（小地方—大世界）与归谬（若小地方无权利，则大世界亦无）。论证的薄弱环节在共识的脆弱——各国分歧如何弥合，罗斯福以“协商与耐心”一语带过。

## (3) 语言风格

句式以美式中短句为主，朴素清晰，偶有短句格言；术语密度低，刻意用日常语言写人权，少法律术语。词汇以权利、尊严、家园、邻里、共识为主，偶用比喻（宣言如大宪章、人权如家园）。语气是人权委员会主席的温和而坚定：协商多于命令，耐心多于独断；与读者的距离是主席与各国代表——写给全世界读的宣言。禁词/禁句式：不用国家至上的语言、不用一国中心主义、不用法学黑话、不用煽情的谴责。

## (4) 原则与价值排序

- 原则清单：
- 人权始于家门口的小地方
- 世界人权宣言为全人类的自由大宪章
- 共识须以协商与耐心缔造
- 尊严在日常生活中
- 价值排序：先保人的尊严，后保国家的主权；先保小地方的权利，后保大世界的宣言；先保共识，后保一国的立场。

## (5) 判例 / 立法风格

立法者写法：宣言起草以共识缔造为特色：先讲小地方，再讲普世，最后逐条协调各国分歧。报告（人权委员会报告）则以散文体论证：先讲进展，再讲分歧，最后讲共识。判例不是她的文体，宣言起草与报告才是。

## (6) 该写什么 / 不该写什么

- 该写：
- 小地方的人权论证
- 宣言为自由大宪章的论证
- 共识缔造的论证
- 日常生活中的尊严论证
- 朴素语言写人权
- 不该写：
- 国家至上的语言
- 一国中心主义
- 法学黑话
- 煽情的谴责
- Negative prompt: `No state-above-all language, no one-country centrism, no legal jargon, no sentimental condemnation`

## (7) 测试提示词示例（现代题材：社区调解中的人权）

- Prompt: `In the style of Eleanor Roosevelt, a report on human rights in community mediation. Begin where human rights begin: in small places, close to home — the neighbourhood, the school, the workshop. Show that unless these rights have meaning there, they have little meaning anywhere. Plain American prose, dignity in daily life.`
- 中文对照：埃莉诺·罗斯福风格：报告社区调解中的人权。从人权开始的地方写起——家门口的小地方：邻里、学校、作坊。说明若这些权利在那里没有意义，在别处也几乎没有意义。朴素的美式散文，日常生活中的尊严。
- Negative: `No state-above-all language, no one-country centrism, no legal jargon, no sentimental condemnation`
- 检验点：是否从家门口的小地方入手；宣言是否为自由大宪章；共识是否以协商缔造。
