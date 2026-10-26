# John Snow — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Snow, plot every case as a dot, let the dots cluster around one pump, and let the map do the arguing that words alone cannot`
- ZH: 斯诺风格：把每个病例画成一个点，让点群聚向一口水泵，让地图完成文字无法完成的论证。

## (2) 考察方法

- 田野方式：逐户调查与病例定位：走访霍乱病例住址，核对取水水泵；以地图检验水源假说。 `artifact`
- 证据偏好：病例住址与取水记录为主，辅以水泵位置实测；几乎不用无住址依据的病例上图。 `artifact`
- 尺度偏好：街区尺度：以宽街一带为单元，点群密度即论证。 `artifact`

## (3) 制图与空间表达

- 地图风格：病例点图：黑点为病例，水泵为标志；点群聚向水泵即结论。 `artifact`
- 空间表达：以点群组织图面：点是主语，聚集是论证，水泵是落点。 `artifact`
- 质感：图面极简，点与泵而已；文字报告附后，讲调查方法与例外病例。 `artifact`

## (4) 理论建构习惯

- 论述结构：先列病例表，再逐点上图，最后对照水泵：调查在前，图面在后。 `artifact`
- 核心概念：病例点图、点群聚集、水源假说、逐户调查、例外病例。概念之间以前一项为证据、后一项为落点衔接：从病例点图出发，经点群聚集、水源假说、逐户调查，落在例外病例。 `artifact`
- 论证落点：结论落在点群上：病例聚向宽街水泵，移开泵把手后病例下降。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是病例分布的格局；聚集不是巧合，是水源的证据。 `artifact`
- 时间观：疫情时间：病例按发病先后上图，时间以点的累积表达。 `artifact`
- 人地关系：人水关系：水源是传播路径，环境以取水行为与人连接。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 病例住址的逐点定位
- 点群向水泵的聚集
- 例外病例的如实标注
- 逐户调查的方法说明
- 不该研究：
- 无住址依据的病例上图
- 为求聚集删掉例外病例
- 把点图写成已证明病原
- 无调查依据的传播断言
- Negative prompt: `no case plotted without an address, no outlier deleted to sharpen the cluster, no presenting the dot map as proof of the germ itself, no transmission claim without house-to-house evidence`

## (7) 测试提示词示例（现代题材：一张外卖骑手聚集的城市点图）

- Prompt: `In the style of John Snow, plot every late-night delivery order as a dot, let the dots cluster around one dark kitchen, and mark the exceptions honestly so the map argues rather than asserts.`
- 中文对照：斯诺风格：把每个深夜外卖订单画成一个点，让点群聚向一家暗厨，并如实标注例外订单，让地图论证而非断言。
- Negative: `no case plotted without an address, no outlier deleted to sharpen the cluster, no presenting the dot map as proof of the germ itself, no transmission claim without house-to-house evidence`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在点群上：病例聚向宽街水泵，移开泵、是否出现 Negative prompt 禁止的套路。
