# Percy Bysshe Shelley — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shelley: prophetic lyric, west wind and cloud, love and liberty in soaring lines, the poet as unacknowledged legislator`
- ZH: 珀西·比希·雪莱风格：预言式抒情，西风与云，爱与自由在高飞的行里，诗人是未被承认的立法者。

## (2) 意象

- 主意象：西风、云、普罗米修斯、爱、自由、星；辅意象：夜莺、百灵、月亮；禁意象：田园闲适、犬儒收束；密度高，意象多取自自然与神话，高飞而热烈。

## (3) 韵律与句式

- 以自由体与十四行并行，《西风颂》以三行连锁体（terza rima 变体）写成；句式长短交错，善用排比与跨行；节奏如风，快慢交替，朗读时有高飞感。

## (4) 语言密度与词汇

- 词汇热烈而高飞：自然词、神话词、自由词并置；动词有力；形容词丰富；禁词：犬儒词、口语俚语。

## (5) 结构习惯

- 抒情长诗与短诗并行：《西风颂》五节，以风推进；《阿多尼斯》以挽歌体写济慈；开头多直入自然意象（西风、云），结尾多以预言或希望收束；视角多为第一人称歌者；推进靠意象递进与预言翻转。

## (6) 该写什么 / 不该写什么

- 该写：西风与云、普罗米修斯与自由；高飞的长行、预言式收束；爱与自由同行。
- 不该写：风格上的禁区——pastoral ease, no cynical ending, no ironic detachment, no abstract discourse without an image, no flat prosaic lines。
- Negative prompt: `No pastoral ease, no cynical ending, no ironic detachment, no abstract discourse without an image, no flat prosaic lines`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮的人）

- Prompt: `In the style of Shelley, a person buys oden at a convenience store late at night. Prophetic lyric, west wind and cloud, love and liberty in soaring lines, the steam as a small west wind.`
- 中文对照：雪莱风格：一个人深夜在便利店买关东煮。预言式抒情，西风与云，爱与自由在高飞的行里，热气如一阵小西风。
- Negative: `No pastoral ease, no cynical ending, no ironic detachment, no abstract discourse without an image, no flat prosaic lines`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
