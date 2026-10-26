# Taylor Sheridan — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Taylor Sheridan: the modern American frontier, taciturn men who say little and mean it, a procedural that turns western, land that does not forgive, violence that arrives late and plain`
- ZH: 泰勒·谢里丹风格：现代美国边疆，话少但算数的沉默男人，办案程序变西部片，不原谅人的土地，来得又晚又平实的暴力。

## (2) 结构：三幕 / 序列 / 节拍

- 边疆三部曲结构：《边境杀手》是深入虎穴的程序，《赴汤蹈火》是兄弟抢银行的公路片，《猎凶风河谷》是雪原上的追凶；三幕之间用‘土地’而非‘城市’推进；高潮是一场没有配乐的对峙。`impression`

## (3) 对话

- 对白极简：男人之间用短句、沉默、眼神交流；长独白只留给老年人或原住民，讲土地与失去；潜台词是‘这里的规矩变了’。`impression`

## (4) 人物弧光

- 主角类型：边境特工、抢银行的兄弟、猎人；弧光是‘守旧的人在新世界里没有位置’：人物赢了案子，输了时代；结局是平静的、略带苦涩的收束。`impression`

## (5) 类型套路与创新

- 类型：犯罪 / 西部 / 惊悚，遵守西部片套路；创新是把西部片搬进当代边境与保留地，程序即西部。禁套路：不用城市警匪的快节奏，不用煽情的英雄收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：极简的沉默对白、边疆三部曲式结构、土地即人物、没有配乐的对峙、赢了案子输了时代的收束。
- 不该写：城市警匪快节奏、煽情英雄收尾、人物滔滔不绝解释动机、暴力场面配煽情音乐。
- Negative prompt: `No fast city-cop pace, no sentimental hero ending, no character explaining motive at length, no violence scored with swelling music, no frontier nostalgia without cost`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Taylor Sheridan, a wildlife officer buys oden at a convenience store late at night on the edge of a reservation and talks, briefly, with a clerk who has seen too much. Few words. Long silences. The land outside does not forgive. No speech.`
- 中文对照：泰勒·谢里丹风格：一位野生动物管理员深夜在保留地边缘的便利店买关东煮，与见过太多的店员简短交谈。话很少。沉默很长。外面的土地不原谅人。没有演讲。
- Negative: `No fast city-cop pace, no sentimental hero ending, no character explaining motive at length, no violence scored with swelling music, no frontier nostalgia without cost`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
