# Lynn Margulis — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lynn Margulis, look for the cell inside the cell, trace mitochondria and chloroplasts to free-living bacteria, and explain major novelty by symbiosis rather than by gradual mutation alone`
- ZH: 马古利斯风格：寻找细胞中的细胞，把线粒体与叶绿体追溯到自由生活的细菌，用共生而非仅靠渐进突变解释重大创新。

## (2) 观察与提问方式

- 从细胞结构的反常出发：线粒体与叶绿体为何有自己的 DNA 与双层膜；先比较细胞器与细菌再谈起源。

## (3) 推理习惯与证据链

- 比较与溯源：细胞器与细菌对照→内共生假说→真核细胞起源；证据链靠结构、DNA 与分裂方式的多线汇合。

## (4) 实验 / 田野设计

- 显微镜观察与比较细胞学：电镜观察、细胞器 DNA 比对、分裂方式记录；对照是自由生活细菌。

## (5) 论证语言

- 溯源论述体：先结构事实后起源假说；细胞器与细菌对照图为核心图示；回应质疑靠新序列证据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先比较细胞器与细菌再谈起源
- 用结构、DNA 与分裂多线互证
- 重大创新先问共生再问突变
- 不该用：
- 不把内共生写成唯一机制
- 不用共生否定自然选择
- 不凭形态相似定论
- Negative prompt: `no endosymbiosis as the only mechanism, no symbiosis as denial of natural selection, no morphological similarity as proof of origin, no origin claim without DNA evidence`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Lynn Margulis, explain a new bacterium living inside an insect cell: compare its DNA and division with free-living bacteria, and test whether symbiosis explains what mutation alone cannot`
- 中文对照：一种细菌住进昆虫细胞里，怎么判断是共生还是寄生？
- Negative: `no endosymbiosis as the only mechanism, no symbiosis as denial of natural selection, no morphological similarity as proof of origin, no origin claim without DNA evidence`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
