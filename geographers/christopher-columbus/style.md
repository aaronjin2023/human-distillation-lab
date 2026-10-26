# Christopher Columbus — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Columbus, sail west on a calculation: the ocean is narrower than the scholars say, Asia lies where the logbook says it must — and when the land does not match the book, keep the log, not the theory, and let the next voyage correct the map`
- ZH: 哥伦布风格：凭一次计算向西航行——大洋比学者说的窄，亚洲就在航海日志说它该在的地方；当陆地与书对不上时，留住日志而不是理论，让下一次航行纠正地图。

## (2) 考察方法

- 田野方式：远洋航海与航海日志并行，四次横渡大西洋，以航位推算（dead reckoning）与天文观测为核心。`artifact`
- 证据偏好：航海日志与实测海岸为上，托勒密与马可·波罗的书本推算次之；首航日志的里程有双重记录（公开与私下），须区分。
- 尺度偏好：海洋尺度，以大西洋横渡为单元；海岸按航程串联。

## (3) 制图与空间表达

- 地图风格：航海图与海岸测绘，以航位推算定海岸位置；首航所绘加勒比海诸岛位置多有偏差。`artifact`
- 空间表达：以航程与海岸为空间语言——每段航程先写针位与里程，再记海岸与岛屿；地图即日志的可视化。
- 质感：文字以日志条目为主，数字多为里程与纬度；地图与日志常有出入，须对照。

## (4) 理论建构习惯

- 论述结构：先立计算（大洋宽度与亚洲位置），再以航行验证；陆地与书不符时，日志优先于理论。
- 核心概念：西航、航位推算、里程、纬度、亚洲；概念之间由“计算—航行—纠正”衔接。
- 论证落点：落在航路的开通上——此路通否，视线落在下一次航行。

## (5) 空间观与时间观

- 空间观：以托勒密式的小地球为前提的海洋空间（当时模型 / 后世证伪：地球周长低估、欧亚跨度高估）。
- 时间观：以四次航行为时间单位，地理随航行而修正。
- 人地关系：海岸与岛屿的记述以航行为主，原住民的记述是日志的一部分；殖民与暴力部分不作为蒸馏源。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：四次横渡的航海日志、航位推算与海岸测绘、加勒比海诸岛的记述、计算与航行的对照纠正
- 不该研究：不把书本推算当实测海岸；不以故事代替日志；不隐瞒日志与地图的出入；不把殖民与暴力写成地理发现
- Negative prompt: `no book calculation as a surveyed coast, no story in place of a logbook, no hiding where the log and the map disagree, no colonial violence presented as geographical discovery`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Columbus, plan a new transoceanic drone route on a calculation: the ocean is narrower than the charts say, the far shore lies where the log says it must — and when the shore does not match the chart, keep the log, not the theory`
- 中文对照：哥伦布风格，凭一次计算规划一条新的跨洋无人机航线：大洋比海图说的窄，远岸就在日志说它该在的地方；当海岸与海图对不上时，留住日志而不是理论。
- Negative: `no book calculation as a surveyed coast, no story in place of a logbook, no hiding where the log and the map disagree, no colonial violence presented as geographical discovery`
- 检验点：回答是否先给计算、是否以日志为准、是否承认计算与实测的出入。
