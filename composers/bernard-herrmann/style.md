# Bernard Herrmann — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Film score composition, short obsessive ostinatos, string-only shrieks, unresolved dissonance, psychological tension without resolution`
- ZH: 电影配乐作曲，短小执拗的固定音型，纯弦乐尖啸，不解决的不协和，心理张力而不解决。

## (2) 旋律与和声

- 旋律：短小、重复、半音化的动机，音域窄，呼吸急促，歌唱性让位于执拗感。
- 和声：半音化与不协和堆积，功能和声被悬置；主：半音化小调；禁：属—主强解决；不协和度高，解决被延迟或取消。

## (3) 节奏与织体

- 节奏：固定音型驱动，急促、机械；织体：弦乐齐奏与分部对位，密度中高，留白极少、压迫感强。

## (4) 配器与音色

- 配器：弦乐为主，间或铜管与打击；音色：尖锐、冷、带金属感；力度：突强与极弱交替，动态突变。

## (5) 曲式与结构

- 曲式：固定音型变奏与主题碎片拼贴；结构：动机重复中微变；高潮在不协和最密处；结尾常悬置、不解决。

## (6) 该写什么 / 不该写什么

- 该写：短小半音固定音型、纯弦乐尖啸、不解决的不协和、心理张力的持续累积。
- 不该写：抒情长线条、属—主强解决、温暖的管弦全奏、主题的完整再现。
- Negative prompt: `No lyrical long lines, no strong dominant-tonic resolution, no warm orchestral tutti, no complete thematic reprise, no comforting consonance`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Bernard Herrmann, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a short obsessive string ostinato, unresolved dissonance, sharp stabs, psychological tension`
- 中文对照：赫尔曼风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，短小执拗的弦乐固定音型，不解决的不协和，尖锐顿挫，心理张力。。
- Negative: `No lyrical long lines, no strong dominant-tonic resolution, no warm orchestral tutti, no complete thematic reprise, no comforting consonance`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
