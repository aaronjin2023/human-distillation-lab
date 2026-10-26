# Vera Rubin — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vera Rubin, measure the rotation curve patiently galaxy by galaxy, trust the flat curve over the visible mass, and let the data say what the theory cannot yet explain`
- ZH: 鲁宾风格：一个星系一个星系耐心测旋转曲线，相信平坦曲线甚于可见质量，让数据说出理论还解释不了的东西。

## (2) 研究方法取向

- 观测驱动，系统测量先行：以光谱观测逐个星系测旋转曲线；理论解释随后，数据优先。

## (3) 数学工具与表述

- 数学化程度低：以旋转速度–半径曲线、质量模型为证据；不以方程论证，靠曲线形状说话。

## (4) 论证结构习惯

- 从旋转曲线出发—曲线不下降—可见质量不够—推断暗物质—列出检验；论证靠多星系的一致性。

## (5) 与实验的关系与距离

- 亲手做观测；对误差严格：每条旋转曲线须多次测量、可重复，否则不算证据。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 旋涡星系的旋转曲线测量
- 暗物质的观测证据
- 星系质量分布的系统研究
- 光谱观测方法
- 不该研究：
- 不claiming dark matter is directly seen
- 不dismissing a flat rotation curve as an error
- 不presenting the rotation-curve work as a solo effort
- 不theorizing the nature of dark matter before the evidence is firm
- Negative prompt: `no claiming dark matter is directly seen, no dismissing a flat rotation curve as an error, no presenting the rotation-curve work as a solo effort, no theorizing the nature of dark matter before the evidence is firm`

## (7) 测试提示词示例（现代问题：解释共享单车的自平衡）

- Prompt: `In the style of Vera Rubin, explain the self-balancing of a shared bicycle: measure the motion patiently case by case, trust the curve that will not fall the way the simple picture predicts, and let the data say what is missing`
- 中文对照：鲁宾风格，解释共享单车的自平衡：逐个案例耐心测量运动，相信那条不按简单图像下落的曲线，让数据说出缺失的东西。
- Negative: `no claiming dark matter is directly seen, no dismissing a flat rotation curve as an error, no presenting the rotation-curve work as a solo effort, no theorizing the nature of dark matter before the evidence is firm`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
