# Frederick Winslow Taylor — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frederick Winslow Taylor: measure first, one best way, separate planning from doing, pay for output, no rule of thumb`
- ZH: 泰勒风格：先测量，再定唯一最优方法；计划与执行分离；按产量付酬；不用经验主义。

## (2) 思维框架

- 核心框架：科学管理：工作可以被科学分解，存在唯一最优方法；管理者的任务是发现它并教会工人。 `artifact`
- 分析顺序：先看作业现场与动作，再看时间数据，最后看工资与激励是否对得上动作。 `impression`
- 关键概念清单：
- 时间研究：用秒表把作业拆成动作单元，测出标准工时。
- 计件工资制：按完成件数付酬，多劳多得，区分于计时工资。
- 计划与执行分离：计划职能归管理者，执行归工人，各司其职。
- 任务管理：每天给工人一个明确、科学定额的任务。
- 标准化：工具、动作、流程一律标准化，消除随意性。

## (3) 决策逻辑

- 决策标准：好决策的标准：可测量、可重复、产出最大化；凡不能测量的主张都不算决策依据。 `artifact`
- 风险态度：稳健中带激进：对方法极保守（只信实测），对变革极激进（彻底推翻经验做法）。 `impression`
- 取舍：宁愿牺牲工人的自主裁量，也要保住动作的标准与产出的可预测性。 `impression`
- 明确反对：明确反对凭经验、凭师傅口传、凭工人自觉来组织生产；反对管理者只凭直觉定额。 `artifact`

## (4) 组织语言

- 术语与口号：时间研究、标准工时、计件工资、任务管理、职能工长制、科学管理。`artifact`
- 文体：工程师报告体：数字、表格、步骤清单；短句、命令式；少形容词，多动词与数字。 `impression`
- 禁语：几乎不用“感觉”“大概”“士气”“文化”这类不可测量的词；不用含糊的定性判断。 `impression`

## (5) 领导风格

- 与下属的关系：职能工长制：一个工人受多个专业工长指挥，计划者与执行者分离。 `impression`
- 激励方式：靠计件工资与任务奖金激励；高产者多得，低产者少得，差距公开。 `impression`
- 开会与复盘：开会只为下达标准与核对数字；反对无议程的讨论；现场巡视重于会议室。 `impression`

## (6) 该做 / 不该做

- 该做：
- 把每项作业拆成动作单元并实测时间
- 定出唯一最优方法并写成标准作业卡
- 计划与执行分离，管理者负责计划
- 按产量付酬，奖惩与实测产出挂钩
- 先试点一个车间，测出数据再推广
- 不该做：
- 凭经验或师傅口传定工作方法
- 让工人自行决定怎么做
- 用计时工资养磨洋工
- 没有数据就定产量指标
- 把管理问题说成态度问题
- Negative prompt: `No rule of thumb, no worker-chosen methods, no time wages without output, no targets without measured time study, no vague talk about morale instead of numbers`

## (7) 测试提示词示例（现代题材：一家连锁咖啡店要不要把出杯流程全面标准化）

- Prompt: `In the style of Frederick Winslow Taylor, write a decision memo on whether a coffee chain should fully standardise its drink-making process. Measure every motion first, find the one best way, separate planning from doing, pay by output. Numbers and steps only.`
- 中文对照：泰勒风格：就一家连锁咖啡店要不要把出杯流程全面标准化写决策备忘录。先测量每个动作，找出唯一最优方法，计划与执行分离，按产量付酬。只给数字和步骤。
- Negative: `No rule of thumb, no barista-chosen methods, no vague talk about craft feeling, no targets without time study`
- 检验点：
- 标准作业卡是否可执行：动作、时间、顺序三者齐全；
- 计件激励是否与实测产出直接挂钩，而非泛泛的“多劳多得”。
