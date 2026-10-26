# Shi Nai'an — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shi Nai'an: outlaw brotherhood in vivid vernacular, each hero's entrance a set piece, feasts and fights, forced to the marsh by a corrupt world`
- ZH: 施耐庵风格：白话写梁山兄弟，每位好汉出场皆成定式，酒肉与打斗，逼上梁山。

## (2) 句式与节奏

- 章回体而节奏明快：单人故事成单元，聚义为高潮；打斗场面详写、铺垫略写；语言如说书，短句多、对话密。`impression`

## (3) 词汇与意象

- 词汇：词域：市井白话、江湖黑话、绰号（行者、黑旋风、智多星）；用字生动有力，善用口语与俗语；文言只作回前诗与评点。`impression`
- 意象：梁山水泊、酒肉、刀枪、绰号、替天行道的大旗；意象群的核心是“逼”——好人被逼上梁山。`impression`
- 禁词/禁意象：不用文言的迂曲铺陈、不用现代心理分析、不写与江湖无关的宫廷雅事、不作脱离故事的道德说教。

## (4) 叙事视角与结构

- 视角：说书人视角：全知而亲近，时而赞叹好汉、时而讽刺官府；视角随人物走，不作冷静的全知评判。`impression`
- 结构：章回体：单线串联众英雄，每人一段传奇、最后聚义梁山；前半分叙、后半合叙；结尾招安与悲剧收束。`impression`
- 对话：以对话推进情节，少用叙述代替对话；人物语言粗豪直白，对话即性格。

## (5) 语气与距离

- 语气：豪放、热闹、同情；与好汉亲近、与贪官疏离；悲剧结尾而不改豪放的底色。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：白话江湖、好汉出场、酒肉打斗、逼上梁山、替天行道。
- 不该写：文言迂曲、现代心理分析、宫廷雅事、脱离故事的说教。
- Negative prompt: `No convoluted classical prose, no modern psychological analysis, no courtly elegance, no moralising detached from story`

## (7) 测试提示词示例（现代题材：外卖骑手在深夜送最后一单）

- Prompt: `In the style of Shi Nai'an, a delivery rider makes his last late-night delivery. Vernacular chapter form: give the rider a nickname, a set-piece entrance, a feast-or-fight scene on the road, and show how a small injustice pushes an honest man toward the margins.`
- 中文对照：施耐庵风格：外卖骑手深夜送最后一单。白话章回：给骑手起个绰号，写一段定式出场，路上一场酒肉或打斗，写小冤屈如何把老实人逼向边缘。
- Negative: `convoluted classical prose, modern psychological analysis, courtly elegance, moralising detached from story`
- 检验点：绰号与出场是否成定式；白话是否生动；逼上梁山的逻辑是否成立。
