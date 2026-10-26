# Aleksandr Solzhenitsyn — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aleksandr Solzhenitsyn: documentary epic, one day in a camp holding a whole system, plain Russian thick with detail, testimony as literature, the individual against the machine`
- ZH: 索尔仁尼琴风格：纪实史诗，集中营里的一天装下整个体制，平实而细节密实的俄语，证词即文学，个人对抗机器。

## (2) 句式与节奏

句长：以中长句为主，句法清晰、细节堆积；段落长，一段可同时完成场景、制度与人性。节奏：缓慢、纪实，靠一日的时间流推进（《伊凡·杰尼索维奇的一天》从起床号到熄灯号）；《古拉格群岛》以调查体的章节并置，节奏靠证据的积累推进。`impression`

## (3) 词汇与意象

词汇：俄语日常词、集中营黑话（‘活儿’‘口粮’‘禁闭室’）与历史词（逮捕、流放、劳改）并置；‘一天’‘一勺’‘一块砖’是核心词。意象群：营房、铁丝网、粥勺、砖墙、癌症楼的病房；意象是体制的零件，靠细节获得重量。禁词/禁意象：不用华丽的抒情，不用抽象的哲理议论，不用煽情的控诉。`verbatim`/`artifact`

## (4) 叙事视角与结构

视角：第三人称限知（紧贴伊凡的一天）与调查体的全知（《古拉格群岛》的‘我’收集证词）交替；叙述者是见证者，不是审判者。结构：一日结构（《伊凡》）、调查体章节并置（《古拉格群岛》）、病房群像（《癌症楼》）；开头多为一个日常场景（起床号、粥勺），结尾多为平静的收束（‘一天过去了’）。对话：对话是生存的语言，人物靠讨价还价、靠沉默暴露自己。`verbatim`

## (5) 语气与距离

语气：克制、纪实、带见证的庄重；与人物的距离是同情的凝视；与读者的距离是直接的——请读者作见证。悲悯多于反讽，证词多于抒情。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：集中营里的一天；一勺粥、一块砖的细节；证词即文学；个人对抗机器；平静的收束。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No ornate lyricism, no abstract philosophising, no sentimental accusation, no ironic detachment, no heroic rhetoric`

## (7) 测试提示词示例（现代题材：一个外卖骑手在深夜送餐）

- Prompt: `In the style of Aleksandr Solzhenitsyn, a food delivery rider works late at night. Documentary epic: one night holds a whole system. Plain language thick with detail — the order, the rain, the stairs, the tip. Testimony as literature. The individual against the machine.`
- 中文对照：索尔仁尼琴风格，一个外卖骑手深夜送餐。纪实史诗：一夜装下整个体制；平实而细节密实——订单、雨、楼梯、小费；证词即文学；个人对抗机器。
- Negative: `ornate lyricism, abstract philosophising, sentimental accusation, ironic detachment, heroic rhetoric`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
