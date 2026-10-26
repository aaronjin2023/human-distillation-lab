# Robert Frost — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Frost: plain New England speech in blank verse, stone walls and two roads, the woods lovely dark and deep, meaning hiding in the ordinary, a quiet turn at the end`
- ZH: 弗罗斯特风格：新英格兰的平实口语写空白体，石墙与两条路，树林幽暗而深邃，意义藏在日常里，结尾安静地一转。

## (2) 意象

- 石墙（《修墙》：墙的修与不修）
- 两条路（《未选择的路》的选择）
- 树林与雪（幽暗而深邃）
- 苹果与白桦（新英格兰的物）
- 夜与灯（《夜里熟识》）
- 禁意象：华丽的修辞、直白的说教、都市的轻佻
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 空白体与叙事体为主：以口语的节奏写五音步，句式平实、停顿自然；《北波士顿》以对话体推进；短行抒情诗以四行体求简；整体节奏由叙事的舒缓向抒情的简演变。

## (4) 语言密度与词汇

- 词汇：日常词极准（墙、路、雪、苹果），口语与空白体并置；抽象词（选择、孤独）借日常物落地；禁词：华丽形容词、直白说教词、都市俚语。

## (5) 结构习惯

- 单篇多以一景（墙、路、雪）起兴，叙事或对话推进，末句安静翻转；叙事诗以对话体推进，抒情诗以四行体收束；结尾多为含蓄的翻转而非爆发。

## (6) 该写什么 / 不该写什么

- 该写：
- 石墙、两条路、树林的意象
- 口语空白体的节奏
- 日常藏意义的结构
- 安静的翻转收束
- 不该写：
- 华丽修辞与直白说教
- 都市轻佻
- 冗长铺陈
- 煽情的爆发收束
- Negative prompt: `No ornate rhetoric, no direct preaching, no urban frivolity, no long explanatory passages, no sentimental outburst, no explaining the symbol`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Robert Frost, a small Yorkshire terrier sits on a subway seat at night. Plain New England speech in blank verse, the stone wall of the carriage, two roads diverging in the crowd, the woods lovely dark and deep, a quiet turn at the end.`
- 中文对照：弗罗斯特风格：一只约克夏犬深夜坐在地铁座位上。新英格兰的平实口语写空白体，车厢如石墙，人群中分出两条路，树林幽暗而深邃，结尾安静地一转。
- Negative: `No ornate rhetoric, no preaching, no urban frivolity, no long passages, no sentimental outburst, no explaining the symbol`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
