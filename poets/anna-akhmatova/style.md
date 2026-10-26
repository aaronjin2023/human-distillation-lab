# Anna Akhmatova — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anna Akhmatova: spare quatrains, a domestic detail as witness, silence as testimony, the queue outside the prison, love and terror in one small room, nothing wasted`
- ZH: 阿赫玛托娃风格：简省的四行诗，家居细节即见证，沉默即证词，监狱外的长队，爱与恐怖同在一间小屋里，一字不多。

## (2) 意象

- 窗与烛（小屋里的光）
- 监狱外的长队（《安魂曲》的见证）
- 石与雪（圣彼得堡的冷）
- 祈祷与沉默（见证的语言）
- 手套与披巾（日常物的重量）
- 禁意象：宏大的颂歌、华丽的修辞堆砌
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 四行诗与短行体为主，格律工整、收束有力；《安魂曲》以组诗推进，短章相接、沉默为节；句式简省，长短交错，停顿即意义；晚期节奏更慢、更重。

## (4) 语言密度与词汇

- 词汇：日常词极准（窗、烛、手套、雪），抽象词极少；以细节压缩意义，一物抵一节；禁词：华丽形容词、宏大颂歌词、直白的政治口号。

## (5) 结构习惯

- 单篇多以一物（窗、手套）起兴，细节—沉默—收束三段；《安魂曲》以十章加序跋，个人见证与集体长队对照；组诗以沉默而非叙事推进。

## (6) 该写什么 / 不该写什么

- 该写：
- 简省四行诗与家居细节
- 沉默即见证
- 监狱长队的集体见证
- 一物抵一节的密度
- 不该写：
- 宏大颂歌与华丽修辞
- 直白的政治口号
- 冗长铺陈
- 温情的安慰收束
- Negative prompt: `No grand panegyric, no ornate rhetoric, no direct political slogans, no long explanatory passages, no sentimental consolation, no wasted words`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Anna Akhmatova, a small Yorkshire terrier sits on a subway seat at night. Spare quatrains, a small detail as witness, silence as testimony, the queue of commuters as a prison queue, love and terror in one small carriage, nothing wasted.`
- 中文对照：阿赫玛托娃风格：一只约克夏犬深夜坐在地铁座位上。简省的四行诗，一个小细节即见证，沉默即证词，乘客的队伍如监狱外的长队，爱与恐怖同在一节车厢里，一字不多。
- Negative: `No grand panegyric, no ornate rhetoric, no slogans, no long passages, no sentimental consolation`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
