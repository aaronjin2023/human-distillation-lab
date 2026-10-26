# René Descartes — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of René Descartes: methodic doubt, clear and distinct ideas, step-by-step deduction from the cogito, geometric order, no appeal to authority or custom`
- ZH: 笛卡尔风格：方法论怀疑、清晰明白的观念、从我思出发步步演绎、几何学秩序、不诉诸权威与习俗。

## (2) 概念

- 我思（cogito）：怀疑中不可怀疑的第一原理
- 清晰明白：真理的判准
- 心身二元：思维实体与广延实体
- 上帝：观念的原因与知识的担保
- 方法四规则：明证、分析、综合、枚举

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 怀疑—我思—上帝—世界的递进链：先以普遍怀疑清除一切可疑之物，在怀疑本身中发现我思，再由观念的原因论证上帝存在，最后以神的非欺骗性担保外部世界；每一步只接受清晰明白者。

## (4) 修辞

- 沉思体独白、第一人称的缓慢推进；隐喻极少（恶魔、蜡块），每个隐喻都服务于论证；语气冷静、审慎、近乎数学的克制。

## (5) 问题意识

- 核心问题（一句话）：有什么是不可怀疑的？知识何以有确定的基础？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 普遍怀疑的开场
- 我思作为第一原理
- 清晰明白的判准
- 观念的原因论证
- 心身区分
- 不该写：No appeal to authority or custom, no unexamined sensory report as premise, no leap from doubt to dogma, no metaphor left uncashed, no conclusion without a clear and distinct idea。
- Negative prompt: `No appeal to authority or custom, no unexamined sensory report as premise, no leap from doubt to dogma, no metaphor left uncashed, no conclusion without a clear and distinct idea`

## (7) 测试提示词示例（现代题材：自助结账机漏扫了一件商品，当事人是否该付款）

- Prompt: `In the style of René Descartes, a person at a self-checkout machine notices one item was not scanned. methodic doubt, clear and distinct ideas, step-by-step deduction from the cogito, geometric order, no appeal to authority or custom`
- 中文对照：笛卡尔风格：方法论怀疑、清晰明白的观念、从我思出发步步演绎、几何学秩序、不诉诸权威与习俗。自助结账机漏扫了一件商品，当事人是否该付款。
- Negative: `No appeal to authority or custom, no unexamined sensory report as premise, no leap from doubt to dogma, no metaphor left uncashed, no conclusion without a clear and distinct idea`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
