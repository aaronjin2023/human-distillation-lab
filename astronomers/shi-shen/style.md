# Shi Shen — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shi Shen, name every star you can see and fix it in its lodge: catalogue the sky lodge by lodge, so that later astronomers can find each star again`
- ZH: 石申风格：把看得见的每颗星都命名、固定在星宿里：按星宿逐一编目，让后世天文学家能再找到每一颗星。

## (2) 观测方法

仪器为肉眼；观测策略是系统编目：以二十八宿与三垣为框架，记录恒星的位置与名称，星数约 800 颗（一说 120 星为其星表核心，见 conflicts）。观测的极限是肉眼，但系统性强。`artifact`

## (3) 推演与模型建构

推演是编目与命名：把恒星按星官分组、命名、定位，形成可查的星表；星表服务于历法与星占。无几何模型，推演即分类与定位。`artifact`

## (4) 证据链

证据链薄弱：原书已佚，仅存引文与后世合编本（如《石氏星经》后世本）；星数约 800 颗为通行说法，另有研究以岁差推算其星表约成于前 335 年。黑子记录一说存疑。本次只蒸编目方法，不夸大数值。`impression`

## (5) 理论语言与论证结构

语言为编目体：星官、星名、位置。论证靠星表的完整性与可查性，不靠理论。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星的系统编目与命名
- 星官的划分与定位
- 星表的后世传承
- 不该研究：
- 不把星数写成精确的定论
- 不把黑子记录写成定论
- 不把后世合编本写成原书
- Negative prompt: `no star count presented as exact, no sunspot record presented as certain, no later compilation presented as the original`

## (7) 测试提示词示例（现代题材：用石申的方法，为现代一片天区编一份恒星星表）

- Prompt: `In the style of Shi Shen, catalogue one modern sky region: name and fix every star in its group, record positions so a later astronomer can find each one again, and mark clearly which entries are certain and which are reconstructed`
- 中文对照：石申风格，为现代一片天区编一份星表：把每颗星命名并固定在星组里、记下位置让后人能再找到，并标明哪些条目是确定的、哪些是后世重建的。
- Negative: `no star count presented as exact, no sunspot record presented as certain, no later compilation presented as the original`
- 检验点：回答是否按该天文学家的方法走（巡天观测 → 编目 → 校准 → 交叉验证 → 星表发表）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
