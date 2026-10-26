# Tang Shu-shen — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tang Shu-shen: classical Chinese imagery inside Cantonese pop, dream and fate, elegant diction, love as a play that cannot be rehearsed`
- ZH: 唐书琛风格：古典意象住进粤语流行，梦与命，雅词，爱情是一场无法排练的戏。

## (2) 意象

- 古典意象群：故人、梦、戏、红尘，古典语汇写现代爱情；命运意象群：今生今世、来世、缘，时间拉长到生生世世；身体意象群：心、眼、泪，情绪落在身体细节上。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 粤语九声填词，韵脚雅致、换韵克制；主歌长句铺陈如戏、副歌短句收束如叹；善用古典词汇入韵，不拗口。 `impression`

## (4) 句式与口语密度

- 口语密度低：书面雅词为主，粤语口语只作调味；句式偏长、偏文言；对话感弱、独白感强。 `impression`

## (5) 情感弧线

- 起：一个梦境或戏台场景进场；转：梦醒或戏散，命运翻面；合：副歌收在宿命式短句上，结尾开放、不解释。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：古典意象写现代爱情、梦与戏的隐喻、宿命式收束、雅词入韵、独白体。
- 不该写：大白话、直白口号、市井俚语、解释性议论、廉价煽情。
- Negative prompt: `No plain vernacular, no direct slogans, no street slang, no explanatory commentary, no cheap sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tang Shu-shen, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：唐书琛风格：古典意象住进粤语流行，梦与命，雅词，爱情是一场无法排练的戏。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No plain vernacular, no direct slogans, no street slang, no explanatory commentary, no cheap sentimentality`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
