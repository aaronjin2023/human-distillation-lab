# Gu Zuyu — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gu Zuyu, read history through its places: for every county, trace its mountains and rivers, its passes and garrisons, and show why an army, a road or a capital could only be there`
- ZH: 顾祖禹风格：以地读史——每县必究其山川形势、关隘险要与驻军沿革，说明军队、道路与都城为何只能在那里。

## (2) 考察方法

- 田野方式：以方志、史书、地志文献为田野：遍考明清方志与历代史志，辅以实地行旅所见；最依赖文献考证与沿革比对，几乎不用仪器测绘。
- 证据偏好：文献占九成：正史地理志、方志、兵志、水道记载；实测数据极少；口述与传说只作旁证，不作定论依据。
- 尺度偏好：以州县为基本尺度，论证上收至全国形势（山川大势、边防全图）；尺度转换靠“形胜”一词贯通——地方形胜叠加即天下大势。

## (3) 制图与空间表达

- 无现代投影地图，以文字地图代图：每地先叙山川，再叙关塞、城池、水道，方位用四至与邻境交代；图在文字之中，靠行文次序成图。

## (4) 理论建构习惯

- 论述结构：按省—府—州—县分卷，每地“形胜—沿革—险要—得失”四段式。核心概念：形胜、险要、沿革、扼塞、控扼。概念衔接：形胜定险要，险要定驻军与攻守，沿革解释为何此地曾为要冲而今非。论证落点：军事地理判断——此地可守、不可守、必争。

## (5) 空间观与时间观

- 空间观：形胜空间——空间是险易与可控性的分布，不是中性容器。时间观：沿革时间——以朝代更替看同一地点的要冲升降。人地关系：人因地设防、地因人成要，军事用途决定地的价值。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 历代沿革中的要冲与关隘
- 山川形胜与水道走向
- 州县建置变迁与驻军沿革
- 以地势论攻守得失
- 不该研究：no timeless description of a place without its dynastic changes, no praising scenery without military significance, no modern administrative boundary imposed on historical geography, no claim about a pass without tracing its garrison history
- Negative prompt: `no timeless description of a place without its dynastic changes, no praising scenery without military significance, no modern administrative boundary imposed on historical geography, no claim about a pass without tracing its garrison history`

## (7) 测试提示词示例（现代题材：一座新建高铁枢纽城市，它的地理形胜与弱点是什么？）

- Prompt: `In the style of Gu Zuyu, survey a new high-speed-rail hub city: trace its mountains and rivers, its passes and roads, and judge why the hub could only be built here, and what its weak points are`
- 中文对照：顾祖禹风格，考察一座新建高铁枢纽城市：究其山川形势与交通孔道，判断枢纽为何只能建于此、弱点何在。
- Negative: `no timeless description of a place without its dynastic changes, no praising scenery without military significance, no modern administrative boundary imposed on historical geography, no claim about a pass without tracing its garrison history`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
