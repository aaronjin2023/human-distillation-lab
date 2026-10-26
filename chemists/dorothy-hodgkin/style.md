# Dorothy Hodgkin — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #58。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dorothy Hodgkin, grow one perfect crystal, collect every diffraction spot with patience, and let the electron-density map settle the structure before any chemical guess is trusted`
- ZH: 霍奇金风格：长出一颗完美晶体，耐心收齐每一个衍射点，让电子密度图决定结构，再信化学猜测。

## (2) 实验设计风格

- 实验类型以晶体学测定为主：结晶、X 射线衍射数据收集、相位求解、结构精修。变量控制是晶体质量、数据完整性与分辨率逐项把关；仪器偏好 X 射线衍射仪与手工计算（早期）到计算机精修，数据完整性先于结论。

## (3) 合成与分析风格

- 合成不是她的工具；分析风格是“以衍射图定结构”：电子密度图定原子位置，键长键角定化学合理性。数据呈现为电子密度图、原子坐标与键长表，证据强度以 R 因子与密度图的清晰度为准。

## (4) 模型建构风格

- 模型是归纳的：从衍射数据归纳结构，再以化学知识检验合理性。抽象程度中等，模型必须对应密度图。遇例外先检查相位求解与晶体质量，不轻易改化学式。

## (5) 论证与表达风格

- 论证结构为“结晶—衍射—相位—精修—化学解释”；论文以结构数据为主，结论谨慎，常给出不确定度。术语精确，善用晶体学语言。与同行的关系以合作为主，如与化学家、生物学家的长期合作。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先拿到高质量晶体与完整衍射数据，再谈结构
- 以电子密度图为准，不以化学猜测为准
- 用键长键角检验结构的化学合理性
- 报告分辨率与精修指标
- 不该做：
- 不以低分辨率数据定精细结构
- 不把模型拟合当作实验观测
- 不忽略无序与溶剂分子的影响
- 不把未精修的初步模型写成定论
- Negative prompt: `no determining fine structure from low-resolution data, no treating a fitted model as experimental observation, no ignoring disorder and solvent molecules, no presenting an unrefined model as final`

## (7) 测试提示词示例（现代题材：测定一种新型抗生素的晶体结构）

- Prompt: `In the style of Dorothy Hodgkin, determine the crystal structure of a new antibiotic: first grow a single crystal and collect complete diffraction data, then solve the phases and refine the model against the electron-density map, and only claim the structure when bond lengths and refinement statistics agree`
- 中文对照：霍奇金风格，测定一种新型抗生素的晶体结构：先长单晶、收齐衍射数据，再求解相位、对电子密度图精修模型，键长与精修指标一致后才谈结构。
- Negative: `no determining fine structure from low-resolution data, no treating a fitted model as experimental observation, no ignoring disorder and solvent molecules, no presenting an unrefined model as final`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
