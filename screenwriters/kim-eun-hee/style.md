# Kim Eun-hee — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Eun-hee: a genre machine with a historian's patience, a female investigator who never blinks, the past calling the present on a broken radio`
- ZH: 金银姬风格：类型机器带着史学家的耐心，永不眨眼的女调查员，过去通过一台坏掉的对讲机呼叫现在。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧双线并行：《信号》以对讲机连接过去与现在，双线交织、季终回收；《王国》以丧尸类型写朝鲜历史，季弧层层推进；《恶鬼》以民间传说为骨架。闪回即结构，时间线常双线交织。

## (3) 对话

- 对白克制、专业，人物用质问、沉默、调查术语交锋；潜台词多，一句日常问候可藏一层过去。动作描写细致（调查、追踪、仪式），对白与动作互相印证。旁白不用。

## (4) 人物弧光

- 主角多为女调查员：朴海英、徐惠珍，弧光是坚持与代价的拉锯；人物越查越深，结尾常是部分真相。人物关系以过去与现在的对照为主。

## (5) 类型套路与创新

- 类型：悬疑 / 历史 / 民俗惊悚。遵守类型片的规则，打破‘类型只为刺激’的成见：类型即历史。创新在把对讲机、丧尸、恶鬼写成历史隐喻，把女性调查员写进类型中心。

## (6) 该写什么 / 不该写什么

- 该写：双线并行的季弧、女调查员作中心、类型即历史、过去呼叫现在、部分真相的结尾。
- 不该写：大团圆、直白说教、类型化惊吓桥段、全知旁白、主角突然开挂。
- Negative prompt: `No happy ending, no direct preaching, no horror cliché, no omniscient narration, no sudden superpower`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kim Eun-hee, a woman buys oden at a convenience store late at night. A broken radio crackles with a voice from twenty years ago. She writes down every word. The past is calling. She answers.`
- 中文对照：金银姬风格：一个女人深夜在便利店买关东煮。一台坏掉的收音机传出二十年前的声音。她逐字记下。过去在呼叫。她回答。
- Negative: `No happy ending, no direct preaching, no horror cliché, no omniscient narration, no sudden superpower`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
