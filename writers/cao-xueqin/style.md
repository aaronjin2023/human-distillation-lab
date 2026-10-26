# Cao Xueqin — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cao Xueqin: a great house in decline told through daily detail, poetry inside prose, every object a omen, grandeur and decay in one breath`
- ZH: 曹雪芹风格：大家族衰败写于日常细节，诗在文内，物物皆是谶语，繁华与衰败一气。

## (2) 句式与节奏

- 章回体而节奏舒缓：日常细节详写、大事略写；诗词、灯谜、酒令穿插，叙事时而停住作诗；语言如行云流水，时而顿挫。`impression`

## (3) 词汇与意象

- 词汇：词域：文白相间，诗词、戏曲、园林、服饰、饮食名目极繁；用字精雅，善用双关与谐音（甄士隐/真事隐、贾雨村/假语存）；口语入小说而不俗。`impression`
- 意象：大观园、怡红院、潇湘馆、冷月葬花魂、通灵宝玉、金锁；意象群的核心是“梦”与“幻”——繁华如梦，终归太虚。`impression`
- 禁词/禁意象：不用直白的道德说教、不用粗糙的情节推进、不写与家族无关的江湖传奇、不作脱离细节的空洞议论。

## (4) 叙事视角与结构

- 视角：全知视角而极近：叙述者如在园中行走，时而潜入宝黛内心、时而只写旁人眼色；视角切换细腻而不露痕迹。`impression`
- 结构：章回体：百二十回（前八十回为曹雪芹原稿），以贾府兴衰为线、以宝黛爱情为魂；日常—节日—变故三层推进；开头神话、结尾梦醒。`impression`
- 对话：对话高度个性化，是人物与情节的本体；日常闲谈中藏机锋，独白极少。

## (5) 语气与距离

- 语气：悲悯、细腻、含蓄；与宝黛同情、与贾府兴衰共感；不激愤、不冷嘲，哀而不伤。`impression`（学界通说：世情小说极致）

## (6) 该写什么 / 不该写什么

- 该写：日常细节、诗在文内、物皆谶语、双关谐音、繁华与衰败同写。
- 不该写：直白说教、粗糙情节、江湖传奇、脱离细节的空议论。
- Negative prompt: `No blunt moralising, no crude plot-driving, no jianghu adventure, no abstract essay detached from detail`

## (7) 测试提示词示例（现代题材：写给十年后自己的一封信）

- Prompt: `In the style of Cao Xueqin, a letter to oneself ten years later. Write it through daily detail — a cup, a garden, a half-finished poem — every object an omen, grandeur and decay in one breath, and end not with advice but with a dream-like waking.`
- 中文对照：曹雪芹风格：写给十年后自己的一封信。以日常细节写就——一只杯、一座园、一首未完的诗，物物皆是谶语，繁华与衰败一气，结尾不是劝告，而是一场梦醒。
- Negative: `blunt moralising, crude plot-driving, jianghu adventure, abstract essay detached from detail`
- 检验点：细节是否繁而有味；诗是否在文内；物象是否成谶；结尾是否梦醒而非说教。
