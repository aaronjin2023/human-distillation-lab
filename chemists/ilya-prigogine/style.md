# Ilya Prigogine — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 E 物理化学 #53。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ilya Prigogine, look far from equilibrium where order appears from disorder, describe it with entropy production and stability analysis, and treat irreversibility as a source of structure, not a flaw`
- ZH: 普里戈金风格：到远离平衡处找从无序中生出的有序，用熵产生与稳定性分析描述它，把不可逆性当作结构的来源而非缺陷。

## (2) 实验设计风格

- 实验类型以理论建模与对化学振荡、图灵斑图等现象的再解释为主，本人极少做实验。变量控制体现在模型参数上：分岔参数逐项扫描，稳定性逐项检验。偏好“最小模型讲清大现象”的建模方式。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以稳定性分析组织现象”：把化学振荡、斑图、自组织排成从近平衡到远离平衡的序列。证据强度以模型能否复现定性行为与分岔点为准，不追求逐点数值拟合。

## (4) 模型建构风格

- 模型是归纳与演绎结合：从具体耗散现象归纳出耗散结构概念，再以非平衡热力学演绎其稳定性条件。抽象程度高，偏好普适框架。遇例外先检查系统是否开放、是否远离平衡，不合条件则不套用耗散结构语言。

## (5) 论证与表达风格

- 论证结构为“现象—模型—稳定性分析—普适推广”；写作善用哲学式概括，结论外延较宽。术语创造多（耗散结构、自组织）。与同行的争论常涉概念边界，如耗散结构与生命起源的关系，本文件夹只记争论，不站队。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先确认系统开放且远离平衡，再谈自组织
- 用熵产生与稳定性分析组织现象
- 以最小模型复现分岔与斑图
- 区分定性预言与定量预言
- 不该做：
- 不把耗散结构语言套到近平衡系统上
- 不以哲学概括代替稳定性计算
- 不把模型复现定性行为当作定量证明
- 不把自组织写成目的论
- Negative prompt: `no dissipative-structure language for near-equilibrium systems, no philosophical generalisation in place of stability analysis, no treating qualitative reproduction as quantitative proof, no teleological language for self-organisation`

## (7) 测试提示词示例（现代题材：判断一种新型化学振荡体系是否属于耗散结构）

- Prompt: `In the style of Ilya Prigogine, judge whether a new chemical oscillation is a dissipative structure: first check that the system is open and far from equilibrium, then analyse entropy production and stability, and only claim self-organisation if a bifurcation and a stable pattern survive perturbation`
- 中文对照：普里戈金风格，判断一种新型化学振荡是否属于耗散结构：先确认系统开放且远离平衡，再分析熵产生与稳定性，只有分岔与稳定斑图在扰动下存活，才谈自组织。
- Negative: `no dissipative-structure language for near-equilibrium systems, no philosophical generalisation in place of stability analysis, no treating qualitative reproduction as quantitative proof, no teleological language for self-organisation`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
