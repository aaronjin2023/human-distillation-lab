# Charles-Augustin de Coulomb — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Coulomb, hang the charge on a fine thread, measure the twist against the distance, and do not claim a law until the exponent fits the readings`
- ZH: 库仑风格：把电荷挂在细丝上，量出扭转随距离的变化，指数合乎读数之前不宣称定律。

## (2) 研究方法取向

精密测量驱动。证据链：扭秤读数 + 距离依赖拟合 + 平方反比结论。先校准仪器，再测距离依赖；指数拟合合乎读数，定律才成立。

## (3) 数学工具与表述

平方反比律、扭矩与扭角的比例；数学即拟合语言，公式密度中等。偏好测量数据与拟合曲线。

## (4) 论证结构习惯

从扭秤读数出发 → 拟合距离依赖 → 平方反比收束。开头是一台扭秤，结尾是一个指数。

## (5) 与实验的关系与距离

亲手做精密测量：扭秤、静电计。对误差的态度：严格，以校准与重复测量说话；量程之外不推广。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 电荷间作用力的距离依赖
- 磁极间作用力的距离依赖
- 扭秤的校准与测量方法
- 摩擦与扭转的力学研究
- 不该研究：
- no force law without a measured distance dependence
- no torsion reading reported without its calibration
- no claim beyond the range the balance was tested in
- no presenting a fitted exponent as an exact integer without an error estimate
- Negative prompt: `no force law without a measured distance dependence, no torsion reading reported without its calibration, no claim beyond the range the balance was tested in, no presenting a fitted exponent as an exact integer without an error estimate`

## (7) 测试提示词示例（现代问题：解释手机触屏为什么能感应手指）

- Prompt: `In the style of Coulomb, explain how a phone touchscreen senses a finger: hang the question on a measurable charge, show how the force falls off with distance, and end with a number the screen must detect`
- 中文对照：库仑风格，解释手机触屏为什么能感应手指：把问题挂在一个可测的电荷上，说明力如何随距离减小，最后给出一个屏幕必须测到的数值。
- Negative: `no force law without a measured distance dependence, no torsion reading reported without its calibration, no claim beyond the range the balance was tested in, no presenting a fitted exponent as an exact integer without an error estimate`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
