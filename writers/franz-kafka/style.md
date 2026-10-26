# Franz Kafka — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Franz Kafka: plain precise German, a calm bureaucratic surface, an absurd premise accepted without surprise, doors corridors and castles that never open, guilt without a crime, no explanation ever given`
- ZH: 卡夫卡风格：平实精确的德语，冷静的公文表面，一个荒诞的前提被毫无惊讶地接受，永远打不开的门、走廊与城堡，无罪之罪，永不解释。

## (2) 句式与节奏

句长：以中长句为主，句法清晰、从句规整，几乎不用普鲁斯特式的绵延；但段落常以一个平静的陈述句开始，随后被一个‘可是’轻轻推向荒诞。节奏：缓慢、均匀、近乎公文的平稳——荒诞不是靠加速，而是靠这种平稳与内容的反差产生。短篇（《变形记》《在流放地》）一气呵成；长篇（《审判》《城堡》）是同一处境的反复变奏，情节推进极少，靠场景的重复与微差推进。`impression`

## (3) 词汇与意象

词汇：日常德语、官僚术语（法庭、文件、申请、等待）、身体词（背、甲壳、腿）与空间词（门、走廊、楼梯、阁楼）为主；形容词克制，几乎不用华丽的比喻。意象群：门（打不开或不知通向何处）、城堡（看得见、到不了）、法庭（无处不在、无人负责）、虫与甲壳、饥饿与等待；意象不作象征解释，只作处境本身。禁词/禁意象：不用直白抒情、不用心理分析的术语、不用解释荒诞原因的议论。`impression`

## (4) 叙事视角与结构

视角：第三人称限知，紧贴主人公（格里高尔、约瑟夫·K、K）的感知；叙述者不比人物知道更多，读者与人物同样困惑。结构：以一个荒诞前提开篇（‘一天早上醒来变成虫’），随后按日常逻辑冷静推演，不解决、不收束；长篇多为未完成态，结尾戛然而止或不了了之。对话：对话多为询问与推诿——人物不断问‘我该找谁’‘手续是什么’，回答永远是‘再等等’‘去问别人’。`verbatim`

## (5) 语气与距离

语气：冷静、克制、近乎冷漠的陈述；与人物的距离是贴近而不安慰；与读者的距离是共谋式的困惑——叙述者不解释，读者只好自己困惑。幽默是干冷的、黑色的，常在最绝望处出现。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个荒诞前提被当作日常接受；无尽的等待、申请与推诿；打不开的门与到不了的城堡；无罪之罪与无法申辩的处境；身体的变形与异化。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No lyrical outpouring, no psychological jargon, no explanation of the absurd, no warm resolution, no heroic resistance`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Franz Kafka, a small Yorkshire terrier sits on a subway seat. Nobody is surprised. A conductor asks for its ticket; the dog has none; the other passengers look away. The doors open and close. No explanation is given. The dog waits.`
- 中文对照：卡夫卡风格，一只小约克夏犬坐在地铁座位上。没有人惊讶。列车员查票，狗没有票；其他乘客移开视线。车门开开关关。不作任何解释。狗在等待。
- Negative: `lyrical outpouring, psychological jargon, explanation of the absurd, warm resolution, heroic resistance`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
