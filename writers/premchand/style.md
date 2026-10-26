# Premchand — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Premchand: Hindi realism of village India, a peasant's dignity against debt and caste, plain speech that accuses without shouting`
- ZH: 普列姆昌德风格：印地语写实，印度乡村，农民的尊严对着债务与种姓，平白之语不喊而有力。

## (2) 句式与节奏

- 小说叙事节奏：从容铺叙、细节多、对话密；长篇《戈丹》由乡村日常层层推向悲剧；语言如说话，平实而有力。`impression`

## (3) 词汇与意象

- 词汇：词域：印地语口语、乡村、土地、债务、种姓；用字平实，少用华丽辞藻；善用农民的口语与谚语。`impression`
- 意象：牛（戈丹即“献牛”）、土地、债务、乡村集市；意象群的核心是“牛”——农民的命即牛的命。`impression`
- 禁词/禁意象：不用华丽的抒情、不用脱离乡村的都市雅事、不写与农民无关的宫廷传奇、不作空洞的说教。

## (4) 叙事视角与结构

- 视角：第三人称全知而亲近：叙述者站在农民一边，与地主与高利贷者疏离；视角不潜入内心，只写言行与处境。`impression`
- 结构：长篇：线性叙事、乡村为舞台、债务为线索；短篇：由一事见全貌；结尾多为悲凉收束。`impression`
- 对话：印地语口语对话推进情节，人物语言即阶层与性格；独白少，叙述者常借对话作社会评论。

## (5) 语气与距离

- 语气：平实、悲悯、克制；与农民同情、与压迫者疏离；不激愤、不幽默，只作平实的陈述。`impression`（学界通说：印地语现实主义之父）

## (6) 该写什么 / 不该写什么

- 该写：乡村写实、农民尊严、债务与种姓、平白控诉、悲凉收束。
- 不该写：华丽抒情、都市雅事、宫廷传奇、空洞说教。
- Negative prompt: `No ornate lyricism, no urbane elegance detached from the village, no courtly romance, no empty moralising`

## (7) 测试提示词示例（现代题材：外卖骑手在深夜送最后一单）

- Prompt: `In the style of Premchand, a delivery rider makes his last late-night delivery. Plain Hindi-realist prose: the rider's debt and dignity, the city as a village writ large, dialogue in the workers' own speech, and an ending that accuses by telling, without shouting.`
- 中文对照：普列姆昌德风格：外卖骑手深夜送最后一单。平白写实：骑手的债务与尊严，城市如放大的乡村，对话用劳动者自己的话，结尾以叙事控诉，不喊。
- Negative: `ornate lyricism, urbane elegance, courtly romance, empty moralising`
- 检验点：乡村/劳动者视角是否在；债务与尊严是否成线索；控诉是否平白而不喊。
