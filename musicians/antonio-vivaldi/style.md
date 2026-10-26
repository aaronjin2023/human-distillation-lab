# Antonio Vivaldi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Italian Baroque, ritornello concerto, vivid pictorial writing, driving rhythm, brilliant violin figuration, clear tonality and motoric energy`
- ZH: 意大利巴洛克，利都奈罗协奏曲，生动的描绘性写作，驱动性节奏，辉煌小提琴音型，清晰调性与动力能量。

## (2) 音高与和声方向

- 主：利都奈罗（ritornello）与独奏段交替；功能和声清晰；模进转调。禁：半音化滥用、复调的失控堆砌。调性：调性稳定，转调靠模进。

## (3) 旋律与节奏

- 旋律：小提琴音型辉煌、重复性强；描绘性动机（如鸟鸣、雷雨）直接可辨。节奏：驱动性强，重复音型、切分。织体：独奏与全奏对比；复调少，主调为主。

## (4) 配器与音色

- 乐器：小提琴独奏、弦乐队、通奏低音；《四季》用弦乐描绘自然。音色：明亮、辉煌。力度：独奏—全奏对比强烈。

## (5) 曲式与结构

- 曲式：独奏协奏曲（三乐章快—慢—快）、大协奏曲、歌剧、圣咏。结构：利都奈罗—独奏段交替；高潮在独奏华彩与全奏齐奏处。结尾：明确收束。

## (6) 该写什么 / 不该写什么

- 该写：利都奈罗协奏曲、描绘性音型、驱动节奏、小提琴辉煌、清晰调性。
- 不该写：半音化滥用、复调的失控堆砌、模糊调性、沉闷慢速。
- Negative prompt: `aimless chromaticism, uncontrolled dense counterpoint, vague tonality, sluggish tempo, heavy orchestration`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Antonio Vivaldi, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Italian Baroque ritornello concerto, vivid pictorial writing, driving rhythm, brilliant violin figuration, clear tonality, bright and energetic`
- 中文对照：维瓦尔第风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，意大利巴洛克利都奈罗协奏曲，生动描绘，驱动节奏，辉煌小提琴音型，清晰调性，明亮有力。
- Negative: `aimless chromaticism, uncontrolled dense counterpoint, vague tonality, sluggish tempo, heavy orchestration`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
