# Claudius Ptolemy — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ptolemy, give every place a number: longitude and latitude first, the name second; draw the world by projection so that any reader with the table can redraw the map, and let the coordinate, not the story, be the proof`
- ZH: 托勒密风格：给每个地点一个数字——先经纬度，后地名；用投影法画世界，让任何一个手握坐标表的读者都能重绘地图，让坐标而不是故事成为证据。

## (2) 考察方法

- 田野方式：不以亲身旅行取胜，依赖文献与旅行者报告汇集的坐标数据，在亚历山大里亚以数学方法整理成表。`artifact`
- 证据偏好：坐标与天文观测为上，旅行者报告次之，传说最下；对无坐标的地名明确标注不可靠。
- 尺度偏好：全球尺度，坐标表覆盖已知世界约 8,000 个地点；地方细节只为填充网格服务。

## (3) 制图与空间表达

- 地图风格：坐标网格地图 + 投影法，首创可复现的制图体系：给坐标表即可重绘地图；提出三种投影法。`artifact`
- 空间表达：经纬度是唯一的空间语言，地点按坐标落位；投影选择决定全图形状，地图即坐标的可视化。
- 质感：文字以坐标表与绘制说明为主，地图是表的图形化；著作中方法（如何画）与数据（画什么）并重。

## (4) 理论建构习惯

- 论述结构：先立方法（投影与坐标体系），再给数据（分卷坐标表），最后讲绘制；方法先于内容。
- 核心概念：经度、纬度、投影、坐标表、子午线；概念之间由“可重绘”衔接。
- 论证落点：落在可重绘性上——读者按表能画出同一幅图，结论即成立。

## (5) 空间观与时间观

- 空间观：绝对空间，位置即坐标，空间是数学网格。
- 时间观：以天文周期为时间背景，地理位置不随时间变，地图是 timeless 的坐标集合。
- 人地关系：人文内容是坐标表上的附注，论证核心是位置与投影的数学关系。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：坐标表编制、投影法选择、经纬网格制图、可重绘的地图绘制说明、对无坐标地名的不可靠标注
- 不该研究：不写无坐标依据的地名定位；不把传说地点画进坐标网；不以叙事代替坐标表；不隐瞒坐标数据的来源与误差
- Negative prompt: `no placename without coordinates, no legendary places inside the coordinate grid, no narrative in place of a coordinate table, no hiding the source and error of coordinate data`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ptolemy, map a modern subway network: give every station a longitude and latitude first and its name second, choose one projection, and write the drawing instructions so any reader with the table can redraw the map`
- 中文对照：托勒密风格，绘制一座现代地铁网：先给每个车站经纬度，后给站名，选定一种投影，写出绘制说明，让手握坐标表的读者都能重绘此图。
- Negative: `no placename without coordinates, no legendary places inside the coordinate grid, no narrative in place of a coordinate table, no hiding the source and error of coordinate data`
- 检验点：回答是否先给坐标后给名称、是否写清投影与重绘方法、是否标注数据来源与误差。
