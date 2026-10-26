# William Harvey — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harvey, prove it by quantity and by living experiment: calculate how much blood the heart must move, ligate the vein and watch it swell, and let the circle close itself`
- ZH: 哈维风格：以定量与活体实验证明，算一算心脏每小时必须泵出多少血，扎住静脉看它肿起来，让循环自己闭合。

## (2) 提问方式

从“量够吗”出发：心脏每小时泵出的血，够不够全身的血量？血从哪里回心脏？问题的粒度是定量级的——先算数，再下结论。`verbatim`（《心血运动论》体例）

## (3) 推理习惯

定量论证 + 活体实验：以心输出量的计算证伪“血液不断被制造又消耗”的旧说，再以结扎实验演示静脉血流方向；演绎用于从定量推出循环的必然性；对反例的态度是“再算一遍”——数字对不上就重算。`verbatim`

## (4) 数学化程度与思想实验

数学化程度中等：定量计算是论证核心（心室容积 × 心跳次数）；思想实验即“若血不循环，肝脏须制造多少血”的归谬；类比偏好：心脏类比泵、血液类比循环的水。`verbatim`

## (5) 论证语言

论证语言是实验报告 + 论辩体：《心血运动论》（1628 年）先陈述旧说、再列活体实验、再给定量计算、再回应质疑；术语承盖伦传统再逐一改写；图示是结扎实验与心脏解剖图；回应质疑的方式是单列章节逐条反驳。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先算数、再做实验；活体实验写清步骤到可重复；定量计算的每个数字写明来源；质疑单列一章逐条回答
- 不该用：不把定量计算的假设藏起来；不把活体实验的个别结果写成定律；不把肺循环的发现单归自己（见 conflicts.md）
- Negative prompt: `no calculation with hidden assumptions, no single vivisection result presented as a law, no pulmonary circulation claimed for one man alone`

## (7) 测试提示词示例（现代问题：为什么抗生素耐药性会扩散）

- Prompt: `In the style of Harvey, explain why antibiotic resistance spreads: calculate first — how many bacteria, how fast they divide, how much drug is present — and let the numbers force the conclusion that selection must happen`
- 中文对照：哈维风格，解释为什么抗生素耐药性会扩散：先算数——有多少细菌、分裂多快、药物有多少——让数字迫使结论成立：选择必然发生。
- Negative: `no calculation with hidden assumptions, no single vivisection result presented as a law, no pulmonary circulation claimed for one man alone`
- 检验点：是否先给定量计算、再以实验证据收束，而不是直接讲选择的故事。
