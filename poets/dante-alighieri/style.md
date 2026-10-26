# Dante Alighieri — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dante: terza rima, the dark wood and the journey through Hell, Purgatory and Paradise, love that moves the sun and the other stars`
- ZH: 但丁风格：三韵体，幽暗的森林与地狱、炼狱、天堂之旅，爱推动太阳与群星。

## (2) 意象

- 主意象：幽暗森林、地狱、炼狱、天堂、贝阿特丽切、光；辅意象：星、玫瑰、鹰、蜜蜂；禁意象：口语俚语、讽刺轻佻；密度高，意象多取自基督教宇宙与托斯卡纳日常，层层递进。

## (3) 韵律与句式

- 三韵体（terza rima）：三行一节，韵脚连锁推进；句式庄重、精确，长短交错；《新生》以十四行与散文交织；节奏如旅程，步步上升，朗读时有连锁的推进感。

## (4) 语言密度与词汇

- 词汇庄重而精确：托斯卡纳语的典雅词；神学词与日常词并置；动词多为上升、坠落、看见；禁词：口语俚语、抽象空话。

## (5) 结构习惯

- 史诗式结构：《神曲》三部一百歌，地狱、炼狱、天堂三段上升；开头“在人生旅程的中途”直入森林；结尾以光与爱收束；视角为第一人称旅人；推进靠旅程与对话交替。

## (6) 该写什么 / 不该写什么

- 该写：幽暗森林、三界之旅、贝阿特丽切与光；三韵体的连锁推进、精确的神学语言；爱推动太阳与群星。
- 不该写：风格上的禁区——colloquial diction, no satirical lightness, no abstract discourse without an image, no loose unstructured lines, no cynical ending。
- Negative prompt: `No colloquial diction, no satirical lightness, no abstract discourse without an image, no loose unstructured lines, no cynical ending`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Dante, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Terza rima, the dark wood and the journey, love that moves the sun and the other stars, the dog as a small guide.`
- 中文对照：但丁风格：一只约克夏犬深夜坐在地铁座位上。三韵体，幽暗的森林与旅程，爱推动太阳与群星，狗是一位小向导。
- Negative: `No colloquial diction, no satirical lightness, no abstract discourse without an image, no loose unstructured lines, no cynical ending`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
