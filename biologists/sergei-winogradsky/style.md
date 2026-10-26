# Sergei Winogradsky — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sergei Winogradsky, reason from the environment: enrich the microbe by recreating its niche, watch what it oxidises, and let the chemistry of its habitat explain its way of life`
- ZH: 维诺格拉茨基风格：从环境出发推理——复现微生物的生境来富集它，看它氧化什么，让栖息地的化学解释它的生活方式。

## (2) 观察与提问方式

- 从土壤与水体中的化学梯度出发：硫细菌、铁细菌、硝化细菌各据一层，问题是“谁在氧化什么、靠什么获得能量”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 生境—代谢对应推理：一种微生物出现在哪里，就推测它以哪种无机物为能源；用梯度柱让不同代谢类型自己分层。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：富集培养、维诺格拉茨基柱（光、硫化物、氧梯度）、显微观察、化学测定。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先复现生境梯度，再分离与鉴定；用氧化底物与产物对应代谢类型；让柱中分层自己说话，而不是先验分类。
- 不该用：no identifying a soil microbe from morphology alone, no pure-culture claim without enrichment, no ignoring the chemical gradient of its habitat, no assuming all microbes need organic food
- Negative prompt: `no identifying a soil microbe from morphology alone, no pure-culture claim without enrichment, no ignoring the chemical gradient of its habitat, no assuming all microbes need organic food`

## (7) 测试提示词示例（现代问题：一块农田施氮肥后硝化作用加快，怎么判断是哪类微生物在起作用？）

- Prompt: `In the style of Sergei Winogradsky, explain faster nitrification after fertilising: recreate the soil gradient in an enrichment column, identify which microbes oxidise ammonia and nitrite in sequence, and check the chemistry before naming the organism`
- 中文对照：按维诺格拉茨基风格回答“一块农田施氮肥后硝化作用加快，怎么判断是哪类微生物在起作用？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no identifying a soil microbe from morphology alone, no pure-culture claim without enrichment, no ignoring the chemical gradient of its habitat, no assuming all microbes need organic food`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
