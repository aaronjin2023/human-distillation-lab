# Olivier Messiaen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Messiaen style, modes of limited transposition, non-retrogradable rhythm, birdsong transcription, luminous chord colour, time suspended, Catholic mysticism in sound`
- ZH: 梅西安风格，有限移位调式，不可逆行节奏，鸟鸣记谱，明亮的和弦色彩，时间悬置，声音中的天主教神秘主义。

## (2) 音高与和声方向

- 主：有限移位调式（七种对称调式）、平行和弦、泛音式和声；调性悬置、色彩即和声；禁：功能和声的属—主解决。`artifact`

## (3) 旋律与节奏

- 旋律：鸟鸣记谱的短小片段、有机碎片重组；节奏：不可逆行节奏（回文）、附加值节奏、印度节奏；织体：各声部独立线条叠置。`artifact`

## (4) 配器与音色

- 管弦乐色彩极丰：钢琴、马特诺电波琴（《图兰加利拉》）、打击乐群、木管鸟鸣；力度从极弱到辉煌的全幅度。`artifact`

## (5) 曲式与结构

- 曲式：多乐章组曲、交响曲十乐章；结构：调式与节奏的循环即结构，高潮靠色彩叠加，结尾常归于光亮的静止。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：有限移位调式、鸟鸣片段、不可逆行节奏、平行和弦、色彩叠加、时间悬置。
- 不该写：见 Negative prompt。
- Negative prompt: `functional cadence, Germanic motivic development, regular metre, sentimental melody, dense Romantic swell`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Olivier Messiaen, a 30-second piece for a rainy bus stop at dusk in a modern city, Messiaen style, modes of limited transposition, non-retrogradable rhythm, birdsong transcription, luminous chord colour, time suspended, Catholic mysticism in sound`
- 中文对照：梅西安风格，为现代城市黄昏雨中的公交站写一段 30 秒配乐，梅西安风格，有限移位调式，不可逆行节奏，鸟鸣记谱，明亮的和弦色彩，时间悬置，声音中的天主教神秘主义。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
