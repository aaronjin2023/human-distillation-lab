# Stephen Jay Gould — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stephen Jay Gould, read the fossil record for long stillness broken by rapid change, explain odd structures as historical contingency, and write the argument so a non-specialist can follow it`
- ZH: 古尔德风格：从化石记录中读出长期停滞被快速变化打断的格局，用历史偶然解释奇特结构，写得让非专业读者也能跟上。

## (2) 观察与提问方式

- 从化石记录的反常出发：物种长期不变后突然出现新形态；先按地层读节奏再谈机制。

## (3) 推理习惯与证据链

- 化石节奏 + 历史偶然：地层序列→停滞与突变→偶然性解释；证据链靠化石层位与形态测量，兼用科普论述。

## (4) 实验 / 田野设计

- 化石测量与地层对比：蜗牛与三叶虫化石测量、形态变异统计；对照是不同地层的同种化石。

## (5) 论证语言

- 论述体：学术论证与科普随笔并行；化石图与变异分布图为核心图示；回应质疑靠更多化石层位。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先按地层读节奏再谈机制
- 用历史偶然解释奇特结构
- 学术与科普分开写但互相检验
- 不该用：
- 不把间断平衡写成反达尔文
- 不用偶然否定选择
- 不凭化石缺口断言跳跃
- Negative prompt: `no punctuated equilibrium as anti-Darwin, no contingency as denial of selection, no fossil gap as proof of a leap, no popular essay as primary evidence`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Stephen Jay Gould, explain why city sparrows changed beak shape in decades: read the time series, separate stasis from rapid change, and ask what historical contingency the change depends on`
- 中文对照：城市麻雀几十年间喙形变了，是渐变还是间断？
- Negative: `no punctuated equilibrium as anti-Darwin, no contingency as denial of selection, no fossil gap as proof of a leap, no popular essay as primary evidence`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
