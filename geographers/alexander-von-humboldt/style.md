# Alexander von Humboldt — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alexander von Humboldt, measure everything on the mountain and connect it all: altitude, temperature, plants and people in one profile, and let the whole of nature argue against any single cause`
- ZH: 洪堡风格：在山上测量一切并把一切连起来——海拔、气温、植物与人画进同一剖面，让自然的整体反对任何单一原因。

## (2) 考察方法

- 田野方式：科学考察：南美安第斯山实测海拔、气温、气压与植物分布；仪器测量为主。 `artifact`
- 证据偏好：仪器实测数据为主，辅以标本与文献；几乎不用未经测量的推测。 `artifact`
- 尺度偏好：全球尺度：以山地剖面为单元，再推及全球植被带。 `artifact`

## (3) 制图与空间表达

- 地图风格：剖面图与等值线：植被垂直带谱为代表作；地图是测量的可视化。 `artifact`
- 空间表达：以剖面组织论述：海拔是主语，温度与植被随海拔变。 `artifact`
- 质感：文字宏大，数据密集；图表并重，剖面图置于论述核心。 `artifact`

## (4) 理论建构习惯

- 论述结构：先实测，再比较，最后综合成宇宙：测量在前，综合在后。 `artifact`
- 核心概念：自然整体、植被垂直带、等温线、比较地理、宇宙。概念之间以前一项为证据、后一项为落点衔接：从自然整体出发，经植被垂直带、等温线、比较地理，落在宇宙。 `artifact`
- 论证落点：结论落在综合上：自然是一个相互关联的整体，不是孤立事实的堆积。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是相互关联的整体；地方是全球关系的一个节点。 `artifact`
- 时间观：共时为主：剖面呈现同一时刻的垂直关联，历史为背景。 `artifact`
- 人地关系：互动论：环境设限，人以种植与聚落回应；反对单一环境决定。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 山地剖面的实测数据
- 植被垂直带的比较
- 等温线的全球对照
- 自然整体的综合论述
- 不该研究：
- 未经测量的推测
- 单一原因解释复杂现象
- 孤立事实的罗列
- 把综合写成神秘主义
- Negative prompt: `no claim without a measurement, no single cause for a complex pattern, no list of isolated facts without connection, no presenting synthesis as mysticism`

## (7) 测试提示词示例（现代题材：一座新城区的垂直剖面）

- Prompt: `In the style of Alexander von Humboldt, measure a new urban district as one profile: height, temperature, greenery and people together, and let the whole argue against any single cause for how the district lives.`
- 中文对照：洪堡风格：把一座新城区测成一幅剖面——高度、气温、绿化与人同在一图，让整体反对任何单一原因解释这座城区的活法。
- Negative: `no claim without a measurement, no single cause for a complex pattern, no list of isolated facts without connection, no presenting synthesis as mysticism`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在综合上：自然是一个相互关联的整体、是否出现 Negative prompt 禁止的套路。
