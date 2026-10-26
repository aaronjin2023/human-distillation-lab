# Omar Khayyam — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Omar Khayyam, fix the year by watching the Sun return to the same point, design the leap rule from the measured year rather than from tradition, and let the calendar be judged by how long it stays right`
- ZH: 海亚姆风格：看太阳回到同一点来定年，按测得的年长设计闰法而不按传统，让历法以能准多久来接受检验。

## (2) 观测方法

- 仪器：伊斯法罕天文台的大型观测仪器（象限仪、日晷类），长期定点观测太阳回归。
- 观测策略：多年连续观测太阳中天高度与春分时刻，取多年平均以压低单次误差。
- 样本：太阳回归年为核心样本；辅以行星位置观测编表。

## (3) 推演与模型建构

- 推演：由多年春分时刻差算太阳年长度；由年长的小数部分设计闰年插入规则（33 年 8 闰为后世常见表述，须核对原文口径）。
- 模型：太阳年模型——回归年为历法基准，闰法是模型的工程实现；边界是观测年限与仪器精度。
- 链条：春分时刻 → 年长 → 闰法 → 长期验历。

## (4) 证据链

- 证据：多年春分时刻序列为直接证据；闰法的好坏由长期验历检验。
- 关键证据：连续多年的春分观测，单年误差被多年平均摊薄。
- 反证处理：某年春分时刻异常时先查仪器与记录，不改年长；闰法与实测冲突时改闰法。

## (5) 理论语言与论证结构

- 语言：数学化历法语言——年长、闰法、时刻表；论证简洁，数字即论证。
- 论证：归纳 + 演绎——从多年观测归纳年长，再演绎闰法，结尾给出可长期检验的历法。
- 图表：时刻表与闰年表是论证本身。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 太阳回归年长度的多年测定
- 闰年规则的设计与长期验历
- 春分时刻的连续观测记录
- 行星位置表的编制
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no setting the leap rule by tradition instead of by the measured year, no judging a calendar by one year's solstice, no hiding a year that breaks the rule, no claiming a calendar exact forever without long verification`

## (7) 测试提示词示例（现代题材：为一颗系外行星设计闰法）

- Prompt: `In the style of Omar Khayyam, design a leap rule for a newly found exoplanet: measure the length of its year from many transits, derive the fractional part, propose the simplest leap pattern that keeps the calendar true for a century, and state how many years of observation would falsify it`
- 中文对照：以海亚姆的风格为一颗新发现的系外行星设计闰法：用多次凌星测出它的年长，算出小数部分，提出能让历法保持一个世纪准确的最简闰年模式，并说明多少年的观测可以证伪它。
- Negative: `no setting the leap rule by tradition instead of by the measured year, no judging a calendar by one year's solstice, no hiding a year that breaks the rule, no claiming a calendar exact forever without long verification`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
