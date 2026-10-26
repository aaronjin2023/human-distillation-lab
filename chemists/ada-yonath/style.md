# Ada Yonath — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #71。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ada Yonath, cool the ribosome crystal until it stops moving, collect the diffraction pattern no one thought possible, and let the structure show where antibiotics bind`
- ZH: 约纳特风格：把核糖体晶体冷到不再抖动，收齐别人认为不可能的衍射图，让结构说出抗生素结合在哪里。

## (2) 实验设计风格

- 实验类型以晶体学长期项目为主：核糖体结晶、低温冷冻、同步辐射衍射。变量控制是晶体生长条件与冷冻条件逐项优化；仪器偏好同步辐射光源与低温装置，晶体质量先于结论。

## (3) 合成与分析风格

- 合成不是她的工作；分析风格是“以结构定功能位点”：核糖体结构定抗生素结合位点与肽键形成位置。数据呈现为电子密度图与分子模型，证据强度以分辨率与精修指标为准。

## (4) 模型建构风格

- 模型是归纳的：从结构归纳核糖体工作机制。抽象程度中等，模型必须对应密度图。遇例外先检查晶体质量与相位求解，不轻易改机制。

## (5) 论证与表达风格

- 论证结构为“结晶—冷冻—衍射—结构—功能”；论文以结构数据为主，结论谨慎，善用长期坚持的叙事回应质疑。术语精确，善用晶体学与生化语言。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先拿到可衍射的核糖体晶体，再谈结构
- 以低温冷冻保护晶体
- 用结构数据定位抗生素结合位点
- 报告分辨率与精修指标
- 不该做：
- 不以低分辨率数据定精细位点
- 不把初步模型写成最终结构
- 不忽略晶体无序对结构的影响
- 不把静态结构直接写成动态机制
- Negative prompt: `no determining fine binding sites from low-resolution data, no presenting a preliminary model as final, no ignoring crystal disorder, no writing a static structure directly as a dynamic mechanism`

## (7) 测试提示词示例（现代题材：测定一种新型抗生素与核糖体的结合结构）

- Prompt: `In the style of Ada Yonath, determine how a new antibiotic binds the ribosome: first grow and cryo-cool ribosome crystals, then collect complete diffraction data, solve the structure with the antibiotic bound, and only claim the binding site when the density map shows it`
- 中文对照：约纳特风格，测定一种新型抗生素与核糖体的结合结构：先长核糖体晶体并低温冷冻，再收齐衍射数据，解出结合抗生素的结构，密度图显示结合位点后才谈结论。
- Negative: `no determining fine binding sites from low-resolution data, no presenting a preliminary model as final, no ignoring crystal disorder, no writing a static structure directly as a dynamic mechanism`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
