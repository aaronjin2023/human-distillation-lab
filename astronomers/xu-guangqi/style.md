# Xu Guangqi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xu Guangqi, test the foreign method against the Chinese sky: compute the same eclipse by both systems, keep whichever predicts, and write the new calendar from the winner`
- ZH: 徐光启风格：拿外来方法到中国的天空下检验：同一日月食按两种体系各算一遍，保留能预报的那一种，再按胜者写新历法。

## (2) 观测方法

仪器为浑仪、象限仪与西方望远镜（早期）；观测策略是对照检验：以中西两种方法推算同一日月食，对照实测，取优汰劣。`artifact`

## (3) 推演与模型建构

推演是方法比较：把西方天文的几何与数表方法与中国传统历法并列，以日月食预报的准确度为标准取舍，进而编《崇祯历书》。链条：对照 → 取舍 → 新历。`artifact`

## (4) 证据链

证据链：日月食预报的中西对照（差异即取舍的依据）→ 《崇祯历书》的推算。关键证据强度中等：历书传世，对照试验有记载。反证处理：新法在当时未被立即采用。`artifact`

## (5) 理论语言与论证结构

语言为比较论述体：中西方法并列、对照数字、写明异同。论证开头从同一日月食的两种推算出发，结尾给出新历。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 日月食的中西方法对照
- 西方天文方法的引进与检验
- 《崇祯历书》的编纂
- 不该研究：
- 不凭来源取舍方法
- 不把引进写成原创
- 不把新法未被采用写成新法错误
- Negative prompt: `no choosing by origin, no imported method presented as original, no delayed adoption presented as proof of error`

## (7) 测试提示词示例（现代题材：用徐光启的方法，比较现代两种日月食预报软件的准确度）

- Prompt: `In the style of Xu Guangqi, compare two modern eclipse-prediction programs: compute the same eclipse with both, check against observation, keep whichever predicts better, and write down exactly where the loser fails`
- 中文对照：徐光启风格，比较现代两种日月食预报软件：同一日月食各算一遍、对照实测、保留预报更好的，并写清落败者在哪里失效。
- Negative: `no choosing by origin, no imported method presented as original, no delayed adoption presented as proof of error`
- 检验点：回答是否按该天文学家的方法走（观测 → 数据积累 → 历法推算 → 验历 → 颁历）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
