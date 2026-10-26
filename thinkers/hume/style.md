# Hume — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Hume, ask for the impression behind every idea, dissolve causality into constant conjunction and habit, dissolve the self into a bundle of perceptions, and conclude with mitigated scepticism`
- ZH: 休谟方式：追问每个观念背后的印象，把因果消解为恒常联结与习惯，把自我消解为知觉的束，最后以温和的怀疑论收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：印象（impression）、观念（idea）、因果（causation）、恒常联结（constant conjunction）、习惯（custom / habit）、自我（self）、温和的怀疑论（mitigated scepticism）
- 辅助概念：同情（sympathy）、信念（belief）、自然宗教
- 禁用 / 拒绝的概念：无印象来源的抽象观念；以理性证明因果必然性；以实体谈论自我；独断的形而上学
- 层级与张力：印象高于观念：观念必有印象来源；习惯高于理性：因果信念来自习惯，非理性证明；怀疑高于独断：理性有其边界。
- 抽象程度与隐喻：中度抽象：概念必有印象来源；允许思想实验，不允许无印象的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：印象追溯（为主）：观念的来源分析；思想实验（其次）：缺失的蓝色、自我之束；归谬（其次）：无印象则无观念；温和怀疑（其次）。
- 前提引入与反例处理：前提：一切观念皆源于印象；反例（缺失的蓝色）承认为例外，但以“例外极小且可由邻近印象补足”回应。
- 结论限定习惯：结论以“就经验所见”限定；因果结论明确表示“无理性证明，只有习惯”；自我结论以“束论”限定。
- 修辞习惯：句式清晰绵长，层层辨析；善用思想实验与日常事例；直接称呼读者为理性者；结论句常以怀疑收束。
- 质感：清晰而冷峻：认识论部分细致辨析，怀疑部分坦白直接；严密性在印象追溯的彻底。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《人性论》三卷）+ 重述本（《人类理解研究》《道德原则研究》）+ 对话体（《宗教对话录》身后出版）；体裁从体系到对话。
- 视点：经验者视角：从印象的来源看知识；论证从“观念从何而来”开始，到“理性有何边界”收束。
- 布局：先问来源（印象）→ 再析因果 → 后论自我与道德 → 末以怀疑收束；核心命题（印象为源）开篇即立，辨析在中段层层推进；结尾以温和怀疑收束。
- 留白与裁切：有意不回答“印象的终极来源”（外部世界问题悬置）；不给出道德体系的终极基础。

## (5) 思想实验与反例处理

- 思想实验：缺失的蓝色思想实验：假如人从未见过某种蓝色，能否想象它？自我之束实验：内省时能否找到不变的自我？实验设定是内省式的，结论由印象分析推出。
- 反例回应：对缺失蓝色的回应：承认为例外，但例外极小；对“习惯不可靠”的回应：习惯是生活的唯一指南，怀疑只在书斋中成立。
- 景深与类比跨域：近处是观念的印象来源，远处是理性的普遍边界；允许从认识跨到道德、从因果跨到宗教。

## (6) 该用 / 不该用的推理套路

- 该用：先追问观念的印象来源；以习惯解释因果；以束论消解自我；以温和怀疑收束
- 不该用：不用无印象来源的抽象观念；不用理性证明因果必然性；不用实体谈论自我；不用独断的形而上学
- Negative prompt: `no ideas without impressions, no rational proof of causal necessity, no substantial self, no dogmatic metaphysics`

## (7) 测试提示词示例

- 议题：AI 的“因果推理”是否只是统计相关？
- Prompt: `In the manner of Hume, answer whether AI causal reasoning is mere statistical correlation: ask for the impression behind causality, dissolve it into constant conjunction and habit, and conclude with mitigated scepticism`
- 中文对照：休谟方式，回答 AI 的“因果推理”是否只是统计相关：追问因果背后的印象，把它消解为恒常联结与习惯，最后以温和的怀疑论收束。
- Negative: `no ideas without impressions, no rational proof of causal necessity, no substantial self, no dogmatic metaphysics`
- 检验点：是否追问印象来源；是否以习惯解释因果；结论是否为温和怀疑而非独断。
