# Auguste Comte — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Auguste Comte: the law of three stages, the hierarchy of the sciences, positive knowledge only, classification as argument, no theology, no metaphysics as science`
- ZH: 孔德风格：三阶段法则、科学等级、只认实证知识、分类即论证、无神学、无作为科学的形而上学。

## (2) 概念

- 三阶段：神学—形而上学—实证
- 科学等级：数学—天文—物理—化学—生物—社会学
- 实证：只问如何，不问为何
- 社会学：最晚到来的科学
- 人道教：晚期的宗教转向

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 分类—历史—体系：先以三阶段法则讲人类心智的历史，再以科学等级排定各科学的次序，最后以社会学收束体系；论证靠分类与历史分期，不靠演绎。

## (4) 修辞

- 分类表与历史分期；长句系统；语气确信、立法式；晚期转向人道教，语气近乎宗教。

## (5) 问题意识

- 核心问题（一句话）：知识如何进步？社会能否成为科学？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 三阶段法则
- 科学等级的排列
- 实证判准的提出
- 社会学的定位
- 历史分期的论证
- 不该写：No theology as science, no metaphysics as science, no unobservable cause as explanation, no argument that ignores the hierarchy of the sciences, no conclusion without a place in the system。
- Negative prompt: `No theology as science, no metaphysics as science, no unobservable cause as explanation, no argument that ignores the hierarchy of the sciences, no conclusion without a place in the system`

## (7) 测试提示词示例（现代题材：自助结账机漏扫了一件商品，当事人是否该付款）

- Prompt: `In the style of Auguste Comte, a person at a self-checkout machine notices one item was not scanned. the law of three stages, the hierarchy of the sciences, positive knowledge only, classification as argument, no theology, no metaphysics as science`
- 中文对照：孔德风格：三阶段法则、科学等级、只认实证知识、分类即论证、无神学、无作为科学的形而上学。自助结账机漏扫了一件商品，当事人是否该付款。
- Negative: `No theology as science, no metaphysics as science, no unobservable cause as explanation, no argument that ignores the hierarchy of the sciences, no conclusion without a place in the system`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
