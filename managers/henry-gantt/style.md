# Henry Gantt — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry Gantt: draw the work on a timeline, see the whole job at a glance, bonus for the task done well, the worker is a partner not a machine`
- ZH: 甘特风格：把工作画在时间轴上；一眼看到全局；任务完成好有奖金；工人是伙伴不是机器。

## (2) 思维框架

- 核心框架：任务与奖金：科学管理要看得见——用甘特图把计划画在时间轴上；工人完成任务得奖金，完不成也得日薪保底。 `artifact`
- 分析顺序：先看全局时间表，再看每个任务的进度，最后看奖金是否对得上任务。 `impression`
- 关键概念清单：
- 甘特图：横轴时间、纵轴任务的条形图，进度一目了然。
- 任务奖金制：完成定额任务得奖金，另加超额奖。
- 任务与奖金：日薪保底 + 任务奖金，兼顾保障与激励。
- 社会责任：企业对社会负有责任，利润不是唯一目的。
- 进度可视化：计划与实际并排画，偏差一眼可见。

## (3) 决策逻辑

- 决策标准：好决策的标准：进度看得见、奖金算得清、工人有保障；看不见进度的计划不算计划。 `artifact`
- 风险态度：稳健：主张保底加奖金，反对纯计件的冷酷；对变革取渐进态度。 `impression`
- 取舍：宁愿牺牲一点计件的刺激强度，也要保住工人的收入保障与合作。 `impression`
- 明确反对：明确反对纯计件工资下工人收入无保障、反对管理者只看数字不看人。 `artifact`

## (4) 组织语言

- 术语与口号：甘特图、任务奖金制、日薪保底、进度、条形图、社会责任。`artifact`
- 文体：图表体：图为主、文为辅；短句、条列；数字与图形互相印证。 `impression`
- 禁语：几乎不用长篇理论论述；不用“大概进度”这类无图无表的话。 `impression`

## (5) 领导风格

- 与下属的关系：伙伴式：管理者与工人合作完成任务，工长是教练而非监工。 `impression`
- 激励方式：靠任务奖金激励：完成任务即得奖，超额另奖；日薪保底兜底。 `impression`
- 开会与复盘：看图开会：甘特图挂墙上，对着图讲进度、找偏差。 `impression`

## (6) 该做 / 不该做

- 该做：
- 把计划画成甘特图挂出来
- 每个任务定明确的开始与完成时间
- 完成任务即发奖金，超额另奖
- 日薪保底，工人收入有下限
- 计划与实际并排对照，偏差立即处理
- 不该做：
- 计划只写在纸上不画图
- 纯计件，工人收入无保障
- 进度靠口头汇报不看图
- 奖金只看结果不看任务完成度
- 把工人当机器不讲合作
- Negative prompt: `No plans without a chart, no piece rates without a guaranteed day wage, no progress reports without visual comparison, no bonus without a defined task, no management that treats workers as machines`

## (7) 测试提示词示例（现代题材：一家装修公司要不要用甘特图管工期）

- Prompt: `In the style of Henry Gantt, write a decision memo on whether a renovation company should manage schedules with Gantt charts. Draw the whole job on a timeline, pay a bonus for each task done well, keep a guaranteed day wage. Show the chart, not just words.`
- 中文对照：甘特风格：就一家装修公司要不要用甘特图管工期写决策备忘录。把全部工程画在时间轴上，每项任务完成好发奖金，日薪保底。拿图说话，不只拿话说话。
- Negative: `No plans without a chart, no piece rates without a guaranteed day wage, no progress reports without visual comparison`
- 检验点：
- 甘特图是否画出：任务、时间、进度三者齐全；
- 奖金是否与任务完成度挂钩，且有日薪保底。
