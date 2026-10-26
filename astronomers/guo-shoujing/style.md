# Guo Shoujing — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guo Shoujing, survey the whole country before you fix the year: twenty-seven stations, a tall gnomon, a simplified armillary sphere — then a calendar accurate to a day in three centuries`
- ZH: 郭守敬风格：先全国测量、再定回归年：27 处测站、高表、简仪，然后是一部三百年才差一天的历法。

## (2) 观测方法

仪器为简仪、高表与浑仪；观测策略是全国测验：在 27 处测站测冬至影长与北极星高度，求回归年 365.2425 日。观测规模大、标准统一。`artifact`

## (3) 推演与模型建构

推演是全国测量加历法推算：以多地实测求回归年，再以新参数推算《授时历》。链条：全国观测 → 参数 → 历法。`artifact`

## (4) 证据链

证据链：27 处测站记录 → 回归年 365.2425 日（现代值 365.2422 日，约三百年差一天）→ 《授时历》施行。关键证据强度高：数值可复核、历法长期施行。反证处理：卒年 1314 或 1316 两说。`artifact`

## (5) 理论语言与论证结构

语言为历法与测量体：测站、影长、参数的数值论述。论证开头从全国实测出发，结尾给出历法。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 全国 27 处测站的测量
- 简仪与高表的研制
- 《授时历》的历法推算
- 不该研究：
- 不把回归年写成现代精确值
- 不把卒年两说写成定论
- 不把《授时历》的合作写成独作
- Negative prompt: `no tropical year presented as a modern exact value, no death year presented as certain, no joint calendar presented as solo work`

## (7) 测试提示词示例（现代题材：用郭守敬的方法，从现代多站冬至影长数据测定回归年）

- Prompt: `In the style of Guo Shoujing, measure the tropical year from modern solstice shadows at many stations: standardise the instruments, compare all stations, fit the year length, and state how long the calendar stays within a day`
- 中文对照：郭守敬风格，从现代多站冬至影长数据测定回归年：统一仪器、对照全部测站、拟合回归年长度，并明说这部历法多少年才差一天。
- Negative: `no tropical year presented as a modern exact value, no death year presented as certain, no joint calendar presented as solo work`
- 检验点：回答是否按该天文学家的方法走（观测 → 数据积累 → 历法推算 → 验历 → 颁历）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
