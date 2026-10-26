# Walter Christaller — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Walter Christaller, analyse a new district's shops and clinics: rank its centres by function and threshold population, draw nested hexagonal market areas, and test whether a missing middle-order centre explains the travel burden.`
- ZH: 克里斯塔勒风格，分析一座新城区的商铺与诊所：按职能与门槛人口给中心地分级，画出嵌套的六边形市场区，检验缺失的中级中心是否解释了居民的出行负担。

## (2) 考察方法

- 以德国南部城镇的实地调查与统计资料为底，用几何演绎建模型：先数城镇的职能与服务范围，再把圆形市场区压成六边形，推出等级嵌套。调查与演绎各半。`artifact`

## (3) 制图与空间表达

- 六边形市场区图是核心表达：不同等级中心地嵌套，K=3 为市场原则、K=4 为交通原则、K=7 为行政原则；图例即理论。`artifact`

## (4) 理论建构习惯

- 论述结构：从中心地职能的实证分类出发，推导市场区几何，再分三原则展开等级体系，最后以德国南部案例验证；结论落在城镇体系的一般等级规律。
- 核心概念：中心地, 中心性, 服务范围, 门槛人口, 六边形市场区, K 值体系。概念之间按上述结构衔接。`artifact`
- 论证落点：结论落在理论命题与可检验的判断上，视线落点在概念与案例的对照处。

## (5) 空间观与时间观

- 空间观：均质平原上的等级空间：空间是层层嵌套的市场区，中心性决定等级。
- 时间观：静态均衡：等级体系被当作稳定结构，历史变迁只在验证章出现。
- 人地关系：供给与需求决定的人地关系：居民为最近的中心服务而移动，环境只以均质平原进入假设。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 城镇职能与服务范围的等级分类
- 六边形市场区的嵌套与 K 值推导
- 用门槛人口检验一个中心地能否存在
- 中心地等级与交通、行政原则的对照
- 不该研究：
- 无职能数据的城镇等级断言
- 把六边形当作真实地图照抄
- 忽略交通原则与市场原则的区分
- 把静态等级体系说成历史必然
- Negative prompt: `no ranking towns without functional data, no copying the hexagon as a real map, no confusing the marketing, transport and administrative principles, no presenting a static hierarchy as historical necessity`

## (7) 测试提示词示例（现代题材：一座新城区的商铺与诊所等级）

- Prompt: `In the style of Walter Christaller, analyse a new district's shops and clinics: rank its centres by function and threshold population, draw nested hexagonal market areas, and test whether a missing middle-order centre explains the travel burden.`
- 中文对照：克里斯塔勒风格，分析一座新城区的商铺与诊所：按职能与门槛人口给中心地分级，画出嵌套的六边形市场区，检验缺失的中级中心是否解释了居民的出行负担。
- Negative: `no ranking towns without functional data, no copying the hexagon as a real map, no confusing the marketing, no transport and administrative principles, no presenting a static hierarchy as historical necessity`
- 检验点：回答是否用了该地理学家的方法与核心概念、是否落在可检验的判断上、是否出现 Negative prompt 禁止的套路。
