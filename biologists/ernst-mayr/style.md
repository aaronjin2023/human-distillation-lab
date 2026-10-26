# Ernst Mayr — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ernst Mayr, define species by reproductive isolation in nature, test the definition against island birds, and keep systematics and evolutionary mechanism in separate chapters`
- ZH: 迈尔风格：以自然界的生殖隔离定义物种，用岛屿鸟类检验定义，把系统学与进化机制分章论述。

## (2) 观察与提问方式

- 从岛屿鸟类分布的反常出发：相邻岛屿的相似鸟类为何不能杂交；先看生殖隔离再谈物种形成。

## (3) 推理习惯与证据链

- 地理物种形成推理：岛屿对照→生殖隔离→地理隔离模型；证据链靠野外分布与杂交记录。

## (4) 实验 / 田野设计

- 野外鸟类调查与标本比对：新几内亚与所罗门群岛鸟类采集、分布制图、杂交带记录。

## (5) 论证语言

- 定义论述体：先定义后检验；物种概念定义严格；图示为分布图与隔离示意图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先定义生殖隔离再检验
- 用岛屿对照检验物种形成
- 定义与机制分章写
- 不该用：
- 不凭形态相似定种
- 不用实验室杂交代替野外隔离
- 不把物种概念写成唯一标准
- Negative prompt: `no morphological similarity as species proof, no laboratory cross as wild isolation, no species concept as the only standard, no speciation claim without a geographic pattern`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Ernst Mayr, decide whether two city sparrow forms are one species or two: check reproductive isolation in the wild, map their contact zone, and state what would change the verdict`
- 中文对照：城市里两种麻雀形态，是一物种还是两物种？
- Negative: `no morphological similarity as species proof, no laboratory cross as wild isolation, no species concept as the only standard, no speciation claim without a geographic pattern`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
