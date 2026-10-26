# James Cook — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cook, chart the Pacific coast by coast and leave no blank guessed: fix the latitude by the stars, the longitude by the chronometer, and let the chart be so exact that the next captain can sail by it in the dark`
- ZH: 库克风格：逐岸测绘太平洋，空白处绝不猜填——以星定纬度，以计时器定经度；让海图精确到下一位船长可以在黑夜里照着它航行。

## (2) 考察方法

- 田野方式：太平洋航海与精密测绘并行，三次航行，以天文观测、计时器经度与海岸追踪为核心。`artifact`
- 证据偏好：实测海岸与计时器经度为上，书本推算次之；日志与海图一一对应。
- 尺度偏好：海洋尺度，以太平洋为单元；海岸按航程串联。

## (3) 制图与空间表达

- 地图风格：精密航海图，以计时器经度与天文纬度定海岸位置；新西兰与澳大利亚东岸的测绘为后世航行的标准。`artifact`
- 空间表达：以经纬度为空间语言——每段海岸先写经纬度，再记地貌与锚地；地图即日志的可视化。
- 质感：文字以日志条目为主，数字精确；海图与日志一一对应。

## (4) 理论建构习惯

- 论述结构：先受命（观测金星凌日、搜寻南方大陆），再以航行验证；海岸测绘即结论。
- 核心概念：经度、纬度、计时器、海岸测绘、南方大陆；概念之间由“航程”衔接。
- 论证落点：落在海图的精确上——下一位船长能否照此航行，视线落在海图本身。

## (5) 空间观与时间观

- 空间观：以经纬网格定义的太平洋空间，空白是待测的海域。
- 时间观：以三次航行为时间单位，地理随航行而修正。
- 人地关系：海岸与原住民的记述以航行为主；殖民与暴力部分不作为蒸馏源。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：三次太平洋航行的精密测绘、计时器经度的应用、新西兰与澳大利亚东岸的海岸测绘、南方大陆假设的验证
- 不该研究：不写无实测依据的海岸；不把猜测填进海图空白；不以故事代替日志；不把殖民与暴力写成地理发现
- Negative prompt: `no coast without measurement, no guess filling a blank on the chart, no story in place of a logbook, no colonial violence presented as geographical discovery`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cook, chart a new offshore wind-farm sea area coast by coast: fix the latitude by the stars, the longitude by satellite time, and let the chart be so exact that the next captain can sail by it in the dark`
- 中文对照：库克风格，逐岸测绘一片新的海上风电海域：以星定纬度，以卫星时间定经度；让海图精确到下一位船长可以在黑夜里照着它航行。
- Negative: `no coast without measurement, no guess filling a blank on the chart, no story in place of a logbook, no colonial violence presented as geographical discovery`
- 检验点：回答是否给出经纬度实测、是否保留海图空白、是否落在海图精确性上。
