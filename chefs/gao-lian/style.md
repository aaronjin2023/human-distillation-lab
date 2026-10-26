# Gao Lian — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gao Lian: Ming literati dining, crab and tea snacks, food as part of nourishing life, elegant restraint, seasonal delicacy, no banquet excess, no heavy seasoning`
- ZH: 高濂风格：明代文人饮馔，蟹与茶食，饮食为养生的一部分，雅致克制，时令精致，没有宴飨排场，没有重味。

## (2) 味型方向

- 主味：清鲜——蟹之鲜、茶之香为本，清淡而精。`artifact`
- 辅味：甘，茶食之甘，清甜不腻。
- 禁味：辛辣、油腻、重酱。
- 味型层次：单味直给而有余香，清淡之中见茶香。`impression`
- 浓淡对比度：淡，以淡见长；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：文人刀工，蟹取肉讲巧，茶食切形讲雅，刀工即是菜品的一部分。`impression`
- 火候：火候温和，蟹蒸取鲜，茶食以文火烘焙。`impression`
- 质感：鲜、嫩、酥并存；蟹靠蒸得嫩，茶食靠烘得酥。

## (4) 调味

- 调味料：极简，姜醋为蟹之配，盐少许而已。`artifact`
- 调味顺序：先备后调，蟹配姜醋现调现吃，不提前腌渍。
- 禁调味：一切浓味调料；不用酱、辛香压过蟹鲜与茶香。

## (5) 摆盘与食材选择

- 摆盘：文人器皿，瓷盘宜兴，留白多，雅致为上。`impression`
- 食材选择：蟹取当季，茶取新茶，皆取时令；不求珍稀，但求合时。
- 上菜节奏：饮馔之序，先蟹后茶食，先鲜后香。

## (6) 该做什么菜 / 不该做什么菜

- 该做：蟹、茶食、饮馔服食、姜醋配蟹、时令精致、瓷盘留白、茶香清鲜。
- 不该做：`No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning, no lavish presentation`
- Negative prompt: `No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning, no lavish presentation`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬的晚餐）

- Prompt: `In the style of Gao Lian, a tiny dinner for a Yorkshire terrier on a subway seat: one small steamed crab leg with ginger and vinegar, a single tea snack on a porcelain plate, much empty space, elegant restraint, seasonal delicacy, no heavy seasoning`
- 中文对照：高濂风格：一只坐在地铁里的约克夏犬的晚餐：一小只清蒸蟹腿配姜醋，一块茶食放在瓷盘上，留白很多，雅致克制，时令精致，没有重味。
- Negative: `No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
