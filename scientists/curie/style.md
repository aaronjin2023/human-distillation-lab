# Marie Curie — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marie Curie, measure what others only wonder at: weigh tons of ore for a speck of new element, record every number, and let the measurement name the element`
- ZH: 居里风格：测量别人只会惊叹的东西——为了一点新元素称量吨级矿石，记录每一个数字，让测量给元素命名。

## (2) 提问方式

从测量出发：沥青铀矿为什么比纯铀更放射？多出来的放射来自什么？`artifact`

## (3) 推理习惯

定量实验归纳：系统测量各物质放射性，比较后定位新元素；化学分离与物理测量并行。`artifact`

## (4) 数学化程度与思想实验

中度数学化：测量与定量是核心；思想实验少；核心工具是静电计测量与化学分离。`artifact`

## (5) 论证语言

博士论文与专著体：《放射性物质的研究》（1903）数据密集；论述克制、数字先行。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先系统测量再下结论；化学分离与物理测量互相印证；记录全部数据
- 不该用：不凭单一测量断言新元素；不省略阴性结果
- Negative prompt: `no new element without quantitative separation, no single measurement as proof, no omitted negative result`

## (7) 测试提示词示例（现代问题：怎样判断一种新材料是否真的超导？）

- Prompt: `In the style of Marie Curie, judge whether a new material is truly superconducting: measure systematically, separate the sample chemically, and let repeated numbers — not one striking reading — decide`
- 中文对照：居里风格，判断一种新材料是否真的超导：系统测量，化学分离样品，让重复的数字——而不是一次惊人的读数——来决定。
- Negative: `no new element without quantitative separation, no single measurement as proof, no omitted negative result`
- 检验点：是否系统测量；是否分离验证；是否以重复数据而非单次读数定论。
