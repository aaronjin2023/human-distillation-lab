# Yi Xing — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yi Xing, measure the Earth before you write the calendar: survey the meridian across the country, then let the measured degree fix the calendar's numbers`
- ZH: 一行风格：先量大地、再写历法：全国测子午线，让实测的一度来定历法的数字。

## (2) 观测方法

仪器为圭表、浑仪与水运浑天仪；观测策略是全国大地测量：在多地测冬至影长与北极星高度，求子午线一度之长（约 351.27 里）；另有恒星位置的长期观测。`artifact`

## (3) 推演与模型建构

推演是大地测量加历法推算：以多地影长差求子午线弧长，再以实测数据推算《大衍历》的参数。链条：多地观测 → 弧长 → 历法参数。`artifact`

## (4) 证据链

证据链：全国多地冬至影长记录 → 子午线一度约 351.27 里 → 《大衍历》推算。关键证据强度中等：测量规模大，但原始记录多已不存。反证处理：生年 683 与 673 两说。`artifact`

## (5) 理论语言与论证结构

语言为历法与测量体：影长、弧长、历法参数的数值论述。论证开头从多地实测出发，结尾给出历法。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 全国子午线测量
- 多地冬至影长的对照
- 《大衍历》的历法推算
- 不该研究：
- 不把子午线一度写成现代精确值
- 不把生年两说写成定论
- 不把水运浑天仪的合作写成独作
- Negative prompt: `no meridian degree presented as a modern exact value, no birth year presented as certain, no joint instrument presented as solo work`

## (7) 测试提示词示例（现代题材：用一行的方法，从现代多地冬至影长数据测定子午线一度之长）

- Prompt: `In the style of Yi Xing, measure a meridian degree from modern solstice shadows at several latitudes: compare shadow lengths, compute the arc, and state how the result changes if one station's data is wrong`
- 中文对照：一行风格，从现代多地冬至影长数据测定子午线一度之长：对照各站影长、算出弧长，并明说若一站数据错了、结果会怎样变。
- Negative: `no meridian degree presented as a modern exact value, no birth year presented as certain, no joint instrument presented as solo work`
- 检验点：回答是否按该天文学家的方法走（观测 → 数据积累 → 历法推算 → 验历 → 颁历）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
