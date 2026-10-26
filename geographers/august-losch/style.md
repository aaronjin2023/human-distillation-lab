# August Lösch — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of August Lösch, explain why delivery riders cluster at a new district's edge: build one rider's demand cone, add competing riders until market areas interlock, and read the resulting landscape as an equilibrium, not a plan.`
- ZH: 勒施风格，解释外卖骑手为何聚集在新城区边缘：先建一个骑手的需求锥，再不断加入竞争骑手直至市场区咬合，把形成的景观读作均衡结果而非规划图纸。

## (2) 考察方法

- 以一般均衡理论为骨架、统计资料为血肉：从单个厂商的需求锥出发，旋转成市场区，再让无数市场区叠加成经济景观；演绎为主，实证为辅。`artifact`

## (3) 制图与空间表达

- 需求锥与市场区叠加图：锥体旋转成圆、圆压成六边形网络；图是均衡推导的可视化，每张图对应一步均衡条件。`artifact`

## (4) 理论建构习惯

- 论述结构：从单个市场的需求锥起步，逐步加入竞争者、叠加市场区，最后推出整个经济景观的均衡；结论落在空间经济的一般均衡秩序，不落在单个城市。
- 核心概念：需求锥, 市场区网络, 经济景观, 利润最大化区位, 均衡的空间秩序。概念之间按上述结构衔接。`artifact`
- 论证落点：结论落在理论命题与可检验的判断上，视线落点在概念与案例的对照处。

## (5) 空间观与时间观

- 空间观：由无数市场区叠加而成的经济景观：空间是竞争均衡的结果，不是先验容器。
- 时间观：比较静态：比较不同均衡状态，过程与历史路径不在模型内。
- 人地关系：厂商与消费者按利润与效用选址定价，人地关系被抽象为需求与供给的空间分布。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 单个厂商的需求锥与市场区推导
- 市场区叠加成的经济景观
- 用均衡条件检验市场区边界
- 克里斯塔勒模型的利润假设修正
- 不该研究：
- 无需求数据的市场区断言
- 把经济景观当作真实行政区划
- 忽略竞争者进入对边界的影响
- 把比较静态说成历史过程
- Negative prompt: `no market-area claim without demand data, no reading the economic landscape as real administrative borders, no ignoring competitor entry at the boundary, no presenting comparative statics as a historical process`

## (7) 测试提示词示例（现代题材：新城区边缘的外卖骑手聚集）

- Prompt: `In the style of August Lösch, explain why delivery riders cluster at a new district's edge: build one rider's demand cone, add competing riders until market areas interlock, and read the resulting landscape as an equilibrium, not a plan.`
- 中文对照：勒施风格，解释外卖骑手为何聚集在新城区边缘：先建一个骑手的需求锥，再不断加入竞争骑手直至市场区咬合，把形成的景观读作均衡结果而非规划图纸。
- Negative: `no market-area claim without demand data, no reading the economic landscape as real administrative borders, no ignoring competitor entry at the boundary, no presenting comparative statics as a historical process`
- 检验点：回答是否用了该地理学家的方法与核心概念、是否落在可检验的判断上、是否出现 Negative prompt 禁止的套路。
