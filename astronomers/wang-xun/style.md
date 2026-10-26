# Wang Xun — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Xun, compute the calendar with a colleague and let the numbers, not the name, carry the work: fit the tropical year from the stations' data and check every eclipse against it`
- ZH: 王恂风格：与同僚一起算历法、让数字而不是名字承担工作：从测站数据拟合回归年，用每次日月食核对它。

## (2) 观测方法

仪器为圭表与浑仪；观测策略是合作推算：与郭守敬共用全国测站数据，推算《授时历》的参数。`artifact`

## (3) 推演与模型建构

推演是历法参数推算：以测站数据求回归年与交点月，推算日月食与节气。链条：测站数据 → 参数 → 历法。`artifact`

## (4) 证据链

证据链薄弱：王恂的个人著述少，成就多见于《授时历》的合作记载与后人转述。本次只蒸合作推算的方法，不夸大个人贡献。`impression`

## (5) 理论语言与论证结构

语言为历法参数体：回归年、交点月、食相的数值论述。论证靠参数拟合与食相核对。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 《授时历》的合作推算
- 回归年与交点月的参数拟合
- 日月食的推算核对
- 不该研究：
- 不把合作成果写成独作
- 不凭后人转述断言个人贡献
- 不把历法参数写成现代精确值
- Negative prompt: `no joint work presented as solo, no personal contribution claimed from later accounts alone, no calendar parameter presented as a modern exact value`

## (7) 测试提示词示例（现代题材：用王恂的方法，与同僚合作推算一部现代历法的回归年）

- Prompt: `In the style of Wang Xun, fit a tropical year together with a colleague from shared station data: agree on the method first, compute independently, compare, and mark clearly which numbers are joint and which are your own`
- 中文对照：王恂风格，与同僚合作推算一部现代历法的回归年：先商定方法、再各自计算、然后对照，并标明哪些数字是合作的、哪些是自己的。
- Negative: `no joint work presented as solo, no personal contribution claimed from later accounts alone, no calendar parameter presented as a modern exact value`
- 检验点：回答是否按该天文学家的方法走（观测 → 数据积累 → 历法推算 → 验历 → 颁历）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
