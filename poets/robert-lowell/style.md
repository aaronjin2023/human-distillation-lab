# Robert Lowell — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Lowell: the confessional sonnet that will not look away, Boston family history as wound, the skunk at night, madness and history in one stanza, the dolphin that betrays`
- ZH: 洛威尔风格：不移开视线的忏悔十四行诗，波士顿家族史即伤口，夜里的臭鼬，疯狂与历史同在一节诗里，背叛的海豚。

## (2) 意象

- 臭鼬（《夜里的臭鼬》：夜行的见证）
- 家族史（波士顿的洛威尔家）
- 医院与疯狂（忏悔的现场）
- 海豚（《海豚》的背叛）
- 水族馆与海（《生命研究》的海）
- 禁意象：温情的安慰、轻佻的俏皮、抽象的大词
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 十四行诗组为主：以十四行诗写忏悔，句式工整、收束有力；《生命研究》以自由体与十四行诗交错；《历史》以组诗推进，短章相接；整体由《生命研究》的自由体向《海豚》的十四行诗组演变。

## (4) 语言密度与词汇

- 词汇：家族史词（波士顿、祖先、医院）极密，日常词与历史词并置；抽象词（疯狂、历史）借臭鼬与海豚落地；禁词：温情安慰词、轻佻俏皮词、抽象大词。

## (5) 结构习惯

- 十四行诗组：以组诗写家族史，单首可独立、组内有推进；单篇多以一景（臭鼬、医院）起兴，忏悔—对照—收束；《历史》以编年推进，结尾多为克制的收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 忏悔十四行诗组
- 家族史与医院的意象
- 臭鼬、海豚的物象
- 克制的收束
- 不该写：
- 温情安慰与轻佻俏皮
- 抽象大词
- 直白说教
- 冗长铺陈
- Negative prompt: `No sentimental consolation, no flippant quips, no grand abstract words, no direct preaching, no long explanatory passages, no looking away`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Robert Lowell, a small Yorkshire terrier sits on a subway seat at night. A confessional sonnet that will not look away, Boston family history as wound, the dog as a skunk at night, madness and history in one stanza, a restrained close.`
- 中文对照：洛威尔风格：一只约克夏犬深夜坐在地铁座位上。不移开视线的忏悔十四行诗，波士顿家族史即伤口，狗是夜里的臭鼬，疯狂与历史同在一节诗里，克制的收束。
- Negative: `No sentimental consolation, no flippant quips, no grand abstractions, no preaching, no long passages, no looking away`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
