# Cheer Chen — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cheer Chen: literary Mandarin folk lyrics, travel and solitude imagery, plain diction, gentle rhyme, quiet self-talk, no drama`
- ZH: 陈绮贞风格：文艺国语民谣词，旅行与孤独意象，朴素用词，韵脚柔和，安静自语，不写戏剧化。

## (2) 意象

- 意象群：旅行、吉他、寂寞、城市、雨、夜；意象密度中等，具象而安静；禁意象：华丽古风、戏剧化宣泄。 `impression`

## (3) 韵律

- 押韵：押韵宽松，近韵与自由体并用；句长不齐，长短交错；词曲双全，先词后曲者多。 `impression`

## (4) 句式与口语密度

- 句式：中短句为主，独白多，设问少；口语密度中等，书面文艺；人称第一人称自语。 `impression`

## (5) 情感弧线

- 情感弧线：起于旅行场景—中段一声自问—副歌收在安静的领悟上；结尾开放。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：旅行与孤独意象、朴素用词、安静自语、宽松押韵。
- 不该写：戏剧化宣泄、华丽古风意象、直白议论。
- Negative prompt: `No dramatic outburst, no ornate classical imagery, no direct moralising, no forced rhyme, no sentimental excess`

## (7) 测试提示词示例

- Prompt: `In the style of Cheer Chen, lyrics about a letter to oneself ten years from now, written on a train. Literary Mandarin, travel and solitude imagery, quiet self-talk. Verse, chorus.`
- 中文对照：陈绮贞风格：写一封在火车上写给十年后自己的信。文艺国语，旅行与孤独意象，安静自语。
- Negative: `No dramatic outburst, no ornate classical imagery, no direct moralising, no forced rhyme, no sentimental excess`
- 检验点：意象是否对位；韵脚是否顺口；副歌是否收在该作词人的情感弧线上；禁区写法是否出现。
