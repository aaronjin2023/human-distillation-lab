# Liu Chia-chang — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liu Chia-chang: sentimental Mandarin ballad lyrics, memory and homeland imagery, neat rhymed lines, singable chorus, no irony`
- ZH: 刘家昌风格：抒情国语歌谣，记忆与故土意象，工整押韵，副歌好唱，不写反讽。

## (2) 意象

- 意象群：往事、梅花、秋月、故乡、帘幕、梦；意象密度中等，明喻为主，象征直接；禁意象：冷峻都市、抽象哲理、讽刺。 `impression`

## (3) 韵律

- 押韵：句尾工整押韵，韵脚开口音多，主副歌同韵；句长整齐，多为 7 字句，换气规律；词曲双全，先词后曲者多。 `impression`

## (4) 句式与口语密度

- 句式：整齐短句为主，排比常见；口语密度中等偏高，书面语浅白；人称第一人称回忆独白。 `impression`

## (5) 情感弧线

- 情感弧线：起于往事追忆—中段情感上扬—副歌收在深情的咏叹上；结尾收束圆满或怅然，情感强度浓烈直接。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：往事与故土意象、工整押韵、副歌咏叹、深情直抒。
- 不该写：反讽与冷峻、抽象哲理议论、拗口长句。
- Negative prompt: `No irony, no cold urban cynicism, no abstract philosophising, no convoluted long lines, no detached commentary`

## (7) 测试提示词示例

- Prompt: `In the style of Liu Chia-chang, lyrics about a small Yorkshire terrier sitting on a subway seat, reminding an old man of his hometown. Sentimental Mandarin, memory imagery, neat rhyme, singable chorus. Verse, chorus.`
- 中文对照：刘家昌风格：写一只坐在地铁上的约克夏犬，让一位老人想起故乡。抒情国语，记忆意象，工整押韵，副歌好唱。
- Negative: `No irony, no cold urban cynicism, no abstract philosophising, no convoluted long lines, no detached commentary`
- 检验点：意象是否对位；韵脚是否顺口；副歌是否收在该作词人的情感弧线上；禁区写法是否出现。
