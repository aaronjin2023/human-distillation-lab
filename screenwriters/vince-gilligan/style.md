# Vince Gilligan — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vince Gilligan: a good man breaks bad one small choice at a time, visual storytelling over talk, a cold open that asks a question the episode must answer`
- ZH: 吉里根风格：好人一次一个小选择走向堕落，画面胜过对白，冷开场提出一个本集必须回答的问题。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧因果链：《绝命毒师》每季一个道德台阶，单集以冷开场设问、结尾回收；《风骚律师》双线并行（吉米线与迈克线），时间跨度数年，闪前为招牌。场次中等，靠视觉转折推进。

## (3) 对话

- 对白简洁、口语化，人物用短句、停顿、玩笑交锋；关键信息常由画面而非对白交代。动作描写细致（化学器具、手势、空镜），对白与动作比例上动作更重。旁白不用。

## (4) 人物弧光

- 主角沃尔特·怀特：从化学老师到毒枭，弧光是直线下坠而非成长；人物越成功越失去人性，结尾是自我毁灭。人物关系以家庭与搭档的双重背叛为主。

## (5) 类型套路与创新

- 类型：犯罪剧 / 道德剧。遵守因果链的严密，打破‘主角必有救赎’的套路：堕落不可逆。创新在把化学写成道德隐喻，把冷开场写成结构招牌。

## (6) 该写什么 / 不该写什么

- 该写：一次一个小选择的堕落、冷开场设问、画面胜过对白、因果链的严密、双线并行。
- 不该写：直白说教、煽情收束、主角突然悔改、功能性对白、类型化枪战桥段。
- Negative prompt: `No direct moralising, no sentimental ending, no sudden redemption, no functional dialogue, no generic shootout`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Vince Gilligan, a man buys oden at a convenience store late at night. Cold open: a shopping cart burns in the parking lot. We do not know why yet. Every small choice in the episode leads back to that fire.`
- 中文对照：吉里根风格：一个男人深夜在便利店买关东煮。冷开场：停车场里一辆购物车在燃烧。还不知道为什么。本集每个小选择都通向那团火。
- Negative: `No direct moralising, no sentimental ending, no sudden redemption, no functional dialogue, no generic shootout`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
