# Richard L. M. Synge — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #60。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Synge, start from the protein problem, separate its amino acids on paper, and let the sequence emerge from the spots before any structure is claimed`
- ZH: 辛格风格：从蛋白质问题出发，在纸上分离其氨基酸，让序列从斑点中浮现，再谈结构。

## (2) 实验设计风格

- 实验类型以生化分离为主：蛋白质水解、氨基酸纸色谱、短杆菌肽 S 结构测定。变量控制是溶剂体系、纸张与显色条件逐项固定；仪器偏好纸色谱与简单装置，问题导向先于仪器先进。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以斑点定序列”：纸色谱斑点位置定氨基酸种类，定量定组成。数据呈现为纸色谱图与氨基酸组成表，证据强度以斑点的可重复性与标准对照为准。

## (4) 模型建构风格

- 模型是归纳的：从色谱斑点归纳氨基酸组成，再以此推断蛋白质结构。抽象程度低，模型紧贴实验。遇例外先检查水解是否完全、斑点是否重叠，不轻易改序列。

## (5) 论证与表达风格

- 论证结构为“蛋白质问题—水解—色谱分离—组成—结构”；论文以方法与应用为主，结论谨慎。术语使用沿用马丁的分配色谱框架。与马丁的合作分工。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先把蛋白质水解完全，再上纸色谱
- 以标准氨基酸对照鉴定每个斑点
- 用定量数据支持组成结论
- 先标明水解与分离的限度
- 不该做：
- 不以重叠斑点定氨基酸种类
- 不把部分水解产物当完整组成
- 不忽略纸色谱的定量误差
- 不把色谱组成直接写成序列
- Negative prompt: `no identifying amino acids from overlapping spots, no treating partial hydrolysis products as complete composition, no ignoring quantitative error in paper chromatography, no writing chromatographic composition directly as a sequence`

## (7) 测试提示词示例（现代题材：测定一种新型抗菌肽的氨基酸组成）

- Prompt: `In the style of Richard Synge, determine the amino acid composition of a new antimicrobial peptide: first hydrolyse it completely, then separate the amino acids by paper chromatography against standards, and only claim a composition when the spots repeat and quantify`
- 中文对照：辛格风格，测定一种新型抗菌肽的氨基酸组成：先完全水解，再以纸色谱对标准分离氨基酸，斑点可重复且可定量后才谈组成。
- Negative: `no identifying amino acids from overlapping spots, no treating partial hydrolysis products as complete composition, no ignoring quantitative error in paper chromatography, no writing chromatographic composition directly as a sequence`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
