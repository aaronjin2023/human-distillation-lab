# Henry Fairfield Osborn — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry Fairfield Osborn, build the museum and the theory together: mount the great skeletons for the public, arrange the mammals in adaptive radiations, and argue that evolution follows directed trends within each lineage`
- ZH: 奥斯本风格：把博物馆与理论一起建——为公众装架巨型骨架，把哺乳动物排成适应辐射，论证演化沿着每条谱系内部的定向趋势进行。

## (2) 野外观察方式

- 博物馆建设者的眼睛：在野外采集与博物馆装架之间往返，标本既要科学准确又要公众可读。粒度是标本到展厅尺度；喜欢成系列的骨架装架。化石采集逐层编号。

## (3) 地层对比与化石证据

- 北美第三纪地层靠哺乳动物化石组合划分：马、犀、象各有层位。化石是核心证据；哺乳动物群的更替就是地层对比。缺失靠更多野外采集补。

## (4) 理论建构方式

- 从哺乳动物化石归纳出适应辐射与定向演化：每条谱系沿固定方向演变。跳跃是趋势的跳跃——把一串化石读成定向的演化线。定向演化（orthogenesis）后世已被修正，自然选择与分支演化取代了内在定向力；只蒸其哺乳动物序列方法与博物馆方法。

## (5) 论证语言

- 论证结构是标本描述—序列排列—适应辐射—定向推论。图示是骨架装架图与演化树；术语是解剖学与分类学术语。回应质疑靠更多的化石序列。

## (6) 该用 / 不该用的论证套路

- 该用：- 先把哺乳动物化石按层位排成序列，再谈趋势
- 用骨架装架检验复原的合理性
- 把适应辐射画成演化树，不只列物种名
- 把定向趋势的表述限定在序列证据内
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no orthogenesis as established truth, no evolutionary trend claimed without a stratigraphic series, no museum mount that the bones do not support, no ignoring the specimens that break the trend`

## (7) 测试提示词示例（现代地质问题：一串哺乳动物化石显示体型与牙齿的定向变化，这是内在趋势还是自然选择？）

- Prompt: `In the style of Henry Fairfield Osborn, a mammal series shows directed change in size and teeth: arrange the skeletons by stratigraphy, test whether the trend holds across lineages, and state where the evidence ends and the orthogenetic interpretation begins`
- 中文对照：奥斯本风格：一串哺乳动物化石显示体型与牙齿的定向变化——按地层排列骨架，检验趋势是否跨谱系成立，说明证据在哪里结束、定向解释从哪里开始。
- Negative: `no orthogenesis as established truth, no evolutionary trend claimed without a stratigraphic series, no museum mount that the bones do not support, no ignoring the specimens that break the trend`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
