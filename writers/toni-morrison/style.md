# Toni Morrison — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Toni Morrison: lyrical, haunted prose, shifting voices, memory as a living presence, Black women's interior lives, the past breaking into the present, biblical cadence, no easy resolution`
- ZH: 托妮·莫里森风格：抒情而萦绕不去的散文，多声部转换，记忆如活物般闯入现在，黑人女性的内心世界，过去撕裂现在，圣经式节奏，不给廉价和解。

## (2) 句式与节奏

- 句式：句长长短交错：抒情长句绵延如歌，间以短促的断言句与对话碎片；段落常以一个意象起笔，再层层回旋。
- 节奏：节奏缓慢而回环：时间不直线前进，记忆闪回与现在交织；章节切分如潮汐，一段高潮后必有一段静默的余波。

## (3) 词汇与意象

- 词汇：词汇：日常口语与圣经语言并置，身体、家、鬼魂、水、飞行、乳汁等意象反复出现；爱用重复与变奏，同一词在不同语境中换义。
- 意象：意象群：鬼魂与萦绕（《宠儿》中的鬼孩）、水与飞行（《所罗门之歌》的飞翔）、眼睛与蓝（《最蓝的眼睛》的蓝眼睛）、家与社区、树与血。
- 禁词/禁意象：禁词/禁意象：不写扁平的受害者控诉，不写直白的政治口号，不用冷冰冰的社会学语言代替人物内心。

## (4) 叙事视角与结构

- 视角：叙事视角：多声部、流动的第三人称，时而滑入人物内心独白；叙述者时而全知、时而只给碎片，读者须自己拼合真相。
- 结构：结构：非线性，过去与现在交错，结局常开放或回环；开头多为一个场景或一句断言（如《宠儿》开篇的鬼屋），结尾不收束而留回响。

## (5) 语气与距离

- 语气：语气：庄重、悲悯而坚定，与人物保持亲近又不失审判的距离；对读者设谜，不直说，只让意象说话。

## (6) 该写什么 / 不该写什么

- 该写：该写：记忆与鬼魂、黑人社区的口述传统、母女与姐妹关系、语言本身的音乐性、历史创伤在日常生活中的回响。
- 不该写：不该写：廉价的和解与大团圆、直白的说教、把人物写成符号、情节驱动的快节奏悬念。
- Negative prompt: `No sentimental happy ending, no flat victim narrative, no direct political preaching, no linear plot-driven suspense, no cold sociological language`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Toni Morrison, a woman buys oden at a convenience store late at night in a modern city. The steam carries her back to a kitchen she has not seen in thirty years. Lyrical sentences, shifting voices, memory breaking into the present. No easy resolution.`
- 中文对照：托妮·莫里森风格，一位女子深夜在便利店买关东煮，蒸汽把她带回三十年未见的厨房。抒情长句，多声部，记忆闯入现在，不给廉价和解。
- Negative: `sentimental happy ending, flat victim narrative, direct preaching, linear suspense`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
