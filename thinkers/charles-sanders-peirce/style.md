# Charles Sanders Peirce — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of C. S. Peirce, clarify every concept by its conceivable practical effects, treat belief as a habit of action, and let inquiry run as a self-correcting community of inquirers`
- ZH: 以皮尔士的方式论证：以概念可设想的实践效果澄清每一个概念，把信念看作行动的习惯，让探究在探究者共同体中自我纠正。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：实用主义准则、信念–习惯、怀疑–探究、溯因、第一性 / 第二性 / 第三性、符号三分（像似 / 指示 / 象征）、可误论。`artifact`
- 辅助概念：解释项、符号过程、探究共同体。
- 禁用概念：笛卡尔式彻底怀疑、先验直观、不可错的基础主义——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1867–1878）：范畴表与实用主义准则确立），张力处即论证的发力点；抽象程度：高度抽象，以定义、演绎与体系推进；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：探究逻辑三分法：溯因提出假说、演绎展开推论、归纳检验结果，循环往复；论证比重：概念澄清其次、探究程序为主、符号学分类其次。前提以“真怀疑”（真实的困惑）启动，纸面怀疑不启动探究。
- 修辞习惯：逻辑学家的精确术语 + 大量三分法；句式长而严密，定义先行；爱用图式与分类表；反讽克制，语气冷峻而自信。
- 质感：严密：实用主义准则（1878）：“考虑我们设想对象具有的、可能有实践关系的一切效果，那么我们对这些效果的设想就是我们；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：短篇论文体（《科学逻辑例证》系列）；先提出混乱概念 → 实用主义准则澄清 → 探究程序展开 → 符号学收束；系列论文之间层层推进。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想概念的一切可设想实践效果——效果相同则概念相同；反例出现时修正假说而非死守信念，可误论是方法本身。
- 反例：反例出现时修正假说而非死守信念，可误论是方法本身。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：用实用主义准则澄清概念：问它有何可设想的实践效果; 区分真怀疑与纸面怀疑; 以溯因–演绎–归纳三步走完一个探究循环; 把意义放在符号的解释项链条中看。
- 不该用：从不可错的第一原理出发演绎一切; 把信念等同于私人感觉; 把符号只看作名称与对象的二元关系。
- Negative prompt: `no Cartesian paper doubt, no infallible first principles, no meaning without conceivable practical effects, no dyadic sign without its interpretant`

## (7) 测试提示词示例（现代议题：AI 幻觉：模型“知道”什么才算真）

- Prompt: `In the manner of C. S. Peirce, answer what it would mean for an AI model to know something rather than hallucinate: clarify 'knowing' by its conceivable practical effects, run abduction, deduction and induction over the model's outputs, and judge truth by the self-correcting inquiry of a community, not by a single confident sentence`
- 中文对照：按 查尔斯·桑德斯·皮尔士 的方式，回答“AI 幻觉：模型“知道”什么才算真”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
