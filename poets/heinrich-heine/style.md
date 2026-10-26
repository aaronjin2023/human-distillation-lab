# Heinrich Heine — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Heinrich Heine: ironic lyric, the song that turns on itself, love and politics in the same stanza, wit that wounds and heals`
- ZH: 海因里希·海涅风格：反讽抒情，歌唱到一半自我翻转，爱与政治在同一节里，机智既伤人又疗伤。

## (2) 意象

- 主意象：歌、玫瑰、夜莺、莱茵河、德国、冬天；辅意象：月亮、海、流亡；禁意象：田园闲适、甜蜜粉饰；密度中等，意象多取自民歌与日常，反讽锋利。

## (3) 韵律与句式

- 以民歌体与自由体并行，《歌集》以短诗成组；句式短促、锋利，善用反讽翻转；节奏如民歌，快慢交替，朗读时有停顿与一惊。

## (4) 语言密度与词汇

- 词汇朴素而反讽：民歌词、日常词、政治词并置；动词直接；形容词少而重；禁词：华丽堆砌、甜蜜粉饰。

## (5) 结构习惯

- 短诗成组，诗集成集；开头多直入抒情（玫瑰、月亮），结尾多以反讽翻转收束；视角多为第一人称歌者；推进靠反讽递进。

## (6) 该写什么 / 不该写什么

- 该写：民歌体的抒情、反讽的翻转；爱与政治同行、玫瑰与莱茵河；机智的警句收束。
- 不该写：风格上的禁区——sentimental sweetness, no pastoral ease, no ornate excess, no direct preaching, no consoling happy ending。
- Negative prompt: `No sentimental sweetness, no pastoral ease, no ornate excess, no direct preaching, no consoling happy ending`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮的人）

- Prompt: `In the style of Heinrich Heine, a person buys oden at a convenience store late at night. Ironic lyric, the song that turns on itself, love and politics in the same stanza, wit that wounds and heals.`
- 中文对照：海涅风格：一个人深夜在便利店买关东煮。反讽抒情，歌唱到一半自我翻转，爱与政治在同一节里，机智既伤人又疗伤。
- Negative: `No sentimental sweetness, no pastoral ease, no ornate excess, no direct preaching, no consoling happy ending`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
