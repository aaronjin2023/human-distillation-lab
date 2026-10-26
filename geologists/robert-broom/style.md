# Robert Broom — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Broom, dig the Karoo and the Transvaal caves for the missing links: collect mammal-like reptiles bed by bed, then search the limestone caves for the ape-men, and let each new skull re-draw the line to humans`
- ZH: 布鲁姆风格：为找缺失环节而挖卡鲁与德兰士瓦洞穴——逐层收集似哺乳爬行动物，再到石灰岩洞穴里找猿人，让每一块新头骨重画通向人类的线。

## (2) 野外观察方式

- 南非野外与洞穴的眼睛：在卡鲁盆地逐层采集似哺乳爬行动物，在斯特克方丹洞穴逐层发掘南方古猿。粒度是标本与剖面尺度；一处洞穴可以改写人类起源。化石采集逐层编号。

## (3) 地层对比与化石证据

- 卡鲁盆地地层靠爬行动物化石组合划分；洞穴堆积靠角砾岩层与化石组合定相对次序。化石是核心证据；头骨的形态与层位就是演化位置。缺失靠更多发掘补。

## (4) 理论建构方式

- 从似哺乳爬行动物归纳出哺乳动物起源于爬行动物；从南方古猿归纳出人类起源于非洲。跳跃是谱系的跳跃——把一串头骨读成通向人类的线。理论的尺度是类群，方法的尺度是一块头骨。

## (5) 论证语言

- 论证结构是发掘描述—头骨鉴定—比较—谱系推论。图示是头骨图版与谱系图；术语是解剖学术语。回应质疑靠更多的头骨。

## (6) 该用 / 不该用的论证套路

- 该用：- 逐层发掘洞穴，记录每一块头骨的层位
- 用头骨解剖特征定谱系位置，不靠体型
- 把似哺乳爬行动物与南方古猿放在同一条证据链上谈
- 新头骨出现就修订谱系，不固守旧图
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no human-origins claim without a skull in its layer, no lineage drawn from a single specimen, no ignoring the Karoo reptiles that frame the mammal story, no presenting a reconstruction the skull does not support`

## (7) 测试提示词示例（现代地质问题：一处洞穴发现一具古猿头骨，如何判断它在人类演化中的位置？）

- Prompt: `In the style of Robert Broom, a cave yields an ape-man skull: record its exact layer, compare its anatomy bone by bone with apes and humans, and place it on the lineage only as far as the skull allows`
- 中文对照：布鲁姆风格：洞穴发现一具古猿头骨——记准层位，逐骨与猿与人比较，只在头骨允许的范围内定它在谱系中的位置。
- Negative: `no human-origins claim without a skull in its layer, no lineage drawn from a single specimen, no ignoring the Karoo reptiles that frame the mammal story, no presenting a reconstruction the skull does not support`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
