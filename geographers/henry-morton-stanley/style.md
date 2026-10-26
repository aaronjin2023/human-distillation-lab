# Henry Morton Stanley — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry Morton Stanley, march a large caravan across the map, fix each camp by latitude, and turn the route into a continuous measured line from coast to coast`
- ZH: 斯坦利风格：率大队商队横贯地图，每宿营地以纬度定位，把路线写成一条从海岸到海岸的连续实测线。

## (2) 考察方法

- 田野方式：大队商队纵贯考察，依赖大批挑夫与向导；以天文观测与行军日志定路线。 `artifact`
- 证据偏好：行军日志与天文测点为主，辅以沿途村落访谈；几乎不用未经行军验证的传闻定点。 `artifact`
- 尺度偏好：大陆尺度：横贯非洲中部，以刚果河为主轴拼合东西海岸。 `artifact`

## (3) 制图与空间表达

- 地图风格：纵贯路线图：营地序列为节点，刚果河为中轴；地图强调‘贯通’这一条线。 `artifact`
- 空间表达：以营地序列与行军日数组织论述：走了几天、到哪里、河向哪边流。 `artifact`
- 质感：文字密度极高，行军日志体；地图是路线的证据，置于书中核心位置。 `artifact`

## (4) 理论建构习惯

- 论述结构：按行程日数推进，再以全程总图收束：先走，再拼图。 `artifact`
- 核心概念：横贯路线、刚果河主轴、营地序列、行军日数、东西海岸贯通。概念之间以前一项为证据、后一项为落点衔接：从横贯路线出发，经刚果河主轴、营地序列、行军日数，落在东西海岸贯通。 `artifact`
- 论证落点：结论落在总图上：刚果河从哪里来、到哪里去，东西海岸是否贯通。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是待贯通的距离，河流是贯通的轴线；未知以行军填补。 `artifact`
- 时间观：线性行进时间：以行军日数计量空间距离。 `artifact`
- 人地关系：人地关系上重通道与补给：环境是行军障碍（瀑布、疾病、补给断点），以商队规模回应。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 刚果河主轴的实测走向
- 横贯路线的营地序列与行军日数
- 瀑布群与断航点的定位
- 东西海岸贯通的路线证据
- 不该研究：
- 未经行军验证的传闻定点
- 把商队暴力写成考察方法
- 无测点依据的支流走向
- 把贯通写成对当地社会的征服
- Negative prompt: `no locating places from unverified hearsay, no presenting caravan violence as method, no tributary drawn without a measured point, no presenting a traverse as conquest`

## (7) 测试提示词示例（现代题材：一名外卖骑手横贯一座新城区的夜晚）

- Prompt: `In the style of Henry Morton Stanley, send a delivery rider straight across a new urban district at night, camp by camp: depot, bridge, dark estate, bright hub. Fix each stop by time and distance, and let the continuous line prove which streets connect and where the route breaks.`
- 中文对照：斯坦利风格，让一名外卖骑手夜晚横贯一座新城区，逐站记录：配送站、桥、暗区住宅、亮着的枢纽；每站以时间与距离定位，让连续的线证明哪些街道连通、哪里断开。
- Negative: `no locating places from unverified hearsay, no presenting caravan violence as method, no tributary drawn without a measured point, no presenting a traverse as conquest`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在总图上：刚果河从哪里来、到哪里去、是否出现 Negative prompt 禁止的套路。
