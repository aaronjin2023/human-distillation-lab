# Vladimir Vysotsky — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vladimir Vysotsky: a hoarse voice telling the truth sideways, a guitar and a crowd that knows the words, a chorus that is a test of friendship`
- ZH: 维索茨基风格：一把沙哑的嗓子斜着说真话，一把吉他和一群会唱的听众，副歌是一场对友谊的考验。

## (2) 意象

- 马意象（任性的马、悬崖、缰绳）／朋友意象（山、雪、肩膀）／监狱与街头意象（牢房、酒馆、雪地）；意象密度高；多用暗喻与反讽。 `impression`
- 意象密度：意象密度高 `impression`
- 禁意象：华丽辞藻、抽象口号、直白的控诉、与考验无关的抒情。`impression`

## (3) 韵律

- 俄语韵脚工整，韵脚多为开口音与闭口音交替；长句内押中间韵，副歌韵脚最烈；音节与吉他节拍对位，讲究一口气的长度。 `impression`
- 音节与字数：句式以长句为主，短句作断喝；主歌铺场景、副歌收考验，长短句随呼吸换。 `impression`

## (4) 句式与口语密度

- 句式：句式以长句排比与短句断喝交替，设问与自答、独白与对话并置；口语密度极高，俄语口语、俚语、行话并置；多用第一人称独白与第二人称呼唤。 `impression`
- 口语密度：口语密度极高：俄语口语、俚语、行话自然入词；书面语极少；独白体与合唱体交错。 `impression`

## (5) 情感弧线

- 起于一句直白的“我不爱”，中段沿考验推进、越讲越烈，副歌收在友谊的考验上，结尾常是一个未解的追问；情感浓烈而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：马与朋友意象、长句的呼吸、副歌的考验感、斜着说真话。
- 不该写：华丽辞藻、抽象口号、直白的控诉、与考验无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no direct denunciation, no lyricism unrelated to the test of friendship`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Vladimir Vysotsky, lyrics about a small Yorkshire terrier on the subway, a test of who will stay beside it. A hoarse voice telling the truth sideways, chorus as a test of friendship. Verse, chorus, bridge. No ornate diction.`
- 中文对照：维索茨基风格：歌词写一只约克夏犬在地铁上，考验谁会留在它身边。沙哑的嗓子斜着说真话，副歌是一场对友谊的考验。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no direct denunciation, no lyricism unrelated to friendship`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
