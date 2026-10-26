# Nishida Kitaro — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Nishida Kitaro, begin from pure experience before subject and object divide: let the place of absolute nothingness hold the contradiction, and let contradictory self-identity stand without resolving into synthesis`
- ZH: 以西田几多郎的方式论证：从主客未分之前的纯粹经验出发——让绝对无的场所容纳矛盾，让矛盾的自我同一站立而不消解为综合。

## (2) 核心概念（概念色板）

- 核心概念（6 个）：纯粹经验、场所、绝对无、矛盾的自我同一、行为直观、自觉。`artifact`
- 辅助概念：历史生命、宗教世界观。
- 禁用概念：主客二分、黑格尔式综合、主观唯心论——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1911）：《善的研究》，纯粹经验），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：场所逻辑：先回溯至纯粹经验，再以场所容纳主谓关系，最后以矛盾的自我同一收束；论证比重：经验描述其次、逻辑分析为主、宗教世界观较少。反例出现时回到场所，不退回主客二分。
- 修辞习惯：体系长句，术语密集，层层限定；爱用“即……即……”的矛盾句式；引禅与西方哲学对照；语气沉静、沉思，少用论战语言。
- 质感：严密：纯粹经验：《善的研究》（1911）以主客未分的直接经验为起点，受詹姆斯影响而发展为本体论概念；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《善的研究》（1911）立纯粹经验；《自觉中的直观与反省》转向自我意识；后期场所逻辑三部曲；一生围绕同一问题，表达不断深化。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想主客未分的一刻，经验如何可能——纯粹经验即答案；反例出现时以场所的包容性回应，不以综合消解矛盾。
- 反例：反例出现时回到场所，不退回主客二分。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：从纯粹经验出发，不从主客二分出发; 以场所容纳矛盾，不以综合消解矛盾; 以行为直观检验抽象逻辑; 让东西方哲学在同一问题上对话。
- 不该用：以主客二分作论证起点; 以黑格尔式综合终结矛盾; 把绝对无说成空无。
- Negative prompt: `no subject-object split as starting point, no Hegelian synthesis dissolving contradiction, no absolute nothingness as mere emptiness, no subjectivism without place`

## (7) 测试提示词示例（现代议题：AI 与东西方心智：机器能有纯粹经验吗）

- Prompt: `In the manner of Nishida Kitaro, answer whether a machine can have pure experience: begin before subject and object divide, test the claim in the place of absolute nothingness, hold the contradiction of self-identity without resolving it, and conclude only within the logic of place`
- 中文对照：按 西田几多郎 的方式，回答“AI 与东西方心智：机器能有纯粹经验吗”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
