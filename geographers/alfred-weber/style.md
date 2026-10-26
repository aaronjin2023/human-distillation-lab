# Alfred Weber — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Weber, site a new battery gigafactory: draw the location triangle of lithium source, component supplier and market, find the least-transport point, then test labour-cost deviation and agglomeration pull before fixing the site.`
- ZH: 韦伯风格，为一家新建电池超级工厂选址：画出锂矿、零部件供应商与市场的区位三角形，找出最小运费点，再检验劳动力成本偏离与集聚拉力，然后才定址。

## (2) 考察方法

- 以抽象模型与算例推演为主：先设均质平原与单一原料产地，再算运费、劳动力与集聚三股力量的合力落点；几乎不做田野调查，证据是统计表与成本算例。`artifact`

## (3) 制图与空间表达

- 区位三角形、等运费线与成本等值线图；图是论证本身，不是插图：三角形三个顶点为原料地与市场，落点即最小运费点。`artifact`

## (4) 理论建构习惯

- 论述结构：从孤立假设出发，先立最小运费模型，再逐项引入劳动力偏离与集聚偏离，最后讨论现实修正；结论落在区位选择的一般规律，不落在具体城市个案。
- 核心概念：最小运费点, 区位三角形, 集聚因素, 分散因素, 劳动力成本偏离。概念之间按上述结构衔接。`artifact`
- 论证落点：结论落在理论命题与可检验的判断上，视线落点在概念与案例的对照处。

## (5) 空间观与时间观

- 空间观：绝对空间中的成本空间：距离即运费，空间是可计算的均质平面。
- 时间观：静态比较：不同区位方案的成本比较，无历史演进维度。
- 人地关系：经济人假设下的人地关系：人按成本最小化选址，自然只以原料产地与运费进入模型。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 工业选址的运费—劳动力—集聚三角
- 单一产品、单一工厂的最小成本点
- 用等值线比较不同区位的成本差异
- 集聚收益与分散成本的权衡
- 不该研究：
- 无成本数据的印象式选址判断
- 把区位决定归于文化或政治偏好
- 无均质假设说明的模型外推
- 把最小运费点说成唯一最优解
- Negative prompt: `no siting judgement without cost data, no explaining location by culture or politics alone, no model extrapolation without stating the isotropic-plane assumption, no presenting the least-transport point as the only optimum`

## (7) 测试提示词示例（现代题材：一座新城区的电池工厂选址）

- Prompt: `In the style of Alfred Weber, site a new battery gigafactory: draw the location triangle of lithium source, component supplier and market, find the least-transport point, then test labour-cost deviation and agglomeration pull before fixing the site.`
- 中文对照：韦伯风格，为一家新建电池超级工厂选址：画出锂矿、零部件供应商与市场的区位三角形，找出最小运费点，再检验劳动力成本偏离与集聚拉力，然后才定址。
- Negative: `no siting judgement without cost data, no explaining location by culture or politics alone, no model extrapolation without stating the isotropic-plane assumption, no presenting the least-transport point as the only optimum`
- 检验点：回答是否用了该地理学家的方法与核心概念、是否落在可检验的判断上、是否出现 Negative prompt 禁止的套路。
