# Federico García Lorca — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Federico García Lorca: Andalusian ballad, green green, blood and moon and horse, the duende that rises through the body, love and death in the same verse, a song that ends in silence`
- ZH: 洛尔卡风格：安达卢西亚谣曲，绿呀绿，血与月亮与马，贯穿身体的‘杜恩德’（精灵），爱与死在同一诗行里，一首歌以沉默收束。

## (2) 句式与节奏

句长：诗行短促、重复、如歌谣般回环（‘绿呀，我要你绿’），间以长句的抒情爆发；戏剧对白短促、如刀切。节奏：谣曲式的重复推进，靠叠句与意象的回环而非叙事推进；《血的婚礼》三幕以婚礼—逃亡—死亡的仪式节奏推进。`verbatim`

## (3) 词汇与意象

词汇：西班牙语日常词与吉卜赛、安达卢西亚方言词并置；颜色词极密（绿、红、白、黑），身体词（血、手、胸、马）与自然词（月亮、橄榄树、河）并置。意象群：绿（未实现的欲望）、月亮（死亡的见证）、马（欲望与死亡的坐骑）、血（婚礼与葬礼的同一颜色）、水（洗不净的）；意象靠重复获得重量。禁词/禁意象：不用抽象的哲理议论，不用城市的现代器物词，不用冷静的旁观语调。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称抒情‘我’与第三人称的谣曲叙述交替；戏剧中人物直接说话，叙述者退场。结构：谣曲的叠句结构、戏剧的三幕仪式结构；开头多为一个意象的呼告（‘绿呀’），结尾多为死亡或沉默。对话：戏剧对话短促、如歌，人物靠重复与叠句暴露命运。`impression`

## (5) 语气与距离

语气：热烈、悲怆、带歌谣的庄重；与人物的距离是同情的凝视；与读者的距离是邀约式的——请读者听一首歌，而不是读一篇论文。反讽极少，悲悯是主调。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：安达卢西亚的谣曲；绿、月亮、马、血的意象；爱与死在同一诗行里；杜恩德（duende）贯穿身体的瞬间；一首歌以沉默收束。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No abstract philosophising, no modern urban gadgets, no cool detachment, no explanatory commentary, no ironic distance`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Federico García Lorca, a man buys oden at a convenience store late at night. A ballad, green green, the steam like a moon. Blood and salt. The clerk's hands, the fluorescent light, a song that ends in silence. Love and death in the same verse.`
- 中文对照：洛尔卡风格，一个人在深夜便利店买关东煮。一首谣曲，绿呀绿，蒸汽像月亮；血与盐；店员的手、日光灯，一首歌以沉默收束；爱与死在同一诗行里。
- Negative: `abstract philosophising, modern urban gadgets, cool detachment, explanatory commentary, ironic distance`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
