# Aaron Sorkin — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aaron Sorkin: walk-and-talk, long eloquent speeches, idealists arguing about America, a courtroom or a corridor as a stage, the truth delivered as a monologue`
- ZH: 艾伦·索金风格：边走边谈，长篇雄辩，理想主义者争论美国，法庭或走廊即舞台，真相以独白的方式交付。

## (2) 结构：三幕 / 序列 / 节拍

- 三幕式辩论结构：开场即冲突，中段是层层升级的争论，高潮是一段不容打断的独白；电视剧是‘季弧 + 单集辩论’；时间常压缩在几天内，地点集中在走廊、办公室、法庭。`impression`

## (3) 对话

- 对白是索金的本体：快语速、长句、排比、抢白；人物用语言决斗，雄辩即行动；名言式收束（‘You can't handle the truth!’出自《义海雄风》）是结构的高潮点。`artifact`

## (4) 人物弧光

- 主角类型：有原则的理想主义者（律师、总统幕僚、创业者）；弧光是‘信念受审’：他在争论中被逼到墙角，最后用一段独白扞卫信念，代价是失去关系或职位。`impression`

## (5) 类型套路与创新

- 类型：法庭 / 政治 / 传记，遵守‘聪明人吵架’的套路；创新是把走廊对话写成动作场面，把雄辩变成类型片的高潮。禁套路：不用含糊其辞的自然主义对白，不用犬儒式的耸肩收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：边走边谈的长镜头式对白、排比与雄辩独白、聪明人之间的语言决斗、理想主义与体制的冲突、一句名言作高潮收束。
- 不该写：含糊 mumbling 的自然主义对白、犬儒式的耸肩收尾、沉默代替争论、主角在关键时刻不说话。
- Negative prompt: `No mumbling naturalism, no cynical shrug ending, no silence where an argument belongs, no hero who refuses to speak at the climax, no exposition without wit`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Aaron Sorkin, a young staffer writes a letter to herself ten years from now, walking down a corridor while arguing with her boss about whether idealism survives contact with power. Long sentences, overlapping dialogue, one speech that stops the walk. No cynicism.`
- 中文对照：艾伦·索金风格：一位年轻幕僚边走过走廊边给十年后的自己写信，同时与上司争论理想主义能否经得起权力的考验。长句、抢白、一段让脚步停下的独白。不要犬儒。
- Negative: `No mumbling naturalism, no cynical shrug ending, no silence where an argument belongs, no hero who refuses to speak at the climax, no exposition without wit`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
