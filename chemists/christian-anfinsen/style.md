# Christian Anfinsen — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #67。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Christian Anfinsen, unfold a protein, let it refold by itself, and conclude that the amino acid sequence alone carries the folding instructions`
- ZH: 安芬森风格：把蛋白质展开，让它自己重新折叠，得出氨基酸序列本身就带有折叠指令的结论。

## (2) 实验设计风格

- 实验类型以变性与复性实验为主：核糖核酸酶变性、透析去除变性剂、酶活恢复测定。变量控制是变性条件与复性条件逐项固定；仪器偏好分光光度与酶活测定，简单测定先于复杂理论。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以复性定折叠信息来源”：变性后自发恢复活性，则折叠信息在序列中。数据呈现为酶活恢复曲线，证据强度以复性的可重复性与对照为准。

## (4) 模型建构风格

- 模型是归纳的：从复性实验归纳出热力学假说。抽象程度中等，模型必须对应可测的酶活恢复。遇例外先检查复性条件与二硫键配对，不轻易改假说。

## (5) 论证与表达风格

- 论证结构为“变性—复性—酶活—假说”；论文简短，结论明确，善用决定性实验。术语创造（热力学假说）明确。与同行的关系以实验验证与讨论为主。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先证明变性完全，再谈复性
- 以酶活恢复定量复性程度
- 用对照区分自发折叠与协助折叠
- 先标明假说的适用范围
- 不该做：
- 不以部分复性当完全复性
- 不把体外复性直接等同体内折叠
- 不忽略二硫键错配的影响
- 不把热力学假说写成动力学机制
- Negative prompt: `no treating partial refolding as complete refolding, no equating in vitro refolding with in vivo folding, no ignoring mismatched disulfide pairing, no writing the thermodynamic hypothesis as a kinetic mechanism`

## (7) 测试提示词示例（现代题材：判断一种新型蛋白质能否自发复性）

- Prompt: `In the style of Christian Anfinsen, judge whether a new protein refolds by itself: first denature it completely, then remove the denaturant and measure activity recovery, and only claim spontaneous folding when the control repeats and the recovery is quantitative`
- 中文对照：安芬森风格，判断一种新型蛋白质能否自发复性：先完全变性，再去除变性剂、测定酶活恢复，对照可重复且恢复可定量后才谈自发折叠。
- Negative: `no treating partial refolding as complete refolding, no equating in vitro refolding with in vivo folding, no ignoring mismatched disulfide pairing, no writing the thermodynamic hypothesis as a kinetic mechanism`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
