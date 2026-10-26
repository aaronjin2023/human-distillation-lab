# Witold Lutosławski — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Controlled aleatorism, folk-inspired melody, luminous orchestration, two-part form, dramatic climax, Polish colour without quotation`
- ZH: 受控偶然，民间启发的旋律，明亮配器，二部曲式，戏剧高潮，波兰色彩而不直接引用。

## (2) 旋律与和声

- 旋律：民间式级进线条，音程清晰；主题短小、富于发展。`artifact`
- 和声：十二音和弦作色彩块，调性游移；不协和靠音色块移动解决。`artifact`

## (3) 节奏与织体

- 节奏：受控偶然段落中各声部自由进入；固定节奏段落驱动；织体：多层并置，密度可控。

## (4) 配器与音色

- 配器：大编制管弦，明亮木管与弦乐；打击乐点缀；音色层次丰富。

## (5) 曲式与结构

- 曲式：二部曲式（引子—主部）、协奏曲、交响曲；高潮在主部后段，结尾有力收束。

## (6) 该写什么 / 不该写什么

- 该写：受控偶然段落、民间式旋律、二部曲式、明亮管弦配器、十二音和弦色彩块、戏剧高潮。
- 不该写：total chance without control、no folk-song quotation as composition、no functional harmony as structure、no dense counterpoint obscuring the theme、no sentimental swell。
- Negative prompt: `No total chance without control, no folk-song quotation as composition, no functional harmony as structure, no dense counterpoint obscuring the theme, no sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Witold Lutosławski, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, folk-like melody, controlled aleatoric shimmer, luminous orchestration, dramatic climax`
- 中文对照：卢托斯瓦夫斯基风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，民间式旋律，受控偶然闪烁，明亮配器，戏剧高潮。
- Negative: `No total chance without control, no folk-song quotation as composition, no functional harmony as structure, no dense counterpoint obscuring the theme, no sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
