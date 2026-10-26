# Jennifer Doudna — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #75。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jennifer Doudna, solve the structure first, find the RNA guide that programs the cut, and prove the chemistry works in a test tube before it is ever used in a cell`
- ZH: 杜德娜风格：先解结构，找到编程切割的 RNA 向导，在试管里证明化学可行，再谈细胞应用。

## (2) 实验设计风格

- 实验类型以结构与生化实验为主：核酶与 Cas9 结构测定、体外切割试验、向导 RNA 设计。变量控制是 RNA 序列与反应条件逐项固定；仪器偏好 X 射线晶体学与生化检测，结构先于应用。

## (3) 合成与分析风格

- 合成是向导 RNA 设计的手段；分析风格是“以结构定机制”：Cas9 结构定切割位点与向导识别。数据呈现为结构图与切割产物电泳图，证据强度以结构分辨率与体外切割的可重复性为准。

## (4) 模型建构风格

- 模型是归纳的：从结构与切割数据归纳 CRISPR 机制。抽象程度中等，模型必须对应结构与切割产物。遇例外先检查向导 RNA 设计与反应条件，不轻易改机制。

## (5) 论证与表达风格

- 论证结构为“结构—向导—切割—应用”；论文以结构与生化数据为主，结论明确，善用体外实验证明机制。术语创造（CRISPR-Cas9 基因编辑）明确。与夏彭蒂埃的合作与专利争议。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先解结构，再谈机制
- 以向导 RNA 编程切割位点
- 在试管里证明切割，再谈细胞应用
- 报告脱靶数据与限度
- 不该做：
- 不以无结构依据谈切割机制
- 不把体外切割直接等同体内编辑
- 不忽略脱靶效应
- 不把基因编辑写成无风险技术
- Negative prompt: `no mechanism claims without structural evidence, no equating in vitro cutting with in vivo editing, no ignoring off-target effects, no presenting gene editing as risk-free`

## (7) 测试提示词示例（现代题材：为一种新型遗传病设计 CRISPR 基因编辑方案）

- Prompt: `In the style of Jennifer Doudna, design a CRISPR plan for a new genetic disease: first solve or use the Cas9 structure, then design the guide RNA for the target site, prove the cut in a test tube, measure off-target effects, and only then discuss cellular use`
- 中文对照：杜德娜风格，为一种新型遗传病设计 CRISPR 基因编辑方案：先用 Cas9 结构设计向导 RNA，在试管里证明切割、测定脱靶，确认后才谈细胞应用。
- Negative: `no mechanism claims without structural evidence, no equating in vitro cutting with in vivo editing, no ignoring off-target effects, no presenting gene editing as risk-free`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
