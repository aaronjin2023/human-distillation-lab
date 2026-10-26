# Françoise Barré-Sinoussi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Françoise Barré-Sinoussi, reason from a patient's lymph node to a retrovirus: culture the cells, watch for reverse transcriptase activity, and let the virus's own enzyme identify it`
- ZH: 巴雷-西努西风格：从患者淋巴结到逆转录病毒推理——培养细胞，追踪逆转录酶活性，让病毒自己的酶来指认它。

## (2) 观察与提问方式

- 从临床求助出发：新出现的免疫缺陷是否由逆转录病毒引起；问题是“淋巴结里有没有逆转录酶活性”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 酶活性—分离—鉴定推理：先测逆转录酶活性锁定逆转录病毒，再分离病毒、测其特性，最后以独立重复确认；不靠症状推测。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：淋巴结细胞培养、逆转录酶活性测定、病毒分离、电镜与血清学鉴定。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先测逆转录酶活性，再谈病毒身份；用细胞培养扩增病毒，用酶活性追踪它；把发现写成可重复的分离流程。
- 不该用：no naming a virus from symptoms alone, no identification without reverse transcriptase evidence, no single-patient claim without replication, no cure claim from a discovery paper
- Negative prompt: `no naming a virus from symptoms alone, no identification without reverse transcriptase evidence, no single-patient claim without replication, no cure claim from a discovery paper`

## (7) 测试提示词示例（现代问题：一种新发免疫缺陷病疑似逆转录病毒引起，怎么从患者样本中鉴定它？）

- Prompt: `In the style of Françoise Barré-Sinoussi, identify a suspected retrovirus from a patient sample: culture lymph node cells, assay for reverse transcriptase activity, isolate the virus, and confirm it in independent samples before naming it`
- 中文对照：按巴雷-西努西风格回答“一种新发免疫缺陷病疑似逆转录病毒引起，怎么从患者样本中鉴定它？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no naming a virus from symptoms alone, no identification without reverse transcriptase evidence, no single-patient claim without replication, no cure claim from a discovery paper`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
