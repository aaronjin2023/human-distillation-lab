# Guan Hanqing — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guan Hanqing: Yuan zaju drama in plain spoken language, a wronged woman's cry against heaven and earth, comic relief inside tragedy, justice demanded on stage`
- ZH: 关汉卿风格：元杂剧的明白口语，冤女向天地呼告，悲剧中有喜剧，舞台上讨还公道。

## (2) 句式与节奏

- 杂剧曲白相间：曲词抒情、宾白叙事；语言如说话，节奏明快；窦娥的控诉层层递进，如浪拍岸。`impression`

## (3) 词汇与意象

- 词汇：词域：市井口语、衙门、冤狱、天地鬼神；用字直白有力，善用俗语与俚语；曲词雅俗并存。`impression`
- 意象：天地、鬼神、六月飞雪、血溅白练、冤魂；意象群的核心是“冤”——天地不公，冤情须以异象证之。`impression`
- 禁词/禁意象：不用文言的迂曲、不写与百姓无关的宫廷雅乐、不作冷静的旁观、不以喜剧消解冤情。

## (4) 叙事视角与结构

- 视角：人物视角轮唱：窦娥、蔡婆婆、张驴儿各有声口；作者隐身于人物之后，不作全知评判。`impression`
- 结构：杂剧四折一楔子：楔子交代、折子推进、结尾以冤情昭雪或控诉收束；《窦娥冤》以三桩誓愿作高潮。`impression`
- 对话：杂剧以宾白推进剧情，对白口语化、直白有力；独白（上场诗、自报家门）与对白交替。

## (5) 语气与距离

- 语气：悲愤、直白、泼辣；与底层同情、与权贵控诉；喜剧人物只作调剂，不夺悲剧的主调。`impression`（学界通说：元曲四大家之首）

## (6) 该写什么 / 不该写什么

- 该写：市井口语、冤情控诉、曲白相间、三桩誓愿、舞台讨公道。
- 不该写：文言迂曲、宫廷雅乐、冷静旁观、喜剧消解冤情。
- Negative prompt: `No convoluted classical prose, no courtly elegance detached from common people, no detached spectatorship, no comedy that dissolves the injustice`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Guan Hanqing, a man buys oden at a convenience store late at night. Write it as a zaju scene: spoken dialogue in plain language, a small injustice at the till, the man appealing to heaven and earth, a comic shopkeeper, and an ending that demands justice, not comfort.`
- 中文对照：关汉卿风格：一个人在深夜便利店买关东煮。写成杂剧一场：明白口语对白，收银台上一件小冤屈，主人公向天地呼告，喜剧店员作调剂，结尾讨还公道，不给安慰。
- Negative: `convoluted classical prose, courtly elegance, detached spectatorship, comedy dissolving injustice`
- 检验点：对白是否口语化；冤情是否层层递进；喜剧是否只作调剂。
