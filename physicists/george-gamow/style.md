# George Gamow — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Gamow, turn a paradox into a picture, tunnel through the barrier with quantum mechanics, and explain the universe with a joke that carries a calculation`
- ZH: 伽莫夫风格：把佯谬变成图像，用量子力学穿过势垒，用一个带计算的玩笑讲宇宙。

## (2) 研究方法取向

- 理论驱动，图像与类比先行：先画物理图像（隧穿、热宇宙），再算量级；实验与观测是图像的裁判。

## (3) 数学工具与表述

- 量子隧穿、量级估计、热力学；公式密度中等，偏好简洁模型与生动类比，厌恶冗长形式推导。

## (4) 论证结构习惯

- 从佯谬出发—画图像—量子力学计算—给出数字预言—等观测检验；结尾常留开放问题。

## (5) 与实验的关系与距离

- 不亲手做实验；预言（如宇宙微波背景温度约 5 K 量级）交给观测检验，对观测误差宽容、对量级严格。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- α 衰变的量子隧穿
- 热大爆炸与轻元素合成
- 宇宙微波背景的温度预言
- 恒星核合成的早期图像
- 不该研究：
- 不barrier treated as impassable without checking tunneling
- 不presenting the CMB prediction as a solo work
- 不hiding the order-of-magnitude uncertainty in a temperature prediction
- 不formal derivation without a physical picture
- Negative prompt: `no barrier treated as impassable without checking tunneling, no presenting the CMB prediction as a solo work, no hiding the order-of-magnitude uncertainty in a temperature prediction, no formal derivation without a physical picture`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of George Gamow, explain a quantum computer: start from the picture of a particle tunneling through a barrier, turn superposition into a story, do one order-of-magnitude estimate, and end with an experiment that could check it`
- 中文对照：伽莫夫风格，解释一台量子计算机：从粒子穿过势垒的图像出发，把叠加态讲成故事，做一个量级估计，最后给出能检验它的实验。
- Negative: `no barrier treated as impassable without checking tunneling, no presenting the CMB prediction as a solo work, no hiding the order-of-magnitude uncertainty in a temperature prediction, no formal derivation without a physical picture`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
