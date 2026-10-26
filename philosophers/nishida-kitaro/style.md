# Nishida Kitaro — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nishida Kitaro: pure experience, basho as place, absolute nothingness, self-awakening, no subject-object dualism as starting point, no Western logic imposed without basho`
- ZH: 西田几多郎风格：纯粹经验，场所，绝对无，自觉，拒绝以主客二元为起点，拒绝不经场所的西方逻辑强加。

## (2) 概念

- 纯粹经验（pure experience）：主客分化之前的直接经验；意识从中分化出来，而非先于它。`artifact`（《善的研究》）
- 场所（basho）：容纳主客对立的场；逻辑在场所中展开，而非在抽象中展开。`artifact`
- 绝对无（absolute nothingness）：场所的终极形态；不是虚无，而是容纳一切的无。`artifact`
- 自觉（self-awakening）：自我在场所中觉醒；不是主体的自我认识，而是场所的自我展开。`artifact`
- 矛盾的自我同一（contradictory self-identity）：对立双方在场所中既对立又同一。`artifact`
- 行为直观（acting intuition）：知行合一的直观；身体行动中的认识。`artifact`

## (3) 论证结构

经验描述—逻辑化—场所论的三段式：先描述纯粹经验，再以逻辑化展开主客分化，最后以场所收束对立。结论强度是场所性的：对立在场所中同一，而非被某一方消解。反例处理方式是纳入场所——反例只是场所的另一面。`impression`

## (4) 修辞

凝练、禅意、东西方术语互注、短段；语气沉静而坚定，与读者的距离是邀你静观，而非与你辩论。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：意识如何从纯粹经验中分化出主客？
- 问题从哪里来：来自西方哲学的主客二元困境与东方禅宗的启示：二元论无法解释意识的起源。；他把问题推向何处：把问题推向场所逻辑：逻辑本身需要在场所中重新奠基。。

## (6) 该写什么 / 不该写什么

- 该写：
- 纯粹经验、场所、绝对无等概念群
- 以纯粹经验的描述开篇
- 以场所收束对立
- 不该写：
- 以主客二元为起点
- 不经场所的西方逻辑强加
- 把纯粹经验心理化
- 以体系封闭绝对无
- Negative prompt: `No subject-object dualism as starting point, no Western logic imposed without basho, no psychologised pure experience, no system that closes the absolute nothingness`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬：纯粹经验）

- Prompt: `In the style of Nishida Kitaro, a small Yorkshire terrier sits on a subway seat. Before subject and object divide, there is pure experience: the dog, the seat, the gaze, one undivided field. In the basho, seer and seen are contradictorily self-identical. No dualism as starting point, no system that closes the absolute nothingness.`
- 中文对照：西田几多郎风格：一只约克夏犬坐在地铁座位上。在主客分化之前，是纯粹经验：狗、座位、目光，一个未分的场。在场所中，看者与被看者矛盾地自我同一。拒绝以主客二元为起点，拒绝以体系封闭绝对无。
- Negative: `No subject-object dualism as starting point, no Western logic imposed without basho, no psychologised pure experience, no system that closes the absolute nothingness`
- 检验点：是否以纯粹经验开篇而非以主客开篇；场所概念是否在场；结尾是否收束于场所而非给出二元结论。
