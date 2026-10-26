# Kendrick Lamar — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kendrick Lamar: dense internal rhyme chains, a Compton street as a moral stage, voices that argue inside one verse, a chorus that is both prayer and defiance`
- ZH: 拉马尔风格：密集的内部韵链，康普顿街头是道德舞台，一段歌词里多个声音在辩论，副歌既是祷告也是反抗。

## (2) 意象

- 街头意象（康普顿、街角、警车）／圣经意象（祷告、审判、救赎）／身体意象（王冠、伤疤、膝盖）；意象密度极高，一句常叠两三个意象；多用暗喻与双关。 `impression`
- 意象密度：意象密度极高，一句常叠两三个意象 `impression`
- 禁意象：直白口号、廉价的流行副歌、与街头无关的抒情、故作艰深的隐喻。`impression`

## (3) 韵律

- 内部韵与多音节韵脚成链，段落内韵脚密集；韵脚链即Flow，换韵即换一个声音；重音与节拍严格对位。 `impression`
- 音节与字数：段落长短悬殊：快嘴长句与短促的副歌钩子交错；每句音节数不求整齐，求Flow不断；副歌齐整，对比段落的自由。 `impression`

## (4) 句式与口语密度

- 句式：句式以长句排比与短句断喝交替，设问与自答、独白与对话并置；口语密度极高，街头口语与圣经语言跳接；多用第一人称与第二人称质问。 `impression`
- 口语密度：口语密度极高：街头俚语、感叹词、圣经词并置；语气词靠节奏词推进；独白体、对话体、合唱体交错。 `impression`

## (5) 情感弧线

- 起于街头的一个场景，中段多个声音辩论、真相渐次显露，副歌收在祷告与反抗之间，结尾常是一个未解的追问；情感浓烈而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：内部韵链与多声部辩论、街头与圣经意象、副歌的祷告感、未解的追问。
- 不该写：直白口号、廉价的流行副歌、与街头无关的抒情、故作艰深的隐喻。
- Negative prompt: `No plain slogans, no cheap pop hook, no lyricism unrelated to the street, no wilfully obscure metaphor`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kendrick Lamar, lyrics about a small Yorkshire terrier on the subway, a witness to the city at night. Dense internal rhymes, voices arguing inside one verse, chorus as prayer and defiance. Verse, chorus, bridge. No plain slogans.`
- 中文对照：拉马尔风格：歌词写一只约克夏犬在地铁上，见证夜晚的城市。密集的内部韵，一段里多个声音辩论，副歌既是祷告也是反抗。主歌、副歌、桥段。不写直白口号。
- Negative: `No plain slogans, no cheap pop hook, no lyricism unrelated to the street, no obscure metaphor`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
