# Jeremy Bentham — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jeremy Bentham: the greatest happiness of the greatest number, felicific calculus, precise definitions, reform by measurement, no natural rights, no vague moral sentiment`
- ZH: 边沁风格：最大多数人的最大幸福、快乐计算、精确定义、以度量推动改革、无自然权利、无含糊的道德情感。

## (2) 概念

- 功利原则：最大多数人的最大幸福
- 快乐计算：强度、持续、确定、远近、丰度、纯度、广度
- 虚构实体：权利等为语言的虚构
- 最大多数：效用的聚合判准
- 改革：法律与制度按效用重估

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 定义—计算—改革：先定义快乐与痛苦，再列出快乐计算的七个维度，逐项度量行为的效用，最后推出制度改革方案；论证靠分类与算术，不靠情感。

## (4) 修辞

- 分类表与长定义；爱造新词以求精确；语气务实、 impatient，对含糊其辞毫不留情。

## (5) 问题意识

- 核心问题（一句话）：什么使行为正当？法律应当服务于谁的幸福？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 功利原则的提出
- 快乐计算的七维度
- 分类与定义
- 制度改革的推导
- 对自然权利的批判
- 不该写：No natural rights as premises, no vague moral sentiment, no unmeasured assertion, no appeal to tradition, no conclusion without a calculation。
- Negative prompt: `No natural rights as premises, no vague moral sentiment, no unmeasured assertion, no appeal to tradition, no conclusion without a calculation`

## (7) 测试提示词示例（现代题材：算法推荐决定一个人看什么、读什么、买什么）

- Prompt: `In the style of Jeremy Bentham, an algorithm recommends what a person should watch, read and buy. the greatest happiness of the greatest number, felicific calculus, precise definitions, reform by measurement, no natural rights, no vague moral sentiment`
- 中文对照：边沁风格：最大多数人的最大幸福、快乐计算、精确定义、以度量推动改革、无自然权利、无含糊的道德情感。算法推荐决定一个人看什么、读什么、买什么。
- Negative: `No natural rights as premises, no vague moral sentiment, no unmeasured assertion, no appeal to tradition, no conclusion without a calculation`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
