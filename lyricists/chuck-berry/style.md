# Chuck Berry — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chuck Berry: a teenage story told at full speed, plain words that swing, a chorus you can shout, the guitar riff as a second voice`
- ZH: 贝里风格：一个少年故事全速讲出，平实的词带着摇摆，副歌可以喊出来，吉他 riff 是第二声部。

## (2) 意象

- 少年意象（少年、吉他、舞会）／公路与汽车意象（汽车、公路、加油站）／音乐意象（贝多芬、摇滚、舞池）；意象密度中等；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度中等 `impression`
- 禁意象：华丽辞藻、抽象口号、沉重的议论、与少年无关的抒情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；副歌韵脚最亮，讲究喊得顺、记得住；换韵即换一段少年故事。 `impression`
- 音节与字数：句式整齐，叙事句长短一致；副歌短促重复；每句音节数求稳，讲究摇摆感。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中短句为主，陈述与呼唤交替；口语密度极高，像舞池边的人说话；多用第三人称少年故事与第二人称召唤。 `impression`
- 口语密度：口语密度极高：日常口语、少年俚语自然入词；书面语极少；叙事体与合唱体交错。 `impression`

## (5) 情感弧线

- 起于一个少年的场景，中段沿故事推进、越讲越快，副歌收在喊出来的快乐上，结尾常是一个吉他式的落点；情感轻快而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：少年与汽车意象、全速的叙事、副歌的喊唱感、吉他 riff 的呼应。
- 不该写：华丽辞藻、抽象口号、沉重的议论、与少年无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no solemn moralising, no lyricism unrelated to youth`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Chuck Berry, lyrics about a small Yorkshire terrier on the subway, a little rock-and-roll dog on the road. A teenage story at full speed, chorus you can shout. Verse, chorus, bridge. No ornate diction.`
- 中文对照：贝里风格：歌词写一只约克夏犬在地铁上，一只摇滚小狗在路上。少年故事全速讲出，副歌可以喊出来。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no solemn moralising, no lyricism unrelated to youth`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
