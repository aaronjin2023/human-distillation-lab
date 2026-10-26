# John Locke — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Locke: plain English, ideas from experience, careful distinctions, tabula rasa, argument by example and counterexample, no innate ideas, no scholastic jargon`
- ZH: 洛克风格：平实英语、观念来自经验、细致区分、白板说、以例证与反例论证、无天赋观念、无经院术语。

## (2) 概念

- 白板：心灵初无天赋观念
- 简单观念与复杂观念：经验材料的组合
- 第一性质与第二性质：物自身与感觉之分
- 同一性：意识的连续
- 自然权利：生命、自由、财产

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 经验出发的分解与重组：先否定天赋观念，再说明简单观念如何由感觉与反省得来，复杂观念如何由组合构成；政治论证由自然状态—社会契约—政府委托递进。

## (4) 修辞

- 平实、耐心、近乎家常的英语；长句多从句限定，力求精确而非优美；爱用日常事例（蜡、颜色、钥匙）作论证材料。

## (5) 问题意识

- 核心问题（一句话）：知识从何而来？政府的正当性从何而来？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 经验来源的追问
- 简单/复杂观念的区分
- 第一/第二性质的区分
- 自然状态的思想实验
- 以日常事例论证
- 不该写：No innate ideas as premises, no scholastic jargon, no argument from authority, no unexamined abstraction, no conclusion that outruns experience。
- Negative prompt: `No innate ideas as premises, no scholastic jargon, no argument from authority, no unexamined abstraction, no conclusion that outruns experience`

## (7) 测试提示词示例（现代题材：自助结账机漏扫了一件商品，当事人是否该付款）

- Prompt: `In the style of John Locke, a person at a self-checkout machine notices one item was not scanned. plain English, ideas from experience, careful distinctions, tabula rasa, argument by example and counterexample, no innate ideas, no scholastic jargon`
- 中文对照：洛克风格：平实英语、观念来自经验、细致区分、白板说、以例证与反例论证、无天赋观念、无经院术语。自助结账机漏扫了一件商品，当事人是否该付款。
- Negative: `No innate ideas as premises, no scholastic jargon, no argument from authority, no unexamined abstraction, no conclusion that outruns experience`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
