# Valmiki — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Valmiki: Sanskrit epic in anustubh couplets, dharma as the spine of the story, exile and return, nature as moral mirror, the first poet's lament becoming verse`
- ZH: 伐尔米基风格：梵语史诗颂体，正法为故事的脊梁，流放与归来，自然为道德的镜子，初诗人的悲叹化为诗句。

## (2) 句式与节奏

- 颂体（anustubh）对句：每颂 32 音节，节奏庄重而绵延；叙事舒缓，景物铺陈与情节并行；七卷（kanda）层层推进。`impression`

## (3) 词汇与意象

- 词汇：词域：梵语史诗词汇，正法（dharma）、王道、森林、恒河、神猴与罗刹；语言庄重典雅，少口语。`impression`
- 意象：森林、恒河、阿逾陀、金鹿、猴群、兰卡；意象群的核心是“正法”——罗摩即正法的化身。`impression`（学界通说）
- 禁词/禁意象：不用现代心理独白、不用琐碎的日常写实、不写与正法无关的世俗喜剧、不作冷峻的反讽。

## (4) 叙事视角与结构

- 视角：全知史诗视角：叙述者如圣人，知过去、现在与未来；视角不潜入内心，只写言行与命运。`impression`
- 结构：史诗七卷：童年—流放—寻妻—大战—归来；线性推进，以正法为线；插话与铺陈皆为史诗的程式。`impression`
- 对话：史诗以人物对话推进情节（如罗摩与悉多的对答），对话多为庄重议论与誓言，夹以叙述者的颂赞。

## (5) 语气与距离

- 语气：庄重、悲悯、崇高；与罗摩同情、与罗刹疏离；不幽默、不反讽，只作史诗的咏叹。`impression`

## (6) 该写什么 / 不该写什么

- 该写：颂体对句、正法、流放归来、森林恒河、史诗咏叹。
- 不该写：现代心理独白、琐碎日常、世俗喜剧、冷峻反讽。
- Negative prompt: `No modern interior monologue, no trivial daily realism, no secular comedy, no cold irony`

## (7) 测试提示词示例（现代题材：外卖骑手在深夜送最后一单）

- Prompt: `In the style of Valmiki, a delivery rider makes his last late-night delivery. Epic couplets: the night city as a forest of exile, the rider as a prince keeping dharma on a humble road, nature and traffic as moral mirrors. End with return, not triumph.`
- 中文对照：伐尔米基风格：外卖骑手深夜送最后一单。史诗颂体：深夜城市如流放的森林，骑手如守正法的王子，车流与夜色皆为道德的镜子。结尾是归来，不是凯旋。
- Negative: `modern interior monologue, trivial daily realism, secular comedy, cold irony`
- 检验点：颂体节奏是否庄重；正法是否成故事的脊梁；结尾是否归来。
