# Ludwig van Beethoven — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Heroic Classical-Romantic transition, motivic development, dramatic contrasts, expanded sonata form, rhythmic drive, struggle to triumph, late quartets' introspection`
- ZH: 英雄的古典—浪漫过渡，动机发展，戏剧对比，扩展的奏鸣曲式，节奏驱动，斗争到胜利，晚期四重奏的内省。

## (2) 旋律与和声

- 旋律：旋律富于动力，短动机驱动全曲；晚期四重奏旋律内省、断裂。`artifact` 和声：功能和声为基底，突然转调与不协和作戏剧；晚期和声更自由；禁用无动机的随意半音。调性：调性游移靠动机发展，终止有力。

## (3) 节奏与织体

- 节奏：节奏驱动性强，短—短—短—长的动机节奏是标志；切分与突然停顿制造张力。织体：主调与复调并重，晚期四重奏织体复杂；留白靠突然停顿。

## (4) 配器与音色

- 配器与音色：管弦乐队（弦乐、木管、铜管、定音鼓）与合唱（第九）并重；音色有力、辉煌；力度变化极大，靠突然强弱对比；空间感来自维也纳公众音乐会的宏大。

## (5) 曲式与结构

- 曲式：交响曲（九部）、钢琴奏鸣曲、弦乐四重奏、弥撒并重；奏鸣曲式扩展。结构：动机—发展—再现—尾声，高潮在尾声；第九以合唱终乐章收束；晚期四重奏以连续乐章组织。

## (6) 该写什么 / 不该写什么

- 该写：短动机发展、扩展奏鸣曲式、戏剧对比与突然强弱、第九交响曲的合唱终乐章、晚期四重奏的内省。
- 不该写：无动机的旋律堆砌、随意半音与无调性、管弦乐盖过动机、与结构无关的装饰、感伤的滥情。
- Negative prompt: `No motif-free melody piling, no random chromaticism, no orchestra covering motifs, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：清晨苏醒的菜市场）

- Prompt: `In the style of Ludwig van Beethoven, a 30-second piece for a morning vegetable market waking up, heroic classical-romantic transition, motivic development, dramatic contrasts, expanded sonata form, rhythmic drive, struggle to triumph, late quartets' introspection`
- 中文对照：贝多芬风格，为清晨苏醒的菜市场写 30 秒配乐，英雄的古典—浪漫过渡，动机发展，戏剧对比，扩展的奏鸣曲式，节奏驱动，斗争到胜利，晚期四重奏的内省。
- Negative: `No motif-free melody piling, no random chromaticism, no orchestra covering motifs, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
