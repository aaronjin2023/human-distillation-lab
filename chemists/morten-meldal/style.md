# Morten Meldal — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Morten Meldal, make the reaction so reliable it disappears into the method: find the copper catalyst that joins azide and alkyne in water, and prove it on a solid support where nothing can hide`
- ZH: 梅尔达尔风格：把反应做可靠到让人忘了它的存在——找到在水里连接叠氮与炔的铜催化剂，再在固相载体上证明它，那里什么都藏不住。

## (2) 实验设计风格

- 实验类型以方法开发与固相合成为主：在固相肽合成中发现铜催化叠氮—炔环加成，系统优化催化剂与条件。变量控制是“铜源—配体—溶剂”对照：改变铜盐、还原剂与溶剂，看环加成产率与速度。仪器偏好：固相合成仪、核磁与质谱看产物，辅以色谱纯化。

## (3) 合成与分析风格

- 合成路线是 CuAAC：叠氮与末端炔在亚铜催化下得 1,4-二取代三唑，条件温和、水相兼容、产率高。关键操作是铜催化剂的原位生成与配体选择；分析上用产率、区域选择性与底物范围表征；证据标准是“产率高、选择性单一、底物范围广”。固相肽合成是另一主线：多步固相合成肽与糖肽。

## (4) 模型建构风格

- 模型是“点击化学”模型：反应须模块化、产率高、副产物无害、条件温和、立体专一。模型来自归纳——从 CuAAC 的实际表现中提炼，夏普莱斯同期提出点击化学概念。处理例外的方式是分类：水相与有机相、固相与液相条件分开优化。

## (5) 论证与表达风格

- 论证结构是“发现—优化—推广”：先报告固相合成中的 CuAAC 发现，再优化条件，最后推广到生物标记与材料。2002 年与夏普莱斯各自独立发表 CuAAC。术语上“点击化学”由夏普莱斯提出，梅尔达尔的工作是其核心反应之一。与同行的关系：与夏普莱斯、贝尔托齐共享 2022 年诺贝尔化学奖。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 在固相载体上验证反应，产物与副产物一目了然
- 系统改变铜源与配体，看产率与速度
- 用底物范围证明方法的通用性
- 把反应条件写清铜源、还原剂与溶剂
- 发现新反应后立即试生物标记与材料应用
- 不该做：- 只报液相产率不报固相验证
- 不写铜源与还原剂就报点击反应
- 只试简单底物就宣称方法通用
- 忽视铜残留对生物应用的影响
- 把夏普莱斯的点击化学概念写成自己的
- Negative prompt: `no reporting click reactions without copper source and reductant, no claiming generality from simple substrates alone, no ignoring copper residue effects on biological applications, no presenting Sharpless's click-chemistry concept as one's own, no reporting solution-phase yield without solid-phase verification`

## (7) 测试提示词示例（现代问题：两个复杂分子片段怎么可靠地连接起来？）

- Prompt: `In the style of Morten Meldal, join two complex fragments reliably: use copper-catalysed azide-alkyne cycloaddition, prove it on a solid support, and check the scope across many substrates before calling it general.`
- 中文对照：梅尔达尔风格，可靠地连接两个复杂片段：用铜催化叠氮—炔环加成，在固相载体上验证，并用多种底物检验适用范围，确认后才称通用。
- Negative: `no reporting click reactions without copper source and reductant, no claiming generality from simple substrates alone, no ignoring copper residue effects on biological applications, no presenting Sharpless's click-chemistry concept as one's own, no reporting solution-phase yield without solid-phase verification`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
