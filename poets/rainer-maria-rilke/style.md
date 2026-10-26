# Rainer Maria Rilke — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rainer Maria Rilke: the angel as terror and transformation, the thing-poem that turns the visible into the invisible, long elegiac sentences that open like a space, Orpheus singing the dead back into song`
- ZH: 里尔克风格：天使既是恐怖又是转化，物诗把可见转为不可见，哀歌的长句如空间般展开，奥尔甫斯把死者唱回歌中。

## (2) 意象

- 天使（恐怖之美，杜伊诺的呼告）
- 物（豹、喷泉、古罗马石棺：物诗的核心）
- 镜与敞开的空间（内在空间的意象）
- 奥尔甫斯与欧律狄刻（歌与失去）
- 童年与死亡（《哀歌》的两极）
- 禁意象：讽刺的俏皮、都市的轻佻
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 《新诗集》以十四行诗与八行体写物，句式工整、收束有力；《杜伊诺哀歌》以长句奔涌、跨行不断，呼告起兴；《奥尔甫斯十四行诗》以短句轻快、歌谣体推进；整体节奏由物诗的凝练向哀歌的绵长演变。

## (4) 语言密度与词汇

- 词汇：德语长复合词与抽象名词（敞开、转化、内在空间）极密，但每词借具体物落地；善用悖论（恐怖之美、丰盈的空无）；禁词：讽刺俏皮语、轻佻口语、直白说教。

## (5) 结构习惯

- 物诗：以一物（豹、喷泉）起兴，凝视—转化—收束三段；哀歌：以呼告起兴，层层追问，末节以悖论收束；十四行诗组：以奥尔甫斯为轴，歌与死对照推进。

## (6) 该写什么 / 不该写什么

- 该写：
- 天使的恐怖之美
- 物诗的凝视与转化
- 哀歌长句的呼告与追问
- 悖论式收束
- 不该写：
- 讽刺俏皮与都市轻佻
- 无物支撑的抽象议论
- 直白说教
- 琐碎日常絮叨
- Negative prompt: `No ironic quips, no urban frivolity, no abstract discourse without a thing, no direct preaching, no trivial daily chatter, no sentimental consolation`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Rainer Maria Rilke, a small Yorkshire terrier sits on a subway seat at night. The angel of the carriage, the dog as a thing to be gazed at until it turns invisible, long elegiac sentences, Orpheus singing the commuters back into song, a paradoxical close.`
- 中文对照：里尔克风格：一只约克夏犬深夜坐在地铁座位上。车厢里的天使，狗是一件被凝视直至转为不可见的物，哀歌的长句，奥尔甫斯把乘客唱回歌中，悖论式收束。
- Negative: `No ironic quips, no frivolity, no imageless abstraction, no preaching, no trivial chatter`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
