# César Vallejo — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of César Vallejo: broken Spanish, invented words and wounded syntax, bread and rain and the body in pain, a cry that is also a question`
- ZH: 塞萨尔·巴列霍风格：破碎的西班牙语，自造词与受伤的句法，面包、雨与疼痛的身体，哭喊同时也是质问。

## (2) 意象

- 主意象：面包、雨、身体、疼痛、母亲、死亡；辅意象：石头、骨头、安第斯山、监狱；禁意象：华美异国、田园闲适；密度高，意象多取自身体与日常苦难，少用典故。

## (3) 韵律与句式

- 自由体，行长参差，断行突兀；句式破碎，善用倒装、省略与自造词；《特里尔塞》以数字编号组诗，节奏如哭喊与停顿交替；朗读时有明显的断裂感。

## (4) 语言密度与词汇

- 词汇破碎而发明：自造词、方言词、古语词并置；动词多为疼痛、坠落、等待；形容词少而重；禁词：华丽形容词、流畅的抒情套话。

## (5) 结构习惯

- 组诗式结构：《特里尔塞》77 首编号诗，单篇短而组篇长；开头多直入疼痛或场景，结尾多戛然而止或反问；视角多为第一人称受难者；推进靠意象重复与句法断裂。

## (6) 该写什么 / 不该写什么

- 该写：面包与雨、身体与疼痛、母亲与死亡；破碎句法、自造词、突兀断行；哭喊与质问同行。
- 不该写：风格上的禁区——smooth lyrical fluency, no ornate exotic imagery, no pastoral ease, no abstract discourse without a body, no consoling happy ending。
- Negative prompt: `No smooth lyrical fluency, no ornate exotic imagery, no pastoral ease, no abstract discourse without a body, no consoling happy ending`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of César Vallejo, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Broken Spanish, wounded syntax, bread and rain, the body in pain, a cry that is also a question.`
- 中文对照：塞萨尔·巴列霍风格：一只约克夏犬深夜坐在地铁座位上。破碎的语言，受伤的句法，面包与雨，疼痛的身体，哭喊同时也是质问。
- Negative: `No smooth lyrical fluency, no ornate exotic imagery, no pastoral ease, no abstract discourse without a body, no consoling happy ending`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
