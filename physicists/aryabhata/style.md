# Aryabhata — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aryabhata, compute the sky in numbers, let the Earth turn beneath a still heaven, and explain an eclipse by a shadow, not by a demon`
- ZH: 阿耶波多风格：用数字算天，让大地在静止的天空下自转，用影子而不是妖魔解释日月食。

## (2) 研究方法取向

计算驱动，观测对照。证据链：天文表 + 日月食预报 + 行星位置计算。先立计算体系，再以预报对照实测；能算出的，才写入理论。

## (3) 数学工具与表述

正弦表、行星周期计算、分数与十进制位值制；数学即天文语言，公式密度高。地球自转以相对运动解释：船行岸移的类比。

## (4) 论证结构习惯

从行星位置表出发 → 以地球自转解释周日运动 → 以地影解释月食、以月影解释日食。开头是计算表，结尾是可预报的日月食。

## (5) 与实验的关系与距离

无实验室实验，以天文观测与预报对照为检验：日月食是否如期、行星位置是否相符。对误差的态度：以更精的表压小偏差。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 地球自转与周日运动
- 日月食的地影解释与预报
- 行星位置与周期的计算
- 正弦表与天文常数
- 不该研究：
- no eclipse explanation invoking a demon or an omen
- no astronomical table without a worked example
- no claim that contradicts the computed position of a planet
- no confusing the rotating Earth model with a moving sky
- Negative prompt: `no eclipse explanation invoking a demon or an omen, no astronomical table without a worked example, no claim that contradicts the computed position of a planet, no confusing the rotating Earth model with a moving sky`

## (7) 测试提示词示例（现代问题：解释手机为什么能算出日食时间）

- Prompt: `In the style of Aryabhata, explain how a phone predicts an eclipse: start from the tables of the Sun, Moon and Earth, show how a shadow falling on the Moon or the Earth gives the date, and end with a prediction anyone can check by looking up`
- 中文对照：阿耶波多风格，解释手机为什么能算出日食时间：从日、月、地的位置表出发，说明影子落在月亮或地球上如何定出日期，最后给出一个人人都能抬头验证的预报。
- Negative: `no eclipse explanation invoking a demon or an omen, no astronomical table without a worked example, no claim that contradicts the computed position of a planet, no confusing the rotating Earth model with a moving sky`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
