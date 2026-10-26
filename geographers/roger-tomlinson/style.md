# Roger Tomlinson — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roger Tomlinson, start from a planning question the paper map cannot answer, build the system that can overlay, measure and retrieve, and let the inventory become the argument`
- ZH: 汤姆林森风格：从纸质地图答不了的规划问题出发，建一个能叠加、量测、检索的系统，让土地清查本身成为论证。

## (2) 考察方法

- 田野方式：系统建设：以加拿大土地清查为需求，设计数据分层、编码与检索；不依赖个人田野。 `artifact`
- 证据偏好：土地清查数据与系统运行记录为主；几乎不用未经编码的纸质图推断。 `artifact`
- 尺度偏好：国家尺度：以加拿大土地清查为单元，分层覆盖全国。 `artifact`

## (3) 制图与空间表达

- 地图风格：分层叠加：土地利用、土壤、林业、野生动物各成一层，叠加出规划答案。 `artifact`
- 空间表达：以图层组织论述：叠加是主语，量测是论证，检索是落点。 `artifact`
- 质感：文字为系统说明体：需求—设计—运行—应用；图为分层示意图。 `artifact`

## (4) 理论建构习惯

- 论述结构：先定规划问题，再设计系统，最后以应用收束：问题在前，系统在后。 `artifact`
- 核心概念：地理信息系统、加拿大土地清查、图层叠加、空间检索、土地适宜性。概念之间以前一项为证据、后一项为落点衔接：从地理信息系统出发，经加拿大土地清查、图层叠加、空间检索，落在土地适宜性。 `artifact`
- 论证落点：结论落在应用上：系统能否回答‘哪里适宜种什么、保什么’。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是可分层、可量测、可检索的数据；地图是数据库的视图。 `artifact`
- 时间观：共时为主：清查呈现当前土地状况，更新靠再调查。 `artifact`
- 人地关系：人地关系为规划关系：土地适宜性连接人与环境，以系统评价。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 加拿大土地清查的分层数据
- 图层叠加的规划应用
- 空间检索与量测功能
- 系统设计的需求说明
- 不该研究：
- 未经编码的纸质图推断
- 无规划问题的技术炫示
- 图层口径不一的叠加
- 把 GIS 写成单纯的绘图软件
- Negative prompt: `no inference from uncoded paper maps, no technical display without a planning question, no overlay of layers with mismatched definitions, no presenting GIS as mere drawing software`

## (7) 测试提示词示例（现代题材：一个外卖配送区的图层叠加系统）

- Prompt: `In the style of Roger Tomlinson, start from a planning question no paper map can answer — where should night depots go? — layer rider tracks, order density and road closures, and let the overlay answer.`
- 中文对照：汤姆林森风格：从纸质地图答不了的规划问题出发——夜间配送站该设在哪里？——叠加骑手轨迹、订单密度与封路信息，让叠加回答。
- Negative: `no inference from uncoded paper maps, no technical display without a planning question, no overlay of layers with mismatched definitions, no presenting GIS as mere drawing software`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在应用上：系统能否回答‘哪里适宜种、是否出现 Negative prompt 禁止的套路。
