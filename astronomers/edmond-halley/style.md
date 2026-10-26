# Edmond Halley — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edmond Halley, collect every apparition of the same comet across two centuries, fit one orbit to all of them, and publish the year it will return so the sky can prove you right or wrong`
- ZH: 哈雷风格：收集同一颗彗星两个世纪的每一次出现，用一条轨道拟合全部记录，公布它回归的年份，让天空来证明你对错。

## (2) 观测方法

- 仪器：望远镜观测 + 历史记录整理；圣赫勒拿岛南天观测用望远镜与象限仪。
- 观测策略：历史比较法——把 1531、1607、1682 年三次彗星记录当作同一天体的三次观测。
- 样本：三次彗星 apparition 的轨道要素；341 颗南天恒星；恒星位置与古希腊星表比对。

## (3) 推演与模型建构

- 推演：轨道拟合——三次彗星的轨道要素（周期约 76 年）高度一致，推断为同一颗彗星；摄动修正后预报 1758 年底回归。
- 模型：牛顿引力框架下的椭圆轨道模型；模型假设是彗星受行星摄动，边界是摄动计算精度。
- 链条：历史记录 → 轨道要素比对 → 同一彗星推断 → 摄动修正 → 回归预报。

## (4) 证据链

- 证据：三次 apparition 的轨道要素一致性为核心证据；预报 1758 年回归被观测证实（哈雷已去世，预报应验）。
- 关键证据：1531、1607、1682 年三次轨道的相似程度远超巧合。
- 反证处理：预报年份给出范围而非单一年份（1758 年底，摄动不确定性所致）；恒星自行发现亦来自与古星表的比对差异。

## (5) 理论语言与论证结构

- 语言：历史比较 + 轨道计算；论证以表格与轨道要素为主。
- 论证：归纳 + 演绎——从三次记录归纳同一彗星，再演绎回归年份，结尾给出可检验的预报。
- 图表：轨道要素表与星表是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 彗星历史记录的轨道拟合
- 彗星回归年份的预报
- 南天恒星星表的编制
- 恒星自行的发现与论证
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no calling two comets one without matching their orbits, no publishing a return year without stating its uncertainty, no hiding a perturbing planet from the calculation, no claiming a catalogue complete after one season`

## (7) 测试提示词示例（现代题材：检验两次彗星出现是否为同一颗天体）

- Prompt: `In the style of Edmond Halley, test a modern claim that two distant comet apparitions are the same object: fit one orbit to both, compare every orbital element, correct for planetary perturbations, and publish the next return date with its uncertainty range`
- 中文对照：以哈雷的风格检验“两次遥远的彗星出现是同一颗天体”的现代宣称：用一条轨道拟合两者，比较每一项轨道要素，修正行星摄动，公布下一次回归日期及其不确定度范围。
- Negative: `no calling two comets one without matching their orbits, no publishing a return year without stating its uncertainty, no hiding a perturbing planet from the calculation, no claiming a catalogue complete after one season`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
