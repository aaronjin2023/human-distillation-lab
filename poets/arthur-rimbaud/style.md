# Arthur Rimbaud — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arthur Rimbaud: the seer who disorders all the senses, vowels in colour, the drunken boat adrift, prose poems like hallucinations, syntax broken open, adolescence as prophecy, then silence`
- ZH: 兰波风格：以感官错乱求见灵的先知，元音带颜色，醉舟漂流，散文诗如幻觉，句法被打碎，青春即预言，然后沉默。

## (2) 意象

- 醉舟（漂流、无舵、无归）
- 元音的颜色（A 黑、E 白、I 红、O 蓝、U 绿）
- 地狱与天堂（《地狱一季》的自我审判）
- 沙漠、星辰、洪水（《彩画集》的幻象）
- 童年与流浪（出走即方法）
- 禁意象：安稳的家居、温情的田园
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体与散文诗并行：《醉舟》以长句奔涌、跨行不断；《彩画集》以散文段落写诗的密度，句式断裂、意象跳接；晚期短句如电报，省略一切连接词。

## (4) 语言密度与词汇

- 词汇：感官词极密且错位（颜色给声音、味道给光线），新词与古词并置；动词多为暴力态（撕、烧、漂、坠）；禁词：温和的过渡词、解释性的连接词、安慰语。

## (5) 结构习惯

- 单篇多以幻象并置推进，无叙事因果；《地狱一季》以九节独白作自我审判，层层否定；《彩画集》以42 首散文诗作幻象陈列，顺序即意义；结尾多为戛然而止或自我放逐。

## (6) 该写什么 / 不该写什么

- 该写：
- 感官错乱的通感
- 醉舟、元音、地狱的幻象并置
- 断裂的句式与意象跳接
- 青春的预言语气与自我放逐的结尾
- 不该写：
- 安稳家居与温情田园
- 解释性的过渡与因果
- 温和的安慰与团圆
- 工整的格律收束
- Negative prompt: `No cosy domesticity, no explanatory transitions, no sentimental consolation, no neat metrical closure, no cautious moderation, no prose that explains the image`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Arthur Rimbaud, a small Yorkshire terrier sits on a subway seat at night. The drunken boat of the carriage, vowels in colour, the dog as a small seer adrift among strangers, syntax broken open, hallucinatory prose, an ending that abandons the train.`
- 中文对照：兰波风格：一只约克夏犬深夜坐在地铁座位上。车厢如醉舟，元音带颜色，狗是一个漂流在陌生人中的小先知，句法被打碎，幻觉般的散文诗，结尾抛下整列车。
- Negative: `No cosy domesticity, no explanations, no sentimental consolation, no neat closure, no moderation`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
