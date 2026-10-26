# Tao Yuanming — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tao Yuanming: plain unadorned five-character verse, field and garden imagery, quiet return to farming, no ornament, truth in the ordinary`
- ZH: 陶渊明风格：平淡自然的五言诗，田园意象，归隐躬耕，不加雕饰，平常中见真。

## (2) 句式与节奏

- 五言为主，句式整齐而语气舒缓；少排比长句，多短句平铺；《归去来兮辞》以“兮”字收束抒情，散文亦有诗的节奏。`impression`

## (3) 词汇与意象

- 词汇：词域：田园（田、园、菊、松、酒、柴门、鸡犬）、归（归去、归来）、自然（自然、真、拙）；用字极简，几乎不用僻字典故；白描。`impression`
- 意象：菊、松、酒、东篱、南山、桃花源、鸡犬相闻；意象皆日常农事，无奇崛神话；“采菊东篱下”是最具代表性的画面。`verbatim`
- 禁词/禁意象：不用华丽辞藻、不用繁复用典、不写宫廷富贵、不作慷慨激昂的抒情。

## (4) 叙事视角与结构

- 视角：第一人称自述为主；“我”是躬耕的农人，也是旁观的哲人；视角不切换、不作全知评判。`impression`
- 结构：短篇抒情：起兴于眼前之景—转入归隐之思—以平淡之语收束；《桃花源记》为散文叙事：入—见—出—再寻不得，环形结构。`impression`
- 对话：诗中基本无人称对话；以自述与自问自答（如《饮酒》“问君何能尔”）推进抒情。

## (5) 语气与距离

- 语气：平和、恬淡、真率；与自然亲近，与世俗疏离；不悲愤、不讥讽，只作安然的陈述。`impression`（学界通说：平淡为极致）

## (6) 该写什么 / 不该写什么

- 该写：田园白描、菊松酒意象、五言平调、归隐收束、平常之真。
- 不该写：华丽辞藻、繁复用典、宫廷题材、慷慨激昂。
- Negative prompt: `No ornate diction, no dense allusion, no courtly splendour, no vehement rhetoric, no sentimental excess`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Tao Yuanming, a man buys oden at a convenience store late at night. Plain five-character-like lines, steam like morning mist over fields, the shop as a small garden, no ornament. End with quiet contentment, not irony.`
- 中文对照：陶渊明风格：一个人在深夜便利店买关东煮。平淡五言式短句，热气如田间晨雾，便利店如一方小园，不加雕饰。结尾安然自足，不讽刺。
- Negative: `ornate diction, dense allusion, vehement rhetoric, irony, sentimental excess`
- 检验点：是否平淡而非华丽；田园意象是否自然转入现代场景而不生硬；结尾是否安然。
