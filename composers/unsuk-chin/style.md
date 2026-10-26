# Unsuk Chin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Korean contemporary composition, sparkling orchestral colour, playful virtuosity, electronic shimmer, East Asian timbre inside Western forms`
- ZH: 韩国当代作曲，闪烁管弦色彩，游戏式炫技，电子闪光，西方曲式内的东亚音色。

## (2) 旋律与和声

- 旋律：短小、跳跃、带装饰的动机，音域宽，呼吸短促，器乐性强。
- 和声：调式与半音化并置，功能和声淡化；主：调式、半音化；禁：属—主套路；不协和度中高，解决靠音色。

## (3) 节奏与织体

- 节奏：轻快、跳跃，复节奏与突然停顿；织体：闪烁织体，密度中高，留白靠音色切换。

## (4) 配器与音色

- 配器：管弦乐、电子、笙等东亚乐器；音色：闪烁、透明、带金属感；力度：动态宽，突变多。

## (5) 曲式与结构

- 曲式：歌剧、协奏曲、管弦乐；结构：动机—变奏—再现；高潮在音色最闪处；结尾常以轻巧收束。

## (6) 该写什么 / 不该写什么

- 该写：闪烁管弦色彩、游戏式炫技动机、电子闪光、东亚音色对照。
- 不该写：沉重浪漫和声、属—主套路、单调织体、无音色变化的长线。
- Negative prompt: `No heavy Romantic harmony, no formulaic dominant-tonic cadence, no monotonous texture, no long line without timbral change, no sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Unsuk Chin, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, sparkling orchestral colour, playful virtuoso motifs, electronic shimmer, a sheng-like timbre, light and fantastical`
- 中文对照：陈银淑风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，闪烁管弦色彩，游戏式炫技动机，电子闪光，笙式音色，轻巧奇幻。。
- Negative: `No heavy Romantic harmony, no formulaic dominant-tonic cadence, no monotonous texture, no long line without timbral change, no sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
