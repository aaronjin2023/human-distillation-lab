# Emily Dickinson — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emily Dickinson: short lines and dashes, slant rhyme, Death as a quiet guest, the garden and the house as the whole world, a small room holding Eternity, no explanation`
- ZH: 狄金森风格：短行与破折号，半韵，死神是一位安静的客人，花园与房子即整个世界，一间小屋装下永恒，不作解释。

## (2) 意象

- 死神（安静的客人，驾车而来）
- 花园与蜜蜂（小世界的大）
- 房子与房间（内在空间）
- 光与苍蝇（临终的光）
- 永恒与可能（抽象借小物）
- 禁意象：宏大的场面、冗长的铺陈、直白的说教
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 短行、赞美诗体（四行、半韵），破折号即停顿；句式简省，长短交错；跨行少，行断如呼吸；整体节奏短促、顿挫，晚期更简、更密。

## (4) 语言密度与词汇

- 词汇：日常词极准（死神、蜜蜂、花园、房子），抽象词（永恒、可能）借小物落地；善用破折号压缩意义，一折抵一句；禁词：冗长议论词、华丽形容词、直白说教词。

## (5) 结构习惯

- 单篇多以一物（死神、蜜蜂）起兴，短行推进，末句翻转或戛然而止；手抄本以 fascicle（小册）编排，组诗以小册推进；结尾多为开放的顿悟而非收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 短行、破折号与半韵
- 死神、花园、房子的意象
- 小中见大的结构
- 戛然而止的结尾
- 不该写：
- 宏大场面与冗长铺陈
- 直白说教
- 华丽形容词堆砌
- 解释性的收束
- Negative prompt: `No grand scenes, no long explanatory passages, no ornate adjectives, no direct preaching, no sentimental happy ending, no explaining the dash`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Emily Dickinson, a small Yorkshire terrier sits on a subway seat at night. Short lines and dashes, slant rhyme, Death as a quiet guest beside the dog, the carriage as a small house holding Eternity, no explanation.`
- 中文对照：狄金森风格：一只约克夏犬深夜坐在地铁座位上。短行与破折号，半韵，死神是坐在狗身边的安静客人，车厢是一间装下永恒的小屋，不作解释。
- Negative: `No grand scenes, no long passages, no ornate adjectives, no preaching, no sentimental ending, no explaining the dash`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
