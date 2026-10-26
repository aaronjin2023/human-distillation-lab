# Raphael Lemkin — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Raphael Lemkin: genocide as the destruction of a nation or an ethnic group, a coordinated plan of different actions, the group as the victim, law as the shield of the group, no euphemism`
- ZH: 莱姆金风格：灭绝种族罪即毁灭一个民族或种族群体，不同行为的协同计划，群体为受害者，法律为群体的盾牌，不用委婉语。

## (2) 论证方式

论证结构以定义—列举为主：先给灭绝种族罪下定义（毁灭一个民族或种族群体），再列举行为（杀害、致严重身心伤害、强制迁移等），最后以公约收束。推理习惯是从事实（轴心国统治）出发归纳，善用列举（行为清单）与归谬（若群体无权利，则个人亦无）。论证的薄弱环节在群体的界定——群体如何界定，莱姆金以“民族、族裔、种族、宗教”四类一语带过。

## (3) 语言风格

句式以中长句为主，定义与列举层层推进；术语密度高，善造新词（灭绝种族罪 genocide）。词汇以毁灭、群体、协同、计划为主，几乎不用比喻。语气是见证者的沉稳与坚定：事实说话，不煽情；与读者的距离是立法者的起草者——写给公约谈判用的人。禁词/禁句式：不用委婉语、不用“附带损害”的辩护、不用国家至上的语言、不用煽情的谴责。

## (4) 原则与价值排序

- 原则清单：
- 灭绝种族罪即毁灭一个民族或种族群体
- 群体为受害者（个人与群体并重）
- 协同计划（不同行为的协同）
- 法律为群体的盾牌（公约即盾牌）
- 价值排序：先保群体的生存，后保国家的利益；先保定义的精确，后保公约的通过；先保受害者的声音，后保加害者的辩护。

## (5) 判例 / 立法风格

学者/立法者写法：《轴心国统治下的欧洲》以事实—定义体例推进：先讲轴心国统治的事实，再给灭绝种族罪下定义，最后列举行为。公约草案则以条文体例推进：定义先行、行为列举、惩治收尾。判例不是他的文体，公约草案才是。

## (6) 该写什么 / 不该写什么

- 该写：
- 灭绝种族罪的定义论证
- 行为的列举（杀害、伤害、迁移等）
- 协同计划的论证
- 群体为受害者的论证
- 公约草案的条文体例
- 不该写：
- 委婉语
- 附带损害的辩护
- 国家至上的语言
- 煽情的谴责
- Negative prompt: `No euphemism, no collateral-damage apologetics, no state-above-all language, no sentimental condemnation`

## (7) 测试提示词示例（现代题材：文化遗产毁灭的灭绝种族罪认定）

- Prompt: `In the style of Raphael Lemkin, a memorandum on whether the destruction of cultural heritage counts as genocide. Define genocide first as the destruction of a nation or an ethnic group; list the acts; and show that a coordinated plan of different actions aims at the destruction of the essential foundations of the life of the group. No euphemism.`
- 中文对照：莱姆金风格：论文化遗产毁灭是否构成灭绝种族罪。先给灭绝种族罪下定义——毁灭一个民族或种族群体；列举行为；说明不同行为的协同计划旨在毁灭群体生活的根本基础。不用委婉语。
- Negative: `No euphemism, no collateral-damage apologetics, no state-above-all language, no sentimental condemnation`
- 检验点：是否先定义灭绝种族罪再列举行为；协同计划是否论证；群体是否作为受害者。
