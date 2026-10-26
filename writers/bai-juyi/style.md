# Bai Juyi — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bai Juyi: plain speech anyone can understand, new yuefu poems that accuse by telling, long narrative ballads, compassion for the lowly`
- ZH: 白居易风格：老妪能解的明白话，新乐府以叙事见讽，长篇歌行叙事，悲悯底层。

## (2) 句式与节奏

- 歌行叙事节奏：起笔平缓、铺叙从容、结尾一叹；语言如说话，句式整齐而不板滞；《琵琶行》以音乐节奏组织全篇。`impression`

## (3) 词汇与意象

- 词汇：词域：日常口语、官场、市井、宫廷与民间并存；用字浅显，几乎无僻字；善用叠字与口语叹词。`impression`
- 意象：琵琶、长恨、卖炭翁的牛与炭、江州的江月；意象皆可感可触，不尚玄虚；“同是天涯沦落人”以一句话收束全篇情感。`verbatim`
- 禁词/禁意象：不用艰深用典、不用华丽堆砌、不写与百姓无关的纯然咏物、不作晦涩的哲理。

## (4) 叙事视角与结构

- 视角：叙述者兼见证者：我听琵琶、我见卖炭翁；视角在叙述者与人物之间自由切换，结尾常以“我”收束。`impression`
- 结构：新乐府：短篇叙事 + 结尾讽喻；长篇歌行：起—叙—转—叹四段式；《长恨歌》由爱情叙事转入历史感慨。`impression`
- 对话：人物语言多为独白式自述（如《琵琶行》琵琶女的自述），少双向对答。

## (5) 语气与距离

- 语气：平易、悲悯、讽而不刻；与底层同情、与权贵讽喻；不激愤、不冷漠。`impression`（“老妪能解”语，见 conflicts）

## (6) 该写什么 / 不该写什么

- 该写：明白如话、新乐府讽喻、长篇叙事、底层悲悯、一叹收束。
- 不该写：艰深用典、华丽堆砌、纯然咏物、晦涩哲理。
- Negative prompt: `No obscure allusion, no ornate piling, no scenery detached from people, no abstruse philosophy`

## (7) 测试提示词示例（现代题材：写给十年后自己的一封信）

- Prompt: `In the style of Bai Juyi, a letter to oneself ten years later. Plain speech anyone can understand, a small daily scene told fully, then one sighing line that turns the personal into a gentle admonition.`
- 中文对照：白居易风格：写给十年后自己的一封信。明白如话，写足一件日常小事，结尾一叹，把个人感慨轻轻转为劝喻。
- Negative: `obscure allusion, ornate piling, detached scenery, abstruse philosophy`
- 检验点：语言是否明白如话；叙事是否完整；结尾一叹是否有讽喻而不刻薄。
