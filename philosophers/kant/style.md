# Immanuel Kant — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Immanuel Kant: precise definitions, categorical distinctions, transcendental argument from the conditions of possibility, long periodic sentences, no metaphor without conceptual cash value`
- ZH: 康德风格：精确定义、范畴区分、先验论证、长周期句、无概念兑现价值的隐喻不用。

## (2) 概念

- 先天/后验、分析/综合：知识的两种划分
- 现象/物自体：可知与不可知的界限
- 范畴：知性的先天概念
- 定言命令：无条件有效的道德律令
- 先验：经验得以可能的条件

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 先验论证骨架：问题（综合判断何以可能）—区分（感性/知性/理性）—演绎（范畴的先验演绎）—界限（二律背反）—实践转向；结论强度为先验必然，而非经验或然。

## (4) 修辞

- 体系长句，层层从句；术语高度统一；隐喻极少（法庭、建筑、哥白尼革命），每个隐喻都有概念对应；语气庄重、冷峻、近乎立法。

## (5) 问题意识

- 核心问题（一句话）：形而上学何以可能？人应当做什么？我可以希望什么？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 先验论证
- 现象/物自体区分
- 范畴的先验演绎
- 定言命令的普遍化检验
- 二律背反的回应
- 不该写：No loose essayistic prose, no undefined metaphors, no appeal to emotion as conclusion, no consequentialist reasoning, no unargued assertion。
- Negative prompt: `No loose essayistic prose, no undefined metaphors, no appeal to emotion as conclusion, no consequentialist reasoning, no unargued assertion`

## (7) 测试提示词示例（现代题材：自助结账机漏扫了一件商品，当事人是否该付款）

- Prompt: `In the style of Immanuel Kant, a person at a self-checkout machine notices one item was not scanned. precise definitions, categorical distinctions, transcendental argument from the conditions of possibility, long periodic sentences, no metaphor without conceptual cash value`
- 中文对照：康德风格：精确定义、范畴区分、先验论证、长周期句、无概念兑现价值的隐喻不用。自助结账机漏扫了一件商品，当事人是否该付款。
- Negative: `No loose essayistic prose, no undefined metaphors, no appeal to emotion as conclusion, no consequentialist reasoning, no unargued assertion`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
