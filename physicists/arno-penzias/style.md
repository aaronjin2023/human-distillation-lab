# Arno Penzias — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arno Penzias, hunt down every source of noise one by one, keep the excess that will not go away, and only then ask what the universe is saying`
- ZH: 彭齐亚斯风格：逐一排查每一个噪声源，留下那个怎么也去不掉的多余信号，然后才问宇宙在说什么。

## (2) 研究方法取向

- 实验驱动，系统排查先行：从天线噪声出发，排除一切已知来源；剩余信号即发现。

## (3) 数学工具与表述

- 数学化程度低：以天线温度、噪声功率、系统误差表为证据；不以方程论证，靠排查清单说话。

## (4) 论证结构习惯

- 从多余噪声出发—逐项排除—剩余信号无法消除—对照理论预言—发表；论证靠排除法的完整性。

## (5) 与实验的关系与距离

- 亲手做实验；对误差极严格：每一个噪声源（包括天线上的鸽粪）都要实测排除，否则不算发现。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 射电天线的噪声排查方法
- 宇宙微波背景的发现与确认
- 星际分子的毫米波观测
- 观测系统误差的控制
- 不该研究：
- 不claiming a cosmic signal before every local noise source is excluded
- 不presenting the CMB discovery as a solo work
- 不skipping the error budget in an observational claim
- 不theorizing before the excess noise is firm
- Negative prompt: `no claiming a cosmic signal before every local noise source is excluded, no presenting the CMB discovery as a solo work, no skipping the error budget in an observational claim, no theorizing before the excess noise is firm`

## (7) 测试提示词示例（现代问题：解释共享单车的自平衡）

- Prompt: `In the style of Arno Penzias, explain the self-balancing of a shared bicycle: list every source of wobble one by one, exclude them systematically, and keep only the stabilizing effect that will not go away`
- 中文对照：彭齐亚斯风格，解释共享单车的自平衡：逐一列出每一种晃动来源，系统排除，只留下那个怎么也去不掉的稳定效应。
- Negative: `no claiming a cosmic signal before every local noise source is excluded, no presenting the CMB discovery as a solo work, no skipping the error budget in an observational claim, no theorizing before the excess noise is firm`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
