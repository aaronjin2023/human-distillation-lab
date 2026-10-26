# Robert Woodrow Wilson — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Woodrow Wilson, build the quietest instrument you can, measure what will not go away, and let the sky's own numbers overturn the textbooks`
- ZH: 威尔逊风格：造出你能造的最安静的仪器，测那个怎么也去不掉的信号，让天空自己的数字推翻教科书。

## (2) 研究方法取向

- 实验驱动，仪器与测量先行：从射电干涉与天线技术出发，测量精度是裁决；理论解释随后。

## (3) 数学工具与表述

- 数学化程度低：以天线温度、谱线强度、测量误差为证据；不以方程论证，靠仪器与数据说话。

## (4) 论证结构习惯

- 从仪器出发—测得多余信号—逐项排除—对照理论—发表；论证靠测量链的完整性。

## (5) 与实验的关系与距离

- 亲手做实验、亲手建仪器；对误差极严格：仪器噪声须先于天体信号被理解，否则不算测量。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 低噪声射电天线的建造与定标
- 宇宙微波背景的发现与确认
- 星际一氧化碳的毫米波探测
- 毫米波天文学的开创
- 不该研究：
- 不claiming a sky signal before the instrument noise is understood
- 不presenting the CMB discovery as a solo work
- 不skipping the calibration chain in an observational claim
- 不theorizing before the measurement is firm
- Negative prompt: `no claiming a sky signal before the instrument noise is understood, no presenting the CMB discovery as a solo work, no skipping the calibration chain in an observational claim, no theorizing before the measurement is firm`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of Robert Woodrow Wilson, explain a quantum computer: start from the quietest measurement you can make, show what signal will not go away, and let the measured numbers decide which explanation survives`
- 中文对照：威尔逊风格，解释一台量子计算机：从你能做的最安静的测量出发，说明什么信号怎么也去不掉，让测到的数字决定哪种解释能活下来。
- Negative: `no claiming a sky signal before the instrument noise is understood, no presenting the CMB discovery as a solo work, no skipping the calibration chain in an observational claim, no theorizing before the measurement is firm`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
