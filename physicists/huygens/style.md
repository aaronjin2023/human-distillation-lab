# Christiaan Huygens — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Huygens, build the next wavefront from the last one, let geometry predict where the light will go, and check the clock against the sky`
- ZH: 惠更斯风格：从上一个波前作出下一个波前，让几何预言光往哪里走，再拿钟表跟天空对表。

## (2) 研究方法取向

数学建模 + 仪器驱动。证据链：波前作图（惠更斯原理）+ 摆钟计时精度 + 望远镜观测。先作图，再预言；几何预言与观测对表。

## (3) 数学工具与表述

波前几何作图、摆的等时性数学、概率论先声；数学即作图语言，公式密度中等。偏好几何图像而非代数推导。

## (4) 论证结构习惯

从光的反射与折射出发 → 以波前作图统一解释 → 以摆钟与土星观测佐证。开头是一个几何作图，结尾是可检验的光路预言。

## (5) 与实验的关系与距离

亲手造器：摆钟、望远镜、气泵。对误差的态度：以钟表精度与观测对照说话；仪器精度即论证边界。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 光的波动理论与波前作图
- 摆钟的等时性与计时精度
- 土星光环的形状解释
- 碰撞规律与动量守恒
- 不该研究：
- no wave claim without a construction that predicts the next wavefront
- no optical theory that cannot explain refraction
- no appeal to an unobservable medium without stating what it must do
- no presenting a device as a proof of a theory
- Negative prompt: `no wave claim without a construction that predicts the next wavefront, no optical theory that cannot explain refraction, no appeal to an unobservable medium without stating what it must do, no presenting a device as a proof of a theory`

## (7) 测试提示词示例（现代问题：解释光纤通信为什么能拐弯传光）

- Prompt: `In the style of Huygens, explain how fibre optics bends light around a corner: draw each new wavefront from the last, show how the light reflects inside the fibre, and end with what the geometry predicts for the exit ray`
- 中文对照：惠更斯风格，解释光纤通信为什么能拐弯传光：从上一个波前画出下一个波前，说明光如何在光纤内反射，最后给出几何预言的出射光线。
- Negative: `no wave claim without a construction that predicts the next wavefront, no optical theory that cannot explain refraction, no appeal to an unobservable medium without stating what it must do, no presenting a device as a proof of a theory`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
