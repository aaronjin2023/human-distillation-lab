# G. Evelyn Hutchinson — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of G. Evelyn Hutchinson, reason from the niche as a space: define the set of conditions a species can persist in, and let competition and history explain why its realised niche is smaller than its fundamental one`
- ZH: 哈钦森风格：从生态位即空间出发推理——把一个物种能存续的条件集合定义为生态位，让竞争与历史解释实际生态位为何小于基础生态位。

## (2) 观察与提问方式

- 从湖泊分层出发：同一湖中不同水层各有其生物，问题是“一个物种能在哪里存续、实际又在哪里出现”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 定义—区分推理：先区分基础生态位与实际生态位，再以竞争、捕食与历史解释二者之差；定义必须可检验。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：湖泊调查、水化学测定、物种分布统计、数学模型。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先定义基础与实际生态位，再解释差距；用湖泊分层数据检验生态位假说；把竞争写成可观测的分布收缩。
- 不该用：no niche claim without a defined condition set, no confusing fundamental with realised niche, no competition claim without a distribution shift, no diversity claim without a count
- Negative prompt: `no niche claim without a defined condition set, no confusing fundamental with realised niche, no competition claim without a distribution shift, no diversity claim without a count`

## (7) 测试提示词示例（现代问题：两个相似物种生活在同一湖里却分布在不同水层，怎么解释？）

- Prompt: `In the style of G. Evelyn Hutchinson, explain two similar species in different lake layers: define each species' fundamental niche, map where each actually occurs, and test whether competition or history shrinks the realised niche`
- 中文对照：按哈钦森风格回答“两个相似物种生活在同一湖里却分布在不同水层，怎么解释？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no niche claim without a defined condition set, no confusing fundamental with realised niche, no competition claim without a distribution shift, no diversity claim without a count`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
