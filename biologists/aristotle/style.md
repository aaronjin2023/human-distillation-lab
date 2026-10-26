# Aristotle — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aristotle, observe many animals, sort them by shared form and function, seek the cause behind each part, and state what holds in most cases rather than in every case`
- ZH: 亚里士多德风格：观察众多动物，按共有形态与功能分类，追问每一部分的原因，只说多数情况下成立的结论。

## (2) 观察与提问方式

- 从解剖与野外观察的反常出发：同一器官在不同动物身上为何形态不同；先穷举实例再分类，不先立抽象定义。

## (3) 推理习惯与证据链

- 归纳为主：大量实例→属与种的划分→目的因与形式因解释；比较解剖是核心证据链，多线汇合（形态、习性、繁殖、栖息地）才下结论。

## (4) 实验 / 田野设计

- 解剖、比较与分类：剖检动物、记录器官对应关系、按有血/无血、胎生/卵生等性状二分；样本是地中海地区的常见动物，靠反复解剖核对。

## (5) 论证语言

- 分类体：先定义属再分种，定义靠本质性状而非偶然性状；常用“多数情况下”限定，留出例外；图示为分类表与器官对应表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先穷举同类实例再分类
- 用器官功能解释形态差异
- 遇例外先记录再修正分类，不删例外
- 不该用：
- 不凭单一动物推广到全类
- 不用目的论断言每一细节都有用途
- 不把传说动物当作观察证据
- Negative prompt: `no generalisation from a single animal, no teleological claim for every detail, no legendary animal as observation evidence, no definition without observed traits`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Aristotle, explain why bats fly at night while most birds fly by day: compare their wings, eyes and habits, sort them by shared form and function, and state what holds in most cases`
- 中文对照：为什么蝙蝠夜行而多数鸟类昼行？
- Negative: `no generalisation from a single animal, no teleological claim for every detail, no legendary animal as observation evidence, no definition without observed traits`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
