# Xuanzang — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xuanzang, record each kingdom as a complete entry: its circuit in li, its customs, its monasteries, its neighbours — and where the road was measured by a companion's step, say whose step it was`
- ZH: 玄奘风格：把每个国家写成一条完整的条目——周几里、风俗、寺院、邻国；哪段路是同伴的步子量的，就写明是谁的步子。

## (2) 考察方法

- 田野方式：徒步西行求法为主，629 年自长安出发，经西域、中亚至印度那烂陀，645 年归国；以目验与访谈并行，归国后口述成书。`artifact`
- 证据偏好：亲历见闻为上，沿途传闻与前人记载次之；一百三十八国的条目各有来源，闻见分明。
- 尺度偏好：区域尺度，以西域诸国为单元，按行程串联；印度各国条目最详。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字条目：国名、周里、方位、邻国、佛迹。`artifact`
- 空间表达：以国家条目为空间语言——每国先定周里与方位，再记风俗与寺院；条目之间以行程衔接。
- 质感：文字密度高，条目体，数字多为周里与行程。

## (4) 理论建构习惯

- 论述结构：以行程为线索，按国家分条；每条内部按“方位—周里—风俗—寺院—邻国”的固定顺序展开。
- 核心概念：国、周里、风俗、寺院、邻国；概念之间由行程衔接。
- 论证落点：落在各国的完整条目上——此国何在、风俗如何，视线落在条目本身。

## (5) 空间观与时间观

- 空间观：以长安为起点、印度为中心的条目拼合空间，远方由一百三十八个条目点亮。
- 时间观：以行程为时间单位，十六年西行是地理认知的时间成本。
- 人地关系：风俗随地域而异，论述重心在各国的实录，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：西域诸国的条目式记录、周里与方位的核对、佛迹与风俗的实录、行程与邻国关系的串联
- 不该研究：不写未到之国的细节；不把传闻写成亲历；不以传说代替条目；不脱离行程空谈远方
- Negative prompt: `no details of kingdoms never visited, no hearsay as personal experience, no legend in place of an entry, no talk of distant lands apart from the journey itself`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Xuanzang, survey a modern cross-border rail corridor country by country: each entry gives its circuit, its customs, its stations and its neighbours — and where the distance was measured by a companion's step, say whose step it was`
- 中文对照：玄奘风格，逐国勘察一条现代跨境铁路走廊：每国一条完整条目——周里、风俗、车站、邻国；哪段距离是同伴的步子量的，就写明是谁的步子。
- Negative: `no details of kingdoms never visited, no hearsay as personal experience, no legend in place of an entry, no talk of distant lands apart from the journey itself`
- 检验点：回答是否按国家分条、是否给出周里与方位、是否区分亲历与传闻。
