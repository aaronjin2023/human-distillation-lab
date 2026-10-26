# John Donne — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Donne: metaphysical conceits, the compass and the flea, love and death argued in the same breath, wit that startles`
- ZH: 约翰·多恩风格：玄学派巧喻，圆规与跳蚤，爱与死在同一口气里辩论，机智令人一惊。

## (2) 意象

- 主意象：圆规、跳蚤、指南针、死亡、爱、灵魂；辅意象：地图、钟、血；禁意象：田园闲适、直白抒情；密度极高，意象多取自科学、地理与日常，巧喻一喻多义。

## (3) 韵律与句式

- 以十四行诗与歌谣体并行，句式突兀、倒装多，善用跨行与停顿；节奏如辩论，快慢交替，朗读时有急转与重音。

## (4) 语言密度与词汇

- 词汇博学而突兀：科学词、地理词、神学词并置；动词直接；形容词少而重；禁词：华丽堆砌、田园套话。

## (5) 结构习惯

- 短诗为主，组诗成集；开头多直入巧喻（跳蚤、圆规），结尾多以悖论或警句收束；视角多为第一人称恋人/沉思者；推进靠巧喻递进与论辩翻转。

## (6) 该写什么 / 不该写什么

- 该写：圆规与跳蚤、爱与死的巧喻；突兀的句法、论辩式推进；机智的警句收束。
- 不该写：风格上的禁区——pastoral ease, no smooth lyrical fluency, no sentimental sweetness, no abstract discourse without a conceit, no direct preaching。
- Negative prompt: `No pastoral ease, no smooth lyrical fluency, no sentimental sweetness, no abstract discourse without a conceit, no direct preaching`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮的人）

- Prompt: `In the style of John Donne, a person buys oden at a convenience store late at night. Metaphysical conceits, the compass and the flea, love and death argued in the same breath, wit that startles.`
- 中文对照：约翰·多恩风格：一个人深夜在便利店买关东煮。玄学派巧喻，圆规与跳蚤，爱与死在同一口气里辩论，机智令人一惊。
- Negative: `No pastoral ease, no smooth lyrical fluency, no sentimental sweetness, no abstract discourse without a conceit, no direct preaching`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
