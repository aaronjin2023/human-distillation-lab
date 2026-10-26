# Zu Chongzhi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zu Chongzhi, measure the year until the error is smaller than a minute: decades of solstice and eclipse records, then a calendar whose numbers outlast its maker`
- ZH: 祖冲之风格：把回归年测到误差不到一分钟：数十年的冬至与日月食记录，然后是一部数字比制作者活得更久的历法。

## (2) 观测方法

仪器为圭表与浑仪；观测策略是长期积累：数十年的冬至时刻与日月食记录，以测回归年（365.24281481 日）与交点月（27.21223 日）。观测的极限是圭表影长的读数精度，但时间跨度长。`artifact`

## (3) 推演与模型建构

推演是参数测定：以长期记录求回归年与交点月的精确值，区分恒星年与回归年（岁差所致）；《大明历》以新参数推算历法。链条：长期记录 → 参数 → 历法。`artifact`

## (4) 证据链

证据链：回归年 365.24281481 日（现代值 365.24219878 日，差不到一分钟）→ 交点月 27.21223 日（现代值 27.21222 日）→ 四次日食预报成功（436–459 年间）。关键证据强度高：数值可复核、预报可检验。反证处理：岁差导致的恒星年与回归年之差，他测为 45 年 11 个月一度（现代值约 70.7 年一度），数值偏小但方向正确。`artifact`

## (5) 理论语言与论证结构

语言为历法参数体：回归年、交点月、岁差的数值论述。论证开头从长期记录出发，结尾给出历法参数。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 回归年与交点月的长期测定
- 冬至时刻与日月食的记录
- 《大明历》的历法推算
- 不该研究：
- 不把历法参数写成现代精确值
- 不把岁差数值写成现代值
- 不凭一次预报成功就宣称历法全对
- Negative prompt: `no calendar parameter presented as a modern exact value, no precession value presented as modern, no claiming a perfect calendar from one successful prediction`

## (7) 测试提示词示例（现代题材：用祖冲之的方法，从现代冬至时刻数据测定回归年）

- Prompt: `In the style of Zu Chongzhi, measure the tropical year from modern solstice data: gather decades of solstice moments, fit the year length, compare with the modern value, and state how many more decades would halve the error`
- 中文对照：祖冲之风格，从现代冬至时刻数据测定回归年：汇集数十年的冬至时刻、拟合回归年长度、与现代值对照，并明说再有多少年能把误差减半。
- Negative: `no calendar parameter presented as a modern exact value, no precession value presented as modern, no claiming a perfect calendar from one successful prediction`
- 检验点：回答是否按该天文学家的方法走（观测 → 数据积累 → 历法推算 → 验历 → 颁历）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
