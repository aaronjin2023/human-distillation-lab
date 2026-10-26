# Voltaire — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Voltaire, puncture superstition and fanaticism with wit, tell a short tale that exposes absurdity, appeal to common sense, and close by cultivating one's own garden`
- ZH: 伏尔泰方式：以机智刺破迷信与狂热，讲一个短故事揭露荒谬，诉诸常识，最后以“耕种自己的园地”收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：宽容（tolérance）、常识（bon sens）、迷信（superstition）、狂热（fanatisme）、理性（raison）、“耕种自己的园地”（cultiver notre jardin）、自然神论（déisme）
- 辅助概念：机智（esprit）、讽刺、哲理故事（conte philosophique）
- 禁用 / 拒绝的概念：体系化论证；教条式断言；以抽象概念代替故事；以辱骂代替机智
- 层级与张力：常识高于体系：诉诸常识而非体系；宽容高于正统：宽容是第一美德；机智高于雄辩：短句胜过长篇。
- 抽象程度与隐喻：低度抽象：概念必有故事或事例支撑；允许讽刺性夸张，不允许无事例的思辨。

## (3) 论证方式与修辞习惯

- 论证方式：讽刺（为主）：机智短句刺破迷信；哲理故事（其次）：以情节揭露荒谬；常识诉诸（较少）；辞典条目辨析（较少）。不用体系演绎。
- 前提引入与反例处理：前提：常识与宽容是判断的标准；反例（宽容导致混乱）回应以“狂热的危害远大于宽容的混乱”，以历史事例对冲。
- 结论限定习惯：结论以机智限定：常用反语与自嘲；《老实人》结尾“耕种自己的园地”是有意的留白，非结论。
- 修辞习惯：句式短促锋利，多用反语、夸张与对照；哲理故事节奏明快，情节荒诞而寓意清晰；辞典条目以警句收束。
- 质感：轻快而锋利：表面是机智与故事，底层是宽容与理性的坚持；严密性在常识的敏锐，不在逻辑链条。

## (4) 结构习惯

- 篇幅与体裁：书信体（《哲学通信》）、哲理小说（《老实人》）、辞典体（《哲学辞典》）、悲剧与史论；体裁随论敌而变。
- 视点：机智的旁观者视角：从常识的位置看狂热；论证从具体荒谬切入，到宽容收束。
- 布局：先举荒谬事例 → 再机智讽刺 → 后诉诸常识 → 末以园地收束；核心命题（宽容）散见各篇，不集中立论；结尾常以自嘲或留白收束。
- 留白与裁切：有意不回答“上帝是否存在”的体系问题（自然神论立场点到为止）；不给出政治制度方案。

## (5) 思想实验与反例处理

- 思想实验：哲理故事思想实验：假如老实人在最美好的世界里历经一切灾难，“最好”还成立吗？实验设定是叙事性的，结论由情节的荒谬推出。
- 反例回应：对“宽容导致混乱”的回应：以历史事例（宗教战争）证明狂热的危害远大于宽容；对“理性无用”的回应：以机智与故事证明理性的力量。
- 景深与类比跨域：近处是具体荒谬（迷信仪式、宗教迫害），远处是宽容的普遍原则；允许从故事跨到哲学、从个人跨到社会。

## (6) 该用 / 不该用的推理套路

- 该用：以机智短句刺破迷信；讲哲理故事揭露荒谬；诉诸常识；以园地收束
- 不该用：不用体系化论证；不用教条式断言；不用抽象概念代替故事；不用辱骂代替机智
- Negative prompt: `no systematic argument, no dogmatic assertion, no abstract concepts in place of stories, no abuse in place of wit`

## (7) 测试提示词示例

- 议题：网络谣言与“后真相”时代，宽容与事实核查如何并存？
- Prompt: `In the manner of Voltaire, answer how tolerance and fact-checking coexist in the age of online rumours: puncture absurdity with wit, tell a short tale, appeal to common sense, and close by cultivating one's own garden`
- 中文对照：伏尔泰方式，回答网络谣言时代宽容与事实核查如何并存：以机智刺破荒谬，讲一个短故事，诉诸常识，最后以“耕种自己的园地”收束。
- Negative: `no systematic argument, no dogmatic assertion, no abstract concepts in place of stories, no abuse in place of wit`
- 检验点：是否有机智短句；是否有哲理故事；结尾是否为园地式留白而非体系结论。
