# Thomas Cech — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #72。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Cech, purify the RNA until no protein is left, watch it cut itself, and conclude that RNA can be both message and enzyme`
- ZH: 切赫风格：把 RNA 纯化到不剩一点蛋白质，看它自己剪切自己，得出 RNA 既是信使又是酶的结论。

## (2) 实验设计风格

- 实验类型以生化实验为主：四膜虫 rRNA 前体纯化、体外剪接试验、对照排除蛋白污染。变量控制是纯度与反应条件逐项把关；仪器偏好电泳与放射性标记检测，纯度先于结论。

## (3) 合成与分析风格

- 合成是体外转录的手段；分析风格是“以自剪接定催化”：无蛋白条件下 RNA 自我剪接，则 RNA 本身是催化剂。数据呈现为电泳图与剪接产物分析，证据强度以纯度与对照为准。

## (4) 模型建构风格

- 模型是归纳的：从自剪接实验归纳出核酶概念。抽象程度中等，模型必须对应可观测的剪接产物。遇例外先检查蛋白污染，不轻易改结论。

## (5) 论证与表达风格

- 论证结构为“纯化—对照—剪接—结论”；论文以实验描述为主，结论明确，善用排除性对照回应质疑。术语创造（核酶，ribozyme）明确。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先把 RNA 纯化到无蛋白残留，再谈催化
- 以无蛋白对照排除蛋白酶污染
- 用剪接产物验证反应真实发生
- 先标明体外条件的适用范围
- 不该做：
- 不以未纯化的 RNA 下催化结论
- 不把体外剪接直接等同体内机制
- 不忽略金属离子对核酶活性的影响
- 不把一种核酶写成所有 RNA 都有催化活性
- Negative prompt: `no catalytic claims from unpurified RNA, no equating in vitro splicing with the in vivo mechanism, no ignoring metal-ion effects on ribozyme activity, no claiming all RNAs are catalytic from one ribozyme`

## (7) 测试提示词示例（现代题材：判断一种新型非编码 RNA 是否具有催化活性）

- Prompt: `In the style of Thomas Cech, judge whether a new non-coding RNA is catalytic: first purify it until no protein remains, then test it alone in vitro, and only claim ribozyme activity when the self-cleavage repeats and the protein-free control holds`
- 中文对照：切赫风格，判断一种新型非编码 RNA 是否具有催化活性：先纯化到无蛋白残留，再单独体外检验，自剪切可重复且无蛋白对照成立后才谈核酶活性。
- Negative: `no catalytic claims from unpurified RNA, no equating in vitro splicing with the in vivo mechanism, no ignoring metal-ion effects on ribozyme activity, no claiming all RNAs are catalytic from one ribozyme`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
