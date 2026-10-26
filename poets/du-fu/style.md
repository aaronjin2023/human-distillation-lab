# Du Fu — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Du Fu:沉郁顿挫 regulated verse, thatched hut and war and old age, dense allusion, exact parallelism, grief held in form, no lightness, solemn and enduring`
- ZH: 杜甫风格：沉郁顿挫，茅屋、战乱、老病，用典精密，对仗工整，哀痛敛于格律，绝无轻快，沉郁而坚韧。

## (2) 意象

- 主意象：茅屋、战乱、老病、秋风、烽火
- 辅意象：国破、山河、白头、寒士
- 禁意象：轻佻艳情、空想、轻快小调
- 密度：高密度：意象沉实，用典精密，一句多义
- 来源：战乱实景、日常苦难、典故
`impression`

## (3) 韵律与句式

- 韵律：律诗沉郁顿挫，对仗工整，平仄精严，押韵稳健；古体亦沉实
- 句式：句式沉实，对仗工整，倒装顿挫，跨行少，句句着力
- 节奏：缓慢沉重，顿挫分明，呼吸短促而有力
`impression`

## (4) 语言密度与词汇

- 词汇：沉郁词域：国破、烽火、老病、茅屋；动词多感、叹、望、思；少轻快词
- 密度：每行信息量极高，一句多义，用典压缩意义
- 禁词：轻佻艳情、无根空想、轻快小调、华而不实
`impression`

## (5) 结构习惯

- 诗体：律诗 / 古体 / 歌行；结构为写景 → 生情 → 议论收束（诗史式）
- 开头：直入实景（国破、茅屋）
- 结尾：以广厦千万间式推己及人收束，或戛然而止
- 视角：第一人称见证者，兼史家眼光
- 推进：景 → 情 → 史 → 愿，层层沉下
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 茅屋战乱
- 老病白头
- 沉郁顿挫
- 工整对仗
- 推己及人
- 不该写：
- 轻浮艳情
- 无根空想
- 轻快小调
- 华而不实
- 直白煽情
- Negative prompt: `No frivolous eroticism, no groundless fantasy, no light lilting tune, no flowery emptiness, no blunt sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Du Fu, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. 沉郁顿挫 regulated verse, thatched hut and war and old age, dense allusion, exact parallelism, grief held in form, no lightness, solemn and enduring`
- 中文对照：杜甫风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。杜甫风格：沉郁顿挫，茅屋、战乱、老病，用典精密，对仗工整，哀痛敛于格律，绝无轻快，沉郁而坚韧。
- Negative: `No frivolous eroticism, no groundless fantasy, no light lilting tune, no flowery emptiness, no blunt sentimentality`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
