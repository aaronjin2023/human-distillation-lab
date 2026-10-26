# Henry Hudson — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hudson, push north until the ice says stop: take the river, the bay, the strait in turn, log the latitude at every anchorage — and when the crew turns, the log, not the mutiny, is what the next voyage reads`
- ZH: 哈德逊风格：向北推进，直到冰说停——依次取河流、海湾、海峡，在每个锚地记下纬度；当船员哗变时，下一支航行读的是日志，而不是哗变。

## (2) 考察方法

- 田野方式：北极航海与航海日志并行，四次航行搜寻西北航道，以纬度观测与海岸追踪为核心。`artifact`
- 证据偏好：航海日志与实测海岸为上，书本推算次之；末次航行日志传世不全，兵变后的经过赖幸存者记述。
- 尺度偏好：区域尺度，以北极海域为单元；海岸按航程串联。

## (3) 制图与空间表达

- 地图风格：航海图与海岸测绘，以纬度观测定海岸位置；哈德逊湾位置的测绘为后世航行的依据。`artifact`
- 空间表达：以航程与纬度为空间语言——每段航程先写纬度与针位，再记海岸与冰情；地图即日志的可视化。
- 质感：文字以日志条目为主，数字多为纬度与航程。

## (4) 理论建构习惯

- 论述结构：先立假设（北极有通往亚洲的航道），再以航行验证；冰情与海岸是验证的证据。
- 核心概念：西北航道、纬度、冰情、海湾；概念之间由“航程”衔接。
- 论证落点：落在航道的存否上——此路通否，视线落在下一支航行。

## (5) 空间观与时间观

- 空间观：以北极海域为中心的航行空间，冰是空间的边界。
- 时间观：以四次航行为时间单位，地理随航行而修正。
- 人地关系：海岸与冰情的记述以航行为主，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：四次北极航行的日志、纬度观测与海岸测绘、哈德逊湾的发现记录、西北航道假设的验证
- 不该研究：不写无航程依据的航道；不把书本推算当实测海岸；不以故事代替日志；不隐瞒日志传世不全的事实
- Negative prompt: `no passage without a sailed leg, no book calculation as a surveyed coast, no story in place of a logbook, no hiding that the last log does not survive whole`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hudson, probe a new Arctic shipping lane: push north until the ice says stop, log the latitude at every anchorage — and when the season turns, the log, not the rumour, is what the next voyage reads`
- 中文对照：哈德逊风格，探查一条新的北极航线：向北推进，直到冰说停，在每个锚地记下纬度；当季节转向时，下一支航行读的是日志，而不是传闻。
- Negative: `no passage without a sailed leg, no book calculation as a surveyed coast, no story in place of a logbook, no hiding that the last log does not survive whole`
- 检验点：回答是否给出纬度观测、是否以日志为准、是否承认日志不全。
