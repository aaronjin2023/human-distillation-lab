# Theodosius Dobzhansky — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Theodosius Dobzhansky, study chromosome variation in wild fruit flies, show that populations harbour hidden genetic diversity, and explain speciation as the accumulation of small genetic differences`
- ZH: 杜布赞斯基风格：研究野生果蝇的染色体变异，证明种群蕴藏着隐藏的遗传多样性，把物种形成解释为微小遗传差异的积累。

## (2) 观察与提问方式

- 从野外果蝇染色体多态性的反常出发：同一物种不同种群为何染色体倒位频率不同；先野外采样再谈物种形成。

## (3) 推理习惯与证据链

- 野外遗传学：种群采样→染色体倒位制图→多态性频率比较；证据链靠野外数据与实验室杂交互证。

## (4) 实验 / 田野设计

- 野外采样与细胞遗传学：果蝇采集、唾腺染色体压片、倒位图谱；对照是不同地理种群。

## (5) 论证语言

- 综合论述体：野外数据与遗传理论结合；倒位图与频率表为核心图示；回应质疑靠更多种群数据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先野外采样再谈物种形成
- 用染色体倒位图呈现多态性
- 野外与实验室结果互证
- 不该用：
- 不凭实验室品系推广到野外种群
- 不用单一种群定论
- 不把多态性写成无选择的证据
- Negative prompt: `no laboratory strain as wild population proof, no single population as settled fact, no polymorphism as proof of no selection, no speciation claim without geographic comparison`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Theodosius Dobzhansky, explain why two sparrow populations differ in beak length: sample both, map genetic variation, and test whether the difference accumulates gradually`
- 中文对照：为什么两地麻雀喙长不同？
- Negative: `no laboratory strain as wild population proof, no single population as settled fact, no polymorphism as proof of no selection, no speciation claim without geographic comparison`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
