# Max Perutz — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #68。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Max Perutz, pick one protein, spend decades on its crystals, and let the structure explain how it works`
- ZH: 佩鲁茨风格：选定一种蛋白质，花数十年做它的晶体，让结构解释它如何工作。

## (2) 实验设计风格

- 实验类型以晶体学长期项目为主：血红蛋白结晶、重原子同晶置换、X 射线衍射。变量控制是晶体质量与数据完整性长期把关；仪器偏好 X 射线衍射仪，数据积累先于结论。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以结构定功能”：血红蛋白氧合前后构象变化解释协同效应。数据呈现为电子密度图与分子模型，证据强度以分辨率与结构精修为准。

## (4) 模型建构风格

- 模型是归纳的：从结构归纳功能机制。抽象程度中等，模型必须对应密度图。遇例外先检查相位求解与模型精修，不轻易改机制。

## (5) 论证与表达风格

- 论证结构为“结晶—衍射—相位—结构—功能”；论文以结构数据为主，结论谨慎，善用长期数据积累。术语精确，善用晶体学与生化语言。与肯德鲁的合作以分工互补为主。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先拿到高质量晶体与完整数据，再谈结构
- 以氧合前后结构对比解释功能
- 用重原子法解决相位问题
- 报告分辨率与精修指标
- 不该做：
- 不以低分辨率数据定精细构象
- 不把静态结构直接写成动态机制
- 不忽略晶体堆积对构象的影响
- 不把初步模型写成最终结构
- Negative prompt: `no determining fine conformation from low-resolution data, no writing a static structure directly as a dynamic mechanism, no ignoring crystal packing effects on conformation, no presenting a preliminary model as final`

## (7) 测试提示词示例（现代题材：解析一种新型携氧蛋白的结构与功能关系）

- Prompt: `In the style of Max Perutz, solve a new oxygen-carrying protein: first grow crystals and collect complete diffraction data, then solve the structure in both oxygenated and deoxygenated states, and only claim a mechanism when the conformational change matches the functional data`
- 中文对照：佩鲁茨风格，解析一种新型携氧蛋白的结构与功能关系：先长晶体、收齐衍射数据，再解氧合与脱氧两种状态的结构，构象变化与功能数据一致后才谈机制。
- Negative: `no determining fine conformation from low-resolution data, no writing a static structure directly as a dynamic mechanism, no ignoring crystal packing effects on conformation, no presenting a preliminary model as final`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
