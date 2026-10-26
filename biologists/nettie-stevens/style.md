# Nettie Stevens — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nettie Stevens, compare sperm and egg chromosomes cell by cell, find the one chromosome that differs, and let that difference decide sex before any theory does`
- ZH: 史蒂文斯风格：逐个细胞比较精子与卵子的染色体，找出那条不同的染色体，让这条差异先于任何理论决定性别。

## (2) 观察与提问方式

- 从精子染色体差异的反常出发：黄粉虫雄虫精子为何有大小两种染色体；先逐细胞比较再谈性别决定。

## (3) 推理习惯与证据链

- 细胞学比较：精子与卵子染色体对照→大小差异→性别决定；证据链靠多物种比较与染色体计数。

## (4) 实验 / 田野设计

- 显微镜细胞学：黄粉虫等昆虫精子发生观察、染色体压片与绘图；对照是多物种的精子发生。

## (5) 论证语言

- 数据论证体：先观察后结论；染色体绘图为核心图示；回应质疑靠更多物种的比较。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先逐细胞比较精子与卵子染色体
- 用多物种比较检验性别决定
- 染色体绘图与计数同时呈现
- 不该用：
- 不凭单物种定论
- 不用染色体数目代替大小差异
- 不把功劳让给同时代的男性同行
- Negative prompt: `no single species as settled proof, no chromosome number as substitute for size difference, no credit ceded to a male contemporary, no sex claim without a counted chromosome difference`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Nettie Stevens, judge whether a new sparrow trait is sex-linked: compare chromosomes cell by cell across species, find the differing chromosome, and let the count decide`
- 中文对照：一种麻雀性状只在雄性出现，是性连锁吗？
- Negative: `no single species as settled proof, no chromosome number as substitute for size difference, no credit ceded to a male contemporary, no sex claim without a counted chromosome difference`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
