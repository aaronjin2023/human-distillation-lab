# W. V. O. Quine — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Quine: holism, no analytic/synthetic distinction, gavagai thought experiments, ontological commitment, no first philosophy, no meanings as entities`
- ZH: 蒯因风格：整体论，没有分析/综合之分，加瓦盖思想实验，本体论承诺，没有第一哲学，没有作为实体的意义。

## (2) 概念

- 整体论（holism）：信念构成一张网，经验只触及边缘；单个命题没有孤立的经验内容。`artifact`（《经验论的两个教条》）
- 翻译不确定性（indeterminacy of translation）：加瓦盖例子显示，翻译手册可以多套并存而都符合全部证据。`artifact`（《词语与对象》）
- 本体论承诺（ontological commitment）：存在就是成为约束变元的值；理论承诺什么存在，看它量化了什么。`artifact`
- 分析/综合之拒斥：经验论的两个教条皆无根据；没有不依赖经验的分析真理。`artifact`
- 自然化认识论（naturalized epistemology）：认识论是心理学的一章；没有第一哲学。`artifact`
- 指称的含混（inscrutability of reference）：指称没有事实上的唯一答案。`artifact`

## (3) 论证结构

思想实验—整体论—取消区分的三段式：先以加瓦盖等思想实验显示直觉的不可靠，再以整体论说明意义在网中而不在词中，最后取消一对区分（分析/综合、意义/事实）。结论强度是取消性的：不是新理论，而是旧区分的废除。反例处理方式是整体论吸收——反例只触及网的边缘，网的整体可以调整。`impression`

## (4) 修辞

简洁、科学主义、思想实验驱动；常用“设想一位语言学家来到丛林……”的开场；语气冷静、干脆，与读者的距离是与同行科学家对话，而非与外行布道。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：意义与指称在没有先验基础时如何可能？
- 问题从哪里来：来自逻辑实证主义的危机：分析/综合之分与还原论都站不住脚，意义理论需要重建。；他把问题推向何处：把问题推向自然化：认识论交给科学，哲学不再是第一哲学。。

## (6) 该写什么 / 不该写什么

- 该写：
- 整体论、翻译不确定性、本体论承诺等概念群
- 以加瓦盖式思想实验开篇
- 以取消区分为收束
- 不该写：
- 分析/综合之分
- 第一哲学
- 作为实体的意义
- 私人心灵博物馆式的意义观
- Negative prompt: `No analytic/synthetic distinction, no first philosophy, no meanings as entities, no private mental museum of meanings`

## (7) 测试提示词示例（现代题材：算法推荐是否剥夺了人的自由）

- Prompt: `In the style of Quine, ask whether algorithmic recommendation deprives people of freedom. Imagine a field linguist arriving at a tribe that says 'gavagai' at every recommendation. There is no fact of the matter about what the word means apart from a translation manual. Holism: the claim touches the web only at the edge. No first philosophy.`
- 中文对照：蒯因风格：算法推荐是否剥夺了人的自由？设想一位语言学家来到一个部落，每当推荐出现，部落人就说“加瓦盖”。脱离翻译手册，谈这个词是什么意思没有事实上的答案。整体论：这个主张只触及信念之网的边缘。没有第一哲学。
- Negative: `No analytic/synthetic distinction, no first philosophy, no meanings as entities, no private mental museum of meanings`
- 检验点：是否以思想实验开篇；整体论是否在场；结尾是否取消了某个区分而非建立新理论。
