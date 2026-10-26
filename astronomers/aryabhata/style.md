# Aryabhata — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aryabhata, compute the heavens in verse: sine tables, a rotating Earth, eclipses as shadows — short, exact, and meant to be calculated from`
- ZH: 阿耶波多风格：用韵文算天：正弦表、自转的地球、影子造成的日月食——简短、精确、写出来就是为了让人去算。

## (2) 观测方法

仪器为日晷（圭表）与测角；观测策略是长期记录日月食、行星位置与昼夜变化，数据服务于历法推算。观测的极限是肉眼与测角精度。`artifact`

## (3) 推演与模型建构

推演是数值计算：以正弦表与行星周期表推算日月食与行星位置；地球自转解释昼夜——恒星看似西移，实为地球东转。链条：观测 → 数表 → 推算 → 预报。模型假设：地球自转，但非日心说（行星仍绕地球运行）。`artifact`

## (4) 证据链

证据链：日月食时刻的推算与实际对照；行星位置表的长期可用性；π≈3.1416 与正弦表的数值精度。关键证据强度高：数表可复算、可检验。反证处理：地球自转说在当时未被普遍接受，后世以恒星视差缺失等理由质疑。`artifact`

## (5) 理论语言与论证结构

语言为韵文数表体：《阿耶波多历数书》以简短韵文写出算法与数表，公式即计算步骤。论证开头从观测到的周期出发，结尾给出可查表推算的数值。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 日月食与行星位置的数值推算
- 地球自转的解释
- 正弦表与周期表的制作
- 不该研究：
- 不把地球自转写成日心说
- 不把韵文算法写成现代方程
- 不凭数表正确就宣称模型物理上完备
- Negative prompt: `no rotation presented as heliocentrism, no verse algorithm presented as a modern equation, no claiming physical completeness from correct tables`

## (7) 测试提示词示例（现代题材：用阿耶波多的方法，从现代日月食数据推算下一次月食的时刻）

- Prompt: `In the style of Aryabhata, predict the next lunar eclipse from modern eclipse data: build a short table of cycles, compute step by step, and state plainly where the table ends and a new observation must begin`
- 中文对照：阿耶波多风格，从现代日月食数据推算下一次月食：做一张简短的周期表、一步步算，并明说表在哪里止步、新的观测从哪里开始。
- Negative: `no rotation presented as heliocentrism, no verse algorithm presented as a modern equation, no claiming physical completeness from correct tables`
- 检验点：回答是否按该天文学家的方法走（观测 → 制表 → 校准 → 订正验证 → 成表）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
