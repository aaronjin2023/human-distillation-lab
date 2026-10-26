# Antonio Vivaldi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Italian Baroque concerto, ritornello form, vivid programmatic painting, brilliant violin virtuosity, driving rhythms, clear tonal harmony, Venetian colour`
- ZH: 意大利巴洛克协奏曲，利都奈洛曲式，生动的标题描绘，辉煌的小提琴炫技，驱动性节奏，清晰调性和声，威尼斯色彩。

## (2) 旋律与和声

- 旋律：小提琴旋律辉煌，音型重复与模进驱动；标题描绘（如鸟鸣、雷雨）直接摹画。`artifact` 和声：功能和声明确，属—主收束有力；模进是主要发展；禁用随意半音。调性：调性稳定，转调靠模进与五度圈。

## (3) 节奏与织体

- 节奏：节奏驱动性强，利都奈洛全奏与独奏交替制造脉动；标题段落节奏摹画自然。织体：独奏—全奏交替，织体清晰；留白靠独奏段落。

## (4) 配器与音色

- 配器与音色：弦乐为本体，小提琴独奏辉煌；音色明亮、活泼；力度靠全奏—独奏对比，动态范围大；空间感来自威尼斯教堂与剧场的明亮。

## (5) 曲式与结构

- 曲式：独奏协奏曲（三乐章快—慢—快）、大协奏曲、圣乐（《荣耀颂》）并重；利都奈洛曲式是骨架。结构：全奏主题—独奏插段—全奏再现，高潮在独奏华彩；结尾以全奏收束。

## (6) 该写什么 / 不该写什么

- 该写：利都奈洛曲式、标题描绘（鸟鸣、雷雨）、小提琴炫技音型、快—慢—快三乐章、全奏—独奏交替。
- 不该写：无标题支撑的随意音型、半音化与无调性、管弦乐盖过独奏、慢乐章的冗长堆砌、现代功能和声的滥用。
- Negative prompt: `No random figuration without programme, no chromaticism, no orchestra covering soloist, no overlong slow movement, no modern functional-harmony cliché, no pop phrasing`

## (7) 测试提示词示例（现代题材：清晨苏醒的菜市场）

- Prompt: `In the style of Antonio Vivaldi, a 30-second piece for a morning vegetable market waking up, italian baroque concerto, ritornello form, vivid programmatic painting, brilliant violin virtuosity, driving rhythms, clear tonal harmony, venetian colour`
- 中文对照：维瓦尔第风格，为清晨苏醒的菜市场写 30 秒配乐，意大利巴洛克协奏曲，利都奈洛曲式，生动的标题描绘，辉煌的小提琴炫技，驱动性节奏，清晰调性和声，威尼斯色彩。
- Negative: `No random figuration without programme, no chromaticism, no orchestra covering soloist, no overlong slow movement, no modern functional-harmony cliché, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
