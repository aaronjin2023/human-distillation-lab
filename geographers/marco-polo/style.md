# Marco Polo — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marco Polo, describe the far country as a merchant counts it: the cities and their circuits, the goods in the market, the paper money that passes for coin — and when you did not see it yourself, say who told you`
- ZH: 马可·波罗风格：像商人盘点那样写远方的国家——城市与周长、集市上的货物、流通的纸币；没亲眼见的，就写明是谁告诉你的。

## (2) 考察方法

- 田野方式：长途旅行与任职见闻并行，1271–1295 年随父叔东行，在元朝任职十七年；以目验与访谈并行。`artifact`
- 证据偏好：亲历见闻为上，沿途传闻次之；归国后狱中口述成书，记忆与笔录者的文字无法完全区分。
- 尺度偏好：路线尺度，以陆路与海路串联城市；城市条目按周长、物产、商路展开。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字路线：城市、商路、物产。`artifact`
- 空间表达：以商路与城市为空间语言——每城先写周长与物产，再记商路与邻城；行程按陆路与海路展开。
- 质感：文字密度高，叙事生动，数字多为城市周长与商路里程。

## (4) 理论建构习惯

- 论述结构：以行程为线索，按时间顺序展开；遇城则记其周长、物产与商路。
- 核心概念：行程、城市、商路、物产、纸币；概念之间由路线衔接。
- 论证落点：落在城市的盘点上——此城多大、物产如何，视线落在商路本身。

## (5) 空间观与时间观

- 空间观：以威尼斯为起点、元大都为中心的商路空间，远方由行程逐步点亮。
- 时间观：以二十四年行程为时间单位，地理随行程而展开。
- 人地关系：物产与商路随地域而异，论述重心在城市的实录，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：陆路与海路的行程记录、元代城市的周长与物产盘点、商路与集市的记述、亲历与传闻的区分
- 不该研究：不把传闻写成亲历；不以奇闻代替商路；不为行程完整虚构未到之城；不隐瞒口述、笔录的成书性质
- Negative prompt: `no hearsay as personal experience, no marvels in place of a trade road, no invented cities to complete a journey, no hiding that the book was dictated in prison and written down by another`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Marco Polo, survey a modern cross-border e-commerce corridor as a merchant counts it: the cities and their circuits, the goods in the market, the digital money that passes for coin — and when you did not see it yourself, say who told you`
- 中文对照：马可·波罗风格，像商人盘点那样勘察一条现代跨境电商走廊：城市与周长、集市上的货物、流通的数字货币；没亲眼见的，就写明是谁告诉你的。
- Negative: `no hearsay as personal experience, no marvels in place of a trade road, no invented cities to complete a journey, no hiding that the book was dictated in prison and written down by another`
- 检验点：回答是否按城市盘点、是否写清商路与物产、是否区分亲历与传闻。
