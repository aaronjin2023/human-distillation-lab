# Liu Zhuohui — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liu Zhuohui: rock idealism in plain Cantonese, the earth and the grey track, a generation's vow spoken without slogans`
- ZH: 刘卓辉风格：摇滚理想主义的粤语白话，大地与灰色轨迹，一代人的誓言，不喊口号。

## (2) 意象

- 大地意象群：大地、山河、故土，家国写进摇滚；轨迹意象群：灰色轨迹、足印、路，理想即一条走过的路；时间意象群：年月、变迁、旧日，时代感由具体年份与场景带出。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 粤语九声填词，韵脚配合摇滚节拍；主歌叙事长句、副歌短句齐唱感强；换韵处即情绪高点；善用重复句制造合唱感。 `impression`

## (4) 句式与口语密度

- 口语密度高：粤语白话直写，少书面雅词；语气词克制；多用第二人称召唤，副歌有合唱感。 `impression`

## (5) 情感弧线

- 起：一个具体场景或一代人的处境进场；转：理想与现实撞上，情绪翻面；合：副歌收在誓言式短句上，不解释、只立誓。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：大地与轨迹意象、一代人的誓言句、白话摇滚节奏、副歌合唱感、具体场景写时代。
- 不该写：空洞口号、华丽古风意象、无场景的抽象议论、哭诉式煽情、解释性说教。
- Negative prompt: `No empty slogans, no ornate archaic imagery, no abstract commentary without a scene, no forced rhyme, no weeping sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Liu Zhuohui, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：刘卓辉风格：摇滚理想主义的粤语白话，大地与灰色轨迹，一代人的誓言，不喊口号。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No empty slogans, no ornate archaic imagery, no abstract commentary without a scene, no forced rhyme, no weeping sentimentality`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
