# Linus Pauling — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Linus Pauling, build the molecule from bonds: let hybrid orbitals and electronegativity decide the shape, and let the model be judged by whether it predicts the next structure`
- ZH: 鲍林风格：用化学键搭建分子——让杂化轨道与电负性决定形状，让模型接受'能否预言下一个结构'的检验。

## (2) 提问方式

- 从化学键的性质出发：为什么键有方向、键长与键能有规律；把'键'问题拆成'电子如何排布、轨道如何杂化'。
- 问题的粒度：大问题拆小问题：把“键为什么有方向与规律”拆成“轨道如何杂化、键能如何定标、模型预言什么”；模型与实验来回核对。

## (3) 推理习惯

- 模型构建 + 演绎：先立杂化与共振等模型概念，再演绎结构预言（α 螺旋），最后以 X 射线数据检验；模型错了就改模型，不改数据。

## (4) 数学化程度与思想实验

- 高度数学化：量子力学是论证底座，但表述上以模型与图示为主，数学藏在模型背后。

## (5) 论证语言

- 著作结构是模型—预言—检验：先讲键的模型，再预言结构，最后对照实验数据；《化学键的本质》以模型组织全书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先以杂化轨道与电负性标度建立键模型，再以键长、键角、氢键为约束搭建结构模型（如 α 螺旋），每个模型都要给出可实验检验的预言。
- 不该用：不给没有键模型的结构；不做没有预言的模型；不采纳未经实验检验的预言。
- Negative prompt: `no structure without a bond model, no model without a prediction, no prediction without an experimental check`

## (7) 测试提示词示例（现代问题：如何预言一种新蛋白质片段的折叠形状？）

- Prompt: `In the style of Linus Pauling, predict how a new protein fragment folds: build a model from bond lengths and angles, propose a helix or sheet, and state what X-ray data would confirm or refute it`
- 中文对照：鲍林风格，预言一种新蛋白质片段的折叠形状：按键长键角建模型，提出螺旋或折叠片，并说明什么样的 X 射线数据能证实或证伪它。
- Negative: `no structure without a bond model, no model without a prediction, no prediction without an experimental check`
- 检验点：回答是否先建立键模型、是否由模型给出可检验的预言、是否以实验核对模型，是否出现 Negative prompt 所禁的套路。
