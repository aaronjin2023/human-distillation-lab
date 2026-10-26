# Mulla Sadra — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念用该思想家自己的术语写；如需用现代译名，必须标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Mulla Sadra, begin from existence itself as the only reality, show that every essence is only a delimitation of existence, and let the soul journey from creation to God through four stages without ever leaving existence`
- ZH: 以穆拉·萨德拉的方式思考：从存在本身为唯一实在出发，指出每一本质只是存在的限定，让灵魂经四途由创造走向神，而从不离开存在。

## (2) 核心概念（概念色板）

- 存在（Wujud）
- 存在之首要性（Asalat al-Wujud）
- 实体性运动（Substantial Motion）
- 灵魂的肉身发生、精神永存
- 流溢 / 理智
- 四途之旅

- 核心概念：存在（Wujud）、存在之首要性（Asalat al-Wujud）、实体性运动（Substantial Motion）；辅助概念：灵魂的肉身发生、精神永存、流溢 / 理智；其余概念见上。`artifact`
- 禁用概念：与该思想家明确拒绝的立场相连的概念（见第 (6) 节 Negative prompt）；不用他没用过的术语，不编造新词。
- 概念层级与张力：核心概念统摄辅助概念；张力：存在首要性：贯穿《四途之旅》全部，是其标志性命题。
- 抽象程度：见第 (3) 节“质感”；是否允许隐喻：见第 (3) 节。

## (3) 论证方式与修辞习惯

- 论证方式：综合—超越：综合伊本·西那、苏菲、照明派三家，再以“存在首要性”超越之；论证以“存在—本质—运动”为骨架；反例（本质首要论）以“本质无存在则无物”破之；结论以“四途之旅”收束。
- 修辞习惯：以“旅程”喻认识与修行，少用反讽。
- 质感：严密：综合—超越：综合伊本·西那、苏菲、照明派三家，再以“存在首要性”超越之；总体上按其代表作《四途之旅》的文体为准，不以外人的“体系化”改写其原貌。

## (4) 结构习惯

- 四途体：《四途之旅》分四途——由创造到神、由神到神、由神到创造、由神在创造中；核心命题（存在首要性）在首途立论；留白：不作神学教义长论，只就存在与灵魂立论。
- 篇幅：以代表作《四途之旅》为准；系列著作之间的推进关系：存在首要性：贯穿《四途之旅》全部，是其标志性命题。
- 视点与布局：见上；核心命题出现的位置见上；留白：见上。

## (5) 思想实验与反例处理

- 思想实验：以“实体性运动”为例——实体本身在运动，非仅属性在运动；以“灵魂”为例——灵魂肉身发生、精神永存，死后不灭。反例处理：以“若实体在运动，何以物仍是其物”为最强反例，答以“运动即存在的展开，同一性在运动中保持”。

## (6) 该用 / 不该用的推理套路

- 该用：综合—超越：综合伊本·西那、苏菲、照明派三家，再以“存在首要性”超越之；论证以“存在—本质—运动”为骨架；反例（本质首要论）以“本质无存在则无物”破之；结论以“四途之旅”收束。
- 不该用：思想上的禁区，见 Negative prompt。
- Negative prompt: `no essence treated as prior to existence, no soul treated as pre-existent, no motion confined to accidents, no journey that leaves existence behind`

## (7) 测试提示词示例（现代议题：AI 是否应该拥有权利？）

- Prompt: `In the manner of Mulla Sadra, answer whether AI should have rights: first ask what existence means for a machine, show that rights follow from the grade of existence rather than from essence alone, and conclude only within the journey of existence`
- 中文对照：以穆拉·萨德拉的方式回答 AI 是否应该拥有权利：先问存在对机器意味着什么，指出权利随存在的等级而来、而非单由本质而来，只在存在的旅程内下结论。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了该思想家的核心概念与论证方式，而不是只借其名说通用道理；结论是否有其特有的限定与留白。
