# Alexander Pushkin — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pushkin: clear Russian verse, Onegin stanza and lyric ease, freedom and the sea, plain words that are perfect`
- ZH: 亚历山大·普希金风格：清澈的俄语诗，奥涅金诗节与抒情的从容，自由与大海，朴素词语臻于完美。

## (2) 意象

- 主意象：自由、大海、奥涅金、玫瑰、冬天、缪斯；辅意象：高加索、月亮、夜；禁意象：华丽堆砌、抽象空话；密度中等，意象多取自自然与日常，清澈而精确。

## (3) 韵律与句式

- 以奥涅金诗节（十四行变体）与自由体并行；句式清澈、从容，长短交错；善用排比与对仗；节奏如散步，平稳而有力，朗读时有从容感。

## (4) 语言密度与词汇

- 词汇清澈而精确：日常俄语词承载大义；动词有力；形容词少而重；禁词：华丽堆砌、抽象空话。

## (5) 结构习惯

- 长诗与短诗并行：《叶甫盖尼·奥涅金》以诗节成章，八章成篇；短诗成组；开头多直入场景或意象，结尾多以警句或沉思收束；视角多为第一人称叙事者；推进靠诗节递进。

## (6) 该写什么 / 不该写什么

- 该写：自由与大海、奥涅金诗节；清澈的语言、从容的节奏；朴素词语的完美。
- 不该写：风格上的禁区——ornate excess, no abstract discourse without an image, no sentimental sweetness, no political slogans, no loose unstructured lines。
- Negative prompt: `No ornate excess, no abstract discourse without an image, no sentimental sweetness, no political slogans, no loose unstructured lines`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Pushkin, a letter to oneself ten years from now. Clear Russian verse, Onegin stanza and lyric ease, freedom and the sea, plain words that are perfect.`
- 中文对照：普希金风格：一封写给十年后自己的信。清澈的俄语诗，奥涅金诗节与抒情的从容，自由与大海，朴素词语臻于完美。
- Negative: `No ornate excess, no abstract discourse without an image, no sentimental sweetness, no political slogans, no loose unstructured lines`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
