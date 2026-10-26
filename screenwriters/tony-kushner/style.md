# Tony Kushner — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tony Kushner: an epic in two parts, angels and ghosts arguing about history, long lyrical speeches, the personal as political, a dialectic that refuses to resolve`
- ZH: 托尼·库什纳风格：两部曲史诗，天使与幽灵争论历史，长篇抒情演讲，个人即政治，拒绝解决的辩证法。

## (2) 结构：三幕 / 序列 / 节拍

- 史诗双部结构：《天使在美国》是两部曲、多线并行；《林肯》把历史压缩进一个月、一个修正案；《慕尼黑》是复仇与良心的双线；转折点是人物在历史面前的选择。`impression`

## (3) 对话

- 对白是长篇的、抒情的、辩论式的演讲：人物用语言进行哲学与政治论战；天使、幽灵、先知都可以开口；潜台词是‘历史会审判我们吗’。`impression`

## (4) 人物弧光

- 主角类型：历史夹缝中的普通人（律师、同性恋者、总统）；弧光是‘在历史中认领自己’：人物从被历史推着走，到主动选择立场；结局是和解而非胜利。`impression`

## (5) 类型套路与创新

- 类型：历史 / 政治 / 史诗，遵守‘大历史小人物’套路；创新是把天使与超现实写进历史剧，把辩论写成剧情。禁套路：不用历史决定论的冷峻，不用‘好人必胜’的简化。`impression`

## (6) 该写什么 / 不该写什么

- 该写：两部曲与多线并行、长篇抒情演讲、天使与幽灵开口说话、历史压缩进一个月、辩证式开放收束。
- 不该写：历史决定论的冷峻、‘好人必胜’的简化、人物沦为历史注脚、辩论变成说教。
- Negative prompt: `No cold historical determinism, no good-guys-always-win simplification, no character reduced to a footnote, no debate turned into preaching, no ending that pretends history is settled`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Tony Kushner, a man writes a letter to himself ten years from now, and an angel interrupts to argue about whether history moves forward. Long lyrical speeches, ghosts in the room, the personal as political. No settled ending.`
- 中文对照：托尼·库什纳风格：一个男人给十年后的自己写信，一位天使打断他，争论历史是否向前。长篇抒情演讲，房间里有幽灵，个人即政治。没有定论的结局。
- Negative: `No cold historical determinism, no good-guys-always-win simplification, no character reduced to a footnote, no debate turned into preaching, no ending that pretends history is settled`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
