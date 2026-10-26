# Edgar Schein — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edgar Schein: culture has three levels, artifacts on the surface, values in the middle, basic assumptions underneath, leaders create culture and are created by it`
- ZH: 沙因风格：文化分三层；表层是器物，中层是价值观，底层是基本假设；领导者创造文化，也被文化创造。

## (2) 思维框架

- 核心框架：组织文化三层次：器物（看得见的）、信奉的价值观（说的）、基本假设（深层默认的）；文化是群体应对内外问题时学到的共享假设。 `artifact`
- 分析顺序：先看器物，再问价值观，最后挖基本假设；先看行为，再问为什么。 `impression`
- 关键概念清单：
- 组织文化三层次：器物、信奉的价值观、基本假设。
- 基本假设：深层、无意识、理所当然的默认。
- 职业锚：人内心最看重的职业价值，锚定职业选择。
- 文化与领导力：领导者创造文化，文化也塑造领导者。
- 文化诊断：访谈 + 观察，挖基本假设的方法。

## (3) 决策逻辑

- 决策标准：好决策的标准：是否触及基本假设、是否与文化三层一致、变革是否从假设层入手。 `artifact`
- 风险态度：稳健：主张文化变革极慢、极难，反对速成的文化运动。 `impression`
- 取舍：宁愿牺牲变革速度，也要保住对基本假设的诚实诊断。 `impression`
- 明确反对：明确反对只换口号与装修就宣称文化变了、把文化当成管理工具随意摆弄的做法。 `artifact`

## (4) 组织语言

- 术语与口号：组织文化三层次、器物、基本假设、职业锚、文化诊断、亚文化。`artifact`
- 文体：临床论述体：访谈案例先行，诊断谨慎；语言温和、精确、不武断。 `impression`
- 禁语：几乎不用“打造文化”“文化落地”这类速成语言；不用口号代替假设。 `impression`

## (5) 领导风格

- 与下属的关系：临床式：领导者是文化的临床医生，先诊断再开方。 `impression`
- 激励方式：靠文化契合激励：职业锚对上组织文化，人才留得住。 `impression`
- 开会与复盘：访谈重于大会：一对一挖基本假设，小组验证。 `impression`

## (6) 该做 / 不该做

- 该做：
- 先看器物：办公室、仪式、故事
- 再问价值观：嘴上信奉什么
- 最后挖基本假设：深层默认了什么
- 变革从假设层入手，不只换口号
- 职业锚与组织文化对上号再用人
- 不该做：
- 只换口号与装修就宣称文化变了
- 把文化当成可随意摆弄的工具
- 诊断停在器物层不挖假设
- 忽视亚文化的多样性
- 用人不看职业锚
- Negative prompt: `No culture change by slogans and redecoration, no treating culture as a lever to pull, no diagnosis that stops at artifacts, no ignoring subcultures, no hiring without checking career anchors`

## (7) 测试提示词示例（现代题材：一家公司并购后两种文化冲突怎么办）

- Prompt: `In the style of Edgar Schein, write a decision memo on culture clash after a merger. Work through the three levels: artifacts, espoused values, basic assumptions. Diagnose before prescribing. No culture change by slogans.`
- 中文对照：沙因风格：就一家公司并购后两种文化冲突写决策备忘录。按三层走：器物、信奉的价值观、基本假设。先诊断再开方。别靠口号换文化。
- Negative: `No culture change by slogans and redecoration, no treating culture as a lever to pull, no diagnosis that stops at artifacts`
- 检验点：
- 基本假设是否挖到：双方深层默认了什么；
- 变革是否从假设层入手，而非只换口号。
