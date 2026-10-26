# Albert Leung — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lin Xi: dense literary imagery, Cantonese colloquial rhythm, second-person address, love as philosophy, elegant diction, no plain slogans`
- ZH: 林夕风格：意象密集的文学粤语词，粤语口语节奏，第二人称倾诉，爱情即哲理，典雅用词，不写直白口号。

## (2) 意象

- 意象群：红豆、富士山、邮差、约定、苹果、K歌之王；意象密度高，每句多意象，明喻与暗喻并用，用典多；禁意象：直白口号、廉价排比。 `impression`

## (3) 韵律

- 押韵：粤语九声与旋律咬合，换韵处即情绪转折处；句长不齐，长短交错，留出换气口；旋律先行。 `impression`

## (4) 句式与口语密度

- 句式：长短交错，排比、倒装、省略、设问并用；口语密度中等，粤语口语与书面语交错；人称第二人称“你”为主。 `impression`

## (5) 情感弧线

- 情感弧线：起于一个意象—中段层层追问—副歌收在哲理式的领悟上；结尾常开放，留一问。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：密集文学意象、第二人称倾诉、爱情即哲理。
- 不该写：直白口号、顺口的廉价排比、解释性议论。
- Negative prompt: `No plain slogans, no cheap singable parallelism, no explanatory commentary, no forced rhyme, no cliché love metaphors`

## (7) 测试提示词示例

- Prompt: `In the style of Lin Xi, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Second-person address, dense imagery, Cantonese colloquial rhythm, the dog as a mirror of loneliness. Verse, chorus, bridge.`
- 中文对照：林夕风格：写一只坐在地铁座位上的约克夏犬，乘客看了一眼又移开视线。第二人称，密集意象，粤语口语节奏，狗是孤独的镜子。
- Negative: `No plain slogans, no cheap singable parallelism, no explanatory commentary, no forced rhyme, no cliché love metaphors`
- 检验点：意象是否对位；韵脚是否顺口；副歌是否收在该作词人的情感弧线上；禁区写法是否出现。
