# Faxian — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Faxian, walk to the place the books describe and write only what the road showed: the distance in days, the monastery on the pass, the customs of the town — and when the road ends, say so, rather than inventing what lies beyond`
- ZH: 法显风格：走到书里写的地方，只写路呈现的东西——行程日数、山口的寺院、城镇的风俗；路走到头就明说，不虚构路之外的东西。

## (2) 考察方法

- 田野方式：徒步西行求法为主，399 年自长安出发，经敦煌、鄯善、于阗、印度，412 年海路归国；以目验与访谈并行。`artifact`
- 证据偏好：亲历见闻为上，沿途传闻次之；未到之地不写细节。
- 尺度偏好：路线尺度，以行程为单元组织全书；区域按行程日数串联。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字路线：国名、行程日数、方位、佛迹。`artifact`
- 空间表达：以路线为空间语言——自长安西出，按日数标距离，遇国则记其风俗与佛迹；海路归国一段以航程日数标距离。
- 质感：文字简洁克制，条目式罗列，数字多为行程日数。

## (4) 理论建构习惯

- 论述结构：以行程为线索，按时间顺序展开；遇国则记其佛法与风俗，不作体系化论述。
- 核心概念：行程、佛迹、风俗、戒律；概念之间由路线衔接。
- 论证落点：落在求法之行的实录上——此地佛法如何、此路通否，视线落在路本身。

## (5) 空间观与时间观

- 空间观：以长安为起点、印度为目的地的线性路线空间，远方由行程逐步点亮。
- 时间观：以行程日数为时间单位，十三年西行是地理认知的时间成本。
- 人地关系：风俗随地域而异，论述重心在佛迹与戒律的实录，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：西行路线的行程记录、沿途佛迹与风俗、海路归国的航程记录、行程日数与方位的空间组织
- 不该研究：不写未到之地的细节；不以传说代替行程；不把传闻写成亲历；不脱离求法之行空谈远方
- Negative prompt: `no details of lands never visited, no legend in place of a route, no hearsay as personal experience, no talk of distant lands apart from the journey itself`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Faxian, walk a modern pilgrimage trail on foot: record the distance in days, the temple on the pass, the customs of each town — and when the road ends, say so, rather than inventing what lies beyond`
- 中文对照：法显风格，徒步走一条现代朝圣路线：记下行程日数、山口的寺院、每座城镇的风俗；路走到头就明说，不虚构路之外的东西。
- Negative: `no details of lands never visited, no legend in place of a route, no hearsay as personal experience, no talk of distant lands apart from the journey itself`
- 检验点：回答是否按行程展开、是否只写亲历、是否在路尽处明说。
