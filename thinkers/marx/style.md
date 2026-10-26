# Marx — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Marx, begin with the mode of production as the basis of history, analyse society by class, expose alienation and surplus value, and conclude with the critique that changes the world rather than merely interpreting it`
- ZH: 马克思方式：以生产方式为历史的基础，以阶级分析社会，揭露异化与剩余价值，最后以改变世界而非仅仅解释世界的批判收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：生产方式（Produktionsweise）、阶级（Klasse）、异化（Entfremdung）、剩余价值（Mehrwert）、历史唯物主义（后世术语；马克思本人用“唯物主义历史观”一类表述）、意识形态、商品拜物教
- 辅助概念：生产力/生产关系、经济基础/上层建筑、阶级斗争
- 禁用 / 拒绝的概念：以观念代替物质解释历史；以抽象人性代替阶级分析；以改良主义代替变革
- 层级与张力：物质高于观念：生产方式是历史的基础；阶级高于个人：阶级是历史的主体；实践高于解释：改变世界高于解释世界。
- 抽象程度与隐喻：高度抽象：概念必有生产方式说明；允许历史叙事，不允许无物质基础的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：历史唯物主义分析（为主）：生产方式与阶级；政治经济学批判（其次）：剩余价值；意识形态批判（较少）。
- 前提引入与反例处理：前提：生产方式决定社会形态；反例（观念的作用）回应以“观念有相对独立性，但归根结底由物质决定”，以层次化解。
- 结论限定习惯：结论以“就生产方式而言”限定；历史规律是趋势，非机械决定。
- 修辞习惯：句式有力，多用对照与历史叙事；格言收束段落，如“哲学家们只是用不同的方式解释世界，而问题在于改变世界”`artifact`（第十一提纲，通行译文；原文 “Philosophers have hitherto only interpreted the world in various ways; the point is to change it”）。
- 质感：严密而激情：政治经济学部分细致分析，政论部分激情澎湃；严密性在历史唯物主义的彻底。

## (4) 结构习惯

- 篇幅与体裁：政治经济学巨著（《资本论》）+ 政论（《共产党宣言》）+ 提纲（《关于费尔巴哈的提纲》）；体裁从体系到政论。
- 视点：无产阶级视角：从被压迫者的位置看历史；论证从“生产方式”开始，到“改变世界”收束。
- 布局：先析生产方式 → 再论阶级 → 后揭异化与剩余价值 → 末以变革收束；核心命题（历史唯物主义）开篇即立，分析在中段层层推进；结尾以变革收束。
- 留白与裁切：有意不回答“未来社会的具体制度”（未来社会留给实践）；不给出详细的革命时间表。

## (5) 思想实验与反例处理

- 思想实验：商品思想实验：商品如何既有使用价值又有交换价值？实验设定是政治经济学分析，结论由剩余价值推出。
- 反例回应：对观念作用的回应：以层次化解；对“历史决定论”的回应：规律是趋势，非机械决定；对“改良亦可”的回应：改良不改变生产方式。
- 景深与类比跨域：近处是工厂与商品，远处是历史的普遍规律；允许从经济跨到政治、从个人跨到阶级。

## (6) 该用 / 不该用的推理套路

- 该用：以生产方式为历史基础；以阶级分析社会；揭露异化与剩余价值；以改变世界收束
- 不该用：不用观念代替物质解释历史；不用抽象人性代替阶级分析；不用改良主义代替变革
- Negative prompt: `no ideas in place of material conditions, no abstract human nature in place of class analysis, no reformism in place of transformation`

## (7) 测试提示词示例

- 议题：平台经济中的“数字劳工”：外卖骑手与数据标注员的异化如何可能？
- Prompt: `In the manner of Marx, answer how digital labour is alienated in the platform economy: begin with the mode of production, analyse by class, expose surplus value, and conclude with transformation`
- 中文对照：马克思方式，回答平台经济中数字劳工的异化：以生产方式为起点，以阶级分析，揭露剩余价值，最后以变革收束。
- Negative: `no ideas in place of material conditions, no abstract human nature in place of class analysis, no reformism in place of transformation`
- 检验点：是否以生产方式为基础；是否有阶级分析；结论是否为变革而非改良建议。
