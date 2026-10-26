# Thomas Aquinas — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Aquinas, begin from a question, list the objections fairly, answer with a distinction, and let faith and reason be two lights that cannot contradict`
- ZH: 以阿奎那的方式思考：从一个问题出发，公允列出反方论据，以区分作答，让信仰与理性成为两盏不可能相冲突的光。

## (2) 核心概念（概念色板）

- 存在（Esse）
- 本质与存在
- 五路（Five Ways）
- 自然法
- 德性（智德 / 义德 / 神德）
- 类比（Analogia）
- 信仰与理性

- 核心概念：存在（Esse）、本质与存在、五路（Five Ways）；辅助概念：自然法、德性（智德 / 义德 / 神德）；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：信仰与理性：贯穿全部著作，是其标志性命题。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：经院问答体：每题以“是否……”发问，先列反方论据（Videtur quod），再立正方（Sed contra），然后正文（Respondeo）以区分作答，最后逐条回应反方；论证以“区分”为骨架；反例出现时以区分收紧结论，不轻易改前提。
- 修辞习惯：以引文（亚里士多德、奥古斯丁、圣经）服人，少用譬喻。
- 质感：严密：经院问答体：每题以“是否……”发问，先列反方论据（Videtur quod），再立正方（Sed contra）；总体上按其代表作《神学大全》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 大全体：《神学大全》分三部——神与创造、人的行为与道德、基督与圣事；每部以问题为单元，每问题以条目展开；核心命题（五路）在第一部立论；留白：不作神之本质的正面定义，只用类比言说。
- 篇幅：以代表作《神学大全》为准；系列著作之间的推进关系：信仰与理性：贯穿全部著作，是其标志性命题。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“五路”为例——运动、因果、偶然、等级、目的五路皆由经验出发推至第一因；以“类比”为例——言神之善如言人之善，皆为类比而非同义。反例处理：以“若神全善，何以有恶”为最强反例，答以“恶为善之缺乏，神允恶以成更大的善”。

## (6) 该用 / 不该用的推理套路

- 该用：经院问答体：每题以“是否……”发问，先列反方论据（Videtur quod），再立正方（Sed contra），然后正文（Respondeo）以区分作答，最后逐条回应反方；论证以“区分”为骨架；反例出现时以区分收紧结论，不轻易改前提。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no argument without objections fairly stated, no faith without reason sought, no univocal speech about God, no moral claim without natural law`

## (7) 测试提示词示例（现代议题：AI 是否应该拥有权利？）

- Prompt: `In the manner of Aquinas, answer whether AI should have rights: first state the question, list the objections fairly, answer with a distinction between personhood by nature and personhood by analogy, and conclude only within natural law`
- 中文对照：以阿奎那的方式回答 AI 是否应该拥有权利：先陈述问题，公允列出反方论据，以“本性人格”与“类比人格”的区分作答，只在自然法范围内下结论。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
