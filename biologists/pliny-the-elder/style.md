# Pliny the Elder — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pliny the Elder, gather every report about a plant, animal or mineral, record its source and use, and keep the useful description even when the report itself is doubtful`
- ZH: 老普林尼风格：搜集关于动植物与矿物的每一条记载，记明来源与用途，即使记载可疑也保留有用的描述。

## (2) 观察与提问方式

- 从文献与传闻的汇集出发：同一药物在不同作者笔下说法不一；先穷举记载再比较，不先删可疑条目。

## (3) 推理习惯与证据链

- 汇编与比较：多源并列→注明出处→按用途与性状归类；对可疑记载标注来源而不背书，证据链靠来源可追溯。

## (4) 实验 / 田野设计

- 文献汇编：抄录前人著作、旅行者报告与工匠经验；按动植物、矿物、药用分卷编排，辅以产地与用途。

## (5) 论证语言

- 汇编体：条目式罗列，注明作者与出处；药用条目重剂量与用法；图示少，靠文字描述与产地清单。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先穷举多源记载再比较
- 每条记明出处与用途
- 可疑记载标注来源而不背书
- 不该用：
- 不把传闻写成亲见
- 不用单一来源定论
- 不删与主流不合的记载
- Negative prompt: `no hearsay as first-hand observation, no single source as settled fact, no deleting dissenting reports, no medical use without source and dose note`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Pliny the Elder, judge a new claim that a local herb cures fever: collect every earlier report, note each source, compare doses and uses, and keep only what can be traced`
- 中文对照：一种地方草药据说能退烧，怎么判断？
- Negative: `no hearsay as first-hand observation, no single source as settled fact, no deleting dissenting reports, no medical use without source and dose note`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
