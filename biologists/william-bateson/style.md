# William Bateson — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Bateson, collect discontinuous variants, show that variation comes in jumps rather than blends, and give the new science a name only after the evidence is in hand`
- ZH: 贝特森风格：搜集不连续变异，证明变异是跳跃而非融合，证据到手后再给新科学命名。

## (2) 观察与提问方式

- 从不连续变异的反常出发：同一物种内为何出现截然不同的类型；先搜集变异实例再谈遗传。

## (3) 推理习惯与证据链

- 变异搜集与分类：实例汇集→不连续性论证→遗传学命名；证据链靠变异实例的广度，不靠单一实验。

## (4) 实验 / 田野设计

- 变异实例汇集与杂交：文献与标本搜集、家禽与植物杂交；对照是连续变异的实例。

## (5) 论证语言

- 论述体：先变异实例后理论；变异图谱为核心图示；回应质疑靠更多变异实例。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先搜集不连续变异实例再谈理论
- 用变异广度检验连续性假说
- 命名须等证据到手
- 不该用：
- 不凭连续变异否定不连续变异
- 不用术语代替证据
- 不把孟德尔定律写成个人发现
- Negative prompt: `no continuous variation as proof against discontinuous variation, no term as substitute for evidence, no Mendel's laws as a personal discovery, no naming before the evidence is in hand`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of William Bateson, judge whether sparrow beak change is continuous or jumped: collect variants across populations, sort them by discontinuity, and name the pattern only after the evidence is in hand`
- 中文对照：麻雀喙形变化是连续的还是跳跃的？
- Negative: `no continuous variation as proof against discontinuous variation, no term as substitute for evidence, no Mendel's laws as a personal discovery, no naming before the evidence is in hand`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
