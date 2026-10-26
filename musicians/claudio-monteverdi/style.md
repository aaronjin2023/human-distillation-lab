# Claudio Monteverdi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Early Baroque, seconda pratica, text-driven dissonance, monody and expressive recitative, dramatic opera, sacred polyphony and madrigal in one hand`
- ZH: 巴洛克早期，第二实践（seconda pratica），歌词驱动的非协和，单声部歌曲与表现性宣叙调，戏剧歌剧，圣咏复调与牧歌同源。

## (2) 音高与和声方向

- 主：歌词驱动的和声，非协和可不经准备、为表情服务（第二实践）；通奏低音（basso continuo）为骨架。禁：帕莱斯特里纳式严格对位规则的束缚。调性：调式向大小调过渡；不协和为表情，解决靠歌词句读。

## (3) 旋律与节奏

- 旋律：宣叙调贴近语言语调；咏叹调歌唱性强，装饰音为表情；牧歌旋律随词义起伏。节奏：歌词重音主导，节奏自由。织体：单声 + 通奏低音、复调、齐唱交替。

## (4) 配器与音色

- 乐器：通奏低音（羽管键琴、 theorbo）、弦乐、管乐；《奥菲欧》用约 40 件乐器的乐队，音色随剧情切换。音色：丰富、戏剧化。力度：靠配器与织体对比。

## (5) 曲式与结构

- 曲式：歌剧（序幕 + 五幕）、牧歌集、圣母晚祷（诗篇 + 经文歌拼贴）。结构：以剧情 / 歌词结构定音乐结构；宣叙调—咏叹调—合唱交替。高潮在剧情转折处。结尾：按剧情收束。

## (6) 该写什么 / 不该写什么

- 该写：第二实践、宣叙调、牧歌绘词、歌剧、通奏低音、戏剧配器。
- 不该写：严格对位规则、与歌词无关的炫技、功能和声的机械进行。
- Negative prompt: `strict Palestrina counterpoint rules, wordless virtuosity, mechanical functional harmony, orchestral bombast without text`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of Claudio Monteverdi, a quiet night scene at a small convenience store in a modern city, early Baroque seconda pratica, expressive recitative, text-driven dissonance, basso continuo, strings and theorbo, dramatic and tender`
- 中文对照：蒙特威尔第风格，现代城市小便利店夜景，巴洛克早期第二实践，表现性宣叙调，歌词驱动的非协和，通奏低音，弦乐与 theorbo，戏剧而温柔。
- Negative: `strict Palestrina counterpoint rules, wordless virtuosity, mechanical functional harmony`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
