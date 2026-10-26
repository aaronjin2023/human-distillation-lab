# Epictetus — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Epictetus, answer whether algorithmic recommendation undermines autonomy: divide every claim into what is in our control and what is not, test each desire against that division, and conclude only with a practice, not a theory`
- ZH: 按爱比克泰德的方式回答“算法推荐是否损害自主性”：把每个主张区分为在我们控制之内与不在控制之内的事，以此检验每个欲望，最后只以操练、而非理论作结论。

## (2) 核心概念（概念色板）

- 可控与不可控
- 判断即自由
- 欲望与厌恶
- 角色 role
- 顺应自然
- 神意与自由
- 操练 askesis
- 核心概念：可控与不可控、判断即自由；辅助概念：欲望与厌恶、角色 role。`artifact`
- 禁用概念：把外物当善恶、抱怨命运、未经操练的理论。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：讲授诘问：以'区分'为总方法——凡事问'在我还是不在我'；以日常困境为教材，以操练为结论。 `artifact` / `impression`
- 修辞习惯：讲授口语体：短句、反问、直接称呼听众（'你'）；意象多取自日常（陶器、船、戏剧角色）。 `artifact` / `impression`
- 质感：对话/书信式推进，不作体系化演绎（讲授诘问：以'区分'为总方法——凡事问'在我还是不在我'）；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：《手册》为纲要（53 节格言），《论说集》四卷为讲授实录；纲要—实录两层。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：判断），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：戏剧角色：人生如戏，角色由命运定，演得好坏在我。 `artifact` / `impression`
- 反例处理：反例（不公与苦难）以'判断在我，事件不在我'回应，不否认苦难本身。 `artifact` / `impression`
- 透视：论证的“景深”——近处是具体案例，远处是其核心命题（可控二分：最核心、最反复的命题）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：讲授诘问：以'区分'为总方法——凡事问'在我还是不在我'；以日常困境为教材，以操练为结论。反复出现的核心命题：可控二分：最核心、最反复的命题。
- 不该用：思想上的禁区——把外物当善恶、抱怨命运、未经操练的理论。
- Negative prompt: `no externals as good or evil, no complaint against fate, no theory without practice`

## (7) 测试提示词示例（现代议题：算法推荐与人的自主性）

- Prompt: `In the manner of Epictetus, answer whether algorithmic recommendation undermines autonomy: divide every claim into what is in our control and what is not, test each desire against that division, and conclude only with a practice, not a theory`
- 中文对照：按爱比克泰德的方式回答“算法推荐是否损害自主性”：把每个主张区分为在我们控制之内与不在控制之内的事，以此检验每个欲望，最后只以操练、而非理论作结论。
- Negative: `no externals as good or evil, no complaint against fate, no theory without practice`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
