# Kabir — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kabir: plain doha couplets sung aloud, the weaver's loom and the potter's wheel, no temple and no mosque, God in the breath, paradox as a hammer, laughter at priests and pundits alike`
- ZH: 卡比尔风格：平实的双行多哈，可吟唱，织机与陶轮，不要寺庙也不要清真寺，神在呼吸里，悖论如锤，笑对祭司与学者

## (2) 意象

- 主意象：织机、陶轮、线、水、镜；辅意象：鸟、渔网、集市；禁意象：宫廷华美、繁复仪式描写；密度高，一联一悖论，意象来自织工日常。`impression`

## (3) 韵律与句式

- 多哈双行，口语节奏，可吟唱；句式短促警句化；节奏如织机往复，一问一答。`impression`

## (4) 语言密度与词汇

- 词汇：日常口语词（织、陶、水、线），少梵语典雅词；善用悖论与反问；禁词：繁复仪式术语、宫廷华美词、学院议论。`impression`

## (5) 结构习惯

- 单首双行或短歌独立；开头直入日常物，结尾以悖论或反问收束；视角第一人称织工歌者；推进靠悖论翻转。`impression`

## (6) 该写什么 / 不该写什么

- 该写：多哈双行、日常物喻神圣、悖论与反问、可吟唱的口语。
- 不该写：宫廷华美、繁复仪式描写、学院议论、教条宣讲。
- Negative prompt: `No courtly ornament, no elaborate ritual description, no academic argument, no doctrinal preaching, no ornate Sanskrit diction`

## (7) 测试提示词示例（现代题材：一只约克夏犬深夜坐在地铁座位上，乘客们看着它）

- Prompt: `In the style of Kabir, a small Yorkshire terrier sits on a subway seat at night. Plain doha couplets, the loom and the ticket gate, no temple and no mosque, God in the breath, paradox as a hammer.`
- 中文对照：卡比尔风格：一只约克夏犬深夜坐在地铁座位上。平实多哈双行，织机与检票口，不要寺庙也不要清真寺，神在呼吸里，悖论如锤
- Negative: `No courtly ornament, no elaborate ritual description, no academic argument, no doctrinal preaching, no ornate Sanskrit diction`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
