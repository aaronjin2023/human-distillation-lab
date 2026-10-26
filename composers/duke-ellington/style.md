# Duke Ellington — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Big-band orchestration, muted brass colour, blues harmony, sophisticated melody, swing rhythm, extended suite form, individual soloists as colours`
- ZH: 大乐队配器，弱音铜管音色，蓝调和声，精致旋律，摇摆节奏，扩展组曲曲式，独奏者作音色。

## (2) 旋律与和声

- 旋律：蓝调式级进与跳进，歌唱性强；主题短小、富于即兴展开。`artifact`
- 和声：蓝调和声与扩展和弦，调性清晰；不协和作色彩，解决温和。`artifact`

## (3) 节奏与织体

- 节奏：摇摆节奏，切分；织体：大乐队多声部，独奏与合奏交替。

## (4) 配器与音色

- 配器：大乐队（萨克斯、铜管、节奏组），弱音器铜管音色独特；独奏者音色即配器。

## (5) 曲式与结构

- 曲式：歌曲、组曲；《黑、棕与米色》为扩展组曲；高潮在独奏与合奏交替中，结尾明亮收束。

## (6) 该写什么 / 不该写什么

- 该写：弱音铜管音色、蓝调和声、摇摆节奏、大乐队配器、独奏者音色、扩展组曲。
- 不该写：classical sonata form imposed、no atonal wandering、no thin small-combo sound as the main colour、no sentimental pop swell、no free improvisation without a written theme。
- Negative prompt: `No classical sonata form imposed, no atonal wandering, no thin small-combo sound as the main colour, no sentimental pop swell, no free improvisation without a written theme`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Duke Ellington, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, muted brass colour, blues harmony, sophisticated melody, swing rhythm, big-band warmth`
- 中文对照：艾灵顿风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，弱音铜管音色，蓝调和声，精致旋律，摇摆节奏，大乐队温暖感。
- Negative: `No classical sonata form imposed, no atonal wandering, no thin small-combo sound as the main colour, no sentimental pop swell, no free improvisation without a written theme`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
