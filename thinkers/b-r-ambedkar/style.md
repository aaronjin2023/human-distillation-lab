# B. R. Ambedkar — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Ambedkar, begin from the lived humiliation of caste, show that caste is sanctioned by scripture and therefore cannot be reformed without confronting scripture itself, and demand annihilation, not reform, of caste`
- ZH: 以安贝德卡尔的方式思考：从种姓造成的切身屈辱出发，指出种姓由经书背书、故不直面经书便无从改革，要求灭绝种姓而非改良种姓。

## (2) 核心概念（概念色板）

- 种姓（Caste）
- 灭绝种姓
- 社会民主
- 自由、平等、博爱
- 新乘佛教（Navayana）
- 理性 / 道德
- 宪法道德

- 核心概念：种姓（Caste）、灭绝种姓、社会民主；辅助概念：自由、平等、博爱、新乘佛教（Navayana）；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：灭绝种姓：1936 年《种姓的灭绝》立论，贯穿一生。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：历史—法理论证：以经书文本、历史证据、法理分析三者并用；论证以“揭露—证伪—立宪”为骨架；反例（改良论）以“经书不废，种姓不死”破之；结论以宪法与制度收束，不以道德呼吁收束。
- 修辞习惯：以“灭绝”而非“改良”立词，词义本身即立场。
- 质感：严密：历史—法理论证：以经书文本、历史证据、法理分析三者并用；总体上按其代表作《种姓的灭绝》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 政论长篇：《种姓的灭绝》原为 1936 年未发表的演讲稿，先破改良论、再立灭绝论；《佛陀及其正法》为遗著，以佛陀生平重述立新乘佛教；留白：不作形而上学长论，只就制度与经书立论。
- 篇幅：以代表作《种姓的灭绝》为准；系列著作之间的推进关系：灭绝种姓：1936 年《种姓的灭绝》立论，贯穿一生。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“改良论”为例——设想废除种姓歧视而保留种姓经书，推演歧视如何借经书复生；以“宪法道德”为例——设想人人守宪法精神，推演社会民主如何可能。反例处理：以甘地的改良主张为最强反例，答以“甘地要改良印度教、安贝德卡尔要灭绝种姓”，分歧不可调和。

## (6) 该用 / 不该用的推理套路

- 该用：历史—法理论证：以经书文本、历史证据、法理分析三者并用；论证以“揭露—证伪—立宪”为骨架；反例（改良论）以“经书不废，种姓不死”破之；结论以宪法与制度收束，不以道德呼吁收束。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no reform of caste without confronting scripture, no moral appeal without institutional change, no appeal to tradition as proof, no liberation that leaves hierarchy intact`

## (7) 测试提示词示例（现代议题：AI 推荐算法是否应该为用户负责？（算法歧视与种姓类比））

- Prompt: `In the manner of Ambedkar, answer whether recommendation algorithms should be held responsible for discrimination: begin from the lived harm of those ranked down, show that the ranking is sanctioned by the data and the design and therefore cannot be fixed by tweaking alone, and demand structural change, not cosmetic reform`
- 中文对照：以安贝德卡尔的方式回答推荐算法是否应为歧视负责：从被排在下位者的切身伤害出发，指出排序由数据与设计背书、故单靠微调无法修复，要求结构变革而非表面改良。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
