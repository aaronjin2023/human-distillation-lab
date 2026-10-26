# Pete Seeger — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pete Seeger: a question asked until it becomes a chorus, simple words that carry further each time they repeat, hope as a discipline`
- ZH: 西格风格：一个问题问到它变成副歌，简单的词每重复一次走得更远，希望是一种操练。

## (2) 意象

- 工具意象（锤子、镰刀、铃铛）／花与季节意象（花、雨、秋天）／时间意象（转、转、再转）；意象密度低，每句一个意象；多用具体名词与设问。 `impression`
- 意象密度：意象密度低，每句一个意象 `impression`
- 禁意象：华丽辞藻、愤怒的控诉、抽象口号、与集体无关的个人抒情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；设问句与回答句押同一韵；副歌重复推进，换韵即换一轮追问。 `impression`
- 音节与字数：句式整齐，设问句与陈述句长短一致；副歌短促重复；音节求稳。 `impression`

## (4) 句式与口语密度

- 句式：句式以设问与排比为主，问句与答句交替；口语密度高，像课堂上的人说话；多用第一人称复数“我们”与第二人称召唤。 `impression`
- 口语密度：口语密度高：日常口语、口头语自然；书面语极少；合唱体为主，独白体为辅。 `impression`

## (5) 情感弧线

- 起于一个简单的问题，中段每重复一次问题就走远一步，副歌收在集体的回答上，结尾常是开放的追问而非结论；情感温和而坚定。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：设问与排比、简单词的重复推进、集体合唱感、希望的操练。
- 不该写：华丽辞藻、愤怒的控诉、抽象口号、与集体无关的个人抒情。
- Negative prompt: `No ornate diction, no angry denunciation, no abstract slogans, no solitary lyricism detached from the chorus`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Pete Seeger, lyrics about a small Yorkshire terrier on the subway, asking where all the passengers have gone. A question repeated until it becomes a chorus. Verse, chorus, bridge. No ornate diction.`
- 中文对照：西格风格：歌词写一只约克夏犬在地铁上，问乘客们都去了哪里。一个问题问到变成副歌。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no angry denunciation, no abstract slogans, no solitary lyricism`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
