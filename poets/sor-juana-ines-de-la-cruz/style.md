# Sor Juana Inés de la Cruz — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sor Juana: baroque Spanish verse, dense conceits and antithesis, the soul's night journey toward knowledge, wit that argues while it sings`
- ZH: 索尔·胡安娜风格：巴洛克西班牙语诗，繁复巧喻与对仗，灵魂在夜里求知的旅程，机智在歌唱中辩论。

## (2) 意象

- 主意象：夜、梦、灵魂、迷宫、镜子、书与知识；辅意象：玫瑰、星、法厄同（太阳神之子）、金字塔般的阴影；禁意象：田园闲适、直白抒情；密度极高，意象多取自古典神话与经院哲学，典故压缩意义。

## (3) 韵律与句式

- 以十四行诗、谣曲（romance）与西尔瓦（silva）为主；《第一梦》用西尔瓦长行，句长参差、跨行奔涌；句式多对仗、排比、倒装与设问；节奏繁复而严整，朗读时如辩论推进。

## (4) 语言密度与词汇

- 词汇典雅而博学：神话名、哲学词、拉丁语源词并置；善用巧喻（concepto）与双关；动词多为求知、上升、坠落；禁词：口语俚语、直白的情绪词。

## (5) 结构习惯

- 长诗《第一梦》以夜幕开场、灵魂出窍、求知失败、日出收束，七节式推进；短诗多十四行与谣曲，结尾常以警句收束；视角多为第一人称灵魂独白与代言体；推进靠概念递进与转折（volta 在十四行后段）。

## (6) 该写什么 / 不该写什么

- 该写：夜与梦、灵魂求知、迷宫与镜子；繁复巧喻、对仗与警句、经院式论辩；讽刺谣曲（如《愚蠢的男人们》式的质问）。
- 不该写：风格上的禁区——plain colloquial diction, no simple pastoral ease, no direct sentimental confession, no loose unstructured free verse, no moralising without wit。
- Negative prompt: `No plain colloquial diction, no simple pastoral ease, no direct sentimental confession, no loose unstructured free verse, no moralising without wit`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sor Juana, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Baroque Spanish verse, dense conceits, the soul's night journey, the dog as a small mirror of the crowd. Wit that argues while it sings.`
- 中文对照：索尔·胡安娜风格：一只约克夏犬深夜坐在地铁座位上。巴洛克诗，繁复巧喻，灵魂的夜旅，狗是人群的小镜子。机智在歌唱中辩论。
- Negative: `No plain colloquial diction, no simple pastoral ease, no direct sentimental confession, no loose unstructured free verse, no moralising without wit`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
