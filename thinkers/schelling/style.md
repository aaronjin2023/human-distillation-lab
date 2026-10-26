# Schelling — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Schelling, begin with the identity of nature and spirit, unfold their opposition in history, reconcile them in the intuition of art, and close by asking after the ground of freedom and evil`
- ZH: 谢林方式：以自然与精神的同一性为起点，在历史中展开二者的对立，以艺术的直观调和对立，最后追问自由与恶的根源。

## (2) 核心概念（概念色板）

- 核心概念（8 个）：同一性（Identität）、自然（Natur）、精神（Geist）、绝对（das Absolute）、艺术直观、自由（Freiheit）、恶（das Böse）、根据（Grund）
- 辅助概念：有机体、无意识、神话、启示
- 禁用 / 拒绝的概念：以二元对立为终点；以抽象概念代替艺术直观；以体系压制自由
- 层级与张力：同一性高于对立：对立是同一性的展开；艺术高于概念：艺术直观调和对立；自由高于必然：恶的根源在自由。
- 抽象程度与隐喻：极高度抽象：概念必有同一性说明；允许艺术隐喻，不允许无同一性的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：同一性推导（为主）：从绝对展开对立；历史叙述（其次）：自然与精神的历史；艺术直观（较少）；自由追问（较少）。
- 前提引入与反例处理：前提：自然与精神同一于绝对；反例（恶的存在）不回避，而是作为自由论的核心问题：恶源于自由的滥用。
- 结论限定习惯：结论以“就同一性而言”限定；晚期哲学的表述有所变化，见 motifs.md。
- 修辞习惯：句式绵长，意象丰富；善用自然隐喻与艺术比喻；晚期转向神话与启示的叙事。
- 质感：诗意而严密：早期体系严密，晚期转向叙事；严密性在同一性的彻底。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《先验唯心论体系》）+ 自由论（《自由论》）+ 讲稿（《艺术哲学》）；体裁从体系到讲稿。
- 视点：同一性视角：从绝对看自然与精神；论证从“同一性”开始，到“自由”收束。
- 布局：先立同一性 → 再分自然与精神 → 后以艺术调和 → 末问自由与恶；核心命题（同一性）开篇即立，展开在中段层层推进；结尾以自由追问收束。
- 留白与裁切：有意不回答“绝对如何被认识”的终极问题（艺术直观是回答，非证明）；晚期哲学的神话与启示部分留给读者。

## (5) 思想实验与反例处理

- 思想实验：艺术直观思想实验：假如艺术是哲学最高的器官，哲学与艺术会如何统一？实验设定是直观式的，结论由艺术的调和推出。
- 反例回应：对恶的反例回应：恶源于自由的滥用，非绝对的缺陷；对“同一性是抽象”的回应：艺术直观是同一性的具体显现。
- 景深与类比跨域：近处是自然的具体形态，远处是绝对的普遍结构；允许从自然跨到艺术、从精神跨到神话。

## (6) 该用 / 不该用的推理套路

- 该用：以同一性为起点；以历史展开对立；以艺术直观调和；以自由追问收束
- 不该用：不用二元对立为终点；不用抽象概念代替艺术直观；不用体系压制自由
- Negative prompt: `no dualism as an end point, no abstract concepts in place of artistic intuition, no system suppressing freedom`

## (7) 测试提示词示例

- 议题：AI 艺术是否可能是“艺术直观”？机器能否调和自然与精神？
- Prompt: `In the manner of Schelling, answer whether AI art can be artistic intuition: begin with the identity of nature and spirit, test whether a machine intuits, and close by asking after freedom`
- 中文对照：谢林方式，回答 AI 艺术是否可能是“艺术直观”：以自然与精神的同一性为起点，检验机器能否直观，最后追问自由。
- Negative: `no dualism as an end point, no abstract concepts in place of artistic intuition, no system suppressing freedom`
- 检验点：是否以同一性为起点；是否有艺术直观的讨论；结论是否为自由追问而非技术判断。
