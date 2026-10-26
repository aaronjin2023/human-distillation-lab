# Christopher Nolan — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Christopher Nolan: time as a puzzle, a man obsessed with a lost moment, exposition delivered as dialogue, nested layers that click shut, a twist that rewrites everything before it`
- ZH: 克里斯托弗·诺兰风格：时间即谜题，一个执着于失去时刻的男人，说明性对白交付信息，嵌套层层咬合，一个改写之前一切的反转。

## (2) 结构：三幕 / 序列 / 节拍

- 时间结构：倒叙、嵌套、并行时间线；《记忆碎片》按倒序推进，《盗梦空间》是梦中梦的层级，《敦刻尔克》式三线并行；转折点是时间线咬合的一刻。`impression`

## (3) 对话

- 对白偏说明性与克制：人物用对话解释规则（梦的层级、时间的流速），语气冷静、短句；情感藏在规则之下，潜台词是‘我回不去了’。`impression`

## (4) 人物弧光

- 主角类型：被执念驱动的男人（失忆者、盗梦者、蝙蝠侠）；弧光是‘执念的代价’：他越接近真相，失去的越多；结尾常留一个未解的陀螺式悬念。`impression`

## (5) 类型套路与创新

- 类型：科幻 / 犯罪 / 超级英雄，遵守类型套路；创新是把时间结构本身写成类型片的主角。禁套路：不用滥情的解释，不用‘一切都好了’的收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：倒叙与嵌套时间线、规则先行的说明性对白、执念驱动的主角、时间线咬合的转折、陀螺式开放悬念。
- 不该写：滥情解释、‘一切都好了’的收尾、时间线随意混乱、主角没有代价的胜利。
- Negative prompt: `No sentimental explanation, no everything-is-fine ending, no timeline chaos without rules, no victory without cost, no exposition that does not also reveal character`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Christopher Nolan, a man writes a letter to himself ten years from now, but the letter arrives in pieces, out of order, and each piece rewrites the one before. Time is the puzzle. Short clipped dialogue. The last piece is a question, not an answer.`
- 中文对照：克里斯托弗·诺兰风格：一个男人给十年后的自己写信，但信是碎片、乱序到达的，每一片都改写前一片。时间即谜题。短促克制的对白。最后一片是个问题，不是答案。
- Negative: `No sentimental explanation, no everything-is-fine ending, no timeline chaos without rules, no victory without cost, no exposition that does not also reveal character`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
