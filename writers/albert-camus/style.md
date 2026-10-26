# Albert Camus — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Albert Camus: clear dry French, a sunlit indifferent world, a man who refuses to lie, the absurd named plainly, revolt without hope and without despair`
- ZH: 加缪风格：清晰干燥的法语，阳光下冷漠的世界，一个拒绝说谎的人，荒诞被平实地命名，没有希望也没有绝望的反抗。

## (2) 句式与节奏

句长：以短句与中长句为主，句法清晰、少从句嵌套；《局外人》第一部几乎全是短句，第二部转入法庭的长句辩论，句长的变化本身就是结构。节奏：均匀、干燥，像阿尔及尔的阳光——事件按时间平铺，不加速、不渲染；《鼠疫》以编年体逐日记录，节奏是‘日记式’的缓慢积累。`verbatim`

## (3) 词汇与意象

词汇：日常法语、阳光与海的词汇（太阳、海、沙滩、光）、法庭与审判词汇；形容词克制，抽象词（荒诞、反抗、自由）只在关键处出现。意象群：太阳（刺眼、令人眩晕的阳光）、海与沙滩、法庭与审判、鼠疫之城（封锁的奥兰）、西西弗的石头；意象不作象征解释，只作处境本身。禁词/禁意象：不用华丽的抒情，不用心理分析的术语，不用解释荒诞原因的议论。`impression`

## (4) 叙事视角与结构

视角：第一人称（《局外人》默尔索的冷静自述）与编年体全知（《鼠疫》的里厄医生式记录）交替；叙述者不比人物知道更多，读者与人物同样面对荒诞。结构：以一个事件开篇（母亲去世、鼠疫爆发），随后按时间冷静记录，不解决、不升华；结尾多为平静的收束（‘我明白了……’）而非顿悟。对话：对话短促、事实性，人物靠‘说什么’与‘不说什么’暴露自己。`verbatim`

## (5) 语气与距离

语气：清晰、干燥、近乎冷漠的陈述；与人物的距离是贴近而不安慰；与读者的距离是诚实的——叙述者不说谎，读者只好自己判断。幽默是干冷的，悲悯藏在克制之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：阳光下冷漠的世界；一个拒绝说谎、拒绝扮演的人；荒诞被平实地命名；封锁之城中的日常坚守；没有希望也没有绝望的反抗。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No lyrical outpouring, no psychological jargon, no explanation of the absurd, no sentimental uplift, no heroic rhetoric`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Albert Camus, a man buys oden at a convenience store late at night. Clear dry sentences. The fluorescent light, the steam, the clerk's indifference. He does not lie about why he is here. The absurd is named plainly. He eats, he pays, he walks out into the cold. Revolt without hope and without despair.`
- 中文对照：加缪风格，一个人在深夜便利店买关东煮。清晰干燥的句子；日光灯、蒸汽、店员的冷漠；他不为自己为什么在这里说谎；荒诞被平实地命名；他吃完、付钱、走进寒夜；没有希望也没有绝望的反抗。
- Negative: `lyrical outpouring, psychological jargon, explanation of the absurd, sentimental uplift, heroic rhetoric`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
