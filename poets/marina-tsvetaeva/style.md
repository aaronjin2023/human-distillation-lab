# Marina Tsvetaeva — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marina Tsvetaeva: broken syntax and dashes, the rowan tree and the road, farewell as a form, exile as a rhythm, emotion at full pitch with nothing held back`
- ZH: 茨维塔耶娃风格：断裂的句法与破折号，花楸树与道路，分手即形式，流亡即节奏，情感满格，毫无保留。

## (2) 意象

- 花楸树（故乡与苦涩）
- 天鹅（《天鹅之歌》的白军挽歌）
- 道路与分手（流亡的节奏）
- 火与信（书信体的炽热）
- 捷克与布拉格（流亡的居所）
- 禁意象：克制的冷静、温和的和解
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 句式断裂：破折号、省略、短句跳接，节奏急促如心跳；长句少，短句密；《天鹅之歌》以组诗推进，情感满格；晚期节奏更碎、更急。

## (4) 语言密度与词汇

- 词汇：情感词极密（爱、恨、别、火），动词多为炽热态（烧、撕、喊）；善用破折号压缩意义，一折抵一句；禁词：克制的冷静词、温和的和解语、冗长的过渡。

## (5) 结构习惯

- 单篇多以呼告起兴，情感迸发—断裂—再迸发；组诗《天鹅之歌》以挽歌推进；书信体诗以“你”为轴，情感直陈；结尾多为戛然而止或呼告。

## (6) 该写什么 / 不该写什么

- 该写：
- 断裂句法与破折号
- 花楸树、天鹅、分手的意象
- 情感满格的呼告
- 流亡的节奏
- 不该写：
- 克制的冷静与温和和解
- 冗长过渡与解释
- 工整的格律收束
- 温情的安慰
- Negative prompt: `No cool restraint, no mild reconciliation, no long explanatory transitions, no neat metrical closure, no sentimental consolation, no holding back`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Marina Tsvetaeva, a small Yorkshire terrier sits on a subway seat at night. Broken syntax and dashes, the rowan tree of the carriage, farewell as a form, the dog as a small exile, emotion at full pitch, an ending that breaks off.`
- 中文对照：茨维塔耶娃风格：一只约克夏犬深夜坐在地铁座位上。断裂的句法与破折号，车厢里的花楸树，分手即形式，狗是一个小小的流亡者，情感满格，结尾戛然而止。
- Negative: `No cool restraint, no reconciliation, no long transitions, no neat closure, no holding back`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
