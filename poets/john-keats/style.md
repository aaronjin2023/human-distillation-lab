# John Keats — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Keats: odes of sensuous beauty, nightingale and Grecian urn, beauty is truth, truth beauty, the senses opening into eternity`
- ZH: 约翰·济慈风格：感官之美的颂歌，夜莺与希腊古瓮，美即真，真即美，感官通向永恒。

## (2) 意象

- 主意象：夜莺、希腊古瓮、秋天、美、真、星；辅意象：葡萄酒、蜜蜂、月亮；禁意象：抽象议论、犬儒收束；密度高，意象多取自感官与古典，丰盛而克制。

## (3) 韵律与句式

- 以颂歌体（ode）为主，十行一节，句式长短交错，善用跨行与排比；节奏如感官的潮汐，快慢交替，朗读时有丰盛的停顿。

## (4) 语言密度与词汇

- 词汇感官而丰盛：色彩词、味道词、声音词密集；动词温柔；形容词丰富而不堆砌；禁词：抽象大词、犬儒词。

## (5) 结构习惯

- 颂歌式结构：每首颂歌五至十节，以意象推进；开头多直入感官意象（夜莺、古瓮），结尾多以警句收束（美即真）；视角多为第一人称沉思者；推进靠感官递进与哲思翻转。

## (6) 该写什么 / 不该写什么

- 该写：夜莺与古瓮、秋天与美；感官丰盛的颂歌体、美即真的警句；感官通向永恒。
- 不该写：风格上的禁区——abstract discourse without a sense, no cynical ending, no ironic detachment, no flat prosaic lines, no sentimental sweetness。
- Negative prompt: `No abstract discourse without a sense, no cynical ending, no ironic detachment, no flat prosaic lines, no sentimental sweetness`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of John Keats, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Odes of sensuous beauty, nightingale and Grecian urn, beauty is truth, truth beauty, the dog as a small urn.`
- 中文对照：济慈风格：一只约克夏犬深夜坐在地铁座位上。感官之美的颂歌，夜莺与希腊古瓮，美即真，真即美，狗是一只小古瓮。
- Negative: `No abstract discourse without a sense, no cynical ending, no ironic detachment, no flat prosaic lines, no sentimental sweetness`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
