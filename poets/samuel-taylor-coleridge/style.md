# Samuel Taylor Coleridge — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Coleridge: supernatural ballads, the albatross and Kubla Khan, imagination as a shaping power, music that haunts`
- ZH: 塞缪尔·泰勒·柯勒律治风格：超自然歌谣，信天翁与忽必烈汗，想象即塑造的力量，音乐令人萦绕。

## (2) 意象

- 主意象：信天翁、海、冰、忽必烈汗、月亮、梦；辅意象：蛇、水、风；禁意象：都市浮华、直白议论；密度高，意象多取自超自然与东方想象，音乐性极强。

## (3) 韵律与句式

- 以歌谣体与自由体并行，《古舟子咏》以四行歌谣体写成；句式长短交错，善用重复与叠咏；节奏如歌谣，快慢交替，朗读时有音乐的萦绕感。

## (4) 语言密度与词汇

- 词汇古雅而音乐：古语词、自然词、东方词并置；动词有力；形容词少而重；禁词：口语俚语、抽象空话。

## (5) 结构习惯

- 叙事歌谣式：《古舟子咏》以老水手讲故事推进；《忽必烈汗》以梦境片段成篇；开头多直入超自然场景，结尾多以道德或梦醒收束；视角多为第一人称叙事者；推进靠叙事与音乐交替。

## (6) 该写什么 / 不该写什么

- 该写：信天翁与海、忽必烈汗与梦；歌谣体的音乐性、超自然想象；想象即塑造的力量。
- 不该写：风格上的禁区——urban flashiness, no abstract discourse without an image, no plain prosaic lines, no ironic detachment, no cynical ending。
- Negative prompt: `No urban flashiness, no abstract discourse without an image, no plain prosaic lines, no ironic detachment, no cynical ending`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Coleridge, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Supernatural ballads, the albatross and Kubla Khan, imagination as a shaping power, music that haunts.`
- 中文对照：柯勒律治风格：一只约克夏犬深夜坐在地铁座位上。超自然歌谣，信天翁与忽必烈汗，想象即塑造的力量，音乐令人萦绕。
- Negative: `No urban flashiness, no abstract discourse without an image, no plain prosaic lines, no ironic detachment, no cynical ending`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
