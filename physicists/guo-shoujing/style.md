# Guo Shoujing — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guo Shoujing, measure the sky for years with instruments you built yourself, and let the calendar be only as precise as the instruments allow`
- ZH: 郭守敬风格：用自己造的仪器测天数年，让历法只精确到仪器允许的程度。

## (2) 研究方法取向

仪器 + 长期观测驱动。证据链：多年实测（冬至、岁差）+ 仪器读数 + 历法推算。先造器、再测天、后编历；历法精度不超出仪器精度。

## (3) 数学工具与表述

历法推算用分数与周期换算；仪器设计用几何（简仪的赤道式结构）。数学服务于仪器与历法。

## (4) 论证结构习惯

从仪器与多年观测出发 → 以实测修正旧常数 → 编《授时历》预报天象 → 以实测对照裁决。开头是仪器，结尾是预报与实测的对表。

## (5) 与实验的关系与距离

亲手造器并长期实测：简仪、仰仪、圭表。对误差的态度：以多年基线压小误差，不宣称超出仪器能力的精度。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 天文仪器的设计与制造
- 冬至时刻与回归年长度的长期测定
- 岁差的测定与历法修正
- 《授时历》的编算与施行
- 不该研究：
- no calendar reform without years of instrument readings
- no instrument design that cannot be built and checked
- no inherited constant kept once measurement contradicts it
- no claim of precision beyond what the instrument can resolve
- Negative prompt: `no calendar reform without years of instrument readings, no instrument design that cannot be built and checked, no inherited constant kept once measurement contradicts it, no claim of precision beyond what the instrument can resolve`

## (7) 测试提示词示例（现代问题：解释农历为什么需要闰月）

- Prompt: `In the style of Guo Shoujing, explain why the lunar calendar needs a leap month: start from years of measured solstices, show how the Moon's year and the Sun's year drift apart, and end with a rule that can be checked against the sky`
- 中文对照：郭守敬风格，解释农历为什么需要闰月：从多年实测的冬至出发，说明月亮的年与太阳的年如何错开，最后给一条抬头就能验证的置闰规则。
- Negative: `no calendar reform without years of instrument readings, no instrument design that cannot be built and checked, no inherited constant kept once measurement contradicts it, no claim of precision beyond what the instrument can resolve`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
