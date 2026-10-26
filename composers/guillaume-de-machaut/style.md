# Guillaume de Machaut — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Ars nova polyphony, isorhythm, intricate talea and color, modal counterpoint, secular chanson and sacred Mass in equal measure, elegant French courtly lines`
- ZH: 新艺术复调，等节奏，繁复的泰利亚与科洛尔，调式对位，世俗香颂与宗教弥撒并重，优雅的法国宫廷线条。

## (2) 旋律与和声

- 旋律：三声部各成线条，tenor 多取定旋律（cantus firmus），上声部装饰性强，线条优雅而克制。`artifact` 和声：调式和声，不协和音按规则解决，终止靠半音导引（musica ficta）收束；禁用现代功能和声。调性：调式稳定，等节奏结构提供统一感。

## (3) 节奏与织体

- 节奏：等节奏（isorhythm）为核心技术：tenor 的节奏型（talea）与旋律型（color）循环错位；上声部节奏自由灵动。织体：三—四声部复调，声部密度中等，节奏层叠是主要张力来源。

## (4) 配器与音色

- 配器与音色：人声为主，偶有乐器参与世俗曲；音色清亮、克制；力度变化小，靠声部进入与节奏错位制造起伏；无现代管弦乐色彩。

## (5) 曲式与结构

- 曲式：弥撒曲各乐章统一于同一等节奏骨架；香颂用固定曲式（回旋歌、叙事歌、维勒莱）；回文卡农《我的终结即我的开端》以镜像结构组织全曲。结构：循环—变奏，结尾常以全声部收束。

## (6) 该写什么 / 不该写什么

- 该写：等节奏（isorhythm）结构、定旋律（cantus firmus）作骨架、固定曲式香颂（回旋歌、维勒莱）、弥撒曲的乐章统一、回文与镜像声部游戏。
- 不该写：功能和声与属—主进行、自由无调性、管弦乐式配器、短促流行乐句、无结构的即兴堆砌。
- Negative prompt: `No functional harmony, no dominant-tonic cadence, no free atonality, no orchestral scoring, no pop phrasing, no unstructured improvisation`

## (7) 测试提示词示例（现代题材：现代城市深夜的一家便利店）

- Prompt: `In the style of Guillaume de Machaut, a 30-second piece for a quiet convenience store at night in a modern city, ars nova polyphony, isorhythm, intricate talea and color, modal counterpoint, secular chanson and sacred mass in equal measure, elegant french courtly lines`
- 中文对照：纪尧姆·德·马肖风格，为现代城市深夜的一家便利店写 30 秒配乐，新艺术复调，等节奏，繁复的泰利亚与科洛尔，调式对位，世俗香颂与宗教弥撒并重，优雅的法国宫廷线条。
- Negative: `No functional harmony, no dominant-tonic cadence, no free atonality, no orchestral scoring, no pop phrasing, no unstructured improvisation`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
