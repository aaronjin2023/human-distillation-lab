# Miyuki Nakajima — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Miyuki Nakajima: thread and night, fate as a long line, plain words that suddenly turn philosophical, a song that outlives its singer`
- ZH: 中岛美雪风格：线与夜，命运是一条长线，白话忽然转哲理，一首歌比歌手活得久。

## (2) 意象

- 线意象群：线、结、缘，命运写成一条线；夜意象群：夜、雪、星，夜是思考的场；时代意象群：时代、地上之星、旅人，个人即时代。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语音拍填词，韵脚沉稳、换韵如命运转折；主歌叙事长句、副歌短句如箴言；善用重复与排比推进哲理。 `impression`

## (4) 句式与口语密度

- 口语密度中：日常口语入词，哲理句用书面语；对话感弱、独白感强；语气词克制。 `impression`

## (5) 情感弧线

- 起：一个夜或旅途场景进场；转：日常点破命运，情绪翻面；合：副歌收在箴言式短句上，结尾深远、不解释。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：线与夜的隐喻、日常转哲理、箴言式副歌、时代感、深远收束。
- 不该写：直白口号、廉价煽情、抽象议论无场景、华丽辞藻、轻飘收束。
- Negative prompt: `No plain slogans, no cheap sentimentality, no abstract commentary without a scene, no ornate diction, no lightweight endings`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Miyuki Nakajima, lyrics about a man buying oden at a convenience store late at night, thinking of a thread that never breaks. Verse, chorus, bridge.`
- 中文对照：中岛美雪风格：线与夜，命运是一条长线，白话忽然转哲理，一首歌比歌手活得久。题目：lyrics about a man buying oden at a convenience store late at night, thinking of a thread that never breaks。主歌、副歌、桥段。
- Negative: `No plain slogans, no cheap sentimentality, no abstract commentary without a scene, no ornate diction, no lightweight endings`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
