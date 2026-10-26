# Gerardus Mercator — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gerardus Mercator, choose the projection first and let it decide the map: rhumb lines straight, angles true, and every place name placed only where the mathematics puts it`
- ZH: 墨卡托风格：先定投影，让投影决定地图——等角航线成直线，角度保真，每个地名只落在数学算出的位置上。

## (2) 考察方法

- 田野方式：案头制图：汇集航海图、旅行记录与已刊地图，核对坐标；不依赖个人远航。 `artifact`
- 证据偏好：航海图与坐标记录为主，辅以旅行记述；几乎不用无坐标依据的地名上图。 `artifact`
- 尺度偏好：世界尺度：以投影数学统一全球，再分区制图。 `artifact`

## (3) 制图与空间表达

- 地图风格：投影地图：墨卡托投影，等角，纬线间距随纬度拉伸；图例与比例尺严谨。 `artifact`
- 空间表达：以投影与经纬网组织图面：经纬线是骨架，地名是填充。 `artifact`
- 质感：图面严谨，注记克制；地图集按洲分册，文字说明附后。 `artifact`

## (4) 理论建构习惯

- 论述结构：先论投影，再分区制图，最后汇编成集：数学在前，地名在后。 `artifact`
- 核心概念：墨卡托投影、等角航线、经纬网、地图集、航海图。概念之间以前一项为证据、后一项为落点衔接：从墨卡托投影出发，经等角航线、经纬网、地图集，落在航海图。 `artifact`
- 论证落点：结论落在投影上：等角性质使航海直线导航成为可能。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是数学网格：经纬网先于地名存在，地图是投影的展开。 `artifact`
- 时间观：共时呈现：一张图同时呈现全球，不按历史先后排列。 `artifact`
- 人地关系：人地关系淡：地图重数学与航海实用，少论环境决定。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 墨卡托投影的数学依据
- 等角航线的直线表达
- 经纬网的图面骨架
- 地图集的分洲组织
- 不该研究：
- 无投影依据的示意草图
- 无坐标依据的地名上图
- 为图面美观牺牲角度保真
- 把地图集写成旅行叙事
- Negative prompt: `no sketch without a projection, no place name without a coordinate, no sacrificing angle fidelity for a prettier sheet, no turning the atlas into a travel narrative`

## (7) 测试提示词示例（现代题材：一张外卖骑手导航用的城市网格地图）

- Prompt: `In the style of Gerardus Mercator, choose the projection first: draw a city grid where delivery routes run straight, angles stay true at every turn, and each restaurant and block sits only where the grid puts it.`
- 中文对照：墨卡托风格：先定投影——画一张骑手导航用的城市网格图，配送路线成直线，每个路口角度保真，每家餐馆与街区只落在网格算出的位置上。
- Negative: `no sketch without a projection, no place name without a coordinate, no sacrificing angle fidelity for a prettier sheet, no turning the atlas into a travel narrative`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在投影上：等角性质使航海直线导航成、是否出现 Negative prompt 禁止的套路。
