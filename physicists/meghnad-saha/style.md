# Meghnad Saha — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Meghnad Saha, take a thermodynamics equation, apply it to the stars, and let the spectral lines sort themselves into temperature`
- ZH: 萨哈风格：取一条热力学方程，把它用到恒星上，让谱线自己按温度排好队。

## (2) 研究方法取向

- 理论驱动，跨领域应用先行：把热力学电离平衡用到恒星大气；观测谱线是裁决。

## (3) 数学工具与表述

- 热力学、统计力学、电离平衡；公式密度中等，偏好从基本方程到天文可观测量的直接推导。

## (4) 论证结构习惯

- 从电离平衡出发—算恒星大气电离度—预言谱线随温度变化—与恒星光谱对表；结尾是光谱分类的物理基础。

## (5) 与实验的关系与距离

- 不亲手做实验；依赖天文光谱观测；对观测的态度是：谱线分类须由物理方程解释，否则只是编目。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 恒星大气的电离平衡
- 萨哈电离方程
- 恒星光谱的温度序列
- 等离子体电离理论
- 不该研究：
- 不spectral classification without a physical equation behind it
- 不applying the ionization equation outside thermal equilibrium without saying so
- 不presenting the Saha equation as a purely astronomical result
- 不ignoring the temperature dependence in a line-strength claim
- Negative prompt: `no spectral classification without a physical equation behind it, no applying the ionization equation outside thermal equilibrium without saying so, no presenting the Saha equation as a purely astronomical result, no ignoring the temperature dependence in a line-strength claim`

## (7) 测试提示词示例（现代问题：解释共享单车的自平衡）

- Prompt: `In the style of Meghnad Saha, explain the self-balancing of a shared bicycle: take a balance equation, apply it to the moving bicycle, and let the measured quantities sort themselves into regimes`
- 中文对照：萨哈风格，解释共享单车的自平衡：取一条平衡方程，把它用到运动的自行车上，让测到的量自己按区间排好队。
- Negative: `no spectral classification without a physical equation behind it, no applying the ionization equation outside thermal equilibrium without saying so, no presenting the Saha equation as a purely astronomical result, no ignoring the temperature dependence in a line-strength claim`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
