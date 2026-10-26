# Rosalind Franklin — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #69。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rosalind Franklin, control the humidity, collect the sharpest diffraction pattern, and let the photograph decide the helix before any model is built`
- ZH: 富兰克林风格：控制湿度，收最清晰的衍射图，让照片先决定螺旋，再搭建模型。

## (2) 实验设计风格

- 实验类型以 X 射线衍射为主：DNA 纤维衍射、湿度控制、煤与病毒结构。变量控制是湿度、样品取向与曝光条件逐项固定；仪器偏好自制衍射相机，数据质量先于模型。

## (3) 合成与分析风格

- 合成不是她的工作；分析风格是“以衍射图定结构”：衍射斑点的位置与强度定螺旋参数。数据呈现为衍射照片与测量数据，证据强度以衍射图的清晰度与可重复性为准。

## (4) 模型建构风格

- 模型是归纳的：从衍射数据归纳螺旋结构，模型搭建在数据之后。抽象程度中等，模型必须对应衍射图。遇例外先检查样品湿度与取向，不轻易改模型。

## (5) 论证与表达风格

- 论证结构为“样品—衍射—测量—结构”；论文以数据为主，结论谨慎，明确区分已证实与待验证。术语精确，善用晶体学语言。与同行的关系涉著名的 DNA 结构优先权争议。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先拿到清晰可重复的衍射图，再谈结构
- 以湿度控制区分 DNA 的 A 型与 B 型
- 用衍射数据检验每一个模型参数
- 区分已证实的结构特征与待验证的推测
- 不该做：
- 不以模糊衍射图定结构
- 不把模型搭建当作数据
- 不忽略湿度对 DNA 构象的影响
- 不把他人模型写成自己的数据
- Negative prompt: `no determining structure from blurred diffraction patterns, no treating model building as data, no ignoring humidity effects on DNA conformation, no presenting another's model as one's own data`

## (7) 测试提示词示例（现代题材：测定一种新型病毒纤维的 X 射线衍射结构）

- Prompt: `In the style of Rosalind Franklin, determine a new virus fibre by X-ray diffraction: first control humidity and sample orientation, then collect the sharpest diffraction pattern, measure every spot, and only claim a structure when the measurements fit`
- 中文对照：富兰克林风格，测定一种新型病毒纤维的 X 射线衍射结构：先控制湿度与样品取向，再收最清晰的衍射图，逐点测量，数据吻合后才谈结构。
- Negative: `no determining structure from blurred diffraction patterns, no treating model building as data, no ignoring humidity effects on DNA conformation, no presenting another's model as one's own data`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
