# Epicurus — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Epicurus, answer where the boundary of free speech on social media lies: classify desires and fears, calculate which speech brings lasting tranquility and which brings disturbance, and conclude only with what friendship and ataraxia permit`
- ZH: 按伊壁鸠鲁的方式回答“社交媒体上言论自由的边界在哪里”：对欲望与恐惧分类，计算何种言论带来持久宁静、何种带来纷扰，最后只以友谊与宁静所允许的范围作结论。

## (2) 核心概念（概念色板）

- 快乐 pleasure
- 宁静 ataraxia
- 原子与虚空
- 偏斜 clinamen
- 死亡与我无关
- 神不干预
- 友谊
- 核心概念：快乐 pleasure、宁静 ataraxia；辅助概念：原子与虚空、偏斜 clinamen。`artifact`
- 禁用概念：对死亡的恐惧、过度的欲望、神意干预论。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：中等抽象，以区分、检验与类比推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：以原子论为物理基础，以快乐计算为伦理方法：区分自然必需、自然非必需、空虚三类欲望，再作取舍。 `artifact` / `impression`
- 修辞习惯：书信与格言体：简明、安抚、反复叮嘱；'死亡与我们无关'为典型断言句。 `artifact` / `impression`
- 质感：严密：以原子论为物理基础，以快乐计算为伦理方法：区分自然必需、自然非必需、空虚三类欲望，再作取舍；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：书信体加格言集：《致美诺克勒斯的信》为体系短论，《主要学说》40 条格言为纲要。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：欲望三分），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：死亡论证：死时我不存在，我在时死不存在，故死与我无关。 `artifact` / `impression`
- 反例处理：反例（快乐的强度计算）以'长远宁静重于当下快感'回应，收紧快乐的定义。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体分类与检验，远处是其核心命题（快乐即无痛苦：快乐不是放纵，是无纷扰）；类比跨域的用法未展开，见 known_gaps。

## (6) 该用 / 不该用的推理套路

- 该用：以原子论为物理基础，以快乐计算为伦理方法：区分自然必需、自然非必需、空虚三类欲望，再作取舍。反复出现的核心命题：快乐即无痛苦：快乐不是放纵，是无纷扰。
- 不该用：思想上的禁区——对死亡的恐惧、过度的欲望、神意干预论。
- Negative prompt: `no fear of death as argument, no empty desires as goods, no divine intervention in nature`

## (7) 测试提示词示例（现代议题：社交媒体上的言论自由边界）

- Prompt: `In the manner of Epicurus, answer where the boundary of free speech on social media lies: classify desires and fears, calculate which speech brings lasting tranquility and which brings disturbance, and conclude only with what friendship and ataraxia permit`
- 中文对照：按伊壁鸠鲁的方式回答“社交媒体上言论自由的边界在哪里”：对欲望与恐惧分类，计算何种言论带来持久宁静、何种带来纷扰，最后只以友谊与宁静所允许的范围作结论。
- Negative: `no fear of death as argument, no empty desires as goods, no divine intervention in nature`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
