# Arcangelo Corelli — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Italian Baroque instrumental music, concerto grosso, sonata da chiesa and da camera, singing violin lines, clear tonal harmony, elegant sequences, model of Baroque instrumental style`
- ZH: 意大利巴洛克器乐，大协奏曲，教堂奏鸣曲与室内奏鸣曲，歌唱性小提琴线条，清晰调性和声，优雅的模进，巴洛克器乐风格的范式。

## (2) 旋律与和声

- 旋律：小提琴旋律歌唱性强，级进与优雅跳进结合；线条如人声。`artifact` 和声：功能和声成型期，属—主收束明确，模进是主要发展手段；不协和按规则解决；禁用随意半音。调性：调性稳定，转调靠模进与五度圈。

## (3) 节奏与织体

- 节奏：节奏清晰，舞曲（教堂奏鸣曲慢—快交替、室内奏鸣曲舞曲套曲）是骨架；协奏曲以全奏—独奏交替制造节奏对比。织体：独奏—全奏交替（大协奏曲），三重奏鸣曲二小提琴加通奏低音；留白靠独奏段落。

## (4) 配器与音色

- 配器与音色：弦乐为本体，小提琴独奏 + 通奏低音；音色温暖、歌唱；力度靠全奏—独奏对比，动态范围适中；空间感来自合奏与独奏的远近。

## (5) 曲式与结构

- 曲式：大协奏曲、教堂奏鸣曲（慢—快—慢—快）、室内奏鸣曲（舞曲套曲）、变奏曲（《拉·佛利亚》）并重。结构：全奏—独奏交替，高潮在独奏华彩段；结尾以全奏收束。

## (6) 该写什么 / 不该写什么

- 该写：大协奏曲全奏—独奏交替、歌唱性小提琴旋律、模进发展、教堂与室内奏鸣曲、《拉·佛利亚》变奏曲。
- 不该写：无歌唱性的机械音型、随意半音与无调性、管弦乐盖过独奏、与舞曲无关的炫技、现代功能和声的滥用。
- Negative prompt: `No unlyrical mechanical figuration, no random chromaticism, no orchestra covering soloist, no dance-irrelevant virtuosity, no modern functional-harmony cliché, no pop phrasing`

## (7) 测试提示词示例（现代题材：清晨窗台上的一杯咖啡）

- Prompt: `In the style of Arcangelo Corelli, a 30-second piece for a cup of coffee on a windowsill in the morning light, italian baroque instrumental music, concerto grosso, sonata da chiesa and da camera, singing violin lines, clear tonal harmony, elegant sequences, model of baroque instrumental style`
- 中文对照：科雷利风格，为清晨窗台上的一杯咖啡写 30 秒配乐，意大利巴洛克器乐，大协奏曲，教堂奏鸣曲与室内奏鸣曲，歌唱性小提琴线条，清晰调性和声，优雅的模进，巴洛克器乐风格的范式。
- Negative: `No unlyrical mechanical figuration, no random chromaticism, no orchestra covering soloist, no dance-irrelevant virtuosity, no modern functional-harmony cliché, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
