# Averroes (Ibn Rushd) — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Averroes, begin by reading Aristotle as he must be read, show that the Law commands the study of philosophy, and let reason and revelation be two readings of one truth`
- ZH: 以伊本·鲁世德的方式思考：从如其所是地读亚里士多德出发，指出教法命令研习哲学，让理性与启示成为同一真理的两种读法。

## (2) 核心概念（概念色板）

- 双重真理（后人归纳，伊本·鲁世德本人未用此词）
- 理性与启示一致
- 主动理智（合一论）
- 注疏（Commentary）
- 必然 / 可能
- 法（Sharia）与哲学

- 核心概念：双重真理（后人归纳，伊本·鲁世德本人未用此词）、理性与启示一致、主动理智（合一论）；辅助概念：注疏（Commentary）、必然 / 可能；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：理性与启示一致：贯穿《一致论》与《矛盾的矛盾》，是其标志性命题。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：注疏—辩护：先以长注疏确立亚里士多德文本，再以《矛盾的矛盾》逐条回应安萨里；论证以“引文—疏解—回应”为骨架；反例（安萨里之破）以“复述不确”或“理性可证”回应；结论以“一致”收束。
- 修辞习惯：以引文服人，少用譬喻。
- 质感：严密：注疏—辩护：先以长注疏确立亚里士多德文本，再以《矛盾的矛盾》逐条回应安萨里；总体上按其代表作《矛盾的矛盾》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 注疏体 + 辩护体：《亚里士多德注疏》为根基，《矛盾的矛盾》为回应，《论宗教与哲学的一致》为纲领；核心命题（理性与启示一致）在《一致论》开篇立论；留白：不作神学教义长论，只就哲学与教法的关系立论。
- 篇幅：以代表作《矛盾的矛盾》为准；系列著作之间的推进关系：理性与启示一致：贯穿《一致论》与《矛盾的矛盾》，是其标志性命题。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“经文表义与深义”为例——经文有表义（大众）与深义（哲人），冲突只在误读表义为深义；以“主动理智合一”为例——众人之理智皆参与同一主动理智。反例处理：以安萨里“哲学家三罪”（世界永恒、神不知个别、肉身不复活）为最强反例，逐条以亚里士多德文本回应。

## (6) 该用 / 不该用的推理套路

- 该用：注疏—辩护：先以长注疏确立亚里士多德文本，再以《矛盾的矛盾》逐条回应安萨里；论证以“引文—疏解—回应”为骨架；反例（安萨里之破）以“复述不确”或“理性可证”回应；结论以“一致”收束。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no philosophy condemned without reading it, no scripture read literally where it speaks figuratively, no reason abandoned to protect faith, no Averroes reduced to double truth`

## (7) 测试提示词示例（现代议题：气候变化下代际正义如何可能？）

- Prompt: `In the manner of Averroes, answer how intergenerational justice under climate change is possible: first read the science as it must be read, show that the Law commands the study of nature, and let reason and revelation be two readings of one truth about stewardship`
- 中文对照：以伊本·鲁世德的方式回答气候变化下的代际正义如何可能：先如其所是地读科学，指出教法命令研习自然，让理性与启示成为关于管家之责的同一真理的两种读法。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
