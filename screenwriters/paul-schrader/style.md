# Paul Schrader — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Schrader: transcendental loneliness, a diary kept by a man who cannot sleep, the city at night as a purgatory, violence as a failed prayer, a protagonist who watches himself fall`
- ZH: 保罗·施拉德风格：先验式的孤独，一位无法入睡的人写的日记，深夜的城市即炼狱，暴力是一次失败的祈祷，一位注视自己坠落的主角。

## (2) 结构：三幕 / 序列 / 节拍

- 日记式三幕：第一幕立下一个孤独的男人与一本日记，第二幕让他在城市夜里游荡、一次次接近救赎又一次次错过，第三幕以一次暴力爆发收束——不是胜利，而是失败的祈祷。时间跨度短，常为数周，靠日记的日期而非悬念组织。

## (3) 对话

- 对白少而冷：短句、独白、画外音，日记式的自白是标志——人物在日记里说出白天不敢说的话。动作描写写夜游：出租车、街道、霓虹，城市本身就是人物。独白多，对话少。

## (4) 人物弧光

- 主角多为孤独的男人：司机、拳手、舞男。弧光是坠落——从孤独到暴力，从暴力到更深的孤独，救赎只出现一瞬又熄灭。对手是主角自己，城市只是他内心的外化。

## (5) 类型套路与创新

- 心理剧情片 / 黑色电影 / 体育传记片。他遵守黑色电影的夜与孤独套路，但打破了“主角必须行动”的成见：主角大部分时间只是在看、在写日记。创新在先验风格——把日本电影的静默与欧洲艺术片的疏离搬进好莱坞类型片。禁套路：几乎不用群戏的热闹，不写圆满的救赎。

## (6) 该写什么 / 不该写什么

- 该写：先验式孤独与日记结构、深夜城市即炼狱、暴力是一次失败的祈祷、主角注视自己的坠落。
- Negative prompt: `No cozy ensemble warmth, no earned redemption, no fast action spectacle, no witty banter, no sentimental romance`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Paul Schrader, a night-shift taxi driver buys oden at a convenience store at 3 a.m. and writes in his diary about the steam. Transcendental loneliness, the city at night as a purgatory, violence as a failed prayer. He watches himself fall, and writes it down.`
- 中文对照：保罗·施拉德风格：一位夜班出租车司机凌晨三点在便利店买关东煮，在日记里写下蒸汽。先验式的孤独，深夜的城市即炼狱，暴力是一次失败的祈祷。他注视自己坠落，并把它写下来。
- Negative: `No cozy ensemble warmth, no earned redemption, no fast action spectacle, no witty banter, no sentimental romance`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
