# Charles Joseph Minard — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Joseph Minard, let one line carry the whole argument: width for numbers, colour for direction, and place the graph on the map so the disaster can be read at a glance`
- ZH: 米纳德风格：让一条线承担全部论证——线宽表数量、颜色表方向，把统计图画在地图上，让灾难一眼可读。

## (2) 考察方法

- 田野方式：案头统计制图：汇集行军、人口与贸易统计，核对数字来源；不依赖个人田野。 `artifact`
- 证据偏好：官方统计与行军记录为主；几乎不用无来源的数字上图。 `artifact`
- 尺度偏好：国家与洲尺度：以行军路线或贸易流为单元，图上同时呈现空间与数量。 `artifact`

## (3) 制图与空间表达

- 地图风格：专题流量图：线宽表数量，颜色表去向与回程；地图是统计图的底图。 `artifact`
- 空间表达：以流量组织图面：线是主语，宽窄是论证，颜色是方向。 `artifact`
- 质感：图面简洁，数字注记克制；图表即论证，文字说明附后。 `artifact`

## (4) 理论建构习惯

- 论述结构：先列数字表，再定流量线，最后落图：统计在前，图面在后。 `artifact`
- 核心概念：流量图、线宽表数量、去程与回程、统计图形、图上叙事。概念之间以前一项为证据、后一项为落点衔接：从流量图出发，经线宽表数量、去程与回程、统计图形，落在图上叙事。 `artifact`
- 论证落点：结论落在图上：线的收窄与颜色的转折，就是行军溃败的证据。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是流量经过的距离；地图是统计图的坐标，不是风景。 `artifact`
- 时间观：行程时间：去程与回程在同一图上对照，时间以线的位置表达。 `artifact`
- 人地关系：人地关系淡：图重数量与路线，少论环境决定；严寒以温度曲线附图呈现。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 流量线的宽度与数量对应
- 去程与回程的颜色区分
- 温度曲线的附图对照
- 统计来源的注记
- 不该研究：
- 线宽与数量不对应的示意图
- 无来源的数字上图
- 为求美观加装饰性线条
- 把流量图写成战争叙事
- Negative prompt: `no flow line whose width does not match its number, no number without a stated source, no decorative line added for beauty, no turning the flow map into a war narrative`

## (7) 测试提示词示例（现代题材：一张外卖骑手夜晚流量图）

- Prompt: `In the style of Charles Joseph Minard, draw one flow map of delivery riders crossing a city at night: line width for order numbers, colour for outward and return journeys, and a temperature curve below so the thinning line itself tells the story.`
- 中文对照：米纳德风格：画一张外卖骑手夜晚流量图——线宽表订单数、颜色表去程与回程，下附温度曲线，让线的收窄本身讲故事。
- Negative: `no flow line whose width does not match its number, no number without a stated source, no decorative line added for beauty, no turning the flow map into a war narrative`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在图上：线的收窄与颜色的转折，就是、是否出现 Negative prompt 禁止的套路。
