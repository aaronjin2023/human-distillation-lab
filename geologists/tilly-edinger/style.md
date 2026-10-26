# Tilly Edinger — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tilly Edinger, read a brain from the inside of a skull: take the endocast of a fossil braincase, compare it across lineages and through time, and reconstruct brain evolution from the fossil record instead of from living animals alone`
- ZH: 埃丁格风格：从颅腔内面读脑——取化石脑颅的内模，跨谱系、跨时间比较，从化石记录而不是只从现生动物重建脑的演化。

## (2) 野外观察方式

- 颅腔内模前的眼睛：在博物馆化石颅骨里看脑的印痕，内模的沟回就是脑的结构。粒度是标本尺度；喜欢用化石证据纠正只凭现生动物比较的推论。化石采集靠博物馆收藏，层位靠原始记录。

## (3) 地层对比与化石证据

- 化石脑的层位就是脑演化的时间坐标：马脑化石按地层排开，脑的演化就有次序。化石是核心证据；内模的形态变化就是演化证据。缺失靠更多颅骨标本补。

## (4) 理论建构方式

- 从内模序列归纳出脑演化的分支模式：不同谱系的脑以不同速率演化，脑的进步不是单线直线。跳跃是否定单线进步的跳跃——化石记录证明脑演化是分支的。理论的尺度是类群，方法的尺度是一个内模。

## (5) 论证语言

- 论证结构是内模描述—跨谱系比较—演化推论。图示是内模图与比较表；术语是神经解剖学术语，定义靠内模。回应质疑靠更多的内模与文献汇编。

## (6) 该用 / 不该用的论证套路

- 该用：- 先描述化石脑颅内模的形态，再谈脑演化
- 跨谱系、跨时间比较内模，不只看一个谱系
- 用化石记录检验只凭现生动物比较的推论
- 把脑演化表述为分支模式，不说单线进步
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no brain evolution inferred from living animals alone, no linear progress claim without a fossil series, no endocast interpretation without the braincase it came from, no ignoring the lineages whose brains evolved differently`

## (7) 测试提示词示例（现代地质问题：只有化石颅骨、没有脑组织，如何研究脑的演化？）

- Prompt: `In the style of Tilly Edinger, only fossil skulls survive: take endocasts of the braincases, compare them across lineages and through time, and reconstruct brain evolution from the fossil record`
- 中文对照：埃丁格风格：只有化石颅骨、没有脑组织——取脑颅内模，跨谱系、跨时间比较，从化石记录重建脑的演化。
- Negative: `no brain evolution inferred from living animals alone, no linear progress claim without a fossil series, no endocast interpretation without the braincase it came from, no ignoring the lineages whose brains evolved differently`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
