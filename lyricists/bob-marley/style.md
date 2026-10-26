# Bob Marley — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bob Marley: call and response, a plainspoken prophecy, redemption as a chorus everyone can sing, hope without naivety`
- ZH: 马利风格：一呼一应，平实的预言，救赎是人人会唱的副歌，希望而不天真。

## (2) 意象

- 救赎意象（铁链、自由、歌声）／家园意象（牙买加、茅屋、厨房）／自然意象（三只小鸟、日出、雨）；意象密度低；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度低 `impression`
- 禁意象：华丽辞藻、抽象口号、愤怒的控诉、与救赎无关的抒情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；呼应段落押同一韵，副歌重复推进；音节与雷鬼节拍对位。 `impression`
- 音节与字数：句式以中短句为主，呼唤句与回答句交替；副歌短促重复。 `impression`

## (4) 句式与口语密度

- 句式：句式以呼唤与回答为主，设问与宣告交替；口语密度极高，牙买加口语与圣经语言并置；多用第二人称召唤与第一人称复数“我们”。 `impression`
- 口语密度：口语密度极高：牙买加口语、口头语自然入词；圣经语言只在救赎段落出现；合唱体为主。 `impression`

## (5) 情感弧线

- 起于一句呼唤，中段由个人的苦难走向集体的救赎，副歌收在希望本身上，结尾常是平静的坚持；情感浓烈而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：一呼一应、救赎与自由意象、人人会唱的副歌、希望而不天真。
- 不该写：华丽辞藻、抽象口号、愤怒的控诉、与救赎无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no angry denunciation, no lyricism unrelated to redemption`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Bob Marley, lyrics about a small Yorkshire terrier on the subway, singing that every little thing is gonna be alright. Call and response, chorus everyone can sing. Verse, chorus, bridge. No ornate diction.`
- 中文对照：马利风格：歌词写一只约克夏犬在地铁上，唱着一切都会好的。一呼一应，副歌人人会唱。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no angry denunciation, no lyricism unrelated to redemption`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
