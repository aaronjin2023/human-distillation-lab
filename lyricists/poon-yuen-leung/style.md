# Poon Yuen-leung — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Poon Yuen-leung: the wanderer's heart, plain words carrying heavy feeling, Cantonese colloquial rhythm, love as a road that cannot be finished`
- ZH: 潘源良风格：浪子之心，白话承重情，粤语口语节奏，爱情是一条走不完的路。

## (2) 意象

- 道路意象群：浪子、路途、风霜、足印，行走即人生；心意象群：心、边缘、痛，把抽象情绪写成身体位置；夜意象群：夜、漂泊、孤独，夜是浪子的主场。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 粤语九声填词，韵脚工整而不过密；主歌长句铺陈、副歌短句收束；换韵处即情绪翻面处；善用叠字与重复推进情感。 `impression`

## (4) 句式与口语密度

- 口语密度高：粤语白话直写，像男人在酒后说话；语气词少、判断句多；书面语只在点题处出现。 `impression`

## (5) 情感弧线

- 起：一个漂泊者在路上进场；转：爱与痛同时被点破，进退两难；合：副歌收在认命而非认输的判断上，结尾留路、不留答案。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：浪子与道路意象、白话承重情、爱与痛并置、认命式收束、重复推进情感。
- 不该写：华丽古风意象、直白说教、无路可走的抽象抒情、顺口的廉价排比、哭诉式煽情。
- Negative prompt: `No ornate archaic imagery, no direct preaching, no abstract lyricism without a road, no forced rhyme, no weeping sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Poon Yuen-leung, lyrics about a man buying oden at a convenience store late at night, thinking of a road he never finished. Verse, chorus, bridge.`
- 中文对照：潘源良风格：浪子之心，白话承重情，粤语口语节奏，爱情是一条走不完的路。题目：lyrics about a man buying oden at a convenience store late at night, thinking of a road he never finished。主歌、副歌、桥段。
- Negative: `No ornate archaic imagery, no direct preaching, no abstract lyricism without a road, no forced rhyme, no weeping sentimentality`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
