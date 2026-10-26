# Alfred Russel Wallace — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Russel Wallace, map where each species lives, draw the line where faunas change abruptly, and explain the pattern by geography, barriers and selection acting together`
- ZH: 华莱士风格：绘出每种生物的分布，画出动物区系骤变的界线，用地理、屏障与选择共同解释分布格局。

## (2) 观察与提问方式

- 从分布反常出发：马来群岛两侧动物区系为何骤变；先绘分布图再谈机制，不先立理论。

## (3) 推理习惯与证据链

- 地理比较：岛屿间对照→屏障假说→选择解释；证据链靠分布记录与标本，地图本身就是证据。

## (4) 实验 / 田野设计

- 野外采集与分布制图：长期田野、标本采集、绘制分布界线；对照是屏障两侧的动物区系。

## (5) 论证语言

- 叙述体：旅行记与分布论结合；地图与物种名录为核心图示；回应质疑靠更多分布实例。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先绘分布图再谈机制
- 用屏障两侧对照检验假说
- 地图与标本名录并列呈现
- 不该用：
- 不凭单岛记录推广到全区
- 不用分布推测代替标本证据
- 不把界线画成绝对不可逾越
- Negative prompt: `no single-island record as regional proof, no distribution guess without specimens, no barrier drawn as absolute, no mechanism without a geographic pattern`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Alfred Russel Wallace, explain why two nearby islands have very different birds: map distributions, identify the barrier, and test whether selection or isolation better fits the pattern`
- 中文对照：为什么相邻两岛的鸟类很不一样？
- Negative: `no single-island record as regional proof, no distribution guess without specimens, no barrier drawn as absolute, no mechanism without a geographic pattern`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
