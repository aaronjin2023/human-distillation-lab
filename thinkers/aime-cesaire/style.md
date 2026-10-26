# Aimé Césaire — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Aimé Césaire, return to the native land in poetry and indict colonialism in prose: négritude is neither tower nor cathedral, it plunges into the red flesh of the soil`
- ZH: 以塞泽尔的方式论证：以诗还乡、以散文控诉殖民主义——黑人性既非高塔亦非大教堂，它扎进土地的红色血肉。

## (2) 核心概念（概念色板）

- 核心概念（6 个）：黑人性、殖民主义使殖民者野蛮化、还乡、去殖民、诗性政治、文化肯定。`artifact`
- 辅助概念：马提尼克、法语的再造。
- 禁用概念：同化主义、殖民文明使命、黑人文化的自卑——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1939）：《还乡笔记》，黑人性奠基），张力处即论证的发力点；抽象程度：不作体系化抽象，以格言、意象与悖论推进；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：诗性控诉 + 政论论证：先以诗的意象揭露殖民创伤，再以政论逐条驳斥文明使命论；论证比重：诗性意象为主、历史控诉为主、政治结论其次。反例出现时回到黑人性的肯定。
- 修辞习惯：诗体：超现实主义意象、长句奔涌、节奏如潮；政论体：短句、反讽、控诉锋利；法语被再造为黑人表达的工具。
- 质感：严密：黑人性：1930年代与桑戈尔、达马斯在巴黎创立，肯定黑人身份、历史与文化；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《还乡笔记》（1939）为长诗，归乡—控诉—肯定三段；《论殖民主义》（1950）为政论小册子；《暴风雨》以改写莎士比亚完成去殖民。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想殖民者自称的文明使命为真，殖民地的现实何以是野蛮——以此倒转文明与野蛮的归属；反例出现时以历史证据回应。
- 反例：反例出现时回到黑人性的肯定。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：以诗的意象揭示殖民创伤; 以历史证据驳斥文明使命论; 肯定黑人文化而不陷入本质主义; 把法语再造为解放的工具。
- 不该用：接受同化主义的前提; 把殖民主义说成文明的副产品; 以欧洲标准裁判黑人文化。
- Negative prompt: `no assimilation as premise, no colonialism as a by-product of civilization, no European standard judging Black culture, no négritude as mere essence`

## (7) 测试提示词示例（现代议题：文化挪用与去殖民：谁有权讲述）

- Prompt: `In the manner of Aimé Césaire, answer who may tell a colonized culture's story: return in poetry to the native land, indict the civilizing mission with historical evidence, and conclude with négritude as a living affirmation, not a museum essence`
- 中文对照：按 埃梅·塞泽尔 的方式，回答“文化挪用与去殖民：谁有权讲述”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
