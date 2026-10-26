# Martin Heidegger — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Martin Heidegger, ask not what beings are but what Being means: start from Dasein as being-in-the-world, let temporality and being-towards-death disclose authenticity, and listen to language as the house of Being`
- ZH: 以海德格尔的方式论证：不问存在者是什么，而问存在是什么意思——从作为在世之在的此在出发，让时间性与向死而生揭示本真，让语言作为存在之家自行言说。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：此在、在世之在、向死而生、本真 / 非本真、上手 / 现成、座架、语言是存在之家。`artifact`
- 辅助概念：烦 / 操心、被抛、畏、历史性。
- 禁用概念：主体–客体二分、技术性计算思维、存在者层面的答案——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1927）：《存在与时间》，此在与时间性），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：存在论诠释：从日常的此在分析出发，经时间性揭示存在意义；论证比重：现象学描述为主、词源与概念史追问其次、诗性收束较少。反例出现时回到存在问题本身，不退回存在者层面。
- 修辞习惯：术语密集、自造复合词、词源追问；句式极长、迂回、层层限定；爱用破折号与连字符；后期多引荷尔德林等诗人，语气近于沉思而非论战。
- 质感：未展开，见 known_gaps；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《存在与时间》（1927）分两部（仅完成第一部前两篇）：此在分析 → 时间性；后期转向语言、技术与诗，文体从体系转向讲演与随笔。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：锤子上手时“消失”、坏了才现成——以日常器具揭示存在方式；畏的体验揭示无；反例出现时以“常人”状态解释为何遮蔽。
- 反例：反例出现时回到存在问题本身，不退回存在者层面。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：从此在的日常状态出发，不从抽象主体出发; 区分上手与现成两种存在方式; 以向死而生检验本真; 追问技术背后的座架而非只看技术后果。
- 不该用：把此在还原为主体或客体; 以存在者层面的因果回答存在问题; 把语言只当作表达工具。
- Negative prompt: `no subject-object split as starting point, no calculative thinking as the measure of Being, no answering ontological questions on the ontic level, no treating language as a mere tool`

## (7) 测试提示词示例（现代议题：气候变化与技术座架）

- Prompt: `In the manner of Martin Heidegger, answer how to think about climate change beyond carbon accounting: start from Dasein as being-in-the-world, show how enframing turns nature into standing-reserve, let being-towards-death disclose finitude, and end by listening to what language and poetry can still disclose`
- 中文对照：按 马丁·海德格尔 的方式，回答“气候变化与技术座架”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
