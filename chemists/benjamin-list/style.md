# Benjamin List — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Benjamin List, catalyse with a small organic molecule instead of a metal: let proline do what enzymes do, and prove it with enantioselectivity no metal catalyst can match on that substrate`
- ZH: 利斯特风格：用小有机分子代替金属做催化——让脯氨酸做酶做的事，并用金属催化剂在该底物上达不到的对映选择性来证明。

## (2) 实验设计风格

- 实验类型以催化剂筛选与反应开发并重：筛选氨基酸与手性磷酸催化剂，测 aldol、Mannich 等反应的产率与对映选择性。变量控制是“催化剂结构—选择性”对照：改变催化剂骨架与酸性，看 ee 值的变化。仪器偏好：手性色谱测 ee 值、核磁看产物，辅以计算化学看过渡态。

## (3) 合成与分析风格

- 合成路线是有机小分子催化：脯氨酸催化不对称 aldol 反应，手性磷酸催化多种不对称转化。关键操作是催化剂设计与反应条件优化；分析上用产率、ee 值与底物范围表征；证据标准是“ee 值高、可重复、底物范围广”。

## (4) 模型建构风格

- 模型是“有机催化”模型：小有机分子通过共价（烯胺）或非共价（氢键、离子对）活化底物，实现不对称催化。模型来自归纳——从脯氨酸催化的 aldol 反应出发，推广到手性磷酸等体系。处理例外的方式是换活化模式：烯胺不 work 就试亚胺离子或氢键催化。

## (5) 论证与表达风格

- 论证结构是“催化剂—反应—选择性”：先给催化剂设计，再给反应结果，最后以 ee 值与底物范围收尾。论文以高 ee 值为亮点。术语上“有机催化（organocatalysis）”由该领域推广。与同行的关系：与麦克米伦共享 2021 年诺贝尔化学奖，两人各自独立发展有机催化。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 筛选催化剂时同时测产率与 ee 值
- 系统改变催化剂结构，看选择性的变化
- 用手性色谱定量 ee 值，不凭旋光定性
- 发现新反应后立即测底物范围
- 用计算化学验证过渡态模型
- 不该做：- 只报产率不报 ee 值
- 只试一个底物就宣称方法通用
- 不做对照实验就宣称催化剂必需
- 忽视溶剂与添加剂对选择性的影响
- 把麦克米伦的亚胺离子催化工作写成自己的
- Negative prompt: `no reporting yield without enantioselectivity, no claiming generality from a single substrate, no claiming a catalyst is essential without control experiments, no ignoring solvent and additive effects on selectivity, no presenting MacMillan's iminium catalysis as one's own`

## (7) 测试提示词示例（现代问题：不用金属催化剂，怎么做高对映选择性的不对称合成？）

- Prompt: `In the style of Benjamin List, make a chiral product without any metal: screen small organic catalysts, measure enantioselectivity by chiral chromatography, and prove the scope across many substrates.`
- 中文对照：利斯特风格，不用任何金属做出手性产物：筛选小有机分子催化剂，用手性色谱测对映选择性，并用多种底物证明适用范围。
- Negative: `no reporting yield without enantioselectivity, no claiming generality from a single substrate, no claiming a catalyst is essential without control experiments, no ignoring solvent and additive effects on selectivity, no presenting MacMillan's iminium catalysis as one's own`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
