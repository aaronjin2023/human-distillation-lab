# Siu Mei — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Siu Mei: plain Cantonese carrying deep gratitude, mother and friend as mirror, chorus that invites everyone to sing along`
- ZH: 小美风格：粤语白话承深情，母亲与朋友作镜子，副歌邀人合唱。

## (2) 意象

- 亲情意象群：母亲、家、灯火，感恩写进日常；共鸣意象群：有谁共鸣、知音、掌声，孤独与被听见对照；风雨意象群：风雨、路、坚持，时间由风雨量出。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 粤语九声填词，韵脚工整、合唱感强；主歌娓娓道来、副歌收紧；换韵处即情绪高点；善用重复与叠唱。 `impression`

## (4) 句式与口语密度

- 口语密度高：粤语白话自然流畅，像对家人说话；语气词温和；书面语只在点题处出现。 `impression`

## (5) 情感弧线

- 起：一个日常场景进场（家、灯、路）；转：平凡里点破深情，情绪翻面；合：副歌收在感恩或共鸣的短句上，结尾温暖而不滥情。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：日常场景写深情、母亲与朋友意象、副歌合唱感、感恩式收束、风雨写时间。
- 不该写：华丽古风意象、直白说教、无场景的抽象抒情、哭诉式煽情、廉价排比。
- Negative prompt: `No ornate archaic imagery, no direct preaching, no abstract lyricism without a scene, no forced rhyme, no weeping sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Siu Mei, a letter to yourself ten years from now, written in the style of a letter home. Verse, chorus, bridge.`
- 中文对照：小美风格：粤语白话承深情，母亲与朋友作镜子，副歌邀人合唱。题目：a letter to yourself ten years from now, written in the style of a letter home。主歌、副歌、桥段。
- Negative: `No ornate archaic imagery, no direct preaching, no abstract lyricism without a scene, no forced rhyme, no weeping sentimentality`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
