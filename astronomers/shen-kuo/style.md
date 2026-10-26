# Shen Kuo — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Kuo, test the instrument before you trust the sky: improve the armillary sphere, check the pole star's true place, and write down what the instrument, not the book, shows`
- ZH: 沈括风格：先验仪器、再信天：改进浑仪、核对北极星的真位置，把仪器而不是书本显示的东西写下来。

## (2) 观测方法

仪器为浑仪（改进后）与圭表；观测策略是仪器核对：以浑仪实测北极星位置，发现极星离北极三度多；观测月球盈亏，解释月相。`artifact`

## (3) 推演与模型建构

推演是仪器验证：以改进后的浑仪实测，修正旧说（北极星并非正在北极）；月球盈亏以日月相对位置解释。链条：仪器 → 实测 → 修正旧说。`artifact`

## (4) 证据链

证据链：《梦溪笔谈》天文篇的记载（本人著作，可核对）→ 浑仪改进的描述 → 北极星位置修正。关键证据强度中等：著作传世，但仪器原物已佚。`artifact`

## (5) 理论语言与论证结构

语言为笔记论述体：《梦溪笔谈》以条目记观测、仪器与推论。论证开头从仪器实测出发，结尾给出修正后的结论。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 浑仪的改进与实测
- 北极星位置的修正
- 月球盈亏的解释
- 不该研究：
- 不把仪器改进写成新仪器的发明
- 不把笔记中的推测写成定论
- 不凭书本旧说否定仪器实测
- Negative prompt: `no instrument improvement presented as a new invention, no notebook speculation presented as certain, no book authority overruling instrument measurement`

## (7) 测试提示词示例（现代题材：用沈括的方法，用现代一台望远镜核对北极星的真实位置）

- Prompt: `In the style of Shen Kuo, check the pole star's true place with a modern telescope: improve the pointing first, measure where the star really is, compare with the textbook claim, and write down what the instrument shows`
- 中文对照：沈括风格，用现代望远镜核对北极星的真位置：先改进指向、再实测恒星真位置、与书本说法对照，把仪器显示的东西写下来。
- Negative: `no instrument improvement presented as a new invention, no notebook speculation presented as certain, no book authority overruling instrument measurement`
- 检验点：回答是否按该天文学家的方法走（仪器设计 → 试制 → 观测验证 → 改进 → 成书推广）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
