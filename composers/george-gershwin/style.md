# George Gershwin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz harmony in classical form, blues melody, syncopation, brilliant piano and orchestration, song and symphonic scale together`
- ZH: 古典曲式中的爵士和声，蓝调旋律，切分，辉煌钢琴与配器，歌曲与交响规模并存。

## (2) 旋律与和声

- 旋律：蓝调式歌唱线条，级进与跳进交替；主题鲜明、易记。`artifact`
- 和声：蓝调和声与扩展和弦，调性清晰；不协和作色彩，解决明确。`artifact`

## (3) 节奏与织体

- 节奏：切分与摇摆，动感强；织体：主调为主，钢琴与乐队对答。

## (4) 配器与音色

- 配器：钢琴独奏、管弦、爵士乐队色彩；单簧管滑音开场为《蓝色狂想曲》标志。`verbatim`

## (5) 曲式与结构

- 曲式：狂想曲、歌剧、交响诗；结构自由而清晰，高潮明亮，结尾有力收束。

## (6) 该写什么 / 不该写什么

- 该写：蓝调旋律、切分节奏、爵士和声、钢琴与乐队对答、单簧管滑音、歌曲与交响并存。
- 不该写：atonal wandering、no dense counterpoint obscuring the tune、no sentimental swell without syncopation、no thin chamber texture as the main sound、no classical form without jazz colour。
- Negative prompt: `No atonal wandering, no dense counterpoint obscuring the tune, no sentimental swell without syncopation, no thin chamber texture as the main sound, no classical form without jazz colour`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of George Gershwin, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, blues melody, syncopation, brilliant piano, clarinet glissando colour, bright orchestration`
- 中文对照：格什温风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，蓝调旋律，切分，辉煌钢琴，单簧管滑音色彩，明亮配器。
- Negative: `No atonal wandering, no dense counterpoint obscuring the tune, no sentimental swell without syncopation, no thin chamber texture as the main sound, no classical form without jazz colour`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
