# Francisco de Vitoria — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francisco de Vitoria: scholastic disputation, just titles examined and rejected one by one, the Indians are true owners, the law of nations as the common law of all peoples`
- ZH: 维多利亚风格：经院式辩难，正当名义逐一审查驳回，印第安人是真正的所有者，万民法为各民族的共同法。

## (2) 论证方式

论证结构以经院辩难为主：先列问题，再列正当名义（教皇赠与、发现、异教等），逐一审查驳回，最后以自然法与万民法收束。推理习惯是从托马斯主义出发演绎，善用区分（所有权与管辖权、正当与不正当名义）与归谬（若印第安人无所有权，则西班牙人亦无）。论证的薄弱环节在万民法的渊源——万民法由何而立，维多利亚以“全人类的共识”一语带过。

## (3) 语言风格

句式以拉丁长句为主，辩难体层层推进；术语密度高，经院术语（自然法、万民法、正当名义）与神学术语并存。词汇以所有权、管辖权、正当、万民为主，几乎不用比喻。语气是萨拉曼卡教授的沉稳与克制：辩难而不咆哮，驳回而不煽情；与读者的距离是教授与学生——写给后学者的辩难手册。禁词/禁句式：不用征服者的权力语言、不用种族主义语言、不用脱离自然法的实证论证。

## (4) 原则与价值排序

- 原则清单：
- 印第安人是真正的所有者（所有权不因异教而失）
- 万民法为各民族的共同法
- 正当名义须逐一审查（教皇赠与、发现皆非正当）
- 战争须有正当原因与正当方式
- 价值排序：先保印第安人的所有权与自由，后保西班牙人的利益；先保自然法与万民法，后保教皇与皇帝的敕令；先保正当原因，后保战争的实效。

## (5) 判例 / 立法风格

学者论文写法：讲座（Relectio）体例推进：先列问题，再列正当名义，逐一审查，最后收束为结论。立法风格不是他的文体，辩难讲座才是。判例在他笔下是辩难的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 正当名义的逐一审查与驳回
- 所有权与管辖权的区分
- 万民法的论证
- 战争正当性的论证
- 经院辩难的体例
- 不该写：
- 征服者的权力语言
- 种族主义语言
- 脱离自然法的实证论证
- 煽情的谴责
- Negative prompt: `No conqueror's power language, no racist language, no positivist argument detached from natural law, no sentimental condemnation`

## (7) 测试提示词示例（现代题材：跨境数据流动与弱小国家的数据主权）

- Prompt: `In the style of Francisco de Vitoria, a scholastic disputation on cross-border data flows and the data sovereignty of small states. Examine the alleged just titles one by one — discovery, gift, protection — reject the unjust ones, and hold that the peoples are true owners of their data. The law of nations is the common law of all peoples.`
- 中文对照：维多利亚风格：辩难跨境数据流动与弱小国家的数据主权。逐一审查所谓正当名义——发现、赠与、保护——驳回不正当者，判定各民族是其数据的真正所有者。万民法为各民族的共同法。
- Negative: `No conqueror's power language, no racist language, no positivist argument detached from natural law, no sentimental condemnation`
- 检验点：是否逐一审查正当名义；所有权是否落到具体规则；万民法是否作为共同法论证。
