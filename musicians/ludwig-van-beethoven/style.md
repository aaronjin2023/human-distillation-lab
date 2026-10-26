# Ludwig van Beethoven — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Heroic struggle, motivic development, dramatic contrast, expanding sonata form, from Classical balance to Romantic intensity, fate knocking at the door`
- ZH: 英雄斗争，动机发展，戏剧对比，扩展的奏鸣曲式，从古典均衡到浪漫强度，命运敲门。

## (2) 音高与和声方向

- 主：功能和声 + 大胆半音与远关系转调；属—主收束强烈；晚期四重奏半音更自由。禁：无调性、半音滥用。调性：调性为斗争的场域，转调即冲突。

## (3) 旋律与节奏

- 旋律：短小动机（“命运”三短一长），级进与跳进交替；晚期旋律更内省、更碎片。节奏：驱动性强，突然停顿与重音。织体：主调与复调交替；晚期四重奏复调更密。

## (4) 配器与音色

- 乐器：管弦乐队、钢琴、弦乐四重奏、合唱。音色：从明亮到阴郁，幅度大。力度：极强到极弱，幅度为当时之最。

## (5) 曲式与结构

- 曲式：扩展的奏鸣曲式、变奏曲、赋格；交响曲四乐章、晚期四重奏多乐章。结构：呈示—展开—再现，但展开部大幅扩展；高潮在展开与再现交界。结尾：强烈收束，常以肯定收尾。

## (6) 该写什么 / 不该写什么

- 该写：动机发展、扩展奏鸣曲式、戏剧对比、晚期四重奏、英雄交响曲。
- 不该写：无调性、半音滥用、装饰泛滥、情感浮夸。
- Negative prompt: `atonality, aimless chromaticism, excessive ornament, sentimental bombast, pop chord loop`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of Ludwig van Beethoven, a quiet night scene at a small convenience store in a modern city, heroic struggle, motivic development, dramatic contrast, expanding sonata form, orchestra, from storm to affirmation`
- 中文对照：贝多芬风格，现代城市小便利店夜景，英雄斗争，动机发展，戏剧对比，扩展奏鸣曲式，管弦乐队，从风暴到肯定。
- Negative: `atonality, aimless chromaticism, excessive ornament, sentimental bombast, pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
