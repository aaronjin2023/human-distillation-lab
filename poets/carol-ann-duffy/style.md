# Carol Ann Duffy — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carol Ann Duffy: plain speech with a lyric lift, the dramatic monologue that gives the silenced a voice, the onion as a valentine, wives and mothers speaking back, tenderness and anger in one line`
- ZH: 达菲风格：平实的语言带抒情的 lift，戏剧独白让沉默者发声，洋葱即情人节礼物，妻子与母亲们回话，温柔与愤怒同在一行诗里。

## (2) 意象

- 洋葱（《情人节》：以洋葱代玫瑰）
- 妻子的声音（《世界之妻》的代言体）
- 手与厨房（日常的亲密）
- 河与时间（《平均时间》）
- 母亲与女儿（《在你出生之前》）
- 禁意象：华丽的修辞、抽象的大词
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体短行，口语化、节奏轻快；戏剧独白以一人之声推进，停顿即转折；《平均时间》以短章相接；整体节奏由独白的戏剧性向抒情的简演变。

## (4) 语言密度与词汇

- 词汇：日常词极准（洋葱、手、厨房、河），口语与抒情并置；抽象词借日常物落地；禁词：华丽形容词、宏大抽象词、直白说教词。

## (5) 结构习惯

- 戏剧独白：以一人（妻子、母亲、神话女性）之声起兴，独白推进，末句翻转；单篇多以日常一物起兴，情感—翻转—收束；组诗《世界之妻》以代言体对照神话。

## (6) 该写什么 / 不该写什么

- 该写：
- 戏剧独白与代言体
- 洋葱、手、厨房的日常意象
- 平实语言的抒情 lift
- 末句翻转
- 不该写：
- 华丽修辞与抽象大词
- 直白说教
- 冗长铺陈
- 温情的安慰收束
- Negative prompt: `No ornate rhetoric, no grand abstract words, no direct preaching, no long explanatory passages, no sentimental consolation, no voice without a body`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Carol Ann Duffy, a small Yorkshire terrier sits on a subway seat at night. A dramatic monologue in plain speech, the dog as a valentine onion, the commuters' wives speaking back, tenderness and anger in one line, a closing reversal.`
- 中文对照：达菲风格：一只约克夏犬深夜坐在地铁座位上。平实语言的戏剧独白，狗是一颗情人节的洋葱，乘客们的妻子们回话，温柔与愤怒同在一行诗里，结尾翻转。
- Negative: `No ornate rhetoric, no grand abstractions, no preaching, no long passages, no sentimental consolation, no disembodied voice`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
