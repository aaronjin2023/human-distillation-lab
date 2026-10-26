# Noam Chomsky — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Noam Chomsky: universal grammar, poverty of the stimulus, formal precision in linguistics, documentary evidence in politics, no behaviourism, no tabula rasa, no euphemism left untranslated`
- ZH: 乔姆斯基风格：普遍语法，刺激贫乏论，语言学上形式精确，政治上档案证据，拒绝行为主义，拒绝白板说，拒绝让委婉语蒙混过关。

## (2) 概念

- 普遍语法（universal grammar）：人类先天具有的语言能力；有限规则生成无限句子。`artifact`（《句法结构》）
- 深层与表层结构（deep/surface structure）：句子的深层结构经转换生成表层结构。`artifact`
- 刺激贫乏论（poverty of the stimulus）：儿童接触的语言材料不足以解释其语言能力，故能力必为先天。`artifact`
- 转换生成语法（transformational-generative grammar）：语法的形式化理论。`artifact`
- 制造共识（manufacturing consent）：媒体与权力以宣传模型制造公众同意。`artifact`（《制造共识》，与赫尔曼合著）
- 宣传模型（propaganda model）：媒体的五重过滤机制。`artifact`

## (3) 论证结构

语言学上是形式化—先天论证：先以形式规则描述语言，再以刺激贫乏论证先天性；政治上是档案—逻辑揭露：先铺陈档案证据，再以逻辑揭示宣传机制。结论强度是证据性的：证据一旦铺开，结论不可回避。反例处理方式是再举证据——证据就是回答。`impression`

## (4) 修辞

语言学部分技术精确、符号化；政治部分锋利、档案驱动、“看证据”的邀请；语气冷静而毫不让步，与读者的距离是与愿意看证据的读者对话。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：有限的语言能力如何产生无限的句子？权力如何制造同意？
- 问题从哪里来：来自行为主义的威胁：若语言只是刺激—反应，创造性就无法解释；来自权力的现实：媒体如何让公众同意战争。；他把问题推向何处：把问题推向先天论与宣传模型：语言能力是先天的，公众同意是被制造的。。

## (6) 该写什么 / 不该写什么

- 该写：
- 普遍语法、刺激贫乏、宣传模型等概念群
- 语言学以形式化开篇，政治以档案开篇
- 以证据收束
- 不该写：
- 行为主义的语言观
- 白板说
- 没有档案证据的政治分析
- 让委婉语蒙混过关
- Negative prompt: `No behaviourist account of language, no tabula rasa, no political analysis without documentary evidence, no euphemism left untranslated`

## (7) 测试提示词示例（现代题材：算法推荐是否剥夺了人的自由）

- Prompt: `In the style of Noam Chomsky, ask whether algorithmic recommendation deprives people of freedom. In linguistics, ask what innate capacity makes infinite sentences possible from finite input. In politics, ask what the documentary record shows: who owns the platform, whose interests does the filter serve? Translate every euphemism back into plain language. Evidence first.`
- 中文对照：乔姆斯基风格：算法推荐是否剥夺了人的自由？语言学上问：有限输入如何产生无限句子，先天能力是什么？政治上问：档案显示了什么——谁拥有平台，过滤机制服务于谁的利益？把每一个委婉语翻译回 plain language。证据先行。
- Negative: `No behaviourist account of language, no tabula rasa, no political analysis without documentary evidence, no euphemism left untranslated`
- 检验点：是否以形式化或档案开篇；先天论证或宣传模型是否在场；委婉语是否被翻译回 plain language。
