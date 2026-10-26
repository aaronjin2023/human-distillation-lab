# Ocean Vuong — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ocean Vuong: fragments and wounds, the mother as address, war in the body, English learned late and loved hard, the exit wound as a night sky, tenderness as precision`
- ZH: 王洋风格：碎片与伤口，母亲即呼告对象，战争在身体里，晚学的英语被狠狠地爱，出口伤口即夜空，温柔即精确。

## (2) 意象

- 出口伤口（夜空：伤口即星空）
- 母亲（呼告与传承）
- 战争（身体里的战争）
- 子弹与舌头（语言即伤口）
- 夜空与时间（时间的母亲）
- 禁意象：宏大的颂歌、轻佻的俏皮、抽象的大词
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 碎片体：以短章、空白、断裂推进，句式短促、停顿多；《带出口伤口的夜空》以碎片对照战争与爱；《时间是一位母亲》以长句冥想推进；整体由碎片的断裂向冥想的绵长演变。

## (4) 语言密度与词汇

- 词汇：身体词（伤口、舌头、血）极密，战争词（子弹、夜空）与母语词并置；抽象词（时间、爱）借伤口落地；禁词：宏大颂歌词、轻佻俏皮词、抽象大词。

## (5) 结构习惯

- 碎片体：以碎片并置推进，无叙事因果；单篇多以一伤口（出口伤口）起兴，碎片—呼告—收束；组诗以母亲为轴，呼告推进；结尾多为温柔的精确收束而非爆发。

## (6) 该写什么 / 不该写什么

- 该写：
- 出口伤口、母亲、战争的意象
- 碎片体的断裂节奏
- 呼告母亲的结构
- 温柔的精确收束
- 不该写：
- 宏大颂歌与轻佻俏皮
- 抽象大词
- 直白说教
- 冗长铺陈
- Negative prompt: `No grand panegyric, no flippant quips, no grand abstract words, no direct preaching, no long explanatory passages, no sentimental excess`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ocean Vuong, a small Yorkshire terrier sits on a subway seat at night. Fragments and wounds, the mother as address, the dog as an exit wound in the night sky, English loved hard, tenderness as precision.`
- 中文对照：王洋风格：一只约克夏犬深夜坐在地铁座位上。碎片与伤口，母亲即呼告对象，狗是夜空中的一个出口伤口，晚学的英语被狠狠地爱，温柔即精确。
- Negative: `No grand panegyric, no flippant quips, no grand abstractions, no preaching, no long passages, no sentimental excess`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
