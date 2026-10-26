# Kim Sowol — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Sowol: folk-song lyrics in plain Korean, azaleas scattered on the parting road, the beloved leaving and the singer staying, sorrow sung so plainly it needs no ornament`
- ZH: 金素月风格：民谣体抒情，平实的韩语，离别路上撒满杜鹃花，恋人离去而歌者留下，悲伤唱得如此平实，无需装饰

## (2) 意象

- 主意象：杜鹃花、山、花、路、月；辅意象：鸟、溪、村、夜；禁意象：华丽典故、都市现代词；密度低，一首只装一个意象，来自朝鲜山野与民谣。`impression`

## (3) 韵律与句式

- 民谣体，三四音步反复；句式短促，叠句回环；节奏如民谣吟唱，平缓而绵长。`impression`

## (4) 语言密度与词汇

- 词汇：平实韩语日常词，少汉文典故；动词轻柔（撒、望、等、去）；善用叠句；禁词：华丽典故、都市现代词、抽象大词。`impression`

## (5) 结构习惯

- 单篇短诗为主，叠句回环；开头直入花或山，结尾以目送或等待收束；视角第一人称歌者；推进靠叠句与意象重复。`impression`

## (6) 该写什么 / 不该写什么

- 该写：民谣体抒情、杜鹃花意象、叠句回环、目送收束。
- 不该写：华丽典故、都市现代词、抽象大词、冗长议论。
- Negative prompt: `No ornate allusions, no urban modern jargon, no abstract grand words, no long explanatory passages, no sentimental melodrama`

## (7) 测试提示词示例（现代题材：一封写给十年后自己、从未寄出的信）

- Prompt: `In the style of Kim Sowol, a letter to oneself ten years from now, never sent. Folk-song lyrics, azaleas scattered on the parting road, the beloved leaving and the singer staying, sorrow sung plainly.`
- 中文对照：金素月风格：一封写给十年后自己、从未寄出的信。民谣体抒情，离别路上撒满杜鹃花，恋人离去而歌者留下，悲伤唱得平实
- Negative: `No ornate allusions, no urban modern jargon, no abstract grand words, no long explanatory passages, no sentimental melodrama`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
