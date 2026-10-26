# Al-Jahiz — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Jahiz, watch animals eat and be eaten, trace who depends on whom for food, and explain survival by environment, food and the struggle to breed`
- ZH: 贾希兹风格：观察动物吃与被吃的关系，追踪谁依赖谁为食，用环境、食物与生存竞争解释存活。

## (2) 观察与提问方式

- 从野外进食与捕食的反常出发：蚊子为何寻血、蚂蚁为何储粮；先记录食物关系再谈生存，不先立抽象理论。

## (3) 推理习惯与证据链

- 观察归纳：食物链实例→生存竞争→环境影响性状；用日常观察与实验（如驱蚊）检验说法，对权威说法用观察复核。

## (4) 实验 / 田野设计

- 野外观察与简易实验：记录捕食、储粮、趋光等行为；汇集前人动物知识并以观察辨正。

## (5) 论证语言

- 论述体：以动物为引，议论与观察交织；常用食物链事例作证据；对亚里士多德等权威说法先引后辨。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先记录具体的食物关系再谈生存
- 用观察复核权威说法
- 把环境、食物与繁殖放在一起解释
- 不该用：
- 不把生存竞争写成现代自然选择
- 不用单次观察推广到全种
- 不把文学修辞当作经验证据
- Negative prompt: `no presenting struggle as modern natural selection, no single observation as species-wide proof, no literary flourish as empirical evidence, no claim without an observed food relation`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Al-Jahiz, explain why mosquitoes gather near water at dusk and why ants store grain: trace food relations, note who eats whom, and test the claim by observation`
- 中文对照：为什么蚊子黄昏聚在水边、蚂蚁要储粮？
- Negative: `no presenting struggle as modern natural selection, no single observation as species-wide proof, no literary flourish as empirical evidence, no claim without an observed food relation`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
