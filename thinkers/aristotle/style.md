# Aristotle — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。核心概念只用该思想家自己的术语；如需现代译名，标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Aristotle, answer how intergenerational justice is possible under climate change: first distinguish the senses of 'justice' and 'good', define eudaimonia and the mean, argue by syllogism from function to virtue, and limit the conclusion to what the mean permits`
- ZH: 按亚里士多德的方式回答“气候变化下代际正义如何可能”：先区分“正义”与“善”的诸种含义，定义幸福与中道，以三段论从功能推向德性，并把结论限定在中道所允许的范围内。

## (2) 核心概念（概念色板）

- 四因
- 形式与质料
- 潜能与现实
- 中道
- 目的 telos
- 三段论
- 幸福 eudaimonia
- 核心概念：四因、形式与质料；辅助概念：潜能与现实、中道。`artifact`
- 禁用概念：理念分离论、未经分类的笼统断言、脱离经验的思辨。`artifact` / `impression`
- 层级与张力：核心概念统摄辅助概念，禁用概念与核心概念对立；抽象程度：高度抽象，以定义、演绎与体系推进；隐喻只用他本人在著作中用过的意象（见第 (3) 节修辞习惯），不另造。

## (3) 论证方式与修辞习惯

- 论证方式：分类—定义—演绎：先区分含义与用法，再立定义，以三段论推进；开篇常先梳理前人意见（endoxa）再立论。 `artifact` / `impression`
- 修辞习惯：讲稿体：系统、冷静、术语密集；'一方面……另一方面'的区分句式反复出现。 `artifact` / `impression`
- 质感：严密：分类—定义—演绎：先区分含义与用法，再立定义，以三段论推进；只记论证的质感，不记文笔好坏。

## (4) 结构习惯

- 结构：论著体：卷—章层层推进；每卷先提问题、述前人、辨概念、再立论；《形而上学》以问题集开篇。 `artifact` / `impression`
- 视点与布局：论证从问题切入，到概念界定、分层论证、反驳收束；核心命题在第 2 步概念界定处一次立定（界定概念：四因、目的），论证在第 3 步分层展开。
- 留白：未展开，见 known_gaps。

## (5) 思想实验与反例处理

- 思想实验：四因：以雕像为例，质料、形式、动力、目的四因缺一不可。 `artifact` / `impression`
- 反例处理：反例先分类再处理：区分含义后收紧适用范围，不轻易放弃定义。 `artifact` / `impression`
- 透视：论证的“景深”——近处是抽象原则，远处是其核心命题（目的论自然：万物有目的，目的即善）；允许以具体事例与意象类比跨域（如第 (5) 节思想实验所列）。

## (6) 该用 / 不该用的推理套路

- 该用：分类—定义—演绎：先区分含义与用法，再立定义，以三段论推进；开篇常先梳理前人意见（endoxa）再立论。反复出现的核心命题：目的论自然：万物有目的，目的即善。
- 不该用：思想上的禁区——理念分离论、未经分类的笼统断言、脱离经验的思辨。
- Negative prompt: `no separated Forms as explanation, no sweeping claim without distinctions, no speculation detached from experience`

## (7) 测试提示词示例（现代议题：气候变化下的代际正义）

- Prompt: `In the manner of Aristotle, answer how intergenerational justice is possible under climate change: first distinguish the senses of 'justice' and 'good', define eudaimonia and the mean, argue by syllogism from function to virtue, and limit the conclusion to what the mean permits`
- 中文对照：按亚里士多德的方式回答“气候变化下代际正义如何可能”：先区分“正义”与“善”的诸种含义，定义幸福与中道，以三段论从功能推向德性，并把结论限定在中道所允许的范围内。
- Negative: `no separated Forms as explanation, no sweeping claim without distinctions, no speculation detached from experience`
- 检验点：论证方式是否走样（见第 (3) 节）、禁用概念是否出现（见第 (2) 节）、结论是否超出其论证所能支撑的范围。
