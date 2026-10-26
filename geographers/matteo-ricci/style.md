# Matteo Ricci — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Matteo Ricci, draw the world so two map traditions can meet on one sheet: European projection and latitude beside Chinese place names, with the Pacific at the centre`
- ZH: 利玛窦风格：在一张图上让两种制图传统相遇——欧洲投影与纬度配中国地名，太平洋居中。

## (2) 考察方法

- 田野方式：编译与访谈式制图：汇集欧洲地图与中国方志、地名资料，核对译名。 `artifact`
- 证据偏好：已刊欧洲地图与中国文献并重；几乎不用未经核对的传闻地名上图。 `artifact`
- 尺度偏好：世界尺度：以五大洲为单元，中国地名密度高于其他区域。 `artifact`

## (3) 制图与空间表达

- 地图风格：世界地图：椭圆投影框架，太平洋居中；图例与地名双语对照。 `artifact`
- 空间表达：以大洲分区组织图面：欧洲、亚细亚、非洲、美洲，辅以海洋与岛屿。 `artifact`
- 质感：图面文字密度高，地名与注记并列；地图独立成图，附说明文字。 `artifact`

## (4) 理论建构习惯

- 论述结构：先定投影与中心，再分区填地名，最后加注记与图例。 `artifact`
- 核心概念：世界地图、椭圆投影、太平洋居中、中西地名对照、五大洲分区。概念之间以前一项为证据、后一项为落点衔接：从世界地图出发，经椭圆投影、太平洋居中、中西地名对照，落在五大洲分区。 `artifact`
- 论证落点：结论落在图上：世界可在一张图上完整呈现，且中国地名可与欧洲地图对接。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是可拼接的世界：不同传统的地图可以在同一投影下对齐。 `artifact`
- 时间观：共时呈现：一张图同时呈现各洲，不按历史先后排列。 `artifact`
- 人地关系：人地关系淡：地图重地名与疆界，少论环境决定。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 世界地图的投影框架
- 中西地名对照的注记
- 五大洲分区的图面组织
- 太平洋居中的构图选择
- 不该研究：
- 未经核对的传闻地名上图
- 无投影依据的示意草图
- 只抄欧洲地图不补中国地名
- 把地图写成传教叙事
- Negative prompt: `no unvetted hearsay place names on the map, no sketch without a projection, no copying European maps without adding Chinese names, no turning the map into a missionary narrative`

## (7) 测试提示词示例（现代题材：一张外卖骑手活动范围的城市地图）

- Prompt: `In the style of Matteo Ricci, draw one map where two traditions meet: the riders' delivery zones beside the official street grid, with the night market at the centre. Let place names from both sides sit on the same projection so the map can be read either way.`
- 中文对照：利玛窦风格，画一张让两种传统相遇的地图：骑手配送区配官方街道网格，夜市居中；让两边的地名落在同一投影上，双向可读。
- Negative: `no unvetted hearsay place names on the map, no sketch without a projection, no copying European maps without adding Chinese names, no turning the map into a missionary narrative`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在图上：世界可在一张图上完整呈现，、是否出现 Negative prompt 禁止的套路。
