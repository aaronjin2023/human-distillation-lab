# Yun Dong-ju — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yun Dong-ju: quiet lyrics under occupation, counting stars on a clear night, shame before the sky and a promise to walk without shame, the self examined in starlight, resistance as a clean conscience`
- ZH: 尹东柱风格：占领下的寂静抒情，晴夜数星，面对天空的羞愧与无愧而行的誓言，在星光下审视自我，抵抗即清白的良心

## (2) 意象

- 主意象：星、天空、风、夜、镜；辅意象：路、灯、雪、故乡；禁意象：煽情口号、直白控诉；密度低，一首只装一个夜景，来自夜空与内心。`impression`

## (3) 韵律与句式

- 短行抒情，句式简洁，长短有度；节奏如夜行，缓慢而清澈。`impression`

## (4) 语言密度与词汇

- 词汇：清澈日常词（星、风、夜、路），少华丽修饰；动词审视（数、望、走、省）；善用自问；禁词：煽情口号、直白控诉、抽象大词。`impression`

## (5) 结构习惯

- 单篇短诗为主；开头直入夜空或星，结尾以誓言或守望收束；视角第一人称自省者；推进靠自问与意象流转。`impression`

## (6) 该写什么 / 不该写什么

- 该写：夜空抒情、数星意象、自问与誓言、清白良心主题。
- 不该写：煽情口号、直白控诉、抽象大词、冗长议论。
- Negative prompt: `No sentimental slogans, no direct denunciation, no abstract grand words, no long explanatory passages, no ornate decoration`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Yun Dong-ju, a person buys oden at a convenience store late at night. Quiet lyrics, counting stars above the neon, shame before the sky and a promise to walk without shame.`
- 中文对照：尹东柱风格：一个人在深夜便利店买关东煮。寂静抒情，数着霓虹之上的星，面对天空的羞愧与无愧而行的誓言
- Negative: `No sentimental slogans, no direct denunciation, no abstract grand words, no long explanatory passages, no ornate decoration`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
