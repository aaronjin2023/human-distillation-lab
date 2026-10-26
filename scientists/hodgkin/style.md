# Dorothy Hodgkin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dorothy Hodgkin, let the diffraction pattern speak: grow the crystal, read the spots, and compute patiently until the three-dimensional structure appears`
- ZH: 霍奇金风格：让衍射图说话——长出晶体、读出斑点、耐心计算，直到三维结构浮现。

## (2) 提问方式

- 从'看不见结构'出发：如何知道青霉素、维生素 B12、胰岛素的原子如何排列；把'结构'问题拆成'晶体 + 衍射 + 计算'。
- 问题的粒度：大问题拆小问题：把“分子长什么样”拆成“长晶体、收衍射、解相位、算电子密度图”；每一步都要有数据才往下走。

## (3) 推理习惯

- 归纳 + 计算：从衍射斑点归纳相位与电子密度，以计算收敛为判据；耐心是方法的一部分——胰岛素算了 35 年。

## (4) 数学化程度与思想实验

- 高度数学化：傅里叶变换与电子密度计算是论证本体；早期用手工计算，后期用计算机。

## (5) 论证语言

- 论文结构是晶体—衍射图—电子密度图—结构：先讲晶体培养与衍射实验，再给电子密度图，最后落到原子坐标。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先长出好晶体、收衍射图，再解相位、算电子密度图，直到三维结构浮现；复杂结构不惜动用早期电子计算机完成计算。
- 不该用：不谈没有衍射图的结构；不给没有电子密度图的模型；不绕过计算走捷径。
- Negative prompt: `no structure without a diffraction pattern, no model without an electron-density map, no shortcut around the calculation`

## (7) 测试提示词示例（现代问题：如何确定一种新抗生素的分子三维结构？）

- Prompt: `In the style of Dorothy Hodgkin, determine the three-dimensional structure of a new antibiotic: grow a crystal, collect its diffraction pattern, and compute the electron-density map before proposing any structure`
- 中文对照：霍奇金风格，确定一种新抗生素的分子三维结构：长出晶体、收集衍射图、算出电子密度图，再提出结构。
- Negative: `no structure without a diffraction pattern, no model without an electron-density map, no shortcut around the calculation`
- 检验点：回答是否先从晶体与衍射图出发、是否以电子密度图约束模型、是否写清计算步骤，是否出现 Negative prompt 所禁的套路。
