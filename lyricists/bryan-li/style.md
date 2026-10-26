# Bryan Li — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bryan Li: literary Mandarin lyrics, cloudy weather and sudden parting imagery, elegant diction, flowing rhyme, restrained sorrow, no slang`
- ZH: 李焯雄风格：文艺国语词，阴天与忽然离别意象，典雅用词，韵脚流畅，克制的悲伤，不写俚语。

## (2) 意象

- 意象群：阴天、新不了情、忽然之间、雨、房间；意象密度中等，暗喻多；禁意象：俚语、戏剧化宣泄。 `impression`

## (3) 韵律

- 押韵：句尾押韵流畅，韵脚柔和；句长中等偏长，换气自然；旋律先行。 `impression`

## (4) 句式与口语密度

- 句式：中长句为主，独白多；口语密度低，书面文艺；人称第一人称独白。 `impression`

## (5) 情感弧线

- 情感弧线：起于阴天场景—中段情感漫开—副歌收在克制的悲伤上；结尾开放。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：阴天与忽然离别意象、典雅用词、流畅押韵、克制悲伤。
- 不该写：俚语、戏剧化宣泄、直白议论。
- Negative prompt: `No slang, no dramatic outburst, no direct moralising, no forced rhyme, no sentimental excess`

## (7) 测试提示词示例

- Prompt: `In the style of Bryan Li, lyrics about a man buying oden at a convenience store late at night on a cloudy day, suddenly missing someone. Literary Mandarin, cloudy weather imagery, restrained sorrow. Verse, chorus.`
- 中文对照：李焯雄风格：写一个阴天深夜在便利店买关东煮的男人，忽然想起一个人。文艺国语，阴天意象，克制悲伤。
- Negative: `No slang, no dramatic outburst, no direct moralising, no forced rhyme, no sentimental excess`
- 检验点：意象是否对位；韵脚是否顺口；副歌是否收在该作词人的情感弧线上；禁区写法是否出现。
