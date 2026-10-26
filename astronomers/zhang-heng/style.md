# Zhang Heng — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Heng, build the heavens as a machine that turns by water: an armillary sphere driven by a clepsydra, a catalogue of 2,500 stars, and eclipses explained by the sphere itself`
- ZH: 张衡风格：把天造成一台用水驱动的机器：水运浑天仪、2,500 星的星表，日月食由浑天本身来解释。

## (2) 观测方法

仪器为水运浑天仪与浑天仪；观测策略是仪器观测加星表编目：以浑天仪测恒星位置，编星表 124 星座、2,500 星。观测的极限是浑天仪的刻度精度。`artifact`

## (3) 推演与模型建构

推演是浑天模型：天如蛋壳、地如蛋黄，天球绕地旋转；日月食为日月运行至同一直线时的遮挡。链条：仪器观测 → 星表 → 浑天模型 → 食相解释。模型为地心浑天说（当时模型，后世证伪其宇宙结构，但仪器与星表方法可蒸）。`artifact`

## (4) 证据链

证据链：星表（124 星座、2,500 星，直接编目）→ 水运浑天仪的运转与天象对照 → 日月食解释。关键证据强度中等：星表与仪器有记载，浑天仪原物已佚。反证处理：浑天说与盖天说之争，后世以浑天说胜出，但地心结构本身后世被证伪。`artifact`

## (5) 理论语言与论证结构

语言为仪器与模型体：浑天仪的构造、星表的编目、浑天说的论述。论证开头从仪器观测出发，结尾落在浑天模型。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 浑天仪的仪器观测
- 星表的系统编目
- 浑天说下的日月食解释
- 不该研究：
- 不把浑天说写成真理（当时模型，后世证伪）
- 不把已佚的浑天仪写成亲见
- 不把星数写成现代精确值
- Negative prompt: `no celestial-sphere model as truth, no lost instrument presented as seen, no star count presented as a modern exact value`

## (7) 测试提示词示例（现代题材：用张衡的方法，为现代一次日食设计一台演示仪器）

- Prompt: `In the style of Zhang Heng, design a demonstration instrument for a modern eclipse: a sphere that turns by a steady drive, a catalogue of the stars it must show, and an eclipse explained by the machine itself — then state where the machine stops being a model of the sky`
- 中文对照：张衡风格，为现代一次日食设计一台演示仪器：一台匀速转动的浑天仪、它必须展示的星表、日食由机器本身来解释，并明说机器在何处不再是天空的模型。
- Negative: `no celestial-sphere model as truth, no lost instrument presented as seen, no star count presented as a modern exact value`
- 检验点：回答是否按该天文学家的方法走（仪器设计 → 试制 → 观测验证 → 改进 → 成书推广）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
