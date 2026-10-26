# Jerry Goldsmith — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Film score composition, eclectic modernism, twelve-tone fragments beside jazz trumpet, exotic percussion, precise orchestral colour`
- ZH: 电影配乐作曲，折衷现代主义，十二音碎片与爵士小号并置，异域打击乐，精确的管弦色彩。

## (2) 旋律与和声

- 旋律：主题短小、棱角分明，半音化与调式交替，歌唱性与器乐性兼备。
- 和声：十二音碎片、调式与功能和声并用；主：半音化与调式混合；禁：单一和声语言的贯穿；不协和度中高，解决视情境而定。

## (3) 节奏与织体

- 节奏：多变，爵士摇摆与不规则重音并存；织体：主调与复调交替，密度变化大，留白服务于音色。

## (4) 配器与音色

- 配器：管弦乐加异域打击、电子音色、爵士小号；音色：冷峻、精确、带金属与木质对比；力度：动态宽，突变多。

## (5) 曲式与结构

- 曲式：主题—变奏—组曲式；结构：动机按情境分配；高潮在音色叠加处；结尾视影片而定，常悬置。

## (6) 该写什么 / 不该写什么

- 该写：十二音碎片与爵士并置、异域打击乐色彩、短小棱角主题、精确的管弦音色切换。
- 不该写：单一风格贯穿全片、抒情长线的滥用、属—主套路解决、无主题的氛围铺底。
- Negative prompt: `No single style throughout, no overused lyrical lines, no formulaic dominant-tonic cadence, no theme-free ambient wash, no generic action ostinato`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jerry Goldsmith, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, an angular twelve-tone fragment, a lone jazz trumpet, exotic percussion, precise orchestral colour`
- 中文对照：戈德史密斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，棱角分明的十二音碎片，孤独爵士小号，异域打击乐，精确管弦色彩。。
- Negative: `No single style throughout, no overused lyrical lines, no formulaic dominant-tonic cadence, no theme-free ambient wash, no generic action ostinato`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
