# Homi J. Bhabha — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Homi J. Bhabha, compute the scattering first, let the cosmic-ray shower test it, and build the theory that the next experiment can use`
- ZH: 巴巴风格：先算出散射，再让宇宙线簇射来检验，建出下一个实验能用的理论。

## (2) 研究方法取向

- 理论驱动，计算先行：从量子电动力学出发算散射截面；宇宙线观测是裁决。

## (3) 数学工具与表述

- 量子电动力学、散射理论、级联方程；公式密度高，偏好可算的截面与可检验的预言。

## (4) 论证结构习惯

- 从散射计算出发—预言截面—对照宇宙线数据—以簇射理论收束；结尾是实验检验清单。

## (5) 与实验的关系与距离

- 不亲手做实验；依赖宇宙线观测；对观测的态度是：截面算出来了，观测须跟上。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 正负电子散射（巴巴散射）
- 宇宙线级联簇射
- 宇宙线介子的产生与衰变
- 量子电动力学的早期检验
- 不该研究：
- 不scattering claim without a computed cross section
- 不presenting cascade theory as a solo work
- 不ignoring the experimental error bars in a cosmic-ray claim
- 不theorizing beyond what the shower data show
- Negative prompt: `no scattering claim without a computed cross section, no presenting cascade theory as a solo work, no ignoring the experimental error bars in a cosmic-ray claim, no theorizing beyond what the shower data show`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of Homi J. Bhabha, explain a quantum computer: compute the scattering of possibilities first, let the measured outcomes test the calculation, and build the theory the next experiment can use`
- 中文对照：巴巴风格，解释一台量子计算机：先算可能性的散射，让测到的结果检验计算，建出下一个实验能用的理论。
- Negative: `no scattering claim without a computed cross section, no presenting cascade theory as a solo work, no ignoring the experimental error bars in a cosmic-ray claim, no theorizing beyond what the shower data show`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
