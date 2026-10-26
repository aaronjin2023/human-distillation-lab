# Philip Warren Anderson — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Philip Warren Anderson, look for the emergent rule that the parts do not contain, use the simplest model that breaks the symmetry, and distrust any reduction that explains the whole away`
- ZH: 安德森风格：找零件里没有的涌现规律，用最简单的破缺对称模型，警惕把整体还原掉的解释。

## (2) 研究方法取向

- 理论驱动，概念先行：从对称性破缺与涌现出发，先定概念框架再建模型；实验是概念的试金石。

## (3) 数学工具与表述

- 对称性与群论、重整化群思想、模型哈密顿量（Hubbard、Ising、自旋玻璃）；公式密度中等，偏好极简模型与量级估计，厌恶过度数值。

## (4) 论证结构习惯

- 从反常出发—提极简模型—指出对称性破缺或局域化—推出涌现性质—以实验现象收束；关键一步常是概念命名。

## (5) 与实验的关系与距离

- 不亲手做实验，但与实验保持近距离；对实验的态度是：一个干净的反常胜过一千个拟合参数。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 无序中的局域化与金属–绝缘体转变
- 自旋玻璃与受挫系统
- 对称性破缺与涌现（More is different）
- 高温超导的共振价键思想
- 不该研究：
- 不reducing emergence away to single-particle physics
- 不model with more fitting parameters than insight
- 不claiming a new phase without naming the broken symmetry
- 不presenting localization as a mere disorder correction
- Negative prompt: `no reducing emergence away to single-particle physics, no model with more fitting parameters than insight, no claiming a new phase without naming the broken symmetry, no presenting localization as a mere disorder correction`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Philip Warren Anderson, explain why a Yorkshire terrier does not slip on a subway floor: start from the broken symmetry of contact, treat friction as an emergent collective effect of many microscopic contacts, and end with a testable prediction about wet versus dry floors`
- 中文对照：安德森风格，解释地铁里的约克夏犬为什么不会滑倒：从接触的对称性破缺出发，把摩擦看作众多微观接触的涌现集体效应，最后给出干湿地面的可检验预言。
- Negative: `no reducing emergence away to single-particle physics, no model with more fitting parameters than insight, no claiming a new phase without naming the broken symmetry, no presenting localization as a mere disorder correction`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
