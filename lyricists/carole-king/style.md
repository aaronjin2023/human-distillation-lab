# Carole King — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carole King: warm plainspoken lyrics, friendship and reassurance, everyday language carrying deep feeling, chorus as a promise kept`
- ZH: 卡罗尔·金风格：温暖平实的歌词，友谊与安慰，日常语言承载深情，副歌即一句守得住的承诺。

## (2) 意象

- 意象群：(1)朋友与陪伴——朋友、肩膀、电话，陪伴即主题；(2)四季与天气——冬天、春天、雨，季节即心情；(3)自然的女人——自然、真实、不修饰，真实即美。意象密度低，每句至多一个意象，多明喻，用典极少。禁意象：华丽的古风意象、晦涩的象征、苦情的自怜。

## (3) 韵律

- 押韵：句尾押韵自然工整，韵脚多为柔和的尾音；常以重复与排比推进；换韵处即情绪转折处。音节与字数：每句字数中等，长短句交错，贴合钢琴的呼吸；重音即口语重音。

## (4) 句式与口语密度

- 句式：中短句为主，像说话；多用第二人称安慰与第一人称承诺交错，设问偶见。口语密度很高：日常口语、简单句，书面语极少；对话体多，独白体温和。

## (5) 情感弧线

- 情感弧线：起——一个困境进场（冬天、黑暗）；转——一句承诺把情绪推开；合——副歌收在温暖的安慰上，不煽情。情感强度温和深沉，与听众零距离；结尾常收束在一句承诺上。

## (6) 该写什么 / 不该写什么

- 该写：朋友与陪伴意象、平实的安慰句式、四季与天气意象、温和的承诺、副歌一句守得住的话。
- 不该写：华丽的古风意象、晦涩的象征、直白的煽情、苦情的自怜。
- Negative prompt: `No ornate archaic imagery, no obscure symbolism, no blunt sentimentality, no self-pitying lament, no forced rhyme`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Carole King, lyrics about a man buying oden at a convenience store late at night, a friend texting to check on him. Warm plainspoken lines, everyday language, chorus as a promise kept. No sentimentality.`
- 中文对照：卡罗尔·金风格：温暖平实的歌词，友谊与安慰，日常语言承载深情，副歌即一句守得住的承诺。以“一个人在深夜便利店买关东煮”为题写歌词，见英文提示词。
- Negative: `No ornate archaic imagery, no obscure symbolism, no blunt sentimentality, no self-pitying lament, no forced rhyme`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
