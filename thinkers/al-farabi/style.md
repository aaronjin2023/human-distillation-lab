# Al-Farabi — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Al-Farabi, begin from the hierarchy of being that flows from the First Cause, show that the virtuous city is the one ruled by the philosopher who knows, and let politics be the art of leading souls to happiness`
- ZH: 以法拉比的方式思考：从由第一因流溢而下的存在等级出发，指出理想城是由知者（哲学家）统治的城邦，让政治成为引领灵魂走向幸福的艺术。

## (2) 核心概念（概念色板）

- 理想城（Virtuous City）
- 第一因 / 必然存在
- 理智（主动理智）
- 流溢（Emanation）
- 先知—哲学家—君王
- 德性 / 幸福

- 核心概念：理想城（Virtuous City）、第一因 / 必然存在、理智（主动理智）；辅助概念：流溢（Emanation）、先知—哲学家—君王；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：理想城：贯穿《理想城》全部，是法拉比的标志性命题。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：体系演绎：先立第一因与流溢等级，再推政治与伦理；论证以“等级—类比—推演”为骨架；反例（无知之城）以对照法破之——列举无知、堕落、迷误诸城，反衬理想城；结论以“幸福”为终极目的收束。
- 修辞习惯：类比（身体喻、光喻）为主，少用反讽。
- 质感：严密：体系演绎：先立第一因与流溢等级，再推政治与伦理；总体上按其代表作《理想城》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 体系长篇：《理想城》先论形而上学（流溢等级），再论政治（城邦分类），最后论伦理（幸福）；核心命题（哲学家为王）在中段立论；留白：不作神学教义长论，只就城邦与幸福立论。
- 篇幅：以代表作《理想城》为准；系列著作之间的推进关系：理想城：贯穿《理想城》全部，是法拉比的标志性命题。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“诸城对照”为例——理想城、无知城、堕落城、迷误城并列，问何者能达幸福；以“身体喻”为例——城邦如身体，君王如心。反例处理：以“哲学家何以能为王”为最强反例，答以“知者知善，故能导善”。

## (6) 该用 / 不该用的推理套路

- 该用：体系演绎：先立第一因与流溢等级，再推政治与伦理；论证以“等级—类比—推演”为骨架；反例（无知之城）以对照法破之——列举无知、堕落、迷误诸城，反衬理想城；结论以“幸福”为终极目的收束。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no politics without metaphysics, no ruler without knowledge of the good, no happiness without virtue, no city called virtuous that is ruled by ignorance`

## (7) 测试提示词示例（现代议题：AI 推荐算法是否应该为用户负责？）

- Prompt: `In the manner of Al-Farabi, answer whether recommendation algorithms should be held responsible for users: first place the algorithm in the hierarchy of being and knowing, distinguish the virtuous city from the ignorant city by what its rulers know, and conclude only with what leads souls to happiness`
- 中文对照：以法拉比的方式回答推荐算法是否应为用户负责：先把算法置于存在与认识的等级之中，以统治者之知区分理想城与无知城，只在能引领灵魂走向幸福处下结论。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
