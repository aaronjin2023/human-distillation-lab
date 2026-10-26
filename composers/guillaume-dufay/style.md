# Guillaume Dufay — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Early Renaissance polyphony, cantus-firmus Mass, sweet thirds and sixths, clear imitation, fauxbourdon, Burgundian court elegance, sacred and secular balance`
- ZH: 文艺复兴早期复调，定旋律弥撒，甜美的三、六度和声，清晰模仿，福布尔东，勃艮第宫廷优雅，圣俗并重。

## (2) 旋律与和声

- 旋律：四声部线条流畅，级进为主，三、六度平行使和声甜美；上声部歌唱性强。`artifact` 和声：以三度、六度为协和骨架，属—主功能尚未成型，终止靠旋律收束与半音导引；禁用现代功能和声大面积使用。调性：调式稳定，定旋律提供统一。

## (3) 节奏与织体

- 节奏：节奏平稳，偶有切分点缀；声部进入以模仿为主，错落有致。织体：四声部复调，密度均匀；福布尔东段落作和声加厚，留白靠声部减至二声部。

## (4) 配器与音色

- 配器与音色：人声为主，宫廷场合可配乐器；音色温暖、明亮；力度靠声部增减，动态范围适中；空间感来自教堂与宫廷厅堂的共鸣。

## (5) 曲式与结构

- 曲式：定旋律弥撒五乐章统一于同一 cantus firmus；经文歌以仪式场合结构；香颂用固定曲式。结构：动机—模仿—再现，高潮在 Gloria 与 Credo 的全声部段落；结尾庄重收束。

## (6) 该写什么 / 不该写什么

- 该写：定旋律弥撒（cantus firmus）、三、六度和声与福布尔东、清晰的声部模仿、世俗旋律作弥撒骨架、经文歌的仪式结构。
- 不该写：现代功能和声、无调性与随意半音、管弦乐式配器、密集不协和、短促流行乐句。
- Negative prompt: `No modern functional harmony, no free atonality, no random chromaticism, no orchestral scoring, no dense dissonance, no pop phrasing`

## (7) 测试提示词示例（现代题材：清晨窗台上的一杯咖啡）

- Prompt: `In the style of Guillaume Dufay, a 30-second piece for a cup of coffee on a windowsill in the morning light, early renaissance polyphony, cantus-firmus mass, sweet thirds and sixths, clear imitation, fauxbourdon, burgundian court elegance, sacred and secular balance`
- 中文对照：纪尧姆·迪费风格，为清晨窗台上的一杯咖啡写 30 秒配乐，文艺复兴早期复调，定旋律弥撒，甜美的三、六度和声，清晰模仿，福布尔东，勃艮第宫廷优雅，圣俗并重。
- Negative: `No modern functional harmony, no free atonality, no random chromaticism, no orchestral scoring, no dense dissonance, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
