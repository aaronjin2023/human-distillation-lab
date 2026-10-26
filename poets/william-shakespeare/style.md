# William Shakespeare — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shakespeare: the English sonnet perfected, time and beauty and love in antithesis, plain words that turn and shine`
- ZH: 莎士比亚风格：英国十四行诗的完善，时间、美与爱在对仗中，朴素词语一转即发光。

## (2) 意象

- 主意象：时间、美、爱、玫瑰、夏天、镜子；辅意象：海、星、夜、梦；禁意象：抽象议论、口号；密度中等，意象多取自自然与日常，对仗精严。

## (3) 韵律与句式

- 英国十四行诗（三四行 + 对句，转折在第十三行）；句式精确、音乐性强，善用对仗与排比；叙事诗以双韵体写成；节奏平稳而有力，朗读时如独白。

## (4) 语言密度与词汇

- 词汇丰富而精确：日常词承载大义；动词有力；形容词少而重；善用双关与悖论；禁词：口号、抽象空话。

## (5) 结构习惯

- 诗集式结构：《十四行诗集》154 首，青年组、黑夫人组、竞争诗人组；开头多直入意象或质问，结尾对句（couplet）收束全诗；视角多为第一人称恋人；推进靠对仗翻转与对句收束。

## (6) 该写什么 / 不该写什么

- 该写：时间与美、爱与玫瑰、夏天的短暂；英国十四行的对句收束、双关与悖论；朴素词语的发光。
- 不该写：风格上的禁区——political slogans, no abstract discourse without an image, no sentimental sweetness, no loose unstructured lines, no direct preaching。
- Negative prompt: `No political slogans, no abstract discourse without an image, no sentimental sweetness, no loose unstructured lines, no direct preaching`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Shakespeare, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. The English sonnet perfected, time and beauty in antithesis, plain words that turn and shine, the dog as a small summer's day.`
- 中文对照：莎士比亚风格：一只约克夏犬深夜坐在地铁座位上。英国十四行诗的完善，时间与美在对仗中，朴素词语一转即发光，狗是一个小小的夏日。
- Negative: `No political slogans, no abstract discourse without an image, no sentimental sweetness, no loose unstructured lines, no direct preaching`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
