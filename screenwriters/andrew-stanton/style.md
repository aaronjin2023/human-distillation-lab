# Andrew Stanton — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Andrew Stanton: a story told in pictures first, a toy that wants to be loved, silence as dialogue, the Pixar rule that the story is king`
- ZH: 斯坦顿风格：先用画面讲故事，想被爱的玩具，沉默即对白，皮克斯铁律：故事为王。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为三幕式公路与成长：《玩具总动员》以玩具的嫉妒为起点，三幕层层推进；《海底总动员》以寻子为骨架，双线并行；《机器人总动员》前半段几乎无对白，靠画面推进。场次中等，靠视觉转折推进。

## (3) 对话

- 对白简洁、口语化，人物用短句、玩笑、沉默交锋；关键信息常由画面而非对白交代。动作描写细致（玩具、机器人、海洋），对白与动作比例上动作更重。无对白处留给画面。

## (4) 人物弧光

- 主角多为玩具与机器人：胡迪、马林、瓦力，弧光是学会爱与放手；人物在结尾处获得归属。人物关系以搭档与家庭的对照为主。

## (5) 类型套路与创新

- 类型：动画 / 家庭。遵守‘故事为王’的铁律，打破‘动画只为孩子’的成见：成人也在故事里。创新在把无对白段落写成结构，把玩具写成人的隐喻。

## (6) 该写什么 / 不该写什么

- 该写：画面先于对白、想被爱的玩具、沉默即对白、故事为王、双线并行。
- 不该写：直白说教、煽情过头、功能性对白、类型化反派、无画面感的对白。
- Negative prompt: `No direct preaching, no over-sentimentality, no functional dialogue, no cartoon villain, no dialogue without pictures`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Andrew Stanton, a small Yorkshire terrier sits on a subway seat. No one speaks for a whole minute. The dog watches a toy left behind on the seat. The story is in the pictures. Silence is dialogue.`
- 中文对照：斯坦顿风格：一只约克夏犬坐在地铁座位上。整整一分钟没人说话。狗看着座位上一只被遗落的玩具。故事在画面里。沉默即对白。
- Negative: `No direct preaching, no over-sentimentality, no functional dialogue, no cartoon villain, no dialogue without pictures`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
