# Sofia Gubaidulina — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Sacred intensity, Bach quotation transformed, bayan and cello colour, silence and eruption, East-West synthesis, spiritual without denomination`
- ZH: 神圣强度，巴赫引用的变形，巴扬与大提琴音色，沉默与爆发，东西方综合，灵性而不属教派。

## (2) 旋律与和声

- 旋律：巴赫主题变形，级进与大跳交替；线条长而集中。`artifact`
- 和声：调性游移，半音与不协和制造张力；解决靠主题再现。`artifact`

## (3) 节奏与织体

- 节奏：自由与严格并存；沉默是结构部分；织体：极稀疏与极密集并置。

## (4) 配器与音色

- 配器：巴扬手风琴、大提琴、小提琴、管弦；音色暗而集中，泛音丰富。

## (5) 曲式与结构

- 曲式：协奏曲、七乐章组曲；结构靠主题变形，高潮宏大，结尾常宁静收束。

## (6) 该写什么 / 不该写什么

- 该写：巴赫主题变形、巴扬与大提琴音色、沉默与爆发对比、七乐章结构、灵性长线条。
- 不该写：functional harmony as structure、no decorative virtuosity、no sentimental swell、no ironic distance、no dense counterpoint obscuring the theme、no light entertainment tone。
- Negative prompt: `No functional harmony as structure, no decorative virtuosity, no sentimental swell, no ironic distance, no dense counterpoint obscuring the theme, no light entertainment tone`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sofia Gubaidulina, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Bach-like theme transformed, bayan and cello colour, silence then eruption, quiet close`
- 中文对照：古拜杜丽娜风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，巴赫式主题变形，巴扬与大提琴音色，沉默后爆发，安静收束。
- Negative: `No functional harmony as structure, no decorative virtuosity, no sentimental swell, no ironic distance, no dense counterpoint obscuring the theme, no light entertainment tone`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
