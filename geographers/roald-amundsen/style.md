# Roald Amundsen — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roald Amundsen, plan the polar route like a supply problem: depots first, dogs and skis second, and let the measured line to the Pole be the argument`
- ZH: 阿蒙森风格：把极地路线当作补给问题来规划——先布补给点，再谈狗与滑雪板，让通往极点的实测线本身成为论证。

## (2) 考察方法

- 田野方式：极地滑雪与狗拉雪橇考察，依赖因纽特式装备与补给点预布；以天文观测定极点位置。 `artifact`
- 证据偏好：补给点记录、天文测点与行军日志为主；几乎不用未经验证的极地传闻。 `artifact`
- 尺度偏好：极地尺度：以补给线为单元，论证从海岸到极点的可达性。 `artifact`

## (3) 制图与空间表达

- 地图风格：极地路线图：补给点序列为节点，极点为终点；地图强调补给线的完整。 `artifact`
- 空间表达：以补给点序列组织论述：每站存了什么、走了几天、剩多少路。 `artifact`
- 质感：文字简洁，日志体；数字密集（里程、天数、补给量）；地图附于书后。 `artifact`

## (4) 理论建构习惯

- 论述结构：按补给点顺序推进，再以极点测点收束：先布点，再走线。 `artifact`
- 核心概念：补给点、狗拉雪橇、滑雪行军、极点测点、西北航道。概念之间以前一项为证据、后一项为落点衔接：从补给点出发，经狗拉雪橇、滑雪行军、极点测点，落在西北航道。 `artifact`
- 论证落点：结论落在测点上：极点位置的天文观测数据与返程的补给余量。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是补给线覆盖的距离；极点是一个可测量的点，不是象征。 `artifact`
- 时间观：线性行进时间：以行军日数与补给消耗计量。 `artifact`
- 人地关系：环境是极限约束（严寒、暴风、补给断点），以预布补给与轻装回应。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 极地补给点的序列与存量
- 狗拉雪橇行军的日数与里程
- 极点位置的天文测点
- 西北航道的实测航线
- 不该研究：
- 无补给依据的极地冒进叙事
- 未经测点的极点宣称
- 把装备细节写成英雄修辞
- 无日志依据的行军速度
- Negative prompt: `no polar dash without depot evidence, no Pole claimed without an observed fix, no equipment detail turned into hero rhetoric, no marching speed without a log entry`

## (7) 测试提示词示例（现代题材：一名外卖骑手在暴雪夜穿越城市）

- Prompt: `In the style of Roald Amundsen, plan a delivery rider's crossing of a snowbound city like a supply problem: depots first, route second. Fix each depot's stock and each leg's time, and let the measured line prove the crossing is possible.`
- 中文对照：阿蒙森风格，把一名外卖骑手暴雪夜穿越城市当作补给问题来规划——先布补给点，再谈路线；每站记存量、每段记时间，让实测线证明穿越可行。
- Negative: `no polar dash without depot evidence, no Pole claimed without an observed fix, no equipment detail turned into hero rhetoric, no marching speed without a log entry`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在测点上：极点位置的天文观测数据与、是否出现 Negative prompt 禁止的套路。
