# Barbara — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Barbara: a low voice telling a secret, the past returning as a bird over a lake, plain French that bruises gently, a chorus that remembers`
- ZH: 芭芭拉风格：低声说一个秘密，过去如黑鹰掠过湖面，平实的法语轻轻地淤青，副歌是一次回忆。

## (2) 意象

- 湖与鹰意象（黑鹰、湖面、雨）／故乡意象（南特、哥廷根、旧街）／秘密意象（未说出口的话、旧信、童年）；意象密度中等；多用暗喻，少用典。 `impression`
- 意象密度：意象密度中等 `impression`
- 禁意象：华丽辞藻、抽象口号、愤怒的控诉、与秘密无关的抒情。`impression`

## (3) 韵律

- 法语韵脚工整，韵脚多为闭口音与开口音交替；副歌韵脚最轻，换韵即换一段回忆；音节与香颂节拍对位。 `impression`
- 音节与字数：句式以中长句为主，叙事句与抒情句交替；长句里藏短句的落点。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中长句为主，陈述与低语交替；口语密度中等，法语口语与书面语并置；多用第一人称回忆与第二人称倾诉。 `impression`
- 口语密度：口语密度中等：法语口语自然，语气词少；书面语用于回忆段落；独白体为主。 `impression`

## (5) 情感弧线

- 起于一个湖边的秘密，中段沿回忆推进、越讲越轻，副歌收在回忆本身上，结尾常是轻轻的停顿；情感克制而深沉。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：湖与鹰意象、低声的秘密、副歌的回忆感、轻轻的淤青。
- 不该写：华丽辞藻、抽象口号、愤怒的控诉、与秘密无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no angry denunciation, no lyricism unrelated to memory`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Barbara, lyrics about a small Yorkshire terrier on the subway, remembering a lake it once saw. A low voice telling a secret, chorus that remembers. Verse, chorus, bridge. No ornate diction.`
- 中文对照：芭芭拉风格：歌词写一只约克夏犬在地铁上，回忆曾经见过的一个湖。低声说一个秘密，副歌是一次回忆。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no angry denunciation, no lyricism unrelated to memory`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
