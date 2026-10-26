# Richard Dawkins — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Dawkins, rewrite an evolutionary question from the gene's point of view, ask which replicator copies itself best, and test the story against what the gene would predict`
- ZH: 道金斯风格：把进化问题改写成基因视角，问哪种复制子复制得最好，用基因会预言什么来检验故事。

## (2) 观察与提问方式

- 从行为与形态的反常出发：利他行为为何存在；先改写成基因视角再谈解释，不先立群体利益。

## (3) 推理习惯与证据链

- 基因视角推理：复制子→适合度计算→行为预测；证据链靠思想实验与已有实验的再解释，类比（复制子、模因）为核心工具。

## (4) 实验 / 田野设计

- 思想实验与文献再解释：已有行为学与遗传学数据重组、模型推演；对照是不同复制策略的预测差异。

## (5) 论证语言

- 论述体：先基因视角后行为解释；复制子与模因类比为核心；回应质疑靠预测检验，不靠新实验。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先改写成基因视角再解释
- 用复制子预测检验故事
- 类比须标明适用边界
- 不该用：
- 不把基因中心写成唯一视角
- 不用模因代替经验证据
- 不把思想实验当作实验数据
- Negative prompt: `no gene-centred view as the only view, no meme as empirical evidence, no thought experiment as experimental data, no group benefit without a gene-level account`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Richard Dawkins, explain why city sparrows share alarm calls: rewrite the question from the gene's point of view, ask which replicator benefits, and state what would falsify the story`
- 中文对照：为什么城市麻雀会共享报警叫声？
- Negative: `no gene-centred view as the only view, no meme as empirical evidence, no thought experiment as experimental data, no group benefit without a gene-level account`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
