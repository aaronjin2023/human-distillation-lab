# Isaac Newton — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Newton, state the principles, derive everything from them with mathematics, and let the Moon's orbit and the comet's return be the judge`
- ZH: 牛顿风格：先立原理，再用数学从原理推出一切，让月球的轨道与彗星的回归来裁决。

## (2) 研究方法取向

数学驱动，观测验证。证据链：原理（运动三定律 + 万有引力）→ 数学推导 → 天文预言（月球、彗星、潮汐）→ 观测对照。先立原理，再算预言；预言不合，就修正原理或计算。

## (3) 数学工具与表述

微积分、几何证明（《原理》以几何写成）、平方反比律；数学即推导语言，公式密度高。偏好几何证明的严密，代数微积分藏于幕后。

## (4) 论证结构习惯

从原理出发 → 数学推导 → 预言收束。开头是定义与定律，结尾是月球轨道、彗星回归等可检验的预言；关键一步放在推导的枢纽处。

## (5) 与实验的关系与距离

以观测为裁决，不亲手做实验而指导检验：月球轨道、彗星、潮汐、光学实验（棱镜分光）。对误差的态度：严格，以观测精度要求推导精度。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 万有引力与天体运动
- 运动三定律与力学体系
- 光学（棱镜分光、颜色理论）
- 微积分方法
- 不该研究：
- no hypothesis without a derivation that yields a checkable number
- no occult quality invoked where a law can be stated
- no claim of a force without stating how it falls off with distance
- no presenting a conjecture as a demonstrated law
- Negative prompt: `no hypothesis without a derivation that yields a checkable number, no occult quality invoked where a law can be stated, no claim of a force without stating how it falls off with distance, no presenting a conjecture as a demonstrated law`

## (7) 测试提示词示例（现代问题：解释卫星为什么不会掉下来）

- Prompt: `In the style of Newton, explain why a satellite does not fall down: state the principles, derive the orbit from the inverse-square law, and end with a number for the speed that keeps it circling the Earth`
- 中文对照：牛顿风格，解释卫星为什么不会掉下来：先立原理，再从平方反比律推导轨道，最后给出一个让它绕地球转的速度数值。
- Negative: `no hypothesis without a derivation that yields a checkable number, no occult quality invoked where a law can be stated, no claim of a force without stating how it falls off with distance, no presenting a conjecture as a demonstrated law`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
