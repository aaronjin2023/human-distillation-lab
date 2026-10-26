# Murasaki Shikibu — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Murasaki Shikibu: Heian court prose in hiragana, waka poems inside the tale, mono no aware in every season, psychology in a glance, never a raised voice`
- ZH: 紫式部风格：平安假名物语，和歌在文内，物哀在四季中，心理在一瞥间，从不高声。

## (2) 句式与节奏

- 物语叙事节奏：舒缓绵延、细节繁复；和歌穿插，抒情处停住叙事；语言如行云流水，时而顿挫。`impression`

## (3) 词汇与意象

- 词汇：词域：假名文，宫廷、季节、花、月、香、衣；用字雅致，善用和歌与典故；少用汉语词汇的直露。`impression`
- 意象：樱、月、雪、香、衣、源氏的庭院；意象群的核心是“物哀”——美而易逝。`impression`
- 禁词/禁意象：不用激愤的控诉、不用粗粝的口语、不写与宫廷无关的江湖传奇、不作直白的道德说教。

## (4) 叙事视角与结构

- 视角：全知视角而极近：叙述者如在宫中行走，时而潜入人物内心、时而只写眼色；视角切换细腻而不露痕迹。`impression`
- 结构：长篇物语：五十四帖，以源氏一生为线、以四季流转为节；日常—恋爱—衰败三层推进；结尾宇治十帖，余韵不尽。`impression`
- 对话：物语以和歌式问答与人物对答推进，独白（心声）与对话交替；对话含蓄，言外之意重于言内。

## (5) 语气与距离

- 语气：雅致、含蓄、悲悯；与人物同情、与命运共感；不激愤、不幽默，只作物哀的咏叹。`impression`（学界通说：物哀）

## (6) 该写什么 / 不该写什么

- 该写：假名物语、和歌在文内、物哀、心理一瞥、四季流转。
- 不该写：激愤控诉、粗粝口语、江湖传奇、直白说教。
- Negative prompt: `No vehement denunciation, no coarse vernacular, no jianghu adventure, no blunt moralising`

## (7) 测试提示词示例（现代题材：写给十年后自己的一封信）

- Prompt: `In the style of Murasaki Shikibu, a letter to oneself ten years later. Heian court prose: let a waka carry the feeling, let the seasons turn inside the letter, psychology in a glance, mono no aware in every line, never a raised voice.`
- 中文对照：紫式部风格：写给十年后自己的一封信。平安物语：让一首和歌载情，让四季在信中流转，心理在一瞥间，物哀在每一行，从不高声。
- Negative: `vehement denunciation, coarse vernacular, jianghu adventure, blunt moralising`
- 检验点：和歌是否在文内；物哀是否在四季中；心理是否在一瞥间。
