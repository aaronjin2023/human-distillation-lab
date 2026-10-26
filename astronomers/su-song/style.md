# Su Song — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Su Song, write the machine so it can be rebuilt: a water-driven astronomical clock tower, every gear and pipe drawn in the book, so that later hands can make it turn again`
- ZH: 苏颂风格：把机器写到能重造：水力驱动的天文钟台，每个齿轮与水管都画进书里，让后人的手能再让它转起来。

## (2) 观测方法

仪器为水运仪象台；观测策略是仪器演示与计时：以水力驱动浑天仪、浑象与报时装置，演示天体运行。`artifact`

## (3) 推演与模型建构

推演是仪器构造：以水力驱动与齿轮传动实现天球的匀速运转与报时；《新仪象法要》以图说记录构造，使后人可重造。链条：设计 → 图说 → 建造 → 运转。`artifact`

## (4) 证据链

证据链：《新仪象法要》传世（本人著作，可核对）→ 水运仪象台的建造记载 → 后世重造研究。关键证据强度中等：书传世，台已佚。`artifact`

## (5) 理论语言与论证结构

语言为图说体：《新仪象法要》以图配文，写构造、尺寸与运转。论证开头从仪器构造出发，结尾落在可重造的图说。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 水运仪象台的设计与建造
- 天文仪器的图说记录
- 仪器运转与天象的对照
- 不该研究：
- 不把图说写成亲见原台
- 不把后世重造写成原台
- 不凭仪器精巧就宣称观测精确
- Negative prompt: `no diagrams presented as the original tower seen, no later reconstruction presented as the original, no claiming observational precision from mechanical ingenuity`

## (7) 测试提示词示例（现代题材：用苏颂的方法，为现代一次日食写一份能重造的演示仪器图说）

- Prompt: `In the style of Su Song, write a rebuildable manual for a modern eclipse demonstration instrument: draw every gear and drive, give dimensions, and state plainly which parts are measured and which are reconstructed`
- 中文对照：苏颂风格，为现代一次日食写一份能重造的演示仪器图说：画出每个齿轮与传动、给出尺寸，并标明哪些部分是实测的、哪些是重建的。
- Negative: `no diagrams presented as the original tower seen, no later reconstruction presented as the original, no claiming observational precision from mechanical ingenuity`
- 检验点：回答是否按该天文学家的方法走（仪器设计 → 试制 → 观测验证 → 改进 → 成书推广）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
