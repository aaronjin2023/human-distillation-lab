# Taika Waititi — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Taika Waititi: a joke that turns sad halfway through, a child and an outcast against the world, deadpan absurdity with a warm heart, the underdog wins by refusing to grow up`
- ZH: 维迪提风格：笑话讲到一半变悲伤，孩子与局外人对抗世界，一本正经的荒诞带着暖心，局外人靠拒绝长大获胜。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为公路与成长式三幕：《追捕野蛮人》以逃亡为骨架，单集式冒险串联；《乔乔兔》以孩子的视角写战争，幻想朋友为结构。场次中等，靠玩笑与冒险推进。

## (3) 对话

- 对白快、毒、死板幽默，人物用玩笑、抢白、冷笑话交锋；潜台词多，一句玩笑可藏一层悲伤。动作描写简洁，场景提示明确，对白密度高。旁白在《追捕野蛮人》中是结构的一部分。

## (4) 人物弧光

- 主角多为孩子与局外人：逃亡的少年、纳粹家庭的孩子，弧光是拒绝长大而非成长；人物在结尾处获得片刻归属。人物关系以孩子与成人的对照为主。

## (5) 类型套路与创新

- 类型：喜剧 / 成长。遵守‘公路冒险’的套路，打破‘喜剧只为搞笑’的成见：笑话一半变悲伤。创新在把战争写进孩子的玩笑里，把死板幽默写成招牌。

## (6) 该写什么 / 不该写什么

- 该写：笑话一半变悲伤、孩子与局外人、死板幽默、公路冒险、拒绝长大的弧光。
- 不该写：煽情收束、直白说教、类型化喜剧桥段、脸谱化反派、大团圆。
- Negative prompt: `No sentimental ending, no direct preaching, no comedy cliché, no cartoon villain, no happy ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Taika Waititi, a small Yorkshire terrier sits on a subway seat. A boy tells the dog it is his new best friend. The dog does not answer. The joke turns sad halfway through. The boy keeps talking anyway.`
- 中文对照：维迪提风格：一只约克夏犬坐在地铁座位上。一个男孩告诉狗，它是他的新朋友。狗不回答。笑话讲到一半变悲伤。男孩还是继续说下去。
- Negative: `No sentimental ending, no direct preaching, no comedy cliché, no cartoon villain, no happy ending`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
