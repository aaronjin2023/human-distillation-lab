# Ludwig Wittgenstein — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Ludwig Wittgenstein, do not explain language from outside: look at its use in a language-game, notice the family resemblances, and let the philosophical problem dissolve whereof one cannot speak`
- ZH: 以维特根斯坦的方式论证：不要从外部解释语言——看它在语言游戏中的使用，注意家族相似，让哲学问题在不可言说处自行消解。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：图像论、语言游戏、意义即使用、家族相似、生活形式、私人语言论证、说 / 显示。`artifact`
- 辅助概念：遵守规则、确定性、语法考察。
- 禁用概念：语言的本质定义、私人语言、形而上学的使用——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1921）：《逻辑哲学论》，图像论），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：治疗式考察：不建理论，只描述使用——提出日常例子、设想语言游戏、指出类比误导；论证比重：例子与设想为主、类比批判其次、格言收束较少。反例出现时换一个语言游戏再看。
- 修辞习惯：编号命题（前期）与对话式评注（后期）；短句、反问、自问自答；爱用“设想……”“看看……”的邀请句式；格言收束，如“对于不可说的东西，必须保持沉默”`artifact`（《逻辑哲学论》末句，通行译文）。
- 质感：松散：图像论：前期命题是事实的图像，语言与世界共享逻辑形式；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：前期《逻辑哲学论》（1921）为编号命题树，图像论一以贯之；后期《哲学研究》（1953年身后刊）为评注集，无体系结构，以“考察”推进；前后两期构成自我反驳。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：建筑工人甲乙只用“石块、柱子、石板、横梁”四词——意义在活动中显现；私人语言设想：为私人感觉记日记，何以无规则可言；反例即方法。
- 反例：反例出现时换一个语言游戏再看。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：问一个词在哪个语言游戏中如何使用; 以家族相似代替本质定义; 设想简单的语言游戏再回到复杂用法; 区分说与显示。
- 不该用：追问语言的唯一本质; 设想脱离公共使用的私人语言; 用科学标准裁判宗教、伦理语言游戏。
- Negative prompt: `no essence of language, no private language, no theory that explains use from outside, no judging one language-game by another's rules`

## (7) 测试提示词示例（现代议题：AI 语言模型“理解”语言吗）

- Prompt: `In the manner of Ludwig Wittgenstein, answer whether a language model understands language: do not ask for an inner essence of understanding, look at the language-games the model plays, compare them with human forms of life, and show where the analogy with understanding holds and where it breaks down`
- 中文对照：按 路德维希·维特根斯坦 的方式，回答“AI 语言模型“理解”语言吗”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
