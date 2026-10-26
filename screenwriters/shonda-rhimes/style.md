# Shonda Rhimes — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shonda Rhimes: fast talk, big feelings, an ensemble that never stops moving, a cliffhanger at the end of every act, love and work in the same breath`
- ZH: 莱梅斯风格：快语速，大情绪，群像永不停歇，每幕结尾一个悬念，爱情与工作同一口气。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧多线并行、群像交织：《实习医生格蕾》以医院为容器，每集多线并行、每幕结尾设钩子；季弧以人物关系的大事件为节点。单集结构紧凑，闪回少，靠悬念推进。

## (3) 对话

- 对白快、密、情绪饱满，人物用抢白、长句、独白交锋；金句多，潜台词少，情绪直接说出口。动作描写简洁，场景提示明确，对白密度高。独白（旁白）是招牌结构。

## (4) 人物弧光

- 主角多为职业女性：医生、危机公关人、律师，弧光是成长与跌倒交替；人物在每季大事件后改变，又在下一季面临新考验。人物关系以职场与爱情的交织为主。

## (5) 类型套路与创新

- 类型：职场剧 / 情感剧。遵守‘每幕一钩子’的套路，打破‘职场剧只写工作’的成见：工作即情感。创新在把群像与快节奏写成招牌，把女性主角写进主流黄金档中心。

## (6) 该写什么 / 不该写什么

- 该写：快语速与大情绪、群像多线并行、每幕结尾的悬念、职场即情感、女性主角作中心。
- 不该写：慢节奏、冷峻克制、直白说教、单线独角戏、无悬念的平铺。
- Negative prompt: `No slow pacing, no cold detachment, no direct preaching, no single-thread story, no flat plotting without a hook`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Shonda Rhimes, a surgeon buys oden at a convenience store late at night after a twelve-hour shift. She talks fast. Her phone buzzes with a crisis. Every act ends on a question. Love and work in the same breath.`
- 中文对照：莱梅斯风格：一位外科医生值完十二小时班，深夜在便利店买关东煮。她语速很快。手机震动，又有危机。每幕结尾一个问题。爱情与工作同一口气。
- Negative: `No slow pacing, no cold detachment, no direct preaching, no single-thread story, no flat plotting without a hook`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
