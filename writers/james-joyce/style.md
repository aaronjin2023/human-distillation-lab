# James Joyce — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Joyce: stream of consciousness, interior monologue, epiphany in the ordinary, Dublin in exact street-by-street detail, language that bends and breaks, myth under the everyday`
- ZH: 乔伊斯风格：意识流，内心独白，日常中的顿悟，都柏林按街道逐一写实的细节，弯曲甚至断裂的语言，日常之下的神话结构。

## (2) 句式与节奏

句长：长短剧烈交错——内心独白可以是一整页无标点的长流，对话与动作描写则短促、碎片；《尤利西斯》最后一章是著名的无标点长流，而‘风’一章又近乎电报体。节奏：一天（《尤利西斯》）被拉成七百多页，时间密度极高；章节之间换体裁、换文体、换视角，节奏靠章节切换驱动。`impression`

## (3) 词汇与意象

词汇：都柏林方言、拉丁语、法语词、造词与双关并置；日常词（肥皂、肾、土豆）与神话词（奥德修斯、代达罗斯）同处一句。意象群：都柏林的街道、酒馆、教堂与海；水与溺亡、眼睛与凝视、食物与身体；《都柏林人》的‘瘫痪’意象（雪、灰尘、寂静）。禁词/禁意象：不用全知叙述者的解释性议论，不用抒情的、脱离都柏林具体细节的抽象升华。`impression`/`artifact`

## (4) 叙事视角与结构

视角：早期第三人称限知（《都柏林人》《画像》），《尤利西斯》发展为自由间接引语 + 内心独白 + 多视角轮换，同一事件在不同人物意识中呈现不同形状；叙述者时而消失、时而以戏拟的文体出现。结构：单日环形（《尤利西斯》以奥德赛十八章对应一天）、短篇集的‘童年—青年—成年—公众生活’递进；开头多为场景切入（一个街角、一次葬礼），结尾多为顿悟（epiphany）或无标点的意识长流。对话：对话即意识的碎片，常无引号、无提示语，靠排版与破折号区分。`verbatim`

## (5) 语气与距离

语气：冷峻的观察与温柔的同情并存；反讽是核心——对都柏林的瘫痪既批判又眷恋；与读者的距离是设谜式的：典故、双关与文体游戏要求读者主动解码。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：都柏林（或任何一座城市）的街道、酒馆与日常琐事；一个普通人的内心独白；日常细节中突然降临的顿悟；神话结构套在平凡一日之上；语言的游戏与变形。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No omniscient explanatory commentary, no sentimental uplift, no plot-driven suspense, no plain journalistic reportage`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of James Joyce, a man buys oden at a convenience store late at night. Stream of consciousness, no quotation marks, the steam, the dashi, the price tag, a snatch of a song, and suddenly an epiphany about his father. Dublin detail transposed to a modern city street. Myth under the everyday.`
- 中文对照：乔伊斯风格，一个人在深夜便利店买关东煮。意识流，无引号，蒸汽、高汤、价签、一句歌词，忽然降临关于父亲的顿悟；都柏林式的街道写实移到现代城市；日常之下的神话。
- Negative: `omniscient explanatory commentary, sentimental uplift, plot-driven suspense, plain journalistic reportage`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
