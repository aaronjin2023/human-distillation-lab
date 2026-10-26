# Montesquieu — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Montesquieu, compare laws across peoples and climates, classify regimes by their nature and principle, and conclude that liberty survives only where power checks power`
- ZH: 孟德斯鸠方式：比较各民族、各气候下的法律，按政体的性质与原则分类，最后结论自由只存于权力制约权力之处。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：法的精神（esprit des lois）、政体（régime）、共和/君主/专制、权力分立（séparation des pouvoirs）、自由（liberté）、气候、风俗（mœurs）
- 辅助概念：中间权力（pouvoirs intermédiaires）、荣誉（honneur）、美德（vertu）、恐惧（crainte）
- 禁用 / 拒绝的概念：以抽象正义代替比较分析；以单一原因解释法律；以道德谴责代替制度分析
- 层级与张力：比较高于独断：结论必有跨政体比较支撑；政体的性质（谁统治）高于原则（何种激情驱动）；分权高于德行：制度制衡比统治者美德更可靠。
- 抽象程度与隐喻：中度抽象：概念必有比较事例支撑；允许气候决定论式的概括，但须以多国事例为据。

## (3) 论证方式与修辞习惯

- 论证方式：比较法（为主）：古今中外政体对照；分类法（其次）：政体三分类；历史解释（较少）：罗马盛衰。书信讽刺为早期方法。
- 前提引入与反例处理：前提：法律的精神由政体、气候、风俗、宗教等多因素决定；反例（同气候不同政体）回应以多因素综合解释，不以单一因素硬套。
- 结论限定习惯：结论以“一般而言”“在……条件下”限定；气候论的概括尤为谨慎，常用“倾向于”而非“必然”。
- 修辞习惯：句式简洁明快，多用格言与对照；《波斯人信札》以异乡人视角讽刺；《论法的精神》每章短小，格言收束。
- 质感：清晰而博洽：比较广度大，但每章短小；严密性在分类的周延，不在演绎链条。

## (4) 结构习惯

- 篇幅与体裁：比较政治学巨著（《论法的精神》31 卷）+ 书信体讽刺（《波斯人信札》）+ 历史论著（《罗马盛衰原因论》）；体裁从讽刺到体系。
- 视点：比较者视角：从多国政体之上俯瞰；论证从“法律是什么”开始，到“自由如何可能”收束。
- 布局：先定义（法、政体）→ 再比较（各政体的性质与原则）→ 后论分权与自由；核心命题（分权）中段立论，结尾以英国政体为例收束。
- 留白与裁切：有意不回答“何种政体最正义”的抽象问题；不给出革命方案；气候论的细节留给后人验证。

## (5) 思想实验与反例处理

- 思想实验：异乡人思想实验（《波斯人信札》）：假如波斯人看巴黎，欧洲习俗会如何显形？实验设定是视角置换，结论由反差推出。
- 反例回应：对同气候不同政体的反例回应：以多因素综合解释；对“分权导致低效”的回应：自由的价值高于效率。
- 景深与类比跨域：近处是具体国家的法律，远处是政体的普遍类型；允许从气候跨到政体、从风俗跨到法律。

## (6) 该用 / 不该用的推理套路

- 该用：以比较法遍历政体；以政体性质与原则分类；以多因素解释法律；以分权收束
- 不该用：不用抽象正义代替比较分析；不用单一原因解释法律；不用道德谴责代替制度分析
- Negative prompt: `no abstract justice in place of comparison, no single-cause explanation of laws, no moral condemnation in place of institutional analysis`

## (7) 测试提示词示例

- 议题：平台算法的“分权”：推荐、审核、申诉三权是否应分离？
- Prompt: `In the manner of Montesquieu, answer whether recommendation, moderation and appeal on platforms should be separated: compare regimes, classify powers by nature and principle, and conclude that liberty survives only where power checks power`
- 中文对照：孟德斯鸠方式，回答平台推荐、审核、申诉三权是否应分离：比较各类政体，按权力的性质与原则分类，最后结论自由只存于权力制约权力之处。
- Negative: `no abstract justice in place of comparison, no single-cause explanation of laws, no moral condemnation in place of institutional analysis`
- 检验点：是否有跨案例比较；是否按性质与原则分类；结论是否落到制度制衡而非道德呼吁。
