# Waldo Tobler — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Waldo Tobler, turn the map into a computation: near things matter more than distant things, interpolate the surface between measured points, and let the algorithm show the pattern the eye alone misses`
- ZH: 托布勒风格：把地图变成计算——近处比远处更相关，在测点之间插值出曲面，让算法呈现肉眼看漏的格局。

## (2) 考察方法

- 田野方式：案头计算制图：汇集城市增长、人口与测点数据，以计算机模拟与插值成图。 `artifact`
- 证据偏好：测点数据与计算模型为主；几乎不用未经计算的示意草图。 `artifact`
- 尺度偏好：城市与区域尺度：以底特律城市增长为案例，方法可推及他处。 `artifact`

## (3) 制图与空间表达

- 地图风格：计算地图：插值曲面、计算机模拟图；地图是计算结果的可视化。 `artifact`
- 空间表达：以距离衰减组织论述：近—远是主语，插值是论证。 `artifact`
- 质感：文字为模型说明体：假设—算法—结果—检验；图为模拟输出。 `artifact`

## (4) 理论建构习惯

- 论述结构：先定空间关系假设，再建计算模型，最后以模拟图收束：假设在前，计算在后。 `artifact`
- 核心概念：地理学第一定律、距离衰减、空间插值、城市增长模拟、地图投影变换。概念之间以前一项为证据、后一项为落点衔接：从地理学第一定律出发，经距离衰减、空间插值、城市增长模拟，落在地图投影变换。 `artifact`
- 论证落点：结论落在模拟图上：城市增长的格局是否如模型所示。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是距离加权的关系场；近处关联强，远处关联弱。 `artifact`
- 时间观：模拟时间：城市增长按时间步推进，图呈现过程。 `artifact`
- 人地关系：人地关系为模型关系：人口与城市增长以空间关系建模。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 地理学第一定律的距离表述
- 测点之间的空间插值
- 底特律城市增长的计算机模拟
- 地图投影的计算变换
- 不该研究：
- 无测点依据的插值曲面
- 把第一定律写成物理定律
- 未经检验的模拟结论
- 把计算地图写成示意图
- Negative prompt: `no interpolated surface without measured points, no presenting the First Law as a law of physics, no simulation conclusion without a test, no presenting a computed map as a sketch`

## (7) 测试提示词示例（现代题材：一张外卖订单密度的插值图）

- Prompt: `In the style of Waldo Tobler, interpolate a surface of delivery-order density between measured blocks, let near blocks weigh more than distant ones, and test whether the computed pattern matches the riders' night.`
- 中文对照：托布勒风格：在实测街区之间插值出外卖订单密度曲面，让近处街区权重高于远处，再检验计算格局是否符合骑手的夜晚。
- Negative: `no interpolated surface without measured points, no presenting the First Law as a law of physics, no simulation conclusion without a test, no presenting a computed map as a sketch`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在模拟图上：城市增长的格局是否如模、是否出现 Negative prompt 禁止的套路。
