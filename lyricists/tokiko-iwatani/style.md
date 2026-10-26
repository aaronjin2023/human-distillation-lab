# Tokiko Iwatani — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tokiko Iwatani: a woman's graceful farewell, night fog and holidays, elegant Japanese diction, love spoken softly and left unsaid`
- ZH: 岩谷时子风格：女性的优雅告别，夜雾与假期，雅致日语，爱情轻声说、留一半不说。

## (2) 意象

- 夜意象群：夜雾、夜、星，夜是告别的场；假期意象群：恋之假期、旅、别离，假期即短暂的爱；永恒意象群：直到永远、永远，短暂对照永恒。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语歌谣曲：音拍优雅、韵脚柔和；主歌长句铺场景、副歌短句收束；换韵克制；善用留白。 `impression`

## (4) 句式与口语密度

- 口语密度中：日常口语优雅入词，书面词只在夜景句出现；独白感强；语气词温和。 `impression`

## (5) 情感弧线

- 起：一个夜或假期场景进场；转：告别点破，情绪翻面；合：副歌收在优雅的告别短句上，结尾留白、不解释。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：夜与假期意象、优雅告别、留白、短暂对照永恒、雅词入韵。
- 不该写：直白口号、大白话、廉价煽情、解释性议论、华丽辞藻。
- Negative prompt: `No plain slogans, no plain vernacular, no cheap sentimentality, no explanatory commentary, no ornate diction`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tokiko Iwatani, lyrics about a man buying oden at a convenience store late at night, thinking of a holiday that ended. Verse, chorus, bridge.`
- 中文对照：岩谷时子风格：女性的优雅告别，夜雾与假期，雅致日语，爱情轻声说、留一半不说。题目：lyrics about a man buying oden at a convenience store late at night, thinking of a holiday that ended。主歌、副歌、桥段。
- Negative: `No plain slogans, no plain vernacular, no cheap sentimentality, no explanatory commentary, no ornate diction`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
