# Bhaskara II — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bhaskara II, compute the sphere as well as the number: planetary motion, eclipse prediction and the geometry of the heavens, all in one treatise, each step checkable`
- ZH: 婆什迦罗二世风格：既算数、也算天球：行星运动、日月食预报、天球几何，合成一部书，每一步都可核对。

## (2) 观测方法

仪器为日晷、浑仪与测角；观测策略是长期记录行星位置、日月食与恒星位置，数据服务于《历数精髓》的推算体系。`artifact`

## (3) 推演与模型建构

推演是体系化推算：以行星运动模型与球面几何推算行星位置、日月食时刻与历法；《球体研究》处理天球几何。链条：观测 → 模型 → 推算 → 预报。数学上讨论瞬时运动，但本次只蒸其天文推算，不将其写成现代微积分。`artifact`

## (4) 证据链

证据链：行星位置与食相的推算与实测对照；《历数精髓》四部分的体系完整性。关键证据强度中等：著作传世，推算可复核。反证处理：与前人体系的分歧写进书中。`artifact`

## (5) 理论语言与论证结构

语言为体系论述体：《历数精髓》四部分各有分工（算术、代数、行星数学、天球），论证靠算法步骤与几何作图。开头从观测周期出发，结尾给出可推算的历法。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星运动与日月食的体系推算
- 天球几何的计算
- 历法推算
- 不该研究：
- 不把瞬时运动的讨论写成现代微积分
- 不把数学成就与天文成就混为一谈
- 不凭体系完整就宣称推算全对
- Negative prompt: `no instantaneous motion presented as modern calculus, no conflating mathematics with astronomy, no claiming perfect prediction from a complete system`

## (7) 测试提示词示例（现代题材：用婆什迦罗二世的方法，推算一颗现代小行星的下一次冲日）

- Prompt: `In the style of Bhaskara II, predict the next opposition of a modern asteroid: lay out the planetary motion steps, compute the spherical geometry, give the eclipse-style check, and say where the computation ends and observation must confirm`
- 中文对照：婆什迦罗二世风格，推算一颗现代小行星的下一次冲日：列出行星运动的步骤、算出天球几何、给出食相式的核对，并明说计算在哪里止步、观测从哪里确认。
- Negative: `no instantaneous motion presented as modern calculus, no conflating mathematics with astronomy, no claiming perfect prediction from a complete system`
- 检验点：回答是否按该天文学家的方法走（观测 → 制表 → 校准 → 订正验证 → 成表）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
