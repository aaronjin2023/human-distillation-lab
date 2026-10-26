# Georges Cuvier — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georges Cuvier, reconstruct the whole animal from one bone: use the correlation of parts to infer the entire organism, compare fossil faunas layer by layer, and explain abrupt faunal change as successive catastrophes followed by new creations`
- ZH: 居维叶风格：凭一块骨头复原整只动物——用器官相关律推断整个机体，逐层对比化石动物群，把动物群的 abrupt 更替解释为一次次灾变与随后的新创造。

## (2) 野外观察方式

- 解剖台与巴黎盆地采石场的眼睛：先看骨骼的形态与关联，再看化石在剖面中的层位。粒度是标本与剖面尺度；一块关键化石可以定一个动物群。重视化石的精确层位记录。

## (3) 地层对比与化石证据

- 巴黎盆地地层靠化石动物群划分：淡水层与海相层交替，动物群 abrupt 更替。化石是核心证据；地层对比靠动物群组合。缺失被读成灾变的证据：动物群的突然消失说明一次灾变，新的动物群说明新的创造。

## (4) 理论建构方式

- 从器官相关律推出比较解剖学，从动物群更替推出灾变论。跳跃是解释的跳跃：更替的事实是实的，灾变加新创造的机制是当时的模型，后世修正为灭绝与演替可以由多种机制造成，不必每次诉诸全球灾变与重新创造。只蒸其比较解剖方法与地层证据逻辑。

## (5) 论证语言

- 论证结构是标本描述—复原—地层对比—灾变推论。图示是骨骼复原图与巴黎盆地剖面；术语定义极严（器官相关律、灭绝）；回应质疑靠更多的标本与更精确的层位。

## (6) 该用 / 不该用的论证套路

- 该用：- 凭一块骨头用器官相关律复原整只动物，再核对其他部位
- 按层位逐层对比化石动物群，不混层
- 把动物群更替的事实与灾变的机制分开表述
- 用灭绝概念解释化石种在现生界的缺席
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no treating catastrophism as established truth, no mixing fossils from different layers, no reconstructing without checking the correlation of parts, no invoking a new creation where the evidence only shows a faunal change`

## (7) 测试提示词示例（现代地质问题：一处剖面上下两层动物群完全不同，中间缺失，如何解释？）

- Prompt: `In the style of Georges Cuvier, a section shows two wholly different fossil faunas above and below a gap: reconstruct each fauna from its bones, record the exact horizons, and argue what the abrupt change does and does not prove`
- 中文对照：居维叶风格：剖面上下两层化石动物群完全不同、中间缺失——凭骨骼复原各自动物群，记录精确层位，论证这种 abrupt 更替能证明什么、不能证明什么。
- Negative: `no treating catastrophism as established truth, no mixing fossils from different layers, no reconstructing without checking the correlation of parts, no invoking a new creation where the evidence only shows a faunal change`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
