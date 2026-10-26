# Ethel Smyth — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Bold English opera and choral writing, Brahmsian warmth with sea drama, march rhythm as conviction, large forms claimed in a small space`
- ZH: 大胆的英国歌剧与合唱写作，勃拉姆斯式暖意加海洋戏剧，进行曲节奏即信念，小篇幅里争来的大型曲式

## (2) 音高与和声方向

- 主：功能和声，半音丰富，调性稳固；禁：无调性、为新奇而新奇的和声。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性强，合唱旋律有力，歌剧旋律戏剧化；节奏：进行曲节奏、海浪节奏；织体：合唱 + 管弦乐厚实，室内乐织体清晰。`artifact`

## (4) 配器与音色

- 配器：歌剧与合唱管弦乐厚实，铜管与合唱推高潮；音色暖、亮、有力。`artifact`

## (5) 曲式与结构

- 曲式：歌剧三幕、弥撒曲五乐章、进行曲短小有力；《沉船者》序曲即海浪与戏剧。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：合唱与歌剧、进行曲节奏、海洋戏剧、勃拉姆斯式暖意
- 不该写：无调性漫游、轻薄配器、为新奇而新奇
- Negative prompt: `atonal wandering, thin orchestration, novelty for its own sake`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Ethel Smyth, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a bold singing melody, march-like rhythm, warm full orchestration, conviction and warmth, like a small overture`
- 中文对照：史密斯风格，为地铁座位上的约克夏犬写 30 秒小品，大胆歌唱旋律，进行曲式节奏，温暖饱满配器，信念与暖意，如一首小序曲
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
