# Watsuji Tetsuro — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Watsuji Tetsuro: aidagara as betweenness, fudo as climate, ethics as the between of persons, no isolated individual as starting point, no ethics without climate and history`
- ZH: 和辻哲郎风格：间柄，风土，伦理即人与人之间，拒绝以孤立个人为起点，拒绝脱离风土与历史的伦理。

## (2) 概念

- 间柄（aidagara）：人与人之间的关系性存在；人不是孤立主体，而是“之间”的存在。`artifact`（《伦理学》）
- 风土（fudo）：气候、风土与历史共同塑造的存在方式；伦理离不开风土。`artifact`（《风土》）
- 伦理即人际：伦理学不是个人德性论，而是人与人之间关系的学问。`artifact`
- 存在即共在：人（ningen）一词本身就包含“之间”；共在先于个体。`artifact`
- 空（emptiness）：间柄的根基是空；绝对否定性使关系成为可能。`artifact`
- 信赖（trust）：人际关系的原初形态；信赖先于契约。`impression`

## (3) 论证结构

文化比较—空间分析—伦理重构的三段式：先比较不同风土中的存在方式（季风、沙漠、草原），再分析“之间”的空间结构，最后重构伦理学。结论强度是风土性的：伦理判断离不开风土与历史。反例处理方式是纳入风土——反例只是另一种风土的存在方式。`impression`

## (4) 修辞

文化史例证、风土描写、“之间”的反复；语气温和、博学，与读者的距离是邀你一起看风土，而非向你下命令。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：人如何不是孤立主体而是“之间”的存在？
- 问题从哪里来：来自西方个人主义的不足：以孤立个人为起点的伦理学无法解释人际关系的原初性。；他把问题推向何处：把问题推向风土：伦理学需要风土与历史的根基。。

## (6) 该写什么 / 不该写什么

- 该写：
- 间柄、风土、人际等概念群
- 以风土比较开篇
- 以“之间”收束
- 不该写：
- 以孤立个人为起点
- 脱离风土与历史的伦理
- 没有“之间”的普遍主义
- 偷运进来的西方个人主义
- Negative prompt: `No isolated individual as starting point, no ethics without climate and history, no abstract universal without betweenness, no Western individualism smuggled in`

## (7) 测试提示词示例（现代题材：自助结账机漏扫：人与人之间的伦理）

- Prompt: `In the style of Watsuji Tetsuro, a person at a self-checkout machine notices one item was not scanned. Do not begin with the isolated individual and her conscience. Begin with aidagara: the between of customer and cashier, the climate of the shop, the trust that makes the machine possible at all. Ethics is the between, not the inside of a subject.`
- 中文对照：和辻哲郎风格：一个人在自助结账机前发现一件商品没有扫上。不要从孤立个人与她的良心开始，而从间柄开始：顾客与收银员之间、商店的风土、使机器成为可能的那份信赖。伦理是之间，不是主体内部。
- Negative: `No isolated individual as starting point, no ethics without climate and history, no abstract universal without betweenness, no Western individualism smuggled in`
- 检验点：是否以“之间”开篇而非以个人开篇；风土概念是否在场；结尾是否收束于人际而非个人德性。
