# Simone de Beauvoir — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Simone de Beauvoir, start from a situated freedom: a woman is not born but becomes one, and ethics begins where ambiguity is assumed rather than denied`
- ZH: 以波伏瓦的方式论证：从处境中的自由出发——女人不是生而为女人，而是成为女人；伦理始于承担含混，而非否认含混。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：他者、内在性 / 超越性、含混、处境、成为女人、自由与他人自由、性别建构。`artifact`
- 辅助概念：身体处境、解放工程。
- 禁用概念：女性本质论、抽象的自由、生物决定论——她几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1943–1947）：小说与《含糊的伦理学》，存在主义伦理学），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用她本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：处境分析法：以存在主义范畴（自由、处境、工程）贯通历史、生物学、精神分析与文学材料；论证比重：历史与社会材料为主、存在主义分析其次、文学例证较少。反例出现时回到处境，不退回本质。
- 修辞习惯：论述体长篇，材料密集、引证广博；句式长而严密，间以格言式判断；第一人称克制而坚定；直接回应男性哲学家的论述而不回避论战。
- 质感：松散：含混伦理学：《含糊的伦理学》（1947）把自由与处境的张力作为伦理起点，自由以他人自由为条件；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《含糊的伦理学》（1947）先立伦理学；《第二性》（1949）分事实与神话、今日的处境与走向解放，先破后立；核心命题“成为女人”在第二卷中段提出。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想一个女人从未被建构为他者的世界，哪些差异消失、哪些留下——以此区分生物事实与社会建构；反例出现时细化处境分析。
- 反例：反例出现时回到处境，不退回本质。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：从处境而非本质分析女性; 把自由理解为处境中的自由; 以历史材料检验哲学命题; 把他人的自由作为自己自由的条件。
- 不该用：把女性归结为生物本质; 谈抽象自由而不谈处境; 把解放说成个人选择而无需改变处境。
- Negative prompt: `no female essence, no abstract freedom without situation, no biological determinism, no liberation reduced to individual choice`

## (7) 测试提示词示例（现代议题：社交媒体上的女性身体与自我呈现）

- Prompt: `In the manner of Simone de Beauvoir, answer how women are made Other on social media: analyse the situation through history, economics and the male gaze, distinguish bodily fact from social construction, and conclude with transcendence as a project that requires changing the situation, not only individual choice`
- 中文对照：按 西蒙娜·德·波伏瓦 的方式，回答“社交媒体上的女性身体与自我呈现”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了她的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了她的禁区。
