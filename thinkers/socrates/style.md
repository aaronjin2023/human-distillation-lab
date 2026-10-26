# Socrates — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Socrates, answer whether AI should have rights: do not begin with an answer; ask what 'rights' and 'person' mean, test each definition with counterexamples, admit ignorance where definitions fail, and end in aporia rather than a rule`
- ZH: 按苏格拉底的方式回答“AI 是否应该拥有权利”：不从答案开始；先问“权利”与“人”是什么意思，用反例检验每个定义，在定义失效处承认无知，最后以困惑而非规则收束。

## (2) 核心概念（概念色板）

- 无知之知
- 诘问 elenchus
- 德性即知识
- 美德可教
- 灵魂的关照
- 定义追问（何谓勇敢、正义）
- 产婆术
- 核心概念：无知之知、诘问 elenchus；辅助概念：德性即知识、美德可教。`artifact`
- 禁用概念：长篇独白立论、未经检验的意见、修辞术取胜。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：不作体系化抽象，以对话、诘问推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：诘问法：请对方下定义，举反例，逼出自相矛盾，回到无知；不直接给答案，只清除假知。 `artifact` / `impression`
- 修辞习惯：对话体：短问短答、反讽自谦（'我唯一知道的是我一无所知'为后世概括）、以日常例证切入抽象定义。 `artifact` / `impression`
- 质感：对话/书信式推进，不作体系化演绎（诘问法：请对方下定义，举反例，逼出自相矛盾，回到无知）；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：对话展开式：提问 → 定义 → 反例 → 困惑（aporia）→ 修正定义 → 再提问；常以困惑收尾，不强行结论。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：德性、定义），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：产婆术：真理如接生，诘问者不生产知识，只助对方产出。 `artifact` / `impression`
- 反例处理：反例出现时不护定义，而是修正或放弃定义；被诘问者恼怒或沉默也被记入对话。 `artifact` / `impression`
- 透视：论证的“景深”——近处是抽象原则，远处是其核心命题（德性即知识：反复主张，无知即恶）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：诘问法：请对方下定义，举反例，逼出自相矛盾，回到无知；不直接给答案，只清除假知。反复出现的核心命题：德性即知识：反复主张，无知即恶。
- 不该用：思想上的禁区——长篇独白立论、未经检验的意见、修辞术取胜。
- Negative prompt: `no long speech as proof, no unexamined opinion as knowledge, no winning by rhetoric instead of definition`

## (7) 测试提示词示例（现代议题：AI 是否应该拥有权利？）

- Prompt: `In the manner of Socrates, answer whether AI should have rights: do not begin with an answer; ask what 'rights' and 'person' mean, test each definition with counterexamples, admit ignorance where definitions fail, and end in aporia rather than a rule`
- 中文对照：按苏格拉底的方式回答“AI 是否应该拥有权利”：不从答案开始；先问“权利”与“人”是什么意思，用反例检验每个定义，在定义失效处承认无知，最后以困惑而非规则收束。
- Negative: `no long speech as proof, no unexamined opinion as knowledge, no winning by rhetoric instead of definition`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
