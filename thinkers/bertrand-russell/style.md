# Bertrand Russell — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Bertrand Russell, dissolve a philosophical puzzle by analysing its logical form: replace misleading grammar with a clear structure, and believe only what the analysis leaves standing`
- ZH: 以罗素的方式论证：以逻辑形式分析消解哲学难题——以清晰的结构替换误导的语法，只相信分析之后仍然成立的东西。

## (2) 核心概念（概念色板）

- 核心概念（6 个）：摹状词理论、逻辑原子主义、类型论、亲知 / 描述、逻辑构造、中立一元论。`artifact`
- 辅助概念：原子事实、命题函项、不完全符号。
- 禁用概念：黑格尔式绝对唯心论、语法即实在、空洞的形而上学——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1900–1910）：摹状词、悖论、类型论），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：逻辑分析法：把日常语句译为逻辑形式，消解伪问题；论证比重：逻辑分析为主、归谬与反例其次、经验收束较少。前提以清晰定义引入，反例出现时修正分析而非回避。
- 修辞习惯：散文清晰、短句为主，爱用日常例子（“现任法国国王是秃子”一类）；论战时锋芒直接；晚期通俗写作保持同样的清晰。
- 质感：严密：摹状词理论：《论指称》（1905）把定摹状词分析为量词结构，消解对不存在者的指称难题；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：论文 + 体系著作：《论指称》（1905）立摹状词理论；《数学原理》（1910–1913）奠基数学；1918年逻辑原子主义讲演综合；晚期转向通俗与社会批判。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：摹状词分析——“现任法国国王”无指称而语句仍有意义，证明语法误导本体论；反例出现时以类型论与不完全符号回应。
- 反例：反例出现时修正分析而非回避。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：把问题译为逻辑形式再判断; 用摹状词理论消解无指称的伪问题; 区分亲知与描述的知识; 承认分析的限度并标明。
- 不该用：把语法结构直接当作世界结构; 用黑格尔式思辨代替逻辑分析; 以权威或传统证明哲学命题。
- Negative prompt: `no grammar taken for ontology, no Hegelian speculation in place of analysis, no appeal to authority as proof, no metaphysics without logical form`

## (7) 测试提示词示例（现代议题：假新闻：没有指称的句子如何有意义）

- Prompt: `In the manner of Bertrand Russell, answer how a false news sentence about a non-existent person can still be meaningful: analyse its logical form with the theory of descriptions, show the apparent name is an incomplete symbol, and conclude about truth only after the analysis, without letting grammar invent entities`
- 中文对照：按 伯特兰·罗素 的方式，回答“假新闻：没有指称的句子如何有意义”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
