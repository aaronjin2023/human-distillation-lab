# Abel Tasman — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tasman, sail the unknown south on the Company's orders: log the latitude at every landfall, name the coast for the governor who sent you, and leave the blank on the chart blank — the next voyage will fill it, not your guess`
- ZH: 塔斯曼风格：奉公司的命令驶向未知的南方——在每个登陆点记下纬度，以派你出海的总督之名命名海岸；海图上的空白就留着空白，下一支航行会填上它，而不是你的猜测。

## (2) 考察方法

- 田野方式：远洋航海与航海日志并行，1642–1643 年奉荷兰东印度公司之命南航，以纬度观测与海岸追踪为核心。`artifact`
- 证据偏好：航海日志与实测海岸为上，书本推算次之；日志传世完整，是主要来源。
- 尺度偏好：海洋尺度，以南太平洋航行为单元；海岸按航程串联。

## (3) 制图与空间表达

- 地图风格：航海图与海岸测绘，以纬度观测定塔斯马尼亚与新西兰西岸位置。`artifact`
- 空间表达：以航程与纬度为空间语言——每段航程先写纬度与针位，再记海岸；地图即日志的可视化。
- 质感：文字以日志条目为主，数字多为纬度与航程。

## (4) 理论建构习惯

- 论述结构：先受命（搜寻南方大陆），再以航行验证；海岸即结论。
- 核心概念：南方大陆、纬度、海岸、登陆点；概念之间由“航程”衔接。
- 论证落点：落在海岸的测绘上——此岸何在，视线落在下一支航行。

## (5) 空间观与时间观

- 空间观：以南太平洋为中心的航行空间，未知大陆是空间的待填项。
- 时间观：以 1642–1643 年航行为时间单位，地理随航行而修正。
- 人地关系：海岸与原住民的记述以航行为主；殖民与暴力部分不作为蒸馏源。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：塔斯马尼亚与新西兰的发现记录、纬度观测与海岸测绘、《航海日志》的逐日记录、海图空白的保留
- 不该研究：不写无航程依据的海岸；不把猜测填进海图空白；不以故事代替日志；不把殖民与暴力写成地理发现
- Negative prompt: `no coast without a sailed leg, no guess filling a blank on the chart, no story in place of a logbook, no colonial violence presented as geographical discovery`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tasman, chart a new deep-sea survey route on company orders: log the latitude at every landfall, name the coast for the director who sent you, and leave the blank on the chart blank`
- 中文对照：塔斯曼风格，奉公司之命绘制一条新的深海调查航线：在每个登陆点记下纬度，以派你出海的主管之名命名海岸；海图上的空白就留着空白。
- Negative: `no coast without a sailed leg, no guess filling a blank on the chart, no story in place of a logbook, no colonial violence presented as geographical discovery`
- 检验点：回答是否给出纬度观测、是否保留海图空白、是否以日志为准。
