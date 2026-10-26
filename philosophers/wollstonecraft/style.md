# Mary Wollstonecraft — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mary Wollstonecraft: reason knows no sex, education as the root of inequality, direct polemic against Burke and Rousseau, no ornamental sensibility, no apology for demanding equality`
- ZH: 沃斯通克拉夫特风格：理性不分性别、教育是不平等的根源、直接论战伯克与卢梭、无矫饰的感伤、无为要求平等而道歉。

## (2) 概念

- 理性无性别：理性能力人人皆有
- 教育：女性'低劣'的真正原因
- 感伤：被培养出的软弱
- 共和美德：公民的理性与独立
- 婚姻：平等者之间的友谊

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 论战—归因—方案：先回应伯克（《人类权利辩护》），再把矛头转向卢梭的教育观，论证女性'低劣'是教育所致而非天性，最后提出男女同校、理性教育的改革方案；论证靠直接驳斥与归因翻转。

## (4) 修辞

- 论战体，锋芒毕露；长句论证间插短句怒斥；直接点名对手；语气急切、毫不道歉。

## (5) 问题意识

- 核心问题（一句话）：女性为何显得低劣？理性与权利是否分性别？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 理性无性别的论证
- 教育归因的翻转
- 对伯克与卢梭的直接驳斥
- 男女同校的方案
- 感伤的批判
- 不该写：No ornamental sensibility, no apology for demanding equality, no argument from nature that fixes women as inferior, no sentimental defence of the status quo, no evasion of the opponent by name。
- Negative prompt: `No ornamental sensibility, no apology for demanding equality, no argument from nature that fixes women as inferior, no sentimental defence of the status quo, no evasion of the opponent by name`

## (7) 测试提示词示例（现代题材：自助结账机漏扫了一件商品，当事人是否该付款）

- Prompt: `In the style of Mary Wollstonecraft, a person at a self-checkout machine notices one item was not scanned. reason knows no sex, education as the root of inequality, direct polemic against Burke and Rousseau, no ornamental sensibility, no apology for demanding equality`
- 中文对照：沃斯通克拉夫特风格：理性不分性别、教育是不平等的根源、直接论战伯克与卢梭、无矫饰的感伤、无为要求平等而道歉。自助结账机漏扫了一件商品，当事人是否该付款。
- Negative: `No ornamental sensibility, no apology for demanding equality, no argument from nature that fixes women as inferior, no sentimental defence of the status quo, no evasion of the opponent by name`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
