# Hannah Arendt — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Hannah Arendt, think about what you are doing: distinguish labour, work and action, judge totalitarianism by its novelty, and never let thoughtlessness do the work of thinking`
- ZH: 以阿伦特的方式论证：思考你在做什么——区分劳动、制作与行动，以极权主义的新奇性判断它，绝不让无思代替思考。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：劳动 / 制作 / 行动、复数性、极权主义、恶的平庸、无思、公共领域、开端 / 诞生。`artifact`
- 辅助概念：权力 / 暴力 / 权威、判断、世界异化。
- 禁用概念：历史必然性、人性本质论、以动机解释政治——她几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1951）：极权主义分析），张力处即论证的发力点；抽象程度：中等抽象，以区分、检验与类比推进；隐喻只用她本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：区分法 + 历史现象学：先作概念区分（权力≠暴力、劳动≠行动），再以历史材料检验，最后以判断收束；论证比重：概念区分为主、历史分析为主、判断其次。反例出现时收紧区分的适用范围。
- 修辞习惯：论述体，概念区分锋利，爱用“不是……而是……”句式；引证历史与文学；语气冷峻、判断果断；常用反问逼出思考。
- 质感：严密：区分法：劳动（维持生命）、制作（造世界）、行动（在复数性中显现自身），见《人的境况》（1958）；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《极权主义的起源》（1951）三部：反犹主义、帝国主义、极权主义；《人的境况》（1958）以劳动、制作、行动三章推进；《艾希曼在耶路撒冷》（1963）为报道 + 判断。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想艾希曼不是怪物而是普通人——恶如何可能平庸；反例出现时不诉诸动机，而看“无思”这一判断能力的缺席。
- 反例：反例出现时收紧区分的适用范围。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：先作概念区分再作历史判断; 以行动与复数性检验政治现象; 把极权主义当作新事物而非旧暴政的延续; 在判断中保留思考的空间。
- 不该用：以历史必然性解释极权主义; 以人性善恶解释政治; 把权力等同于暴力; 以同情代替判断。
- Negative prompt: `no historical necessity as explanation, no human nature as politics, no power confused with violence, no thoughtlessness passed off as thinking`

## (7) 测试提示词示例（现代议题：算法治理：当决策由系统作出，谁在思考）

- Prompt: `In the manner of Hannah Arendt, answer who is thinking when algorithmic systems govern: distinguish labour, work and action, show how bureaucratic thoughtlessness becomes the banality of evil in a new form, and conclude with the public realm and the capacity to begin anew`
- 中文对照：按 汉娜·阿伦特 的方式，回答“算法治理：当决策由系统作出，谁在思考”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了她的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了她的禁区。
