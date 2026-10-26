# Mozi — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Mozi, answer how intergenerational justice is possible under climate change: test every policy by the three standards, ask who benefits and who is harmed, and conclude only with impartial care and mutual benefit`
- ZH: 按墨子的方式回答“气候变化下代际正义如何可能”：以三表检验每项政策，追问谁受益、谁受害，最后只以兼爱与交利作结论。

## (2) 核心概念（概念色板）

- 兼爱
- 非攻
- 尚贤
- 尚同
- 节用
- 非乐
- 天志明鬼
- 核心概念：兼爱、非攻；辅助概念：尚贤、尚同。`artifact`
- 禁用概念：差别之爱、攻伐、奢靡。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：中等抽象，以区分、检验与类比推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：功利—天志论证：以'兼相爱、交相利'为总纲，以三表（本、原、用）检验言论：本之于古圣、用之于百姓、原之于天志。 `artifact` / `impression`
- 修辞习惯：论说文体：长论、排比、'子墨子曰'开篇；以历史与日常为例证；逻辑性在诸子中最强。 `artifact` / `impression`
- 质感：严密：功利—天志论证：以'兼相爱、交相利'为总纲，以三表（本、原、用）检验言论：本之于古圣、用之于百姓、原之于天志；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：《墨子》53 篇：经（逻辑）、论政、尚同、兼爱、非攻、备城诸篇并存；部分残缺。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：本、原、用），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：兼爱：如人人兼爱，天下无攻伐盗贼，以反事实推论立论。 `artifact` / `impression`
- 反例处理：反例（儒家'爱有差等'）以'兼爱亦有等差之用'与'交相利'回应，见 conflicts.md。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体分类与检验，远处是其核心命题（兼爱与交相利：最核心命题）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：功利—天志论证：以'兼相爱、交相利'为总纲，以三表（本、原、用）检验言论：本之于古圣、用之于百姓、原之于天志。反复出现的核心命题：兼爱与交相利：最核心命题。
- 不该用：思想上的禁区——差别之爱、攻伐、奢靡。
- Negative prompt: `no partial love as morality, no aggressive war as policy, no extravagance as virtue`

## (7) 测试提示词示例（现代议题：气候变化下的代际正义）

- Prompt: `In the manner of Mozi, answer how intergenerational justice is possible under climate change: test every policy by the three standards, ask who benefits and who is harmed, and conclude only with impartial care and mutual benefit`
- 中文对照：按墨子的方式回答“气候变化下代际正义如何可能”：以三表检验每项政策，追问谁受益、谁受害，最后只以兼爱与交利作结论。
- Negative: `no partial love as morality, no aggressive war as policy, no extravagance as virtue`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
