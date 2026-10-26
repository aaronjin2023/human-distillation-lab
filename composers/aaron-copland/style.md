# Aaron Copland — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Open American sound, wide intervals, quartal harmony, folk-like diatonic melody, cowboy and Shaker tunes, clear rhythm, spacious orchestration`
- ZH: 开阔美国音响，宽音程，四度和声，民间式全音阶旋律，牛仔与震教徒曲调，清晰节奏，空旷配器。

## (2) 旋律与和声

- 旋律：宽音程跳进与级进交替，民间式简单线条；《阿巴拉契亚之春》引用震教徒曲调《简易赠礼》。`verbatim`
- 和声：四度叠置和弦，调性清晰；不协和短暂，解决明确。`artifact`

## (3) 节奏与织体

- 节奏：清晰节拍，牛仔舞曲律动；织体：主调为主，声部稀疏，留白多，空间感强。

## (4) 配器与音色

- 配器：铜管号角、木管歌唱、弦乐空旷；打击乐克制；室内乐版与管弦版并存。

## (5) 曲式与结构

- 曲式：芭蕾组曲、号角短曲；结构简洁，高潮在中后段，结尾明亮收束。

## (6) 该写什么 / 不该写什么

- 该写：宽音程民间旋律、四度和声、号角式铜管、空旷留白配器、牛仔与震教徒曲调、清晰舞曲节奏。
- 不该写：dense European counterpoint、no chromatic wandering、no sentimental swell、no thick orchestration filling every gap、no ironic distance。
- Negative prompt: `No dense European counterpoint, no chromatic wandering, no sentimental swell, no thick orchestration filling every gap, no ironic distance`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Aaron Copland, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, wide-interval folk-like melody, open quartal harmony, brass fanfare, spacious strings`
- 中文对照：科普兰风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，宽音程民间旋律，开阔四度和声，铜管号角，空旷弦乐。
- Negative: `No dense European counterpoint, no chromatic wandering, no sentimental swell, no thick orchestration filling every gap, no ironic distance`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
