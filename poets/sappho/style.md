# Sappho — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sappho: Sapphic stanza, brief burning lines, the body in love and longing, a fragment that is whole`
- ZH: 萨福风格：萨福体，短促而炽热的行，恋爱中的身体与渴望，残篇即完整。

## (2) 意象

- 主意象：阿佛洛狄忒、爱、月亮、玫瑰、苹果、身体的颤抖；辅意象：麻雀、风、海；禁意象：史诗式战争场面、抽象议论；密度高，意象多取自身体与自然，短行承载大情。

## (3) 韵律与句式

- 萨福体（Sapphic stanza）：三行长行加一行短行，韵律严整；句式短促，善用跨行与停顿；节奏如心跳，快慢交替，朗读时有呼吸的颤抖。

## (4) 语言密度与词汇

- 词汇炽热而精确：身体词、自然词、神名并置；动词多为颤抖、燃烧、渴望；形容词少而重；禁词：史诗式程式语、抽象大词。

## (5) 结构习惯

- 短诗与残篇：仅《致阿佛洛狄忒》完整传世，其余多为残篇；开头多直入呼告（阿佛洛狄忒），结尾多以祈求或宣告收束；视角多为第一人称恋人；推进靠情感递进与意象并置。

## (6) 该写什么 / 不该写什么

- 该写：阿佛洛狄忒的呼告、身体的颤抖、月亮与玫瑰；萨福体的短行与停顿；残篇的完整感。
- 不该写：风格上的禁区——epic battle scenes, no abstract discourse without a body, no detached academic tone, no loose unstructured lines, no sentimental sweetness。
- Negative prompt: `No epic battle scenes, no abstract discourse without a body, no detached academic tone, no loose unstructured lines, no sentimental sweetness`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮的人）

- Prompt: `In the style of Sappho, a person buys oden at a convenience store late at night. Sapphic stanza, brief burning lines, the body in longing, the steam as a small goddess. A fragment that is whole.`
- 中文对照：萨福风格：一个人深夜在便利店买关东煮。萨福体，短促而炽热的行，渴望中的身体，热气如一位小女神。残篇即完整。
- Negative: `No epic battle scenes, no abstract discourse without a body, no detached academic tone, no loose unstructured lines, no sentimental sweetness`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
