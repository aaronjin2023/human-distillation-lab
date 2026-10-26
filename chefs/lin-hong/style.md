# Lin Hong — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lin Hong: mountain household purity, seasonal flowers and fruits in cooking, plum-blossom soup noodles, crab stuffed in orange, elegant restraint, no banquet excess, no heavy seasoning`
- ZH: 林洪风格：山家清供，时令花果入馔，梅花汤饼、蟹酿橙，雅致克制，没有宴飨排场，没有重味。

## (2) 味型方向

- 主味：清雅——清淡而雅，花果之香为本。`artifact`
- 辅味：鲜，蟹之鲜、橙之酸鲜相衬。`artifact`
- 禁味：辛辣、油腻、重酱。
- 味型层次：单味直给而有余香，清淡之中见花果香。`impression`
- 浓淡对比度：极淡，以淡见长；酸度低而清，辣度近于无。

## (3) 刀工与火候

- 刀工：雅致刀工，梅花取形，蟹酿取巧，刀工即是菜品的一部分。`artifact`
- 火候：火候温和，汤饼以沸水出香，蟹酿以蒸取鲜。`impression`
- 质感：清、爽、嫩并存；汤饼靠沸水得爽，蟹酿靠蒸得嫩。

## (4) 调味

- 调味料：极简，盐少许而已，花果本身就是调料。`impression`
- 调味顺序：先备后调，出锅前少许盐提味，不夺花果香。
- 禁调味：一切浓味调料；不用酱、醋、辛香压过花果清香。

## (5) 摆盘与食材选择

- 摆盘：山野器皿，陶碗瓷盘，留白多，雅致为上。`impression`
- 食材选择：时令花果，梅花、橙、蟹皆取当季；不求珍稀，但求合时。
- 上菜节奏：清供之序，先汤饼后蟹酿，先清后鲜。

## (6) 该做什么菜 / 不该做什么菜

- 该做：梅花汤饼、蟹酿橙、山家清供、时令花果入馔、清雅克制、陶碗留白、花果清香。
- 不该做：`No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning, no lavish presentation`
- Negative prompt: `No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning, no lavish presentation`

## (7) 测试提示词示例（现代题材：一份深夜便利店的关东煮）

- Prompt: `In the style of Lin Hong, a late-night convenience store oden reimagined as mountain purity: clear broth with a single plum blossom floating, fish cake cut to suggest a flower, a small orange hollowed for the broth, elegant restraint, served in a plain bowl with much empty space, no heavy seasoning`
- 中文对照：林洪风格：一份深夜便利店关东煮，按山家清供重做：清汤里浮一朵梅花，鱼糕切成花形，小橙子挖空了盛汤，雅致克制，陶碗留白很多，没有重味。
- Negative: `No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no strong seasoning`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
