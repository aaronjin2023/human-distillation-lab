# Bruce Springsteen — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bruce Springsteen: blue-collar rock lyrics, highway and small-town imagery, cinematic detail piling into anthemic chorus, chorus as a promise of escape`
- ZH: 布鲁斯·斯普林斯汀风格：蓝领摇滚歌词，公路与小镇的意象，电影般的细节堆叠成赞歌般的副歌，副歌即一句逃离的承诺。

## (2) 意象

- 意象群：(1)公路与汽车——公路、汽车、引擎，逃离即希望；(2)小镇与工厂——小镇、工厂、酒吧，困境即日常；(3)河流与夜晚——河流、夜晚、霓虹，夜晚即自由。意象密度高，每句多个意象，多明喻，用典克制。禁意象：抽象的哲学概念、廉价的励志口号。

## (3) 韵律

- 押韵：句尾押韵工整有力，韵脚多为短促的口语尾音；常以排比与重复推进，副歌靠叠句点燃；换韵处即情绪爆发处。音节与字数：每句字数中等偏长，长短句交错，贴合摇滚的呼吸；重音即口语重音，唱起来像呐喊。

## (4) 句式与口语密度

- 句式：中长句为主，排比密集；多用第一人称叙事与第二人称邀约交错，设问偶见。口语密度高：蓝领口语、俚语、简单句，书面语极少；叙事体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个小镇画面进场；转——细节堆叠，渴望升温；合——副歌收在逃离的承诺上，浓烈而不滥情。情感强度浓烈真诚，与听众零距离；结尾常收束在公路的一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：公路与汽车意象、小镇与工厂细节、排比堆叠的叙事、赞歌般的副歌、逃离的承诺。
- 不该写：抽象的哲学议论、廉价的励志口号、直白的煽情、生硬的押韵。
- Negative prompt: `No abstract philosophising, no cheap inspirational slogans, no blunt sentimentality, no forced rhyme, no ornate diction`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Bruce Springsteen, lyrics about a man buying oden at a convenience store late at night, dreaming of the highway. Blue-collar detail piling into an anthemic chorus, highway imagery, chorus as a promise of escape. No slogans.`
- 中文对照：布鲁斯·斯普林斯汀风格：蓝领摇滚歌词，公路与小镇的意象，电影般的细节堆叠成赞歌般的副歌，副歌即一句逃离的承诺。以“一个人在深夜便利店买关东煮”为题写歌词，见英文提示词。
- Negative: `No abstract philosophising, no cheap inspirational slogans, no blunt sentimentality, no forced rhyme, no ornate diction`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
