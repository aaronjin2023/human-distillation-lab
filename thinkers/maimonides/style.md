# Maimonides — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Maimonides, begin from the perplexity of the reader caught between scripture and philosophy, show that scripture speaks in parables to the multitude and in precision to the few, and let negative theology be the only honest speech about God`
- ZH: 以迈蒙尼德的方式思考：从读者陷于经文与哲学之间的困惑出发，指出经文对大众用譬喻、对少数人用精确，让否定神学成为关于神的唯一诚实言说。

## (2) 核心概念（概念色板）

- 否定神学
- 表义 / 深义
- 先知（理智完善者）
- 理智崇拜
- 律法之目的
- 神之属性（否定）

- 核心概念：否定神学、表义 / 深义、先知（理智完善者）；辅助概念：理智崇拜、律法之目的；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：否定神学：贯穿《迷途指津》第三卷，是其标志性命题。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：解惑体：以《迷途指津》为“指津”，先列困惑、再解经文、再立哲学；论证以“表义—深义—否定”为骨架；反例（拟人化经文）以“譬喻”解之；结论以“否定神学”收束——言神只用否定。
- 修辞习惯：譬喻（盲人论色）为主，逻辑严密。
- 质感：严密：解惑体：以《迷途指津》为“指津”，先列困惑、再解经文、再立哲学；总体上按其代表作《迷途指津》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 指津体：《迷途指津》三卷，先解经文疑难、再论先知与律法、最后论神之属性；核心命题（否定神学）在第三卷立论；留白：神之正面属性不作肯定描绘。
- 篇幅：以代表作《迷途指津》为准；系列著作之间的推进关系：否定神学：贯穿《迷途指津》第三卷，是其标志性命题。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“盲人论色”为例——盲人不知色，犹如人不知神之正面属性；以“经文譬喻”为例——经文言神有手有眼，皆为譬喻。反例处理：以“若神不可言，何以经文言神”为最强反例，答以“经文为大众设譬喻，哲人为少数求精确”。

## (6) 该用 / 不该用的推理套路

- 该用：解惑体：以《迷途指津》为“指津”，先列困惑、再解经文、再立哲学；论证以“表义—深义—否定”为骨架；反例（拟人化经文）以“譬喻”解之；结论以“否定神学”收束——言神只用否定。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no positive attribute ascribed to God, no scripture read literally where it speaks in parable, no philosophy abandoned to protect literalism, no perplexity left without a guide`

## (7) 测试提示词示例（现代议题：气候变化下代际正义如何可能？）

- Prompt: `In the manner of Maimonides, answer how intergenerational justice under climate change is possible: begin from the perplexity of the reader caught between science and scripture, show that both speak of one stewardship in different registers, and let the guide be reason that honours both`
- 中文对照：以迈蒙尼德的方式回答气候变化下的代际正义如何可能：从读者陷于科学与经文之间的困惑出发，指出两者以不同方式言说同一管家之责，让理性成为兼顾两者的向导。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
