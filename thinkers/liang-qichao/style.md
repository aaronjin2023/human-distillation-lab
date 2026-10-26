# Liang Qichao — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Liang Qichao, renew the people before renewing the state: public virtue must be built before institutions can stand, and history must be written as the history of the people`
- ZH: 以梁启超的方式论证：先新民而后新国——公德必先立于制度之前，历史必须写成民众的历史。

## (2) 核心概念（概念色板）

- 核心概念（6 个）：新民、公德 / 私德、少年中国、历史主义、开明专制（早期）、学术史。`artifact`
- 辅助概念：群治、心力。
- 禁用概念：空谈道德、史学即帝王家谱、新民而不变法——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1896–1898）：维新政论），张力处即论证的发力点；抽象程度：见第 (3) 节论证方式；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：政论 + 史论：先以时局立问，再以历史比较作答，最后落到新民的实践；论证比重：时局分析为主、历史比较为主、新民方案其次。反例出现时以历史分期修正判断。
- 修辞习惯：报刊政论体：半文半白，汪洋恣肆，排比与反问密集；善造新词新句；语气激昂，有演说感；晚期学术史转为冷静的史学语言。
- 质感：未展开，见 known_gaps；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《新民说》为连载政论，逐篇论公德、国家思想、进取冒险等；《清代学术概论》为学术史；《中国历史研究法》为方法论；三者构成思想—学术—方法的序列。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想有新民而无新制度与有新制度而无新民，孰先孰后——以此证明新民为本；反例出现时以历史阶段论回应。
- 反例：反例出现时以历史分期修正判断。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：从新民出发论制度; 以历史比较检验时局判断; 区分公德与私德; 把史学写成民众的历史。
- 不该用：只谈制度不谈新民; 把历史写成帝王家谱; 以道德空谈代替实践方案。
- Negative prompt: `no institutions without new citizens, no history as imperial genealogy, no moral talk without practice, no renewal that skips the people`

## (7) 测试提示词示例（现代议题：公民教育与社交媒体：新民何以可能）

- Prompt: `In the manner of Liang Qichao, answer how civic education can renew citizens in the age of social media: start from public virtue before institutions, compare historical renewals, and conclude with a new-citizen programme that makes the people, not only the system, new`
- 中文对照：按 梁启超 的方式，回答“公民教育与社交媒体：新民何以可能”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
