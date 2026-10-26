# Cole Porter — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cole Porter: urbane wit, list songs that catalogue desire, internal rhyme and double entendre, a chorus that sparkles rather than swells, elegance with a raised eyebrow`
- ZH: 波特风格：都市机锋，罗列式歌曲盘点欲望，内部韵与双关，副歌闪烁而不汹涌，优雅中挑着眉毛。

## (2) 意象

- 都市意象（鸡尾酒、夜总会、巴黎、百老汇）／罗列意象（地名、名人、奢侈品一一报数）／身体与欲望意象（吻、香槟、月光）；意象密度高，一句常叠两三个名目；多用明喻与双关，少用典。 `impression`
- 意象密度：意象密度高，一句常叠两三个名目 `impression`
- 禁意象：浓烈抒情、直白口号、乡土意象、沉重的道德议论。`impression`

## (3) 韵律

- 内部韵与句尾韵并重，韵脚俏皮，常押出人意料的韵；罗列段落靠韵脚串联，换韵即换一轮名目；音节与节拍严丝合缝，讲究字音的轻巧。 `impression`
- 音节与字数：句式整齐而轻快，罗列句长短一致，副歌短促上扬；每句音节数讲究，拗口即失败。 `impression`

## (4) 句式与口语密度

- 句式：句式以罗列与排比为主，设问与自答轻快交替；口语密度中等偏高，都市口语与法语词点缀；多用第一人称倾诉，偶用第二人称调情。 `impression`
- 口语密度：口语密度中等偏高：都市闲谈口吻，法语词与俚语作调味；语气词少，靠俏皮的转折推进；对话体与独白体交错。 `impression`

## (5) 情感弧线

- 起于一句俏皮的开场，中段用罗列堆叠欲望或名单，副歌收在一点闪光的自白上，结尾常是一个双关的回马枪；情感轻盈、克制，几乎不用浓烈抒情。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：罗列式盘点、双关与内部韵、都市机锋、副歌的闪光自白。
- 不该写：浓烈抒情、直白口号、乡土意象、沉重的道德议论。
- Negative prompt: `No heavy sentiment, no plain slogans, no rustic imagery, no solemn moralising`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Cole Porter, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters. A witty list song, internal rhymes and double entendre, chorus that sparkles. Verse, chorus, bridge. No heavy sentiment.`
- 中文对照：波特风格：歌词写一只约克夏犬坐在地铁座位上，通勤者注视着它。机锋的罗列式歌曲，内部韵与双关，副歌闪烁。主歌、副歌、桥段。不写浓烈抒情。
- Negative: `No heavy sentiment, no plain slogans, no rustic imagery, no solemn moralising`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
