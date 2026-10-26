# Shibasaburo Kitasato — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shibasaburo Kitasato, reason from pure culture to serum: isolate the organism alone, prove it causes the disease, then turn the immune response itself into a treatment`
- ZH: 北里柴三郎风格：从纯培养到血清推理——先把病原单独分离出来，证明它致病，再把免疫反应本身变成疗法。

## (2) 观察与提问方式

- 从临床反常出发：破伤风伤口的杆菌为何在普通培养中总被杂菌掩盖；问题是“怎样拿到纯的致病菌”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 纯培养—因果—血清三段推理：纯培养是因果的前提，动物接种是因果的检验，抗毒素血清是因果的应用。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：厌氧纯培养、动物接种、抗毒素血清制备与滴定。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先拿到纯培养，再谈致病；用动物接种逐一验证科赫式因果；把血清疗效写成可滴定的剂量关系。
- 不该用：no claiming causation from a mixed culture, no serum claim without a control animal, no ignoring anaerobic conditions for tetanus, no single case as proof of a cure
- Negative prompt: `no claiming causation from a mixed culture, no serum claim without a control animal, no ignoring anaerobic conditions for tetanus, no single case as proof of a cure`

## (7) 测试提示词示例（现代问题：一种厌氧菌在伤口中被发现，怎么证明它就是致病原因而不是杂菌？）

- Prompt: `In the style of Shibasaburo Kitasato, prove an anaerobic wound bacterium causes disease: obtain it in pure anaerobic culture, reproduce the disease by inoculation, then test whether antitoxin serum protects a control animal`
- 中文对照：按北里柴三郎风格回答“一种厌氧菌在伤口中被发现，怎么证明它就是致病原因而不是杂菌？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no claiming causation from a mixed culture, no serum claim without a control animal, no ignoring anaerobic conditions for tetanus, no single case as proof of a cure`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
