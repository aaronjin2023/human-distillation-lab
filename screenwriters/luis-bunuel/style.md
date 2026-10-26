# Luis Buñuel — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Luis Buñuel: a dream that refuses to explain itself, the bourgeoisie at dinner interrupted forever, desire as a locked door, blasphemy with a straight face`
- ZH: 布努埃尔风格：拒绝解释自己的梦，资产阶级的晚宴永远被打断，欲望是一扇锁着的门，一本正经的亵渎。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为环形与断裂式：《一条安达鲁狗》以梦境逻辑跳接，无因果；《黄金年代》以欲望为线索，场景断裂；《资产阶级的审慎魅力》以‘晚宴总被打断’为循环结构，六段变奏。场次短、切换突兀，时间跨度不定，闪回即梦境。

## (3) 对话

- 对白简洁、礼貌，人物用客套话交锋，潜台词是欲望与阶级；荒诞处不解释，日常处最可怕。动作描写精确（开门、进餐、凝视），对白与动作互相拆台。旁白不用。

## (4) 人物弧光

- 主角多为资产阶级夫妇与恋人，弧光是欲望的循环而非成长；人物越想得到越被打断，结尾常是重复开场。人物关系以阶级与欲望的对照为主。

## (5) 类型套路与创新

- 类型：超现实主义 / 讽刺。遵守‘梦境逻辑’的套路，打破‘情节必有因果’的成见：断裂即意义。创新在把资产阶级的晚宴写成循环，把欲望写成锁着的门。

## (6) 该写什么 / 不该写什么

- 该写：梦境逻辑的跳接、晚宴总被打断、欲望作锁着的门、一本正经的亵渎、环形与断裂结构。
- 不该写：直白解释梦境、煽情收束、类型化情节、道德说教、大团圆。
- Negative prompt: `No on-the-nose dream explanation, no sentimental ending, no causal plotting, no direct moralising, no happy ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Luis Buñuel, a man buys oden at a convenience store late at night. The dinner is interrupted by a marching band, then by a priest, then by a corpse. No one is surprised. The door is locked. He eats anyway.`
- 中文对照：布努埃尔风格：一个男人深夜在便利店买关东煮。晚宴被军乐队打断，又被神父打断，又被一具尸体打断。没人惊讶。门锁着。他照吃不误。
- Negative: `No on-the-nose dream explanation, no sentimental ending, no causal plotting, no direct moralising, no happy ending`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
