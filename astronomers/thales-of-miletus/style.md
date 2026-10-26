# Thales of Miletus — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thales of Miletus, look for a repeating cycle behind a frightening sky event, predict its return from past occurrences, and explain it by nature, not by myth`
- ZH: 泰勒斯风格：在令人恐惧的天象背后找可重复的周期，从既往事例推断其重现，以自然解释代替神话解释。

## (2) 观测方法

肉眼观测为主，工具为日晷与简陋的测角手段；观测策略是长期记录天象发生的时刻与间隔，从重复中找周期。没有望远镜，没有定量星表，观测的极限是人眼与记忆。`artifact`

## (3) 推演与模型建构

推演是周期类比：若某天象以固定间隔重现，则下一次可据此预报。没有几何模型与方程，推演链条只有两环——过去的间隔、未来的重现。模型边界：只能预报“何时”，不能解释“为何”。`artifact`

## (4) 证据链

证据是历史记录的重复：希罗多德记载泰勒斯预报了米底与吕底亚交战之日的日食（前 585 年 5 月 28 日一说）。关键证据的强度弱——预测方法未知，现代学者多认为当时并无可靠的定点日食预报方法，准确预报可能出于运气。反证处理：后世记载分歧。`impression`

## (5) 理论语言与论证结构

语言为描述性自然哲学，无公式、无图表；论证结构是归纳：从个别天象的重复推出一般规律。开头从观测到的天象出发，结尾给出可检验的预报，而不是神话叙事。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 日食、月食等天象的发生时刻与间隔
- 恒星周年视运动与季节
- 天象背后的可重复周期
- 不该研究：
- 不凭神话或神意解释天象
- 不把一次巧合写成普遍规律
- 不超越观测宣称已知预报方法
- Negative prompt: `no mythological explanation, no treating one coincidence as a general law, no claiming a prediction method without evidence`

## (7) 测试提示词示例（现代题材：用泰勒斯的方法分析现代日食预报数据，检验周期规律能预报到什么程度）

- Prompt: `In the style of Thales of Miletus, analyse modern eclipse records: list past solar eclipses, look for a repeating interval, predict the next one from that interval alone, and state plainly where the cycle method fails`
- 中文对照：泰勒斯风格，分析现代日食记录：列出既往日食，仅凭重复间隔预报下一次，并明说周期法在哪里失效。
- Negative: `no mythological explanation, no treating one coincidence as a general law, no claiming a prediction method without evidence`
- 检验点：回答是否按该天文学家的方法走（观测 → 记录 → 推算 → 验证 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
