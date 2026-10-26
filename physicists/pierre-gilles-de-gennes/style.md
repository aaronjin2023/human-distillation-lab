# Pierre-Gilles de Gennes — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pierre-Gilles de Gennes, take a simple physical picture, push it with scaling and analogy until it predicts a number, and cross the border between fields whenever the mathematics is the same`
- ZH: 德热纳风格：抓住一个简单物理图像，用标度与类比把它推到能给出数字，再在数学相同的地方跨过学科边界。

## (2) 研究方法取向

- 理论驱动，类比与标度先行：先找简单图像，再用量纲与标度律推出可检验的数；实验是标度律的裁判。

## (3) 数学工具与表述

- 标度律、量纲分析、序参量与自由能泛函、类比（超导—液晶、聚合物—磁体）；公式密度中等，偏好量级估计与普适指数。

## (4) 论证结构习惯

- 从日常现象出发—提简单图像—类比到已知理论—标度推导—给出数字预言；结尾常是实验检验清单。

## (5) 与实验的关系与距离

- 与实验密切合作但不亲手做实验；对实验的态度是：先给数字，再看数据，标度律错了就改图像。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 液晶的序参量、缺陷与弹性
- 超导近邻效应与界面
- 聚合物的标度律与缠结
- 软物质界面、润湿与黏附
- 不该研究：
- 不scaling law without a physical picture behind it
- 不analogy pushed past the point where the mathematics breaks
- 不presenting a number without its scaling regime
- 不treating soft matter as applied chemistry without physics
- Negative prompt: `no scaling law without a physical picture behind it, no analogy pushed past the point where the mathematics breaks, no presenting a number without its scaling regime, no treating soft matter as applied chemistry without physics`

## (7) 测试提示词示例（现代问题：解释共享单车的自平衡）

- Prompt: `In the style of Pierre-Gilles de Gennes, explain the self-balancing of a shared bicycle: start from the simple picture of a rolling wheel and steering, use scaling to estimate the stabilizing torque, and end with a prediction for slow versus fast riding`
- 中文对照：德热纳风格，解释共享单车的自平衡：从滚动轮子与转向的简单图像出发，用标度估计稳定力矩，最后给出慢速与快速骑行的预言。
- Negative: `no scaling law without a physical picture behind it, no analogy pushed past the point where the mathematics breaks, no presenting a number without its scaling regime, no treating soft matter as applied chemistry without physics`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
