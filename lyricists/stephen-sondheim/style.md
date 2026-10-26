# Stephen Sondheim — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stephen Sondheim: intricate musical-theatre lyrics, psychological precision, wordplay as character, chorus as a sudden self-recognition`
- ZH: 史蒂芬·桑德海姆风格：精密的音乐剧歌词，心理的精确，双关即角色，副歌即一句突然的自我认识。

## (2) 意象

- 意象群：(1)小丑与舞台——小丑、舞台、灯光，表演即人生；(2)星期天与画——星期天、画、点彩，艺术即生活；(3)活着与城市——活着、城市、夜晚，活着即主题。意象密度高，每句多个意象，明喻与暗喻交错，用典密集（文学、艺术史、心理学）。禁意象：直白的煽情、廉价的励志、简单的口号。

## (3) 韵律

- 押韵：句尾押韵极其精密，韵脚密集工整，常以多重内韵与双关推进；换韵处即心理翻转处。音节与字数：每句字数长短大幅交错，贴合音乐剧旋律的复杂呼吸；重音即口语重音，唱起来像说话又像思考。

## (4) 句式与口语密度

- 句式：长短句大幅交错，排比、倒装、设问、双关密集；多用第一人称独白与第二人称对话交错。口语密度中等：日常口语打底，精密书面语点睛；独白体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个日常场景进场；转——心理层层翻转，双关浮现；合——副歌收在突然的自我认识上，不煽情。情感强度深沉克制，与听众保持心理的距离；结尾常开放或戛然而止。

## (6) 该写什么 / 不该写什么

- 该写：小丑与舞台意象、心理的精确、双关即角色、精密的韵脚、副歌一句自我认识。
- 不该写：直白的煽情、廉价的励志、简单的口号、生硬的押韵。
- Negative prompt: `No blunt sentimentality, no cheap inspirational slogans, no simple slogans, no forced rhyme, no explanatory commentary`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Stephen Sondheim, lyrics about a man buying oden at a convenience store late at night, realising something about himself. Psychological precision, wordplay as character, chorus as a sudden self-recognition. No slogans.`
- 中文对照：史蒂芬·桑德海姆风格：精密的音乐剧歌词，心理的精确，双关即角色，副歌即一句突然的自我认识。以“一个人在深夜便利店买关东煮”为题写歌词，见英文提示词。
- Negative: `No blunt sentimentality, no cheap inspirational slogans, no simple slogans, no forced rhyme, no explanatory commentary`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
