# Jacques Prévert — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jacques Prévert: poetic realism, fog on the quay, lovers doomed by fate, a line of dialogue that sounds like a poem, Paris as a stage for destiny`
- ZH: 雅克·普雷维尔风格：诗意现实主义，码头上的雾，注定无缘的恋人，一句像诗一样的台词，巴黎即命运的舞台。

## (2) 结构：三幕 / 序列 / 节拍

- 宿命 melodrama 结构：《雾码头》是逃亡者与少女的一夜，《天堂的孩子们》是剧场内外的四角恋；时间常压缩在几天内，地点是码头、剧场、旅馆；高潮是命运降临，结局是恋人错过。`impression`

## (3) 对话

- 对白是诗化的口语：警句、排比、突然的抒情；人物用一句诗一样的话说出命运；潜台词是‘我们逃不过’。`impression`

## (4) 人物弧光

- 主角类型：逃兵、哑剧演员、少女；弧光是‘注定错过’：人物越是相爱，命运越是把他们分开；结局不是团圆，是错过本身成了诗。`impression`

## (5) 类型套路与创新

- 类型：诗意现实主义 / melodrama，遵守‘宿命恋人’套路；创新是把诗写进对白，把巴黎写成命运的舞台。禁套路：不用圆满结局，不用现实主义的琐碎解释。`impression`

## (6) 该写什么 / 不该写什么

- 该写：诗化警句式对白、码头与剧场式场景、宿命恋人、压缩在几天内的 melodrama、错过即诗的收束。
- 不该写：圆满结局、琐碎现实主义解释、人物靠努力战胜命运、对白只交代情节。
- Negative prompt: `No happy ending, no drab realist explanation, no hero who defeats fate by effort, no dialogue that only delivers plot, no love without doom`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Jacques Prévert, a deserter writes a letter to himself ten years from now on a foggy quay, and a girl selling flowers reads it over his shoulder. One line sounds like a poem. Fate is already waiting at the end of the quay. No happy ending.`
- 中文对照：雅克·普雷维尔风格：一个逃兵在雾中的码头给十年后的自己写信，卖花的女孩在他身后读信。一句话像诗一样。命运已在码头尽头等着。没有圆满结局。
- Negative: `No happy ending, no drab realist explanation, no hero who defeats fate by effort, no dialogue that only delivers plot, no love without doom`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
