# Grażyna Bacewicz — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Neoclassical string virtuosity, Polish folk rhythm, clear form, brilliant violin writing, later sonorist colour, rhythmic drive`
- ZH: 新古典主义弦乐炫技，波兰民间节奏，清晰曲式，辉煌小提琴写法，晚期音色主义色彩，节奏驱动。

## (2) 旋律与和声

- 旋律：小提琴式级进与跳进，民间舞曲轮廓；主题短小、富于发展。`artifact`
- 和声：新古典调性为底，半音点缀；晚期音色主义，和声靠音色块移动。`artifact`

## (3) 节奏与织体

- 节奏：民间舞曲切分，动感强；织体：弦乐多声部，密度可高可低。

## (4) 配器与音色

- 配器：弦乐为主，铜管与打击乐点缀；小提琴独奏与弦乐队对答；晚期加入音色实验。

## (5) 曲式与结构

- 曲式：协奏曲、交响曲、弦乐四重奏；三乐章居多，高潮在中后段，结尾有力收束。

## (6) 该写什么 / 不该写什么

- 该写：弦乐炫技写法、波兰民间舞曲节奏、新古典清晰曲式、小提琴独奏与乐队对答、晚期音色块。
- 不该写：vague impressionist wash、no endless chromatic wandering、no sentimental swell without rhythmic drive、no dense counterpoint obscuring the violin line、no soft-focus strings。
- Negative prompt: `No vague impressionist wash, no endless chromatic wandering, no sentimental swell without rhythmic drive, no dense counterpoint obscuring the violin line, no soft-focus strings`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Grażyna Bacewicz, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, brilliant violin line, Polish dance rhythm, clear concerto form, strings and brass accents`
- 中文对照：巴采维奇风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，辉煌小提琴线条，波兰舞曲节奏，清晰协奏曲式，弦乐与铜管点缀。
- Negative: `No vague impressionist wash, no endless chromatic wandering, no sentimental swell without rhythmic drive, no dense counterpoint obscuring the violin line, no soft-focus strings`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
