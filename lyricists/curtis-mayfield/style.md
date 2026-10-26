# Curtis Mayfield — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Curtis Mayfield: a gentle warning in falsetto's shadow, plain words that lift a crowd, the train as a promise, hope with its eyes open`
- ZH: 梅菲尔德风格：一句温柔的警告藏在假声的影子里，平实的词托起人群，火车是一个承诺，希望睁着眼睛。

## (2) 意象

- 火车意象（火车、铁轨、车站）／街头意象（街角、霓虹、毒品）／上升意象（上楼、翅膀、高处）；意象密度中等；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度中等 `impression`
- 禁意象：华丽辞藻、抽象口号、愤怒的控诉、与街头无关的抒情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；副歌韵脚最稳，换韵即换一段警告；音节与灵魂乐节拍对位。 `impression`
- 音节与字数：句式以中短句为主，警告句与鼓励句交替；副歌短促重复。 `impression`

## (4) 句式与口语密度

- 句式：句式以警告与鼓励为主，设问与宣告交替；口语密度高，像街头的人说话；多用第二人称召唤与第一人称复数“我们”。 `impression`
- 口语密度：口语密度高：日常口语、街头用语自然入词；书面语极少；合唱体与独白体交错。 `impression`

## (5) 情感弧线

- 起于一句温柔的警告，中段由街头的现实走向上升的承诺，副歌收在火车的承诺上，结尾常是清醒的希望；情感克制而坚定。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：火车与上升意象、温柔的警告、副歌的承诺感、清醒的希望。
- 不该写：华丽辞藻、抽象口号、愤怒的控诉、与街头无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no angry denunciation, no lyricism unrelated to the street`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Curtis Mayfield, lyrics about a small Yorkshire terrier on the subway, telling the passengers to move on up. A gentle warning, chorus as a promise. Verse, chorus, bridge. No ornate diction.`
- 中文对照：梅菲尔德风格：歌词写一只约克夏犬在地铁上，告诉乘客继续向上。温柔的警告，副歌是一个承诺。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no angry denunciation, no lyricism unrelated to the street`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
