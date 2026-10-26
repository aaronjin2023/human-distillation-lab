# Olivier Messiaen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Modes of limited transposition, birdsong transcription, non-retrogradable rhythms, luminous Catholic colour, ondes Martenot and vast orchestral colour`
- ZH: 有限移位调式，鸟鸣转录，不可逆节奏，天主教明亮色彩，马特诺琴与宏大管弦色彩。

## (2) 旋律与和声

- 旋律：鸟鸣式短小音型，音程跳跃大；调式旋律长线与鸟鸣碎片并置。`artifact`
- 和声：有限移位调式，和弦色彩浓烈；调性游移，解决靠色彩而非功能。`artifact`

## (3) 节奏与织体

- 节奏：不可逆节奏、附加值节奏、印度节奏；自由与严格并存；织体：多层节奏并置，密度可极高也可极稀疏。

## (4) 配器与音色

- 配器：马特诺琴、钢琴、打击乐、庞大管弦；鸟鸣由木管与钢琴模仿；音色明亮、泛音丰富。

## (5) 曲式与结构

- 曲式：多乐章组曲、交响曲；结构常按数字与对称组织；高潮宏大而明亮，结尾常以光亮收束。

## (6) 该写什么 / 不该写什么

- 该写：有限移位调式、鸟鸣转录音型、不可逆节奏、马特诺琴音色、多层节奏并置、明亮宏大高潮。
- 不该写：functional harmony as structure、no Germanic motivic development、no regular metre throughout、no muted grey orchestration、no ironic distance。
- Negative prompt: `No functional harmony as structure, no Germanic motivic development, no regular metre throughout, no muted grey orchestration, no ironic distance`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Olivier Messiaen, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, birdsong-like motifs, modes of limited transposition, luminous piano and woodwinds`
- 中文对照：梅西安风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，鸟鸣式动机，有限移位调式，明亮钢琴与木管。
- Negative: `No functional harmony as structure, no Germanic motivic development, no regular metre throughout, no muted grey orchestration, no ironic distance`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
