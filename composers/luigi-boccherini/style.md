# Luigi Boccherini — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical chamber music, singing cello lines, elegant string quintet, Spanish colour, graceful melody, clear tonal harmony, intimate galant style`
- ZH: 古典室内乐，歌唱性大提琴线条，优雅的弦乐五重奏，西班牙色彩，优美的旋律，清晰调性和声，亲切的华丽风格。

## (2) 旋律与和声

- 旋律：旋律优美歌唱，大提琴线条如人声；级进为主，装饰克制。`artifact` 和声：功能和声明确，属—主收束清晰；西班牙色彩靠节奏与音型；禁用随意半音。调性：调性稳定，转调靠模进。

## (3) 节奏与织体

- 节奏：节奏优雅，小步舞曲是骨架；《马德里街头夜曲》以街头节奏摹画夜景。织体：弦乐五重奏（两小提琴、中提琴、两大提琴）织体透明；留白靠乐句呼吸。

## (4) 配器与音色

- 配器与音色：弦乐五重奏与大提琴独奏为本体；音色温暖、优雅；力度靠声部对比；空间感来自马德里宫廷的 intimate。

## (5) 曲式与结构

- 曲式：弦乐五重奏（逾百首）、大提琴协奏曲、弦乐四重奏、夜曲并重。结构：奏鸣曲式与小步舞曲交替，高潮在独奏华彩；结尾以清晰终止收束。

## (6) 该写什么 / 不该写什么

- 该写：弦乐五重奏、歌唱性大提琴旋律、小步舞曲、西班牙色彩、《马德里街头夜曲》的街头描绘。
- 不该写：无歌唱性的机械音型、随意半音与无调性、管弦乐盖过独奏、与结构无关的炫技、感伤的滥情。
- Negative prompt: `No unlyrical mechanical figuration, no random chromaticism, no orchestra covering soloist, no structure-irrelevant virtuosity, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：黄昏时分的高铁车窗外）

- Prompt: `In the style of Luigi Boccherini, a 30-second piece for a high-speed train window at dusk, classical chamber music, singing cello lines, elegant string quintet, spanish colour, graceful melody, clear tonal harmony, intimate galant style`
- 中文对照：博凯里尼风格，为黄昏时分的高铁车窗外写 30 秒配乐，古典室内乐，歌唱性大提琴线条，优雅的弦乐五重奏，西班牙色彩，优美的旋律，清晰调性和声，亲切的华丽风格。
- Negative: `No unlyrical mechanical figuration, no random chromaticism, no orchestra covering soloist, no structure-irrelevant virtuosity, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
