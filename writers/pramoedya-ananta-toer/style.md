# Pramoedya Ananta Toer — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pramoedya Ananta Toer: epic realism, the land itself as a character, a Javanese youth against empire, history told through a family, plain Indonesian carrying unbearable weight`
- ZH: 普拉姆迪亚风格：史诗现实主义，土地本身就是人物，一个爪哇青年对抗帝国，历史通过一个家族讲述，平实的印尼语承载难以承受的重量。

## (2) 句式与节奏

句长：以中长句为主，句法清晰、细节堆积；段落长，一段可同时完成场景、历史与人物。节奏：缓慢、史诗，靠家族的代际推进；《人间大地》四部曲以明克的成长为框架，时间跨度大，节奏靠历史的潮汐推进。`impression`

## (3) 词汇与意象

词汇：印尼语日常词、爪哇词与荷兰殖民词汇并置；‘土地’‘家族’‘觉醒’是核心词。意象群：土地（人间大地）、大海与船、甘蔗园与种植园、家族的老屋、书与报纸；意象是历史的零件。禁词/禁意象：不用华丽的抒情，不用抽象的哲理议论，不用冷静的旁观。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称回忆（明克的自述）与第三人称的史诗叙述交替；叙述者是见证者，不是审判者。结构：家族编年 + 历史潮汐，四部曲各自独立又互为接续；开头多为一个家族场景，结尾多为历史的收束。对话：对话是觉醒的语言，人物靠辩论与书信暴露自己。`impression`

## (5) 语气与距离

语气：庄重、纪实、带见证的热情；与人物的距离是同情的凝视；与读者的距离是直接的——请读者作见证。悲悯多于反讽，证词多于抒情。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：土地本身就是人物；一个爪哇青年对抗帝国；历史通过一个家族讲述；平实的语言承载历史的重量；觉醒与反抗。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No ornate lyricism, no abstract philosophising, no cool detachment, no flat reportage, no heroic rhetoric`

## (7) 测试提示词示例（现代题材：一个外卖骑手在深夜送餐）

- Prompt: `In the style of Pramoedya Ananta Toer, a food delivery rider works late at night. Epic realism: the city itself is a character. A young man against an empire of apps. History told through a family. Plain language carrying unbearable weight.`
- 中文对照：普拉姆迪亚风格，一个外卖骑手深夜送餐。史诗现实主义：城市本身就是人物；一个青年对抗一个应用的帝国；历史通过一个家族讲述；平实的语言承载难以承受的重量。
- Negative: `ornate lyricism, abstract philosophising, cool detachment, flat reportage, heroic rhetoric`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
