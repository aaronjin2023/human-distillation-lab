# Arcangelo Corelli — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Italian Baroque, concerto grosso, graceful violin melody, clear tonal harmony, elegant sequence, the model of the Baroque sonata and concerto`
- ZH: 意大利巴洛克，大协奏曲，优雅小提琴旋律，清晰调性和声，优雅模进，巴洛克奏鸣曲与协奏曲的范式。

## (2) 音高与和声方向

- 主：大小调功能和声清晰；模进（sequence）为发展手段；属—主收束明确。禁：半音化滥用、复调的失控堆砌。调性：调性稳定，模进转调温和。

## (3) 旋律与节奏

- 旋律：小提琴歌唱性线条，级进为主，装饰音优雅；模进重复上行/下行。节奏：舞曲与庄严交替，节奏清晰。织体：大协奏曲为独奏组（concertino）与全奏组（ripieno）对比；奏鸣曲为小提琴 + 通奏低音。

## (4) 配器与音色

- 乐器：小提琴、弦乐队、通奏低音。音色：温暖、明亮、均衡。力度：独奏组与全奏组对比（强弱交替）。

## (5) 曲式与结构

- 曲式：大协奏曲、教堂奏鸣曲（慢—快—慢—快）、室内奏鸣曲（舞曲组）。结构：独奏组—全奏组交替；高潮在全奏组齐奏处。结尾：明确收束。

## (6) 该写什么 / 不该写什么

- 该写：大协奏曲、模进、小提琴歌唱旋律、教堂与室内奏鸣曲、清晰调性。
- 不该写：半音化滥用、复调的失控堆砌、炫技泛滥、模糊调性。
- Negative prompt: `aimless chromaticism, uncontrolled dense counterpoint, empty virtuosity, vague tonality, heavy orchestration`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of Arcangelo Corelli, a quiet night scene at a small convenience store in a modern city, Italian Baroque concerto grosso, graceful violin melody, clear tonal harmony, elegant sequence, concertino against ripieno, warm and balanced`
- 中文对照：科雷利风格，现代城市小便利店夜景，意大利巴洛克大协奏曲，优雅小提琴旋律，清晰调性，优雅模进，独奏组与全奏组对比，温暖均衡。
- Negative: `aimless chromaticism, uncontrolled dense counterpoint, empty virtuosity, vague tonality, heavy orchestration`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
