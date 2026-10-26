# Joe Hisaishi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Film score composition, simple singable melodies, pentatonic colour, minimalist piano, warm orchestral swells, Japanese lyricism`
- ZH: 电影配乐作曲，简单可唱的旋律，五声音阶色彩，极简钢琴，温暖的管弦涌动，日本抒情性。

## (2) 旋律与和声

- 旋律：五声音阶级进长线，音域适中，呼吸均匀，歌唱性极强，动机简短、重复中微变。
- 和声：大调—小调功能和声加五声音阶色彩；主：大调、五声调式；禁：密集半音与无调性；不协和度低，解决温和。

## (3) 节奏与织体

- 节奏：平稳、歌谣化，常用三拍与自由呼吸；织体：钢琴独奏或弦乐主调，密度低到中，留白温和。

## (4) 配器与音色

- 配器：钢琴、弦乐、木管、轻打击；音色：温暖、透明、带水汽感；力度：中弱到中强，极少极端。

## (5) 曲式与结构

- 曲式：歌曲式 AABA 与主题变奏；结构：主题—轻变奏—再现；高潮在主题最后一次温暖涌起；结尾常渐弱、留有余温。

## (6) 该写什么 / 不该写什么

- 该写：五声音阶歌谣旋律、极简钢琴与弦乐、温暖的主题再现、克制的情感涌动。
- 不该写：密集半音和声、连续高潮、铜管号角主导、无旋律的氛围铺底。
- Negative prompt: `No dense chromatic harmony, no continuous climax, no brass-fanfare dominance, no melody-free ambient wash, no loud sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Joe Hisaishi, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a simple pentatonic melody, minimalist piano, warm strings, gentle and nostalgic`
- 中文对照：久石让风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，简单五声旋律，极简钢琴，温暖弦乐，温柔怀旧。。
- Negative: `No dense chromatic harmony, no continuous climax, no brass-fanfare dominance, no melody-free ambient wash, no loud sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
