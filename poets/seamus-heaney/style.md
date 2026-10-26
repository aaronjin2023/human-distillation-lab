# Seamus Heaney — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Seamus Heaney: the spade and the bog, digging as memory, consonants you can chew, the Troubles held at arm's length, the local made universal without leaving the parish`
- ZH: 希尼风格：铁锹与泥炭沼，挖掘即记忆，可以咀嚼的辅音，北爱冲突保持一臂之距，地方的即普遍的，不出教区而抵达普遍。

## (2) 意象

- 铁锹与挖掘（《挖掘》：以笔代锹）
- 泥炭沼与沼泽人（历史的保存）
- 黑莓与青蛙（童年的自然）
- 石头与雨（德里郡的物）
- 区与环（晚期的环形）
- 禁意象：轻佻的都市风情、无根的抽象
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体与十四行诗并行：早期以自由体短行写自然，辅音密、节奏实；中期以十四行诗组写政治，句式工整；晚期以短行与对句求简；整体由泥土的实向冥想的简演变。

## (4) 语言密度与词汇

- 词汇：泥土词极密（泥炭、铁锹、黑莓、青蛙），辅音硬、音节实；抽象词借泥土物落地；禁词：轻佻俚语、无根抽象词、直白的政治口号。

## (5) 结构习惯

- 单篇多以一物（铁锹、黑莓）起兴，挖掘—记忆—收束三段；组诗《野外作业》以田野作业对照政治；《区与环》以环形结构收束一生；结尾多为克制的收束而非爆发。

## (6) 该写什么 / 不该写什么

- 该写：
- 铁锹、泥炭沼、黑莓的意象
- 挖掘即记忆的结构
- 辅音密实的语言
- 政治保持一臂之距
- 不该写：
- 轻佻都市风情
- 无根抽象议论
- 直白政治口号
- 煽情的爆发收束
- Negative prompt: `No frivolous urban chic, no rootless abstraction, no direct political slogans, no sentimental outburst, no loose formless verse, no explaining the symbol`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Seamus Heaney, a small Yorkshire terrier sits on a subway seat at night. The spade of the carriage, the bog of the crowd, digging as memory, consonants you can chew, the dog as a small parish, a restrained close.`
- 中文对照：希尼风格：一只约克夏犬深夜坐在地铁座位上。车厢里的铁锹，人群如泥炭沼，挖掘即记忆，可以咀嚼的辅音，狗是一个小小的教区，克制的收束。
- Negative: `No frivolous chic, no rootless abstraction, no slogans, no sentimental outburst, no formless verse, no explaining the symbol`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
