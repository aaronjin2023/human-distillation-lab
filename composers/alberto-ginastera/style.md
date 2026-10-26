# Alberto Ginastera — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Argentine composition, gaucho folk rhythm, malambo ostinato, twelve-tone later period, percussive piano and orchestral drive`
- ZH: 阿根廷作曲，高乔民间律动，马兰博固定音型，晚期十二音，打击性钢琴与管弦驱动。

## (2) 旋律与和声

- 旋律：阿根廷民间歌谣轮廓，跳进与切分并存，动机短小、节奏感强。
- 和声：早期民间调式，中期半音化，晚期十二音；主：调式与十二音分期；禁：无；不协和度由低到高，解决视时期而定。

## (3) 节奏与织体

- 节奏：马兰博固定音型与 6/8 律动，强劲、顿挫；织体：打击性织体，密度中高，留白靠重音停顿。

## (4) 配器与音色

- 配器：管弦乐、钢琴、打击；音色：粗粝、带土地感；力度：动态宽，重音突出。

## (5) 曲式与结构

- 曲式：芭蕾组曲、协奏曲、变奏曲；结构：民间主题—变奏—再现；高潮在打击最密处；结尾常以重音收束。

## (6) 该写什么 / 不该写什么

- 该写：马兰博固定音型、高乔民间旋律、打击性钢琴、民间主题的变奏发展。
- 不该写：无民间根源的抽象十二音、平滑的欧洲浪漫和声、无律动的抒情、单声部民歌照搬。
- Negative prompt: `No rootless abstract twelve-tone writing, no smooth European Romantic harmony, no lyricism without rhythm, no bare folk-song quotation, no atonal wandering without folk pulse`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alberto Ginastera, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a malambo ostinato, gaucho folk melody, percussive piano, driving orchestral rhythm`
- 中文对照：希纳斯特拉风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，马兰博固定音型，高乔民间旋律，打击性钢琴，驱动型管弦律动。。
- Negative: `No rootless abstract twelve-tone writing, no smooth European Romantic harmony, no lyricism without rhythm, no bare folk-song quotation, no atonal wandering without folk pulse`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
