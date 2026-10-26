# Jacques Brel — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jacques Brel: a long breath of a plea, the port as a theatre of desire, plain French that turns suddenly violent, a chorus that begs and accuses at once`
- ZH: 布雷尔风格：一口气的恳求，港口是欲望的剧场，平实的法语忽然变得猛烈，副歌同时是恳求与指控。

## (2) 意象

- 港口意象（阿姆斯特丹、水手、酒馆）／恳求意象（不要离开我、影子、狗）／老去意象（老情人、白发、旧信）；意象密度高，一句常叠两三个意象；多用暗喻与排比。 `impression`
- 意象密度：意象密度高，一句常叠两三个意象 `impression`
- 禁意象：华丽辞藻、抽象口号、廉价的安慰、与欲望无关的抒情。`impression`

## (3) 韵律

- 法语韵脚工整，韵脚多为开口音；长句内押中间韵，副歌韵脚最恳切；音节与香颂节拍对位，讲究一口气的长度。 `impression`
- 音节与字数：句式以长句为主，短句作断喝；主歌铺场景、副歌收恳求，长短句随呼吸换。 `impression`

## (4) 句式与口语密度

- 句式：句式以长句排比与短句断喝交替，设问与自答、恳求与指控并置；口语密度中等，法语口语与书面语并置；多用第二人称呼唤与第一人称独白。 `impression`
- 口语密度：口语密度中等：法语口语自然，语气词少；书面语用于恳求与自省段落；独白体与对话体交错。 `impression`

## (5) 情感弧线

- 起于一句恳求，中段沿港口与欲望推进、越讲越猛烈，副歌收在恳求与指控之间，结尾常是筋疲力尽的停顿；情感浓烈而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：港口与恳求意象、长句的呼吸、副歌的恳求与指控、猛烈的转折。
- 不该写：华丽辞藻、抽象口号、廉价的安慰、与欲望无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no cheap comfort, no lyricism unrelated to desire`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jacques Brel, lyrics about a small Yorkshire terrier on the subway, begging the city not to leave it. A long breath of a plea, chorus that begs and accuses at once. Verse, chorus, bridge. No ornate diction.`
- 中文对照：布雷尔风格：歌词写一只约克夏犬在地铁上，恳求城市不要离开它。一口气的恳求，副歌同时是恳求与指控。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no cheap comfort, no lyricism unrelated to desire`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
