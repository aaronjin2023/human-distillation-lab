# Anton Webern — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Webern style, extreme brevity, pointillist texture, twelve-tone row, silence as structure, pianissimo, Klangfarbenmelodie, crystalline counterpoint`
- ZH: 韦伯恩风格，极度简短，点描织体，十二音音列，静默即结构，极弱，音色旋律，水晶般对位。

## (2) 音高与和声方向

- 主：十二音音列、对称音程（对称的音列结构）、高度不协和但极克制；无调性中心；禁：功能和声的回归与浪漫主义和声填充。`artifact`

## (3) 旋律与节奏

- 旋律：极短动机、单音成句、音程跳进大、音域宽；节奏：静默与单音等重，休止是结构；织体：点描式，单音在不同乐器间跳跃。`artifact`

## (4) 配器与音色

- 小型编制、室内乐与管弦乐小品；音色：极弱、泛音、拨奏、弱音器；力度多在 ppp–mp 之间，突强极少。`artifact`

## (5) 曲式与结构

- 曲式：极短小品、卡农与对称结构；结构：音列的对称性即曲式，全曲常不足十分钟，高潮靠密度而非音量，结尾常归于静默。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：极短小品、点描织体、音列对称、静默结构、极弱音色。
- 不该写：见 Negative prompt。
- Negative prompt: `long melody, loud climax, dense orchestration, tonal cadence, Romantic expression, filler notes`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Anton Webern, a 30-second piece for a cup of coffee left on a windowsill in the morning light, Webern style, extreme brevity, pointillist texture, twelve-tone row, silence as structure, pianissimo, Klangfarbenmelodie, crystalline counterpoint`
- 中文对照：韦伯恩风格，为一杯放在窗台上的咖啡写一段 30 秒配乐，韦伯恩风格，极度简短，点描织体，十二音音列，静默即结构，极弱，音色旋律，水晶般对位。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
