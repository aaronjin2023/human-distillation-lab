# Li Qingzhao — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Qingzhao: delicate ci in a woman's voice, fourteen overlapping words of sorrow, everyday objects holding grief, plain words that cut`
- ZH: 李清照风格：婉约词中女声独白，十四叠字写愁，日常器物皆载悲伤，平白之语最利。

## (2) 句式与节奏

- 词：长短句婉转、顿挫细腻；叠字（“寻寻觅觅，冷冷清清”）造成回环的节奏；语言如泣如诉而不滞。`verbatim`

## (3) 词汇与意象

- 词汇：词域：花、酒、帘、雁、梧桐、细雨、黄昏；用字极精，善用叠字与口语；少用宏大典故，多用眼前之物。`impression`
- 意象：梧桐细雨、黄昏、残花、雁、酒；意象群的核心是“冷”与“愁”——物是人非，景还是景，人已不是人。`impression`
- 禁词/禁意象：不用豪放的江河气象、不用空洞的豪言、不写与己无关的宏大叙事、不作板起面孔的议论。

## (4) 叙事视角与结构

- 视角：第一人称女声：我是词中的女子，也是词外的作者；视角极近，几乎贴着心写。`impression`
- 结构：词：上片写景、下片抒情，或通篇以叠字贯之；《夏日绝句》为五言绝句，二十字作议论，风格一转。`impression`
- 对话：词中基本无人称对话；以自述与独白写愁，不写人物对答。

## (5) 语气与距离

- 语气：婉约、凄清、真切；早期清丽、晚期凄厉；与读者如闺中密语，不作公开的慷慨陈词。`impression`（学界通说：婉约之宗）

## (6) 该写什么 / 不该写什么

- 该写：叠字回环、日常器物、女声独白、物是人非、平白而利。
- 不该写：豪放气象、空洞豪言、宏大叙事、板脸议论。
- Negative prompt: `No grand heroic landscape, no empty bravado, no impersonal epic, no solemn lecturing`

## (7) 测试提示词示例（现代题材：写给十年后自己的一封信）

- Prompt: `In the style of Li Qingzhao, a letter to oneself ten years later. Delicate ci-like lines, overlapping words of sorrow, an everyday object — a cup, a curtain — holding all the grief. Plain words, no consolation offered.`
- 中文对照：李清照风格：写给十年后自己的一封信。婉约词式长短句，叠字写愁，一只杯、一幅帘载尽悲伤。平白之语，不给安慰。
- Negative: `grand heroic landscape, empty bravado, impersonal epic, solemn lecturing`
- 检验点：叠字节奏是否出现；器物是否载愁；语言是否平白而利。
