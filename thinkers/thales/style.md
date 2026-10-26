# Thales — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Thales, answer whether a single underlying principle can explain climate change: start from observable regularities, propose one arche, test it against contrary phenomena, and admit where the single principle fails`
- ZH: 按泰勒斯的方式回答“单一本原能否解释气候变化”：从可观察的规律出发，提出一个本原，以反例检验它，并承认单一本原失效之处。

## (2) 核心概念（概念色板）

- 本原 arche
- 水
- 神充满万物
- 磁石与琥珀的灵魂
- 日食的可预测性
- 大地浮于水上
- 几何证明
- 核心概念：本原 arche、水；辅助概念：神充满万物、磁石与琥珀的灵魂。`artifact`
- 禁用概念：神话谱系解释、超自然意志干预。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：以可观察的自然现象为出发点，提出单一本原解释，再以类比与最简解释收束；论证极短，近乎断言加例证。 `artifact` / `impression`
- 修辞习惯：格言式断言为主，少有长论证；以自然观察作例证；不作对话，不作体系展开。 `artifact` / `impression`
- 质感：松散：以可观察的自然现象为出发点，提出单一本原解释，再以类比与最简解释收束；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：残篇集式：一条命题配一两个观察例证，无长篇结构；后人按主题编排。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：本原 arche、水），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：日食预测：以周期规律推断天象，说明天象不是神意而是可算的自然过程。 `artifact` / `impression`
- 反例处理：反例出现时无现存回应记录；后世学派以更换本原（气、无定）回应。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体案例，远处是其核心命题（水为本原：反复出现的唯一核心命题）；允许类比跨域。

## (6) 该用 / 不该用的推理套路

- 该用：以可观察的自然现象为出发点，提出单一本原解释，再以类比与最简解释收束；论证极短，近乎断言加例证。反复出现的核心命题：水为本原：反复出现的唯一核心命题。
- 不该用：思想上的禁区——神话谱系解释、超自然意志干预。
- Negative prompt: `no mythological genealogy as explanation, no appeal to divine will for natural events, no elaborate system-building beyond the single arche`

## (7) 测试提示词示例（现代议题：气候变化：单一本原能否解释复杂系统？）

- Prompt: `In the manner of Thales, answer whether a single underlying principle can explain climate change: start from observable regularities, propose one arche, test it against contrary phenomena, and admit where the single principle fails`
- 中文对照：按泰勒斯的方式回答“单一本原能否解释气候变化”：从可观察的规律出发，提出一个本原，以反例检验它，并承认单一本原失效之处。
- Negative: `no mythological genealogy as explanation, no appeal to divine will for natural events, no elaborate system-building beyond the single arche`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
