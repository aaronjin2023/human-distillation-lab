# Xia Yan — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xia Yan: literary adaptation with social conscience, small people crushed by great times, plain dialogue carrying heavy history, tragedy without melodrama`
- ZH: 夏衍风格：有社会良心的文学改编，小人物被大时代碾过，平实的对白承载沉重的历史，悲剧而不煽情。

## (2) 结构：三幕 / 序列 / 节拍

- 改编型三幕：第一幕小人物家庭日常切入，时代压力从门外渗入；第二幕压迫层层加码，中点是一次无可挽回的失去；第三幕悲剧收束，不靠高潮靠累积。时间跨度常为数年至数十年，多用季节与时代标记分段，少闪回。

## (3) 对话

- 对白平实、克制，少修辞；人物用日常语言说沉重的事；潜台词是时代压力——没说出口的比说出口的重。动作描写简洁，多写劳作与家庭场景。

## (4) 人物弧光

- 主角多为小人物（祥林嫂、林老板、革命家庭成员），弧光不是成长而是被时代推着走：从忍耐到崩溃，或从忍耐到觉醒。人物关系是家庭与社会的双重压迫；结局人物不胜利，只留下控诉。

## (5) 类型套路与创新

- 类型：社会现实主义改编；遵守套路——小人物、时代、悲剧；打破的一条是：拒绝煽情，悲剧靠累积不靠高潮。创新在剧本层面：把鲁迅、茅盾等小说的内心与时代感转成可演的家庭场景。禁套路：不用英雄主义高潮，不用煽情独白，不用直白口号。

## (6) 该写什么 / 不该写什么

- 该写：小人物与大时代、文学改编的家庭场景、平实克制的对白、悲剧的累积收束、时代标记分段。
- 不该写：英雄主义高潮、煽情独白、直白口号、类型反转、让小人物突然觉醒开挂。
- Negative prompt: `No heroic climax, no sentimental monologue, no direct slogan, no genre twist, no sudden enlightened hero`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Xia Yan, a small shopkeeper buys oden at a convenience store late at night, counting coins, thinking of the rent. Plain words, heavy history. No rescue comes.`
- 中文对照：夏衍风格：一个小店主深夜在便利店买关东煮，数着硬币，想着房租，平实的话，沉重的历史，没有救援到来。
- Negative: `No heroic climax, no sentimental monologue, no direct slogan, no genre twist`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
