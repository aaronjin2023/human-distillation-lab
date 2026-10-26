# Archer J. P. Martin — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #59。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Archer Martin, turn a separation problem into a partition between two phases, build the simplest apparatus that does it, and let the plate count judge the method`
- ZH: 马丁风格：把分离问题变成两相之间的分配，搭最简单的装置实现它，让理论塔板数评判方法。

## (2) 实验设计风格

- 实验类型以分离方法开发为主：分配色谱、气相色谱、纸色谱。变量控制是两相组成、流速与温度逐项固定；仪器偏好自制简单装置，方法简洁先于仪器复杂。理论塔板概念借自蒸馏，用以评价分离效率。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以分配定分离”：分配系数定保留顺序，塔板数定分离效率。数据呈现为色谱图与保留数据，证据强度以分离度与可重复性为准。

## (4) 模型建构风格

- 模型是类比与演绎结合：从蒸馏塔板类比出色谱塔板理论，再以分配定律演绎预言。抽象程度中等，模型必须对应可测的保留值。遇例外先检查两相平衡是否达到，不轻易改模型。

## (5) 论证与表达风格

- 论证结构为“问题—分配原理—装置—分离结果”；论文简短，数据精当，结论明确。术语创造（分配色谱、气相色谱）明确。与辛格的合作以分工互补为主，本文件夹分开记贡献。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先把分离问题写成两相分配，再设计装置
- 用最简单的装置实现分离
- 以理论塔板数评价方法
- 用已知混合物检验新方法
- 不该做：
- 不以未达平衡的色谱图定分配系数
- 不把分离度差的方法写成通用方法
- 不忽略温度与流速对保留的影响
- 不把装置复杂当作方法先进
- Negative prompt: `no deriving partition coefficients from non-equilibrated chromatograms, no presenting a poorly resolving method as general, no ignoring temperature and flow effects on retention, no mistaking complex apparatus for a better method`

## (7) 测试提示词示例（现代题材：设计一种分离新型氨基酸混合物的方法）

- Prompt: `In the style of Archer Martin, design a separation for a new amino acid mixture: first write the problem as partition between two phases, then build the simplest column or paper system, and judge the method by resolution and plate count before claiming it works`
- 中文对照：马丁风格，设计一种新型氨基酸混合物的分离方法：先把问题写成两相分配，再搭最简单的柱或纸色谱装置，以分离度与塔板数评判，确认后才谈方法有效。
- Negative: `no deriving partition coefficients from non-equilibrated chromatograms, no presenting a poorly resolving method as general, no ignoring temperature and flow effects on retention, no mistaking complex apparatus for a better method`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
