# Nizami Ganjavi — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nizami: romantic narrative epic in couplets, lovers parted by fate, seven pavilions and seven colours, love as a spiritual ascent, ornate yet disciplined`
- ZH: 尼扎米风格：爱情叙事长诗，对句体，恋人被命运拆散，七重亭阁七色，爱是精神攀升，华美而有节制

## (2) 意象

- 主意象：恋人、沙漠、亭阁、月、玫瑰园；辅意象：猎鹰、宫殿、星辰、酒；禁意象：粗鄙市井、直白肉欲；密度中等偏高，意象来自宫廷、传说与苏菲象征。`impression`

## (3) 韵律与句式

- 对句体长篇，句长整齐，叙事舒缓、抒情处放慢；对话短句交错；节奏如商队行进，间有停顿咏叹。`impression`

## (4) 语言密度与词汇

- 词汇：爱情、美、命运、灵魂等词域，典雅华美；善用比喻群（月喻面、玫瑰喻唇）；禁词：俚语、粗鄙词、现代抽象词。`impression`

## (5) 结构习惯

- 五卷各自独立又成体系；开头多为献词与祈祷，结尾以道德或苏菲寓意收束；视角全知叙事，恋人独白穿插；推进靠命运阻隔与重逢。`impression`

## (6) 该写什么 / 不该写什么

- 该写：爱情叙事长诗、七重结构与色彩象征、命运阻隔与重逢、苏菲寓意收束。
- 不该写：粗鄙市井描写、直白肉欲铺陈、碎片化短章、现代口语。
- Negative prompt: `No crude street scenes, no explicit carnal detail, no fragmented short lyrics, no modern slang, no cynical irony`

## (7) 测试提示词示例（现代题材：一只约克夏犬深夜坐在地铁座位上，乘客们看着它）

- Prompt: `In the style of Nizami, a small Yorkshire terrier sits on a subway seat at night. Romantic narrative couplets, the dog as a lonely lover parted by fate, seven colours of the carriage lights, love as ascent.`
- 中文对照：尼扎米风格：一只约克夏犬深夜坐在地铁座位上。爱情叙事对句，犬如被命运拆散的恋人，车厢灯光七色，爱是攀升
- Negative: `No crude street scenes, no explicit carnal detail, no fragmented short lyrics, no modern slang, no cynical irony`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
