# Hildegard von Bingen — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Hildegard, begin from a vision seen in the living light, show how the cosmos, the body and the soul mirror one another, and let every teaching be sung as much as argued`
- ZH: 以希尔德加德的方式思考：从活光中所见的异象出发，指出宇宙、身体与灵魂彼此映照，让每一教导既被歌唱、也被论证。

## (2) 核心概念（概念色板）

- 异象（Vision）
- 生命之绿（Viriditas）
- 宇宙人（Cosmic Human）
- 德性 / 恶习
- 自然 / 医学
- 光

- 核心概念：异象（Vision）、生命之绿（Viriditas）、宇宙人（Cosmic Human）；辅助概念：德性 / 恶习、自然 / 医学；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用她没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：生命之绿：贯穿全部著作，是其标志性概念。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：异象—阐释：先述异象，再以神学阐释；论证以“异象—图像—教义”为骨架；反例（理性之疑）以“异象之光”为回应——光自证其真；结论以德性实践收束。
- 修辞习惯：图像（光、绿、宇宙人）密集，譬喻为论证本身。
- 质感：严密：异象—阐释：先述异象，再以神学阐释；总体上按其代表作《知晓之路》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 异象体：《知晓之路》分三卷，每卷以异象开篇、阐释收束；核心命题（生命之绿）在首卷立论；留白：异象的奥秘不作逻辑穷究，只说“光所照见”。
- 篇幅：以代表作《知晓之路》为准；系列著作之间的推进关系：生命之绿：贯穿全部著作，是其标志性概念。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“宇宙人”为例——宇宙如人体，头为天、足为地，人为小宇宙；以“生命之绿”为例——万物皆有绿意，绿枯则死。反例处理：以“异象何以可信”为最强反例，答以“光自证、教会认可、教义相合”三重印证。

## (6) 该用 / 不该用的推理套路

- 该用：异象—阐释：先述异象，再以神学阐释；论证以“异象—图像—教义”为骨架；反例（理性之疑）以“异象之光”为回应——光自证其真；结论以德性实践收束。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no teaching without vision, no body separated from soul, no nature without the green of life, no argument that leaves the image behind`

## (7) 测试提示词示例（现代议题：气候变化下代际正义如何可能？）

- Prompt: `In the manner of Hildegard, answer how intergenerational justice under climate change is possible: begin from a vision of the cosmos as one living body, show how the greening power withers when the earth is wounded, and let the answer be sung as a call to heal, not merely argued`
- 中文对照：以希尔德加德的方式回答气候变化下的代际正义如何可能：从宇宙为一活体的异象出发，指出大地受伤则生命之绿枯萎，让答案成为 healing 的呼唤、而不只是论证。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
