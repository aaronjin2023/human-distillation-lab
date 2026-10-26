# James Clark Ross — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Clark Ross: work along an ice shelf, fix magnetic variation at many points, chart the shelf edge segment by segment, no claim from a single fix`
- ZH: 詹姆斯·克拉克·罗斯风格：磁测多点观测、沿冰架航行，硬闯冰架、无磁测的断言。

## (2) 导航方法

- 南极沿岸测绘：以天文钟定经度、六分仪测纬度；沿冰架边缘航行，测深辨水道；磁测仪测南磁极位置，误差靠多点观测修正。 `impression`

## (3) 造船与帆装

- 埃里伯斯号与恐怖号：英国海军南极探险船，船体加固抗冰；配磁测仪与天文钟；补给靠霍巴特据点。 `impression`

## (4) 航线规划习惯

- 南极远征：1839年离英国，南下至罗斯海，沿罗斯冰架东行，登陆维多利亚地；1841年抵南磁极附近，返程经霍巴特。 `impression`

## (5) 日志与海图语言

- 日志体例为海军远征报告：日期—纬度—经度—风向—冰况—磁偏；返航后出版《南极远征记》（1847年），附海图与磁测表。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：沿冰架边缘的航行、南磁极的多点磁测、罗斯海的逐段成图。
- 不该探索：硬闯冰架、无磁测的断言。
- Negative prompt: `No claim about the pole from a single fix, no forcing through pack ice, no sailing without a magnetic fix, no modern GPS as the only fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of James Clark Ross, an uncrewed survey ship works along an ice shelf in 2026, fixing magnetic variation at many points, charting the shelf edge segment by segment. No claim about the pole from a single fix.`
- 中文对照：罗斯风格：一艘无人测量船2026年沿冰架边缘航行，多点测磁偏，海图逐段成图。不凭单点定位断言磁极。
- Negative: `No claim about the pole from a single fix, no forcing through pack ice, no sailing without a magnetic fix, no modern GPS as the only fix`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
