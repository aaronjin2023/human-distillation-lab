# Hikaru Utada — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hikaru Utada: bilingual confession, first love as a wound that stays tender, R&B phrasing in Japanese, plain words that sound like a voice memo`
- ZH: 宇多田光风格：双语告白，初恋是温柔的伤，R&B 句法说日语，白话像语音备忘录。

## (2) 意象

- 花意象群：樱花、花束，花开花落即感情；时间意象群：初恋、最后、十年，时间由感情量出；身体意象群：声、息、泪，情绪落在身体细节上。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日英混写：日语音拍与英语重音交错；韵脚松散、靠重复与呼吸推进；副歌短句如告白；善用英语词作韵脚点。 `impression`

## (4) 句式与口语密度

- 口语密度高：日常口语直写，像对一个人说话；语气词自然；书面语极少；独白感强。 `impression`

## (5) 情感弧线

- 起：一个私密场景进场；转：告白点破心意，情绪翻面；合：副歌收在温柔的告白短句上，结尾留余味、不决断。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：私密告白、花与时间意象、日英混写、温柔收束、身体细节。
- 不该写：直白口号、抽象议论、华丽辞藻、廉价煽情、说教。
- Negative prompt: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no preaching`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hikaru Utada, a letter to yourself ten years from now, written as a voice memo. Verse, chorus, bridge.`
- 中文对照：宇多田光风格：双语告白，初恋是温柔的伤，R&B 句法说日语，白话像语音备忘录。题目：a letter to yourself ten years from now, written as a voice memo。主歌、副歌、桥段。
- Negative: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no preaching`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
