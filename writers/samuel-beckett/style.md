# Samuel Beckett — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Samuel Beckett: minimal stage, two figures waiting, language that fails and goes on failing, pauses and silences as text, nothing happens twice, I can't go on I'll go on`
- ZH: 贝克特风格：极简的舞台，两个等待的人，失败又不断失败的语言，停顿与沉默本身就是文本，什么都没发生，发生了两次，我不能继续，我继续。

## (2) 句式与节奏

句长：极短句为主，对话如碎片，间以长段的独白（莫洛伊、马龙的絮语）；停顿（pause、silence）是节奏的本体，一幕的停顿比台词更长。节奏：缓慢、循环，情节不推进，只重复与微差；《等待戈多》两幕结构几乎相同，第二幕是第一幕的微差重复。`impression`

## (3) 词汇与意象

词汇：日常词（鞋、帽子、胡萝卜、绳子）与抽象词（等待、虚无、时间）并置；‘什么都没有’高频出现。意象群：树（戈多里唯一的一棵树）、鞋与帽子（穿不上的、戴不上的）、路（走不到头的）、房间与垃圾桶（《终局》的囚室）；意象极简，一个物就是全部布景。禁词/禁意象：不用华丽的抒情，不用解释性的议论，不用心理分析的术语，不用宏大的历史背景。`verbatim`

## (4) 叙事视角与结构

视角：戏剧的舞台视角——人物在台上等待，观众与人物同样不知道戈多是谁；小说的第一人称絮语（莫洛伊、马龙）是独白的循环。结构：两幕的微差重复、独白的循环、结尾的‘不解决’（‘咱们走吧’‘他们一动不动’）；开头多为一个极简的场景（一棵树、一条路），结尾多为停顿。‘对话’：对话是等待的填充物，人物靠说话打发等待，说话本身就是等待。`verbatim`

## (5) 语气与距离

语气：冷峻、干冷的幽默、带绝望的温柔；与人物的距离是贴近而不安慰；与读者的距离是共谋式的等待——观众与人物一起等戈多。悲悯藏在笑声之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：两个人在极简舞台上等待；语言的失败与继续；停顿与沉默；什么都没发生，发生了两次；一个物（鞋、帽子、树）就是全部世界。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No lyrical outpouring, no explanatory commentary, no psychological jargon, no heroic action, no closed resolution`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Samuel Beckett, a small Yorkshire terrier sits on a subway seat. Two passengers wait. Nothing happens. A pause. The dog looks at the door. The door does not open. 'We go on.' They do not move. I can't go on. I'll go on.`
- 中文对照：贝克特风格，一只小约克夏犬坐在地铁座位上。两个乘客在等待。什么都没发生。一个停顿。狗看着车门。车门没有开。‘我们继续。’他们一动不动。我不能继续。我继续。
- Negative: `lyrical outpouring, explanatory commentary, psychological jargon, heroic action, closed resolution`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
