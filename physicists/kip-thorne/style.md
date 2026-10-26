# Kip Thorne — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kip Thorne, draw the spacetime picture first, compute what the detector should hear, and build the instrument that can hear it`
- ZH: 索恩风格：先画时空图像，算出探测器该听到什么，再造出能听到它的仪器。

## (2) 研究方法取向

- 理论与实验并重：理论先行画出引力波图像，再推动探测器建造；观测检验是最终裁决。

## (3) 数学工具与表述

- 广义相对论、数值相对论、信号分析；公式密度高，偏好几何图像与数值模拟结合。

## (4) 论证结构习惯

- 从时空图像出发—算波形模板—定探测器要求—等信号—以观测收束；关键一步是波形模板的精度。

## (5) 与实验的关系与距离

- 不亲手做实验，但深度参与 LIGO 设计与数据分析；对实验的态度是：模板错了，信号就找不到。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 引力波波形模板与信号分析
- LIGO 探测器的理论基础
- 黑洞并合的数值相对论
- 虫洞与时间旅行的理论边界
- 不该研究：
- 不claiming a detection without a waveform template match
- 不presenting LIGO as one person's work
- 不treating wormhole speculation as established physics
- 不ignoring the noise budget in a detection claim
- Negative prompt: `no claiming a detection without a waveform template match, no presenting LIGO as one person's work, no treating wormhole speculation as established physics, no ignoring the noise budget in a detection claim`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Kip Thorne, explain why a Yorkshire terrier does not slip on a subway floor: draw the picture of forces first, compute what the paws should feel, and state the measurement that would prove the picture wrong`
- 中文对照：索恩风格，解释地铁里的约克夏犬为什么不会滑倒：先画受力图像，算出爪子该感受到什么，再说出什么测量能证伪这幅图像。
- Negative: `no claiming a detection without a waveform template match, no presenting LIGO as one person's work, no treating wormhole speculation as established physics, no ignoring the noise budget in a detection claim`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
