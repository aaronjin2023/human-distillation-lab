# Paul Celan — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Celan: German broken open after the catastrophe, black milk of dawn, breath and ash and stone, neologisms that wound the language, silence as the loudest word, the no-man's-rose`
- ZH: 策兰风格：灾难之后被打碎的德语，清晨的黑牛奶，呼吸与灰烬与石头，造词如伤口，沉默是最响亮的词，无人之玫。

## (2) 意象

- 黑牛奶（《死亡赋格》的清晨）
- 灰烬与石头（焚毁与见证）
- 呼吸与气息（语言的最后余烬）
- 雪与无人的玫瑰（《无人的玫瑰》）
- 语言的格栅（言说即囚）
- 禁意象：流畅的抒情、完整的句法、安慰的隐喻
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 短行、断裂、停顿极多；《死亡赋格》以赋格式对位推进，句式重复变奏；后期诗行更短、更碎，标点即节奏；整体由赋格的音乐性向沉默的断裂演变。

## (4) 语言密度与词汇

- 词汇：造词极密（复合新词），日常德语词被拆解重组；抽象词极少，每词借灰烬与石头落地；禁词：流畅的抒情词、完整的从句、安慰的隐喻。

## (5) 结构习惯

- 《死亡赋格》以对位结构推进，重复与变奏；后期单篇多以一词（灰、石、息）起兴，断裂—沉默—再断裂；组诗以呼吸而非叙事推进；结尾多为沉默而非收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 黑牛奶、灰烬、石头的意象
- 断裂短行与沉默的停顿
- 造词与德语的拆解
- 赋格式的重复变奏
- 不该写：
- 流畅抒情与完整句法
- 安慰的隐喻
- 直白的控诉口号
- 温情的收束
- Negative prompt: `No fluent lyricism, no intact syntax, no consoling metaphor, no direct slogans, no sentimental closure, no explanatory paraphrase, no easy beauty`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Paul Celan, a small Yorkshire terrier sits on a subway seat at night. Black milk of dawn in the carriage, breath and ash and stone, the dog as a no-man's-rose, broken German, silence as the loudest word.`
- 中文对照：策兰风格：一只约克夏犬深夜坐在地铁座位上。车厢里是清晨的黑牛奶，呼吸与灰烬与石头，狗是一朵无人之玫，断裂的德语，沉默是最响亮的词。
- Negative: `No fluent lyricism, no intact syntax, no consoling metaphor, no slogans, no sentimental closure, no easy beauty`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
