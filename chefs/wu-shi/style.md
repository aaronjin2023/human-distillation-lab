# Wu Shi — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wu Shi: Song-Yuan household cooking, preserved meats and pickled fish, vegetables and sweets made at home, frugal and exact, no banquet excess, no showy technique`
- ZH: 吴氏风格：宋元家常菜，脯鲊可久藏，制蔬甜食皆出中馈，节俭而精当，没有宴飨排场，没有炫技。

## (2) 味型方向

- 主味：咸鲜——脯鲊之咸鲜，可久藏而不失味。`artifact`
- 辅味：甜，制蔬甜食以果蜜为甜，清甜不腻。`artifact`
- 禁味：辛辣刺激、油腻重酱。
- 味型层次：单味直给，家常之味不求复合，但求恰当。`impression`
- 浓淡对比度：咸鲜为主，甜食清甜；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：家常刀工，切法以实用为主，片、丝、丁皆有，不求炫技。`impression`
- 火候：腌、晒、蒸、煮并用，火候温和；脯鲊重在腌制不在火候。`artifact`
- 质感：咸香、爽脆、软糯并存；脯鲊靠腌晒得咸香，制蔬靠时令得爽脆。

## (4) 调味

- 调味料：盐、酱、醋、蜜为主，调料皆家常所有。`artifact`
- 调味顺序：腌制先行，调味在腌不在炒；甜食以蜜调，不以糖夺味。
- 禁调味：辛香重料、浓油赤酱；不用重味压过家常本味。

## (5) 摆盘与食材选择

- 摆盘：家常器皿，陶碗瓷盘，满而不乱，丰盛即家常。`impression`
- 食材选择：时令蔬菜、鱼肉皆取当季，腌制以备不时之需。
- 上菜节奏：家常之序，先脯鲊后热菜，先咸后甜。

## (6) 该做什么菜 / 不该做什么菜

- 该做：脯鲊、制蔬、甜食、家常菜、腌制久藏、时令蔬菜、果蜜清甜。
- 不该做：`No banquet excess, no showy technique, no chilli heat, no heavy sauce, no greasy richness, no lavish presentation`
- Negative prompt: `No banquet excess, no showy technique, no chilli heat, no heavy sauce, no greasy richness, no lavish presentation`

## (7) 测试提示词示例（现代题材：一份深夜便利店的关东煮）

- Prompt: `In the style of Wu Shi, a late-night convenience store oden reimagined as Song-Yuan household cooking: fish cake preserved in light brine, seasonal vegetables simply simmered, a small sweet of fruit and honey to finish, frugal and exact, served in plain bowls, no banquet excess`
- 中文对照：吴氏风格：一份深夜便利店关东煮，按宋元家常菜重做：鱼糕淡盐水腌过，时令蔬菜清炖收尾一小碟果蜜甜食，节俭而精当，陶碗瓷盘盛着，没有宴飨排场。
- Negative: `No banquet excess, no showy technique, no chilli heat, no heavy sauce, no greasy richness`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
