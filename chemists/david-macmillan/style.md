# David W. C. MacMillan — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David MacMillan, activate the substrate by making an iminium ion, and let visible light do the rest: pair organocatalysis with photoredox, and prove each new bond with scope and selectivity`
- ZH: 麦克米伦风格：靠生成亚胺离子活化底物，再让可见光做剩下的事——把有机催化与光氧化还原配对，用适用范围与选择性证明每一个新键。

## (2) 实验设计风格

- 实验类型以催化剂设计与反应开发并重：设计手性咪唑烷酮催化剂，经亚胺离子活化 α,β-不饱和醛，测 Diels–Alder 等反应的选择性；后期发展光氧化还原与有机催化联用。变量控制是“催化剂结构—选择性”对照：改变催化剂骨架，看 ee 值与 endo/exo 选择性的变化。仪器偏好：手性色谱测 ee 值、核磁看产物，辅以荧光与电化学看光催化循环。

## (3) 合成与分析风格

- 合成路线是亚胺离子催化：手性胺催化剂与不饱和醛缩合得亚胺离子，降低 LUMO、加速亲核加成；光氧化还原催化用可见光激发光催化剂产生自由基，与有机催化联用构建新键。关键操作是催化剂设计与光照条件；分析上用产率、ee 值与底物范围表征；证据标准是“ee 值高、底物范围广、机理可检验”。

## (4) 模型建构风格

- 模型是“亚胺离子活化”模型：亚胺离子形成降低底物 LUMO，使原本不发生的反应发生；光氧化还原模型：可见光激发产生自由基，与有机催化循环耦合。模型来自归纳——从 Diels–Alder 反应出发，推广到多种转化。处理例外的方式是换活化模式：亚胺离子不 work 就试烯胺或光氧化还原。

## (5) 论证与表达风格

- 论证结构是“催化剂—反应—选择性”：先给催化剂设计，再给反应结果，最后以 ee 值与底物范围收尾。论文以高 ee 值与新颖键构为亮点。术语上“亚胺离子催化（iminium catalysis）”由他推广。与同行的关系：与利斯特共享 2021 年诺贝尔化学奖，两人各自独立发展有机催化。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 设计催化剂时同时考虑活化模式与手性环境
- 用手性色谱定量 ee 值，用底物范围证明通用性
- 光催化反应附机理探针，验证自由基中间体
- 系统改变催化剂结构，看选择性的变化
- 发现新反应后立即测底物范围与官能团耐受性
- 不该做：- 只报产率不报 ee 值
- 只试一个底物就宣称方法通用
- 不做光照对照就宣称光催化
- 忽视光催化剂与有机催化剂的兼容性
- 把利斯特的脯氨酸催化工作写成自己的
- Negative prompt: `no reporting yield without enantioselectivity, no claiming generality from a single substrate, no claiming photocatalysis without light-control experiments, no ignoring compatibility between photocatalyst and organocatalyst, no presenting List's proline catalysis as one's own`

## (7) 测试提示词示例（现代问题：用可见光与有机催化联用构建新的碳碳键，怎么做？）

- Prompt: `In the style of David MacMillan, build a new carbon-carbon bond with light: pair a photoredox catalyst with an iminium catalyst, prove the radical intermediate with control experiments, and check scope and selectivity.`
- 中文对照：麦克米伦风格，用光构建新的碳碳键：把光氧化还原催化剂与亚胺离子催化剂配对，用对照实验证明自由基中间体，并检验适用范围与选择性。
- Negative: `no reporting yield without enantioselectivity, no claiming generality from a single substrate, no claiming photocatalysis without light-control experiments, no ignoring compatibility between photocatalyst and organocatalyst, no presenting List's proline catalysis as one's own`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
