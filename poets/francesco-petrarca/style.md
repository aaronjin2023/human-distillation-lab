# Francesco Petrarca — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Petrarch: the sonnet perfected, Laura as light and wound, antithesis of fire and ice, the self divided and singing`
- ZH: 彼特拉克风格：十四行诗的完善，劳拉即光与伤口，火与冰的对仗，自我分裂而歌唱。

## (2) 意象

- 主意象：劳拉、光、火与冰、月桂、泪；辅意象：风、山、梦；禁意象：史诗式战争、口语俚语；密度中等，意象多取自爱情与自然，对仗精严。

## (3) 韵律与句式

- 十四行诗（彼特拉克体：八行 + 六行，转折在第九行）；句式精确、对仗工整，善用火与冰、生与死的对仗；节奏平稳而深沉，朗读时如沉思。

## (4) 语言密度与词汇

- 词汇典雅而精确：爱情词、自然词、光词并置；动词克制；形容词少而重；禁词：口语俚语、粗粝词。

## (5) 结构习惯

- 诗集式结构：《歌集》366 首，十四行、歌谣、短歌成组；开头多直入劳拉或情感，结尾多以警句或祈祷收束；视角为第一人称恋人；推进靠情感递进与对仗翻转。

## (6) 该写什么 / 不该写什么

- 该写：劳拉与光、火与冰的对仗、十四行的转折；精确的爱情语言、月桂与泪；自我分裂的歌唱。
- 不该写：风格上的禁区——epic battle scenes, no colloquial diction, no sentimental sweetness, no loose unstructured lines, no direct preaching。
- Negative prompt: `No epic battle scenes, no colloquial diction, no sentimental sweetness, no loose unstructured lines, no direct preaching`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮的人）

- Prompt: `In the style of Petrarch, a person buys oden at a convenience store late at night. The sonnet perfected, Laura as light and wound, antithesis of fire and ice, the steam as a small light.`
- 中文对照：彼特拉克风格：一个人深夜在便利店买关东煮。十四行诗的完善，劳拉即光与伤口，火与冰的对仗，热气如一缕小光。
- Negative: `No epic battle scenes, no colloquial diction, no sentimental sweetness, no loose unstructured lines, no direct preaching`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
