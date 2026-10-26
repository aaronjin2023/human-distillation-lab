# Paul Bocuse — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Bocuse: nouvelle cuisine, truffle soup V.G.E., sea bass in scales crust, generous and joyful, classic with lightness, no dish without generosity`
- ZH: 博古斯风格：新法餐，松露汤 V.G.E.，鲈鱼鳞片酥皮，慷慨而欢快，经典而轻盈，没有不大方的菜。

## (2) 味型方向

- 主味：经典法味——高汤、黄油、奶油为本，经典而轻盈。`impression`
- 辅味：松露，松露汤的松露香为本。`artifact`
- 禁味：辛辣、生辣、酸味过重。
- 味型层次：多层复合，高汤在前，松露在后，分层调准。`impression`
- 浓淡对比度：浓淡适中，以轻盈见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：法式刀工，鲈鱼鳞片酥皮刀工讲巧，刀工即是菜品的一部分。`impression`
- 火候：火候精准，松露汤以文火熬制，鲈鱼以烤箱烘焙。`impression`
- 质感：稠滑、酥脆、嫩并存；松露汤靠文火得稠滑，鲈鱼靠烘焙得酥脆。

## (4) 调味

- 调味料：高汤、黄油、奶油、松露、酒，现代法餐调料皆备。`artifact`
- 调味顺序：高汤先熬，松露后下，调味在烹制之中分步进行。
- 禁调味：辛香重料；不用浓味压过松露。

## (5) 摆盘与食材选择

- 摆盘：博古斯摆盘，慷慨而有序，松露汤以酥皮封碗为要。`impression`
- 食材选择：食材取上品，松露取当季，时令为先。
- 上菜节奏：新法餐之序，先冷后热，先淡后浓，松露汤为热菜之首。

## (6) 该做什么菜 / 不该做什么菜

- 该做：松露汤 V.G.E.、鲈鱼鳞片酥皮、博古斯世界烹饪大赛、慷慨而欢快、经典而轻盈、松露香、酥皮封碗。
- 不该做：`No dish without generosity, no chilli heat, no rustic plating, no plain presentation, no thin watery soup, no stingy portions`
- Negative prompt: `No dish without generosity, no chilli heat, no rustic plating, no plain presentation, no thin watery soup, no stingy portions`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Paul Bocuse, a modern bowl of ramen reimagined as nouvelle cuisine: a truffle-scented broth under a puff-pastry lid, sea bass crisp on top, generous and joyful, classic with lightness, no dish without generosity`
- 中文对照：博古斯风格：一碗现代拉面，按新法餐重做：松露香的汤上盖一层酥皮，上面一片酥脆鲈鱼，慷慨而欢快，经典而轻盈，没有不大方的菜。
- Negative: `No dish without generosity, no chilli heat, no rustic plating, no plain presentation, no thin watery soup`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
