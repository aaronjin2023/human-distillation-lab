# Li Yu — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Yu: early Qing literati dining, bamboo shoots and crab as the highest tastes, food judged by pleasure not by price, elegant simplicity, no banquet excess, no heavy seasoning`
- ZH: 李渔风格：清初文人饮馔，笋与蟹为至味，饮食以适口为上，不以贵为上，雅致简朴，没有宴飨排场，没有重味。

## (2) 味型方向

- 主味：清鲜——笋之清、蟹之鲜为本，清淡而精。`artifact`
- 辅味：甘，笋的天然甘味，不加糖而甘。
- 禁味：辛辣、油腻、重酱。
- 味型层次：单味直给而有余味，清淡之中见本味。`impression`
- 浓淡对比度：淡，以淡见长；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：文人刀工，笋切片讲薄，蟹取肉讲巧，刀工即是菜品的一部分。`impression`
- 火候：火候温和，笋以沸水出鲜，蟹以蒸取鲜。`impression`
- 质感：清、爽、嫩并存；笋靠沸水得爽，蟹靠蒸得嫩。

## (4) 调味

- 调味料：极简，盐少许而已，笋蟹本身就是调料。`impression`
- 调味顺序：先备后调，出锅前少许盐提味，不夺本味。
- 禁调味：一切浓味调料；不用酱、醋、辛香压过笋清蟹鲜。

## (5) 摆盘与食材选择

- 摆盘：文人器皿，瓷盘留白多，雅致为上。`impression`
- 食材选择：笋取当季，蟹取肥满，皆取时令；不求珍稀，但求合时。
- 上菜节奏：饮馔之序，先笋后蟹，先清后鲜。

## (6) 该做什么菜 / 不该做什么菜

- 该做：笋、蟹、饮馔、清鲜本味、时令精致、瓷盘留白、雅致简朴。
- 不该做：`No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning, no lavish presentation`
- Negative prompt: `No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning, no lavish presentation`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Li Yu, a modern bowl of ramen reimagined as literati dining: clear broth, a few slices of bamboo shoot cut paper-thin, one small crab leg steamed, judged by pleasure not by price, elegant simplicity, served in a plain bowl with much empty space, no heavy seasoning`
- 中文对照：李渔风格：一碗现代拉面，按清初文人饮馔重做：清汤，几片切得极薄的笋，一小只清蒸蟹腿，饮食以适口为上不以贵为上，雅致简朴，陶碗留白很多，没有重味。
- Negative: `No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
