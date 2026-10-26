# Frantz Fanon — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Frantz Fanon, start from the lived experience of the colonized body: the colony splits the soul, decolonization must remake the human, and national consciousness must not rot into a national bourgeoisie`
- ZH: 以法农的方式论证：从被殖民身体的切身经验出发——殖民撕裂灵魂，去殖民必须重造新人，民族意识绝不能腐化为民族资产阶级。

## (2) 核心概念（概念色板）

- 核心概念（6 个）：黑皮肤、白面具、去殖民、民族意识、殖民精神病理学、暴力论争、新人。`artifact`
- 辅助概念：语言与异化、第三世界。
- 禁用概念：殖民心理学的温情、去殖民即换旗、民族资产阶级的继承——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1952）：《黑皮肤，白面具》，殖民心理），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：临床经验 + 政治论证：先以精神病学个案揭示殖民异化，再以政治分析推向去殖民；论证比重：临床与经验描述为主、政治分析为主、号召其次。反例出现时以殖民地的具体处境回应。
- 修辞习惯：论述体锋利、短句密集，夹以临床个案与哲学命题；爱用“必须”“只有”一类决断句式；语气急切，有战地写作的紧迫感。
- 质感：未展开，见 known_gaps；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《黑皮肤，白面具》（1952）论殖民心理；《大地上的受苦者》（1961）论去殖民、暴力与民族意识；《垂死的殖民主义》论阿尔及利亚革命中的社会变迁。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想一个黑人戴上白面具说流利法语，他获得了什么、失去了什么——以此揭示语言异化；反例出现时回到临床经验。
- 反例：反例出现时以殖民地的具体处境回应。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：从被殖民者的切身经验出发; 以临床个案检验政治命题; 区分去殖民与换旗; 警惕民族资产阶级对独立的窃取。
- 不该用：把殖民问题说成心理问题而无关政治; 把去殖民等同于独立仪式; 以温情调解代替结构变革。
- Negative prompt: `no colonialism as a merely psychological problem, no decolonization as a flag-changing ceremony, no national bourgeoisie inheriting independence, no reconciliation without structural change`

## (7) 测试提示词示例（现代议题：数据殖民主义：算法时代的去殖民）

- Prompt: `In the manner of Frantz Fanon, answer what data colonialism does to the colonized: start from the lived experience of being classified and scored, show how the mask is now worn in data, and conclude that decolonization must remake the human and the infrastructure, not merely change the flag`
- 中文对照：按 弗朗茨·法农 的方式，回答“数据殖民主义：算法时代的去殖民”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
