# Adrienne Rich — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Adrienne Rich: re-vision as method, diving into the wreck, cartography of the difficult world, the body as evidence, silence broken open, a common language dreamed into being`
- ZH: 里奇风格：重看即方法，潜入沉船，困难世界的地图学，身体即证据，沉默被打开，共同的语言在梦中成形。

## (2) 意象

- 沉船（潜入沉船：重看历史）
- 地图与罗盘（困难世界的制图）
- 身体（证据与现场）
- 沉默（被打开的沉默）
- 共同语言（梦想的语言）
- 禁意象：温情的安慰、抽象的大词、直白的口号
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体长句与短章交错：《潜入沉船》以叙事长句推进，潜水即节奏；《共同语言的梦想》以短章并置；晚期以长句冥想推进；整体由叙事的潜入向冥想的制图演变。

## (4) 语言密度与词汇

- 词汇：身体词（手、眼、血）极密，地图词（罗盘、纬度）与重看词并置；抽象词（重看、沉默）借身体落地；禁词：温情安慰词、抽象大词、直白口号词。

## (5) 结构习惯

- 潜入体：以潜入（沉船）起兴，下潜—发现—上浮三段；组诗以重看推进，旧文本被重新阅读；单篇多以一景（沉船、地图）起兴，结尾多为重看的翻转而非收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 沉船、地图、身体的意象
- 重看的方法
- 自由体长句的潜入节奏
- 重看的翻转收束
- 不该写：
- 温情安慰与抽象大词
- 直白口号
- 冗长铺陈
- 封闭的收束
- Negative prompt: `No sentimental consolation, no grand abstract words, no direct slogans, no long explanatory passages, no closed conclusive ending, no silence left unopened`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Adrienne Rich, a small Yorkshire terrier sits on a subway seat at night. Diving into the wreck of the carriage, cartography of the difficult world, the dog as a body as evidence, silence broken open, a common language dreamed into being.`
- 中文对照：里奇风格：一只约克夏犬深夜坐在地铁座位上。潜入车厢的沉船，困难世界的地图学，狗是一个作为证据的身体，沉默被打开，共同的语言在梦中成形。
- Negative: `No sentimental consolation, no grand abstractions, no slogans, no long passages, no closed ending, no silence left unopened`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
