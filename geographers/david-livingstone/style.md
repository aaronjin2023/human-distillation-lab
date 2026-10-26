# David Livingstone — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Livingstone, walk the river to its source, record latitude, waterfall and village by village, and let the map argue that Africa is inhabited, traversable and knowable`
- ZH: 利文斯通风格：沿河走到源头，逐站记录纬度、瀑布与村落，让地图本身论证非洲是有人居住、可通行、可认识的。

## (2) 考察方法

- 田野方式：徒步与独木舟沿河考察，依赖向导与当地知识；以天文观测定经纬度。 `artifact`
- 证据偏好：实测经纬度与河道走向为主，辅以向导口述与传教站记录；几乎不用二手地图推测未到之地。 `artifact`
- 尺度偏好：区域尺度：以流域为单元（赞比西河流域、刚果河上游），再拼成非洲中南部的连通图。 `artifact`

## (3) 制图与空间表达

- 地图风格：考察路线图：河道为主线，瀑布、湖泊、村落与传教站为节点；手绘草图后由他人整理成出版地图。 `artifact`
- 空间表达：以河流为骨架组织论述：上游—中游—下游、瀑布为分段标志；分水岭是论证的关键证据。 `artifact`
- 质感：文字密度高，日记体与考察报告交错；地图附于书后，是论证的附录而非装饰。 `artifact`

## (4) 理论建构习惯

- 论述结构：按行程顺序叙事，再以流域综合收束：先走一段河，再论一段地理。 `artifact`
- 核心概念：流域、分水岭、瀑布与通航断点、传教站—商路网络、反奴隶贸易的地理论证。概念之间以前一项为证据、后一项为落点衔接：从流域出发，经分水岭、瀑布与通航断点、传教站—商路网络，落在反奴隶贸易的地理论证。 `artifact`
- 论证落点：结论落在地图与路线上：某河可通航到哪里、某湖与某河是否连通。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是可步行、可测量的连通网络，不是空白；河流是通道，不是边界。 `artifact`
- 时间观：线性行进的时间：考察按日推进，地理发现随行程展开。 `artifact`
- 人地关系：互动论偏向人地关联：环境设限（瀑布断航、疾病），人以商路与传教站回应。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 赞比西河与刚果河流域的河道走向
- 瀑布、湖泊与分水岭的位置关系
- 沿河村落、商路与传教站的分布
- 以实测经纬度定点的考察路线
- 不该研究：
- 未到之地的想象填图
- 无实测依据的河流连通推断
- 把探险写成征服叙事
- 脱离向导与当地知识的单人英雄叙事
- Negative prompt: `no filling unvisited land from imagination, no river connection claimed without measurement, no conquest narrative, no lone-hero account that erases guides and local knowledge`

## (7) 测试提示词示例（现代题材：一名外卖骑手夜晚沿河道骑行穿越城市）

- Prompt: `In the style of David Livingstone, follow a food-delivery rider along a city river at night, station by station: bridge, ferry point, dark bank, lit depot. Record each stop's position and what blocks passage, and let the route itself show which parts of the city are connected and which are cut off.`
- 中文对照：利文斯通风格，跟随一名外卖骑手夜晚沿城市河流骑行，逐站记录：桥、渡口、暗岸、亮着灯的配送站；记下每个节点的位置与通行障碍，让路线本身说明城市的哪些部分连通、哪些部分隔断。
- Negative: `no filling unvisited land from imagination, no river connection claimed without measurement, no conquest narrative, no lone-hero account that erases guides and local knowledge`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在地图与路线上：某河可通航到哪里、、是否出现 Negative prompt 禁止的套路。
