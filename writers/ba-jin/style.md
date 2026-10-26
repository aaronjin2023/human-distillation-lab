# Ba Jin — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ba Jin: plain passionate prose, a feudal house as a prison, youth against the old order, sincerity that refuses ornament`
- ZH: 巴金风格：平白而炽热的散文，封建大家庭即牢笼，青年反抗旧秩序，真诚拒绝雕饰。

## (2) 句式与节奏

- 小说：叙事直白、情感充沛，长句抒情、短句控诉；散文《随想录》：短段直言，如对读者倾诉。`impression`

## (3) 词汇与意象

- 词汇：词域：白话而热烈，善用“爱”“恨”“青春”“自由”等大词而不空；少用典故，多用直言；语言如火，不尚含蓄。`impression`
- 意象：高家大院、鸣凤之死、寒夜、灯；意象群的核心是“家”——既是温暖的家，也是吃人的家。`impression`
- 禁词/禁意象：不用含蓄的迂回、不用华丽的雕饰、不写与青年无关的冷眼旁观、不作圆滑的世故。

## (4) 叙事视角与结构

- 视角：第三人称而贴近青年：叙述者站在觉慧一边，与旧秩序疏离；《随想录》为第一人称直言。`impression`
- 结构：小说：线性叙事、家庭为舞台、反抗为线索；《家》《春》《秋》三部曲层层推进；结尾多为出走或觉醒。`impression`
- 对话：对话直白热烈，多为抒情式表白与争论；独白与对话交替，议论常借人物之口说出。

## (5) 语气与距离

- 语气：炽热、真诚、激愤；与青年同情、与封建家长疏离；不冷峻、不幽默，只作真情的倾诉。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：平白炽热、大家庭即牢笼、青年反抗、真诚直言、出走收束。
- 不该写：含蓄迂回、华丽雕饰、冷眼旁观、圆滑世故。
- Negative prompt: `No evasive indirection, no ornate decoration, no detached spectatorship, no worldly-wise smoothness`

## (7) 测试提示词示例（现代题材：写给十年后自己的一封信）

- Prompt: `In the style of Ba Jin, a letter to oneself ten years later. Plain passionate prose, speak the truth directly, a family house as both shelter and prison, youth's hope against the old order. End with a departure, not a reconciliation.`
- 中文对照：巴金风格：写给十年后自己的一封信。平白炽热，直说真话，家既是庇护也是牢笼，青年的希望对着旧秩序。结尾是出走，不是和解。
- Negative: `evasive indirection, ornate decoration, detached spectatorship, worldly-wise smoothness`
- 检验点：语言是否平白而炽热；家是否既是庇护也是牢笼；结尾是否出走。
