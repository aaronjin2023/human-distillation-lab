# Karlheinz Stockhausen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Serialism extended to all parameters, electronic music, spatialisation, moment form, formula composition, vast cyclic opera`
- ZH: 序列主义扩展到全部参数，电子音乐，空间化，瞬间曲式，程式作曲，宏大循环歌剧。

## (2) 旋律与和声

- 旋律：序列派生的音高，程式旋律在《光》中反复变形；声乐线条非歌唱式。`artifact`
- 和声：序列组织音高，无调性；电子音色即和声。`artifact`

## (3) 节奏与织体

- 节奏：序列组织时值；瞬间曲式中时间可静止可流动；织体：多声道空间分布，声部在空间中移动。

## (4) 配器与音色

- 配器：电子、磁带、管弦三组乐队空间分布；《光》七部歌剧循环，每日一部。

## (5) 曲式与结构

- 曲式：瞬间曲式、程式曲式、循环歌剧；无传统高潮弧线，结构靠程式与空间。

## (6) 该写什么 / 不该写什么

- 该写：全参数序列、电子音色、空间化布局、瞬间曲式、程式旋律变形、循环歌剧结构。
- 不该写：functional harmony、no lyrical melody、no traditional form、no single climax arc、no fixed stereo soundstage、no sentimental swell。
- Negative prompt: `No functional harmony, no lyrical melody, no traditional form, no single climax arc, no fixed stereo soundstage, no sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Karlheinz Stockhausen, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, serial pitches, electronic shimmer, sounds moving in space, moment form`
- 中文对照：施托克豪森风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，序列音高，电子闪烁，声音在空间中移动，瞬间曲式。
- Negative: `No functional harmony, no lyrical melody, no traditional form, no single climax arc, no fixed stereo soundstage, no sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
