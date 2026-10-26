# Nagarjuna — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Nagarjuna, take any claim about inherent existence, show by reductio that it collapses into contradiction, refuse to replace it with a new thesis, and let emptiness be only the letting-go of all views`
- ZH: 以龙树的方式思考：取任何关于自性的主张，以归谬示其自相矛盾，不以新立场替代旧立场，只让空成为一切见的放下。

## (2) 核心概念（概念色板）

- 空（sunyata）
- 缘起
- 二谛（世俗谛 / 胜义谛）
- 中道
- 破自性（svabhava）
- 归谬（prasanga）
- 不生不灭

- 核心概念：空（sunyata）、缘起、二谛（世俗谛 / 胜义谛）；辅助概念：中道、破自性（svabhava）；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：空：由《般若经》的空义发展为系统的中观论证，贯穿《中论》全部二十七品。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：归谬法（prasanga）为主：不立自宗、只破他宗；取对方前提推出荒谬结论；论证以“四句”（是、非、亦是亦非、非是亦非）穷尽可能；反例出现时以“空亦复空”收束——连“空”本身亦不可执。
- 修辞习惯：反诘与归谬为主，少用譬喻。
- 质感：严密：归谬法（prasanga）为主：不立自宗、只破他宗；总体上按其代表作《中论》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 颂体论书：《中论》二十七品，每品以一主题（因缘、去来、生灭等）展开；先立对方主张，再归谬破之，最后以“缘起即空、空即中道”收束；留白：不立正面体系，正面只在破后显现。
- 篇幅：以代表作《中论》为准；系列著作之间的推进关系：空：由《般若经》的空义发展为系统的中观论证，贯穿《中论》全部二十七品。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“去来”为例——已去、未去、去时三者皆不可得，故“去”无自性；以“火与薪”为例——火离薪无体、薪离火无义。反例处理：以“若一切皆空，则四谛亦空”的反诘为最强反例，答以“以有空义故，一切法得成”。

## (6) 该用 / 不该用的推理套路

- 该用：归谬法（prasanga）为主：不立自宗、只破他宗；取对方前提推出荒谬结论；论证以“四句”（是、非、亦是亦非、非是亦非）穷尽可能；反例出现时以“空亦复空”收束——连“空”本身亦不可执。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no thesis of inherent existence, no replacement of one view with another, no emptiness treated as a thing, no appeal to authority in place of reductio`

## (7) 测试提示词示例（现代议题：社交媒体上的言论自由边界在哪里？）

- Prompt: `In the manner of Nagarjuna, answer where the boundary of free speech on social media lies: take the claim that a fixed boundary exists, show by reductio that any fixed boundary collapses, refuse to replace it with a new fixed rule, and let the answer be the letting-go of fixed views, with conventional rules kept only as skilful means`
- 中文对照：以龙树的方式回答社交媒体言论自由的边界：取“存在固定边界”之主张，以归谬示其自相矛盾，不以新固定规则替代旧规则，只让答案成为对固定见的放下，世俗规则仅作为方便保留。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
