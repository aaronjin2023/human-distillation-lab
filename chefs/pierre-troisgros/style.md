# Pierre Troisgros — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pierre Troisgros: French cuisine, salmon with sorrel sauce, Maison Troisgros, acidity as the signature, lightness and precision, no dish without acidity`
- ZH: 特鲁瓦格罗风格：法餐，鲑鱼配酸模酱，Maison Troisgros，酸味就是签名，轻盈而精准，没有没酸味的菜。

## (2) 味型方向

- 主味：酸鲜——酸模酱的酸味衬鲑鱼之鲜，酸就是签名。`artifact`
- 辅味：黄油与奶油，法餐的底味。`impression`
- 禁味：辛辣、生辣、酸味过重。
- 味型层次：多层复合，酸味在前，鲜味在后，分层调准。`impression`
- 浓淡对比度：淡而集中，以酸味见长；酸度中高，辣度近于无。

## (3) 刀工与火候

- 刀工：法式刀工，鲑鱼切法以衬酸模酱为主，片、丁皆匀。`impression`
- 火候：火候精准，鲑鱼以小火煎嫩，酸模酱以文火熬制。`impression`
- 质感：嫩、滑、酸并存；鲑鱼靠小火得嫩，酸模酱靠文火得滑。

## (4) 调味

- 调味料：酸模、黄油、奶油、高汤、酒，法餐调料皆备；酸模为调味之本。`artifact`
- 调味顺序：酸模酱先熬，鲑鱼后煎，调味在烹制之中分步进行。
- 禁调味：辛香重料；不用浓味压过酸味。

## (5) 摆盘与食材选择

- 摆盘：Maison Troisgros 摆盘，精致而有序，鲑鱼以酸模酱的绿为要。`impression`
- 食材选择：鲑鱼取鲜，酸模取当季，皆取上品。
- 上菜节奏：法餐之序，先冷后热，先淡后浓，鲑鱼为热菜之首。

## (6) 该做什么菜 / 不该做什么菜

- 该做：鲑鱼配酸模酱、Maison Troisgros、法式精致料理、酸味就是签名、轻盈而精准、酸模酱、小火煎嫩。
- 不该做：`No dish without acidity, no chilli heat, no rustic plating, no overcooked salmon, no plain presentation, no heavy sauce`
- Negative prompt: `No dish without acidity, no chilli heat, no rustic plating, no overcooked salmon, no plain presentation, no heavy sauce`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Pierre Troisgros, a modern bowl of ramen reimagined as French precision: salmon gently cooked, sorrel sauce bright green, acidity as the signature, lightness and precision, no dish without acidity`
- 中文对照：特鲁瓦格罗风格：一碗现代拉面，按法餐精准重做：鲑鱼小火煎嫩，酸模酱碧绿，酸味就是签名，轻盈而精准，没有没酸味的菜。
- Negative: `No dish without acidity, no chilli heat, no rustic plating, no overcooked salmon, no heavy sauce`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
