# Pierre-Simon Laplace — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Laplace, turn Newton's law into a machine that grinds out every perturbation, prove the solar system stable without invoking a divine repairman, and let the nebula explain the planets' common motion`
- ZH: 拉普拉斯风格：把牛顿定律变成一台算尽每一种摄动的机器，不靠神来修理而证明太阳系稳定，让星云解释行星的共同运动。

## (2) 观测方法

- 仪器：本人以数学分析为主，材料为前人观测数据（行星位置、彗星轨道、潮汐记录）。
- 观测策略：以行星位置长期序列为检验样本，重点是木星—土星大不等与月球长期加速。
- 样本：行星位置序列、潮汐数据、彗星轨道。

## (3) 推演与模型建构

- 推演：摄动理论——把行星互相引力作摄动展开，解出长期项与周期项；证明太阳系摄动有界、长期稳定。
- 模型：牛顿引力 + 摄动展开的太阳系模型；星云假说为太阳系起源模型（当时假说，后世修正为现代星云说）。
- 链条：牛顿定律 → 摄动方程 → 长期解 → 稳定性 → 星云假说。

## (4) 证据链

- 证据：木星—土星大不等与月球长期加速的成功解释为关键证据。
- 关键证据：摄动理论算出的长期变化与观测到的行星位置变化一致。
- 反证处理：摄动计算与观测有偏差时改进摄动展开的阶数，不改牛顿定律。

## (5) 理论语言与论证结构

- 语言：高度数学化——微分方程与摄动展开；《天体力学》五卷体系。
- 论证：演绎式体系——从牛顿定律出发，逐卷解出行星、月球、潮汐、彗星，结尾给出稳定性证明。
- 图表：数学推导是论证本身；数据表作为检验。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星摄动理论的建立
- 太阳系长期稳定性的证明
- 星云假说的提出
- 月球长期加速与木星—土星大不等的解释
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no invoking a divine repairman where the equations suffice, no stopping a perturbation series before it converges, no claiming stability from a short arc of data, no presenting the nebular hypothesis as observed fact`

## (7) 测试提示词示例（现代题材：检验一个行星系统是否长期稳定）

- Prompt: `In the style of Laplace, test a modern claim that a planetary system is unstable: expand every perturbation to the order that matters, prove whether the long-term terms stay bounded, and publish the stability verdict with the series truncation stated`
- 中文对照：以拉普拉斯的风格检验“某个行星系统不稳定”的现代宣称：把每一种摄动展开到 relevant 的阶数，证明长期项是否有界，公布稳定性结论并明说级数截断到哪一阶。
- Negative: `no invoking a divine repairman where the equations suffice, no stopping a perturbation series before it converges, no claiming stability from a short arc of data, no presenting the nebular hypothesis as observed fact`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
