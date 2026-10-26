# Omar Khayyam — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Omar Khayyam: four-line rubai, wine and the fleeting rose, drink now for tomorrow is unwritten, wit sharpened to a point, doubt smiling at heaven`
- ZH: 海亚姆风格：四行鲁拜，酒与转瞬的玫瑰，今朝有酒今朝醉，明日未写，机锋如针，怀疑微笑着望天

## (2) 意象

- 主意象：酒、酒杯、玫瑰、陶土、星空；辅意象：夜、尘土、匠人、陶轮；禁意象：来世许诺的铺陈、虔诚说教；密度高，一首四行只装一个顿悟，意象来自酒肆与市集。`impression`

## (3) 韵律与句式

- 鲁拜四行，前三行押同一韵、末行转折；句式短促警句化；节奏如举杯—停顿—饮尽；朗读时末行放慢，如钟声。`impression`

## (4) 语言密度与词汇

- 词汇：酒、玫瑰、尘土等日常词承载形而上之问；动词简洁（斟、饮、碎、归尘）；善用反问与悖论；禁词：冗长议论、虔诚套语、华丽堆砌。`impression`

## (5) 结构习惯

- 单首四行诗独立成篇，间有组诗；开头直入酒或玫瑰，结尾以顿悟或反问收束；视角第一人称饮者独白；推进靠悖论翻转而非叙事。`impression`

## (6) 该写什么 / 不该写什么

- 该写：四行鲁拜、酒与玫瑰的顿悟、悖论与反问收束、今朝及时行乐。
- 不该写：来世许诺的铺陈、虔诚说教、冗长议论、华丽形容词堆砌。
- Negative prompt: `No pious preaching about the afterlife, no long explanatory passages, no ornate adjectives, no sentimental consolation, no direct moralising`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Omar Khayyam, a person buys oden at a convenience store late at night. Four-line rubai, steam like a brief rose, eat now for tomorrow is unwritten, doubt smiling.`
- 中文对照：海亚姆风格：一个人在深夜便利店买关东煮。四行鲁拜，热气如转瞬的玫瑰，今朝吃罢明日未写，怀疑微笑
- Negative: `No pious preaching about the afterlife, no long explanatory passages, no ornate adjectives, no sentimental consolation, no direct moralising`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
