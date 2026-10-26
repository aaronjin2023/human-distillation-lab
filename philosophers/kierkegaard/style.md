# Søren Kierkegaard — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Søren Kierkegaard: pseudonyms and indirect communication, the leap of faith, irony and paradox, the single individual before God, no system, no crowd`
- ZH: 克尔凯郭尔风格：化名与间接沟通、信仰之跃、反讽与悖论、单个人在上帝面前、无体系、无群氓。

## (2) 概念

- 化名：多声部的间接沟通
- 信仰之跃：非理性的一跳
- 恐惧与战栗：亚伯拉罕的伦理悬置
- 绝望：自我失调的疾病
- 单个人：对抗群氓的单位

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 间接沟通：以化名作者写对立立场，让读者自行抉择；《恐惧与战栗》以亚伯拉罕献祭为思想实验，逼出伦理的悬置；论证靠悖论与抉择，不靠体系证明。

## (4) 修辞

- 化名多声部；反讽与悖论密集；日记体与布道体交织；语气急切、亲密、近乎耳语。

## (5) 问题意识

- 核心问题（一句话）：信仰与伦理冲突时，人当如何？单个人如何面对上帝？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 化名与间接沟通
- 信仰之跃的思想实验
- 悖论的逼问
- 单个人视角
- 抉择而非证明
- 不该写：No system, no crowd as authority, no direct didactic proof, no flattening of paradox, no conclusion that spares the reader a choice。
- Negative prompt: `No system, no crowd as authority, no direct didactic proof, no flattening of paradox, no conclusion that spares the reader a choice`

## (7) 测试提示词示例（现代题材：自助结账机漏扫了一件商品，当事人是否该付款）

- Prompt: `In the style of Søren Kierkegaard, a person at a self-checkout machine notices one item was not scanned. pseudonyms and indirect communication, the leap of faith, irony and paradox, the single individual before God, no system, no crowd`
- 中文对照：克尔凯郭尔风格：化名与间接沟通、信仰之跃、反讽与悖论、单个人在上帝面前、无体系、无群氓。自助结账机漏扫了一件商品，当事人是否该付款。
- Negative: `No system, no crowd as authority, no direct didactic proof, no flattening of paradox, no conclusion that spares the reader a choice`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
