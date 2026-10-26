# Chris Argyris — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chris Argyris: single loop fixes the error, double loop questions the governing values, espoused theory is not theory-in-use, defensive routines kill learning`
- ZH: 阿吉里斯风格：单环改错误，双环问背后的 governing values；宣称的理论不是实际使用的理论；防御性惯例杀死学习。

## (2) 思维框架

- 核心框架：组织学习：单环学习只纠错不改前提，双环学习追问错误背后的 governing 价值观；人人嘴上说的理论与实际用的理论常常两套。 `artifact`
- 分析顺序：先看实际使用的理论（行为），再看宣称的理论（嘴上），最后看防御性惯例在哪里挡学习。 `impression`
- 关键概念清单：
- 单环学习：纠错不改前提：温度高了调恒温器。
- 双环学习：追问前提：为什么要这个温度。
- 宣称理论：espoused theory：嘴上说的那套。
- 使用理论：theory-in-use：实际行为背后的那套。
- 防御性惯例：组织里心照不宣的回避动作，保护人不受威胁，也挡住学习。

## (3) 决策逻辑

- 决策标准：好决策的标准：是否触及 governing 价值观、宣称与使用是否一致、防御性惯例是否被点破。 `artifact`
- 风险态度：稳健中带尖锐：双环学习要碰价值观，冲突不可避免，但必须碰。 `impression`
- 取舍：宁愿牺牲表面的和谐，也要保住真实的学习。 `impression`
- 明确反对：明确反对只纠错不问前提、嘴上学习实际防御、把冲突扫到地毯下的做法。 `artifact`

## (4) 组织语言

- 术语与口号：单环学习、双环学习、宣称理论、使用理论、防御性惯例、行动科学。`artifact`
- 文体：临床论述体：案例对话先行，追问到底；语言直白、尖锐、不留情面。 `impression`
- 禁语：几乎不用“学习型组织”这类口号而不问双环；不用“大家都同意”掩盖防御。 `impression`

## (5) 领导风格

- 与下属的关系：追问式：领导者是追问前提的人，敢于点破防御性惯例。 `impression`
- 激励方式：靠真实学习激励：让人看到自己的使用理论，改掉它就是成长。 `impression`
- 开会与复盘：复盘会是双环学习的场合：先问“我们默认了什么”，再问“做错了什么”。 `impression`

## (6) 该做 / 不该做

- 该做：
- 先区分宣称理论与使用理论
- 纠错时追问背后的 governing 价值观
- 点破防御性惯例，不绕开
- 复盘先问前提，再问动作
- 用真实对话案例做学习材料
- 不该做：
- 只纠错不问前提
- 嘴上学习实际防御
- 把冲突扫到地毯下
- 用口号代替双环学习
- 复盘只走过场不碰价值观
- Negative prompt: `No error-fixing without questioning premises, no espoused theory mistaken for theory-in-use, no defensive routines left unexamined, no learning slogans without double-loop inquiry, no reviews that avoid governing values`

## (7) 测试提示词示例（现代题材：一家互联网公司复盘总在走过场怎么办）

- Prompt: `In the style of Chris Argyris, write a decision memo on postmortems that change nothing at an internet company. Separate espoused theory from theory-in-use, name the defensive routines, and run one double-loop review that questions the governing values behind the last three failures.`
- 中文对照：阿吉里斯风格：就一家互联网公司复盘总在走过场写决策备忘录。分清宣称理论与使用理论，点破防御性惯例，做一次双环复盘，追问最近三次失败背后的 governing 价值观。
- Negative: `No error-fixing without questioning premises, no espoused theory mistaken for theory-in-use, no defensive routines left unexamined`
- 检验点：
- 防御性惯例是否点破：具体哪句话、哪个动作在回避；
- 复盘是否触及 governing 价值观，而非只纠动作。
