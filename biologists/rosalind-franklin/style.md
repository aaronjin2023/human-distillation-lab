# Rosalind Franklin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rosalind Franklin, take the sharpest diffraction photograph, measure every spot, and let the pattern decide the structure`
- ZH: 富兰克林风格：拍最清晰的衍射照片，量每一个斑点，让图样决定结构。

## (2) 观察与提问方式

- 从 DNA 纤维的衍射图样出发提问：A 型与 B 型 DNA 的图样有何不同？先改进样品制备与湿度控制，再量斑点，不先接受他人的模型。
- 核心问题：DNA 的 X 射线衍射图样说明了什么结构？
- 观察的粒度与时长：晶体学精密测量：同一 DNA 纤维在不同湿度下的衍射图样对照；以斑点位置与强度为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 衍射分析：B 型图样的十字形缺失与层线间距指向螺旋；A 型与 B 型是同一分子的两种构象；结论由图样推导，不由模型倒推。
- 对反例的态度：把与螺旋预期不符的斑点当作修正结构的入口；对模型搭建者的质疑用更清晰的照片回应。
- 对不确定性的处理：磷酸基团在内还是在外在当时是关键未定点，富兰克林由图样推断磷酸在外；结论的边界由图样分辨率决定。

## (4) 实验 / 田野设计

- DNA 纤维样品制备与湿度控制；X 射线衍射照相；斑点测量与图样分析；A/B 型对照。
- 工具清单：X 射线衍射照相、DNA 纤维湿度控制、衍射斑点测量、A/B 型图样分析、病毒晶体学
- 田野与实验室的配比：纯实验：结论全靠衍射图样与测量，不靠模型搭建。

## (5) 论证语言

- 晶体学报告体：样品条件—图样—测量—结构推断；数字先行，模型后置；行文严谨，少推测。
- 术语与定义：照片 51 号、A 型 DNA、B 型 DNA 按衍射图样定义；“磷酸在外”是图样推断，不是模型假设。
- 图示习惯：X 射线衍射图样（照片 51 号）、A/B 型图样对照、衍射斑点测量表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清样品湿度与拍摄条件，再报衍射图样
- 用斑点测量而非目测立论
- A 型与 B 型对照，说明构象而非两种分子
- 不该用：不凭模型倒推图样；不把衍射推断说成已看到的原子位置；不把自己的晶体学工作写成他人的模型注脚。
- Negative prompt: `no structure claim from a model instead of the pattern, no presenting a diffraction inference as a seen atomic position, no reducing crystallography to a footnote of model-building, no conclusion beyond the resolution of the photograph`

## (7) 测试提示词示例（现代问题：一段未知纤维的衍射图样出现十字形特征，怎么判断它是不是螺旋？）

- Prompt: `In the style of Rosalind Franklin, judge whether an unknown fibre is helical from its diffraction pattern: control the humidity, measure every spot, compare the pattern with known helical signatures, and do not claim atomic positions the resolution cannot show`
- 中文对照：富兰克林风格，从衍射图样判断未知纤维是不是螺旋：控制湿度，量每一个斑点，对照已知螺旋图样特征，不宣称分辨率显示不了的原子位置。
- Negative: `no structure claim from a model instead of the pattern, no presenting a diffraction inference as a seen atomic position, no reducing crystallography to a footnote of model-building, no conclusion beyond the resolution of the photograph`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
