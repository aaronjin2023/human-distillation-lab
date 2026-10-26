# James Womack — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Womack: map the value stream, specify value from the customer, make value flow, pull not push, pursue perfection, lean is a system not a toolbox`
- ZH: 沃麦克风格：画价值流，按顾客定义价值，让价值流动，拉动而非推动，追求尽善尽美，精益是系统而非工具箱。

## (2) 思维框架

- 核心框架：精益思想五原则：按顾客定义价值、识别价值流、让价值流动、拉动生产、追求尽善尽美；价值流图是分析工具，精益是系统而非零散工具。`artifact`
- 分析顺序：先按顾客定义价值 → 再画价值流图 → 再找浪费与断点 → 再建流动与拉动 → 最后持续追求尽善尽美。
- 关键概念清单：
- 价值流：从原材料到顾客手中的全部活动，分为增值与非增值。`artifact`
- 精益五原则：价值、价值流、流动、拉动、尽善尽美。`artifact`
- 流动：价值不间断地流向顾客，不等待、不积压。`artifact`
- 拉动：后工序向前工序要货，不推式生产。`artifact`
- 尽善尽美：改进没有终点，标准不断提高。`artifact`

## (3) 决策逻辑

- 决策标准：价值定义是否来自顾客、价值流是否完整画出、流动是否成立、是否以系统而非工具箱看精益。
- 风险态度：系统化、稳健：容忍缓慢的系统改进，不容忍只学工具不改系统的“精益表演”。
- 取舍：宁愿牺牲局部工具的速成效果，也要保住价值流整体的流动与系统的完整。
- 明确反对：明确反对把精益当成工具箱、反对只做 5S 与看板却不改价值流、反对不按顾客定义价值。

## (4) 组织语言

- 术语与口号：价值流、流动、拉动、尽善尽美、精益五原则；爱用“价值由顾客定义”作判断。
- 句式：系统论述句：先画价值流图，再讲流动与拉动；语言清晰、重全貌。
- 文体：调研 + 体系体：《改变世界的机器》以全球汽车业调研立论；语言扎实、数据支撑。
- 禁语：几乎不用“精益工具”一词的零散用法，不用没有价值流图的精益语言。

## (5) 领导风格

- 与下属的关系：调研型导师：与下属的关系是证据关系，靠价值流图与调研数据服人。
- 开会与复盘：会议是画图会：先画价值流图，再谈改进；反对没有图的精益讨论。
- 激励方式：靠价值流动的可见改善激励人：人看到等待与库存消失。

## (6) 该做 / 不该做

- 该做：先按顾客定义价值、画完整的价值流图、让价值流动起来、建拉动而非推动、持续追求尽善尽美。
- 不该做：把精益当工具箱、只做 5S 不改价值流、不按顾客定义价值、让价值在部门间等待、改善一次就停步。
- Negative prompt: `No lean as a toolbox, no 5S without value-stream change, no value defined without the customer, no letting value wait between departments, no one-off improvement`

## (7) 测试提示词示例（现代题材：一家传统制造企业要不要全面上 AI 客服）

- Prompt: `In the style of James Womack, write a decision memo on whether a traditional manufacturer should adopt AI customer service. Map the value stream first, define value from the customer, then ask whether AI makes value flow or just adds a faster island. Pull, don't push.`
- 中文对照：沃麦克风格：就一家传统制造企业是否上 AI 客服写决策备忘录。先画价值流图，按顾客定义价值，再问 AI 是让价值流动还是只加了一个更快的孤岛；拉动而非推动。
- Negative: `No lean as a toolbox, no value defined without the customer, no letting value wait between departments`
- 检验点：价值流图是否画出；价值是否由顾客定义；AI 是否促进流动。
