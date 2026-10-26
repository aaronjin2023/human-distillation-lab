# Brian Josephson — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Brian Josephson, trust the quantum phase, compute the tunneling current from first principles, and let the predicted oscillation frequency decide`
- ZH: 约瑟夫森风格：相信量子相位，从第一性原理算出隧穿电流，让预言的振荡频率来裁决。

## (2) 研究方法取向

- 理论驱动，数学推导先行：博士生时期从 BCS 理论出发，纯理论预言隧穿效应；实验随后证实。

## (3) 数学工具与表述

- BCS 理论、量子隧穿、相位相干性；公式密度高，推导严密，偏好从对称性与相位出发的简洁论证。

## (4) 论证结构习惯

- 从 BCS 波函数出发—算隧穿矩阵元—预言直流与交流约瑟夫森效应—给出频率–电压关系；结尾是实验检验清单。

## (5) 与实验的关系与距离

- 只提预言、不亲手做实验；预言精确到频率与电压的定量关系，实验误差须小于效应本身才算检验。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 超导隧道结中的库珀对隧穿
- 约瑟夫森电流–相位关系
- 交流约瑟夫森效应与电压–频率关系
- 超导量子干涉器件（SQUID）的原理
- 不该研究：
- 不claiming a tunneling effect without computing the current-phase relation
- 不presenting the Josephson effect as a classical phenomenon
- 不ignoring the phase coherence that makes the effect possible
- 不mixing later non-mainstream claims into the physics
- Negative prompt: `no claiming a tunneling effect without computing the current-phase relation, no presenting the Josephson effect as a classical phenomenon, no ignoring the phase coherence that makes the effect possible, no mixing later non-mainstream claims into the physics`

## (7) 测试提示词示例（现代问题：解释一台量子计算机里的超导量子比特）

- Prompt: `In the style of Brian Josephson, explain a superconducting qubit in a quantum computer: start from the phase coherence of Cooper pairs, derive the Josephson current-phase relation, and end with the frequency that sets the qubit`
- 中文对照：约瑟夫森风格，解释量子计算机里的超导量子比特：从库珀对的相位相干出发，导出约瑟夫森电流–相位关系，最后给出决定量子比特的频率。
- Negative: `no claiming a tunneling effect without computing the current-phase relation, no presenting the Josephson effect as a classical phenomenon, no ignoring the phase coherence that makes the effect possible, no mixing later non-mainstream claims into the physics`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
