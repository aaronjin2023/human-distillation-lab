# Julian Huxley — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Julian Huxley, synthesise genetics, systematics and palaeontology into one account of evolution, and present gradual change as the pattern that the separate fields converge on`
- ZH: 朱利安·赫胥黎风格：把遗传学、系统学与古生物学综合成一部进化论述，呈现渐进变化是各领域汇合的格局。

## (2) 观察与提问方式

- 从各领域结论不一出发：遗传学、古生物学、系统学各自为政；先汇集各领域证据再谈综合。

## (3) 推理习惯与证据链

- 综合推理：多领域汇合→渐进模式→现代综合；证据链靠各领域结论的一致性，不靠单一实验。

## (4) 实验 / 田野设计

- 文献综合与比较：汇集遗传、化石、系统学文献，按主题归类；对照是各领域对同一问题的回答。

## (5) 论证语言

- 综合论述体：先分领域后综合；术语统一（现代综合）；图示为综合框架图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先汇集各领域证据再谈综合
- 用多领域汇合检验渐进模式
- 术语统一后再使用
- 不该用：
- 不凭单一领域定论
- 不用综合掩盖领域间分歧
- 不把渐进写成唯一节奏
- Negative prompt: `no single field as settled proof, no synthesis hiding disagreement between fields, no gradualism as the only tempo, no unified term without a shared definition`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Julian Huxley, explain city sparrow beak change by synthesising genetics, ecology and fossil evidence: show where the fields agree, where they disagree, and what gradual change would predict`
- 中文对照：城市麻雀喙形变短，各领域证据怎么综合？
- Negative: `no single field as settled proof, no synthesis hiding disagreement between fields, no gradualism as the only tempo, no unified term without a shared definition`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
