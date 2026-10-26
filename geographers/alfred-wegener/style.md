# Alfred Wegener — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Wegener, fit the coasts together and follow the clues across the ocean: fossils, rocks and climates that only make sense if the continents once moved`
- ZH: 魏格纳风格：把海岸线拼合起来，追踪越洋的线索——化石、岩石与气候，只有大陆曾经移动才能解释它们。

## (2) 考察方法

- 田野方式：以跨学科证据汇编为田野：海岸线拼合、化石分布、古气候证据、地质构造对比；最依赖多学科证据的汇合。
- 证据偏好：多学科证据并重：古生物、地质、古气候、大地测量；几乎不用单一学科的孤证，结论必多线汇合。
- 尺度偏好：以全球为基本尺度，论证下至具体海岸与化石点；尺度转换靠“拼合”——地方证据叠加即全球漂移。

## (3) 制图与空间表达

- 古地理复原图为主：盘古大陆拼合图、化石分布图、古气候带图；符号是复原与推测，须标明证据等级；地图是假说的可视化。

## (4) 理论建构习惯

- 论述结构：海岸拼合 → 化石与地质证据 → 古气候证据 → 漂移假说 → 机制难题的坦白。核心概念：大陆漂移、盘古大陆、化石证据、古气候、漂移机制。概念衔接：拼合提问题，化石与地质给证据，古气候给佐证，机制留作难题。论证落点：理论命题——大陆漂移说，机制未解。

## (5) 空间观与时间观

- 空间观：移动空间——大陆不是固定容器，是会移动的板块前身。时间观：地质时间——以亿年计的漂移。人地关系：不直接论人地，只论地球演化。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 海岸线拼合的证据
- 跨洋化石与地质对比
- 古气候带的复原
- 多学科证据的汇合论证
- 不该研究：no drift claim from a single fossil, no hiding the missing mechanism, no presenting a reconstruction as an observation, no dismissing contrary evidence without answering it
- Negative prompt: `no drift claim from a single fossil, no hiding the missing mechanism, no presenting a reconstruction as an observation, no dismissing contrary evidence without answering it`

## (7) 测试提示词示例（现代题材：一座位于断层带上的新城，它的地质证据说明了怎样的移动史与地震风险？）

- Prompt: `In the style of Alfred Wegener, judge a new city's earthquake risk: fit the coasts, follow the fossils and rocks across the fault, and say what the moving ground implies`
- 中文对照：魏格纳风格，判断一座新城的地震风险：拼合海岸、追踪断层两侧的化石与岩石，说出移动的大地意味着什么。
- Negative: `no drift claim from a single fossil, no hiding the missing mechanism, no presenting a reconstruction as an observation, no dismissing contrary evidence without answering it`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
