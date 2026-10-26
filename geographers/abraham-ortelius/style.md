# Abraham Ortelius — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abraham Ortelius, gather the best maps of every region, give each its source, and bind them into one theatre of the world that can be revised map by map`
- ZH: 奥特柳斯风格：汇集各地最好的地图，每图注明来源，装订成一部可以逐图修订的世界剧场。

## (2) 考察方法

- 田野方式：案头编纂：收集各国地图师的成图，核对来源与版本；不依赖个人远航。 `artifact`
- 证据偏好：已刊地图与地图师名录为主；几乎不用无来源的地图入集。 `artifact`
- 尺度偏好：世界尺度：以洲为单元分图，再以总图收束。 `artifact`

## (3) 制图与空间表达

- 地图风格：地图集：统一图幅与风格，分洲成图；每图注明来源地图师。 `artifact`
- 空间表达：以洲分区组织全集：总图在前，分洲图在后，古今对照附后。 `artifact`
- 质感：图面统一，注记注明来源；文字说明附于图后，讲每图的来历。 `artifact`

## (4) 理论建构习惯

- 论述结构：先定总图，再分洲编图，最后附古代地理对照：编纂在前，考证在后。 `artifact`
- 核心概念：地图集、世界概观、来源注记、分洲成图、逐版修订。概念之间以前一项为证据、后一项为落点衔接：从地图集出发，经世界概观、来源注记、分洲成图，落在逐版修订。 `artifact`
- 论证落点：结论落在全集上：世界可由各地最好的地图拼成，且每图可溯源、可修订。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是可编纂的世界：各地地图在统一图幅下对齐。 `artifact`
- 时间观：共时为主，古今对照为辅：今图在前，古图附后。 `artifact`
- 人地关系：人地关系淡：地图集重疆界与地名，少论环境决定。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 地图集的分洲组织
- 每图的来源注记
- 统一图幅的编纂体例
- 逐版修订的更新方式
- 不该研究：
- 无来源的地图入集
- 来源不明的地名上图
- 为求全收录劣质地图
- 把地图集写成个人游记
- Negative prompt: `no map without a named source, no place name from an unnamed source, no inferior map included merely to fill the atlas, no turning the atlas into a personal travelogue`

## (7) 测试提示词示例（现代题材：一本外卖配送区的地图集）

- Prompt: `In the style of Abraham Ortelius, gather the best delivery-zone map for every district, name the source of each, and bind them into one atlas that can be revised zone by zone.`
- 中文对照：奥特柳斯风格：汇集每个片区最好的配送地图，每图注明来源，装订成一部可以逐区修订的地图集。
- Negative: `no map without a named source, no place name from an unnamed source, no inferior map included merely to fill the atlas, no turning the atlas into a personal travelogue`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在全集上：世界可由各地最好的地图拼、是否出现 Negative prompt 禁止的套路。
