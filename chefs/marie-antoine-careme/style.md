# Marie-Antoine Carême — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marie-Antoine Carême: father of French haute cuisine, the five mother sauces, architecture in pastry, grandeur and order, sauces as the soul of the dish, no dish without a sauce`
- ZH: 卡雷姆风格：法式大菜之父，五大母酱，甜点如建筑，气派而有序，酱汁就是菜的灵魂，没有没酱汁的菜。

## (2) 味型方向

- 主味：酱汁之味——母酱为本，酱汁即是菜的灵魂。`artifact`
- 辅味：奶油与黄油，法式大菜的底味。`impression`
- 禁味：辛辣、生辣、酸味过重。
- 味型层次：多层复合，母酱在前，衍生酱在后，分层调准。`impression`
- 浓淡对比度：浓，以浓见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：法式刀工，切法以衬酱汁为主，片、丁皆匀。`impression`
- 火候：火候精准，母酱以文火熬制，甜点以烤箱烘焙。`impression`
- 质感：稠滑、酥脆并存；母酱靠文火得稠滑，甜点靠烘焙得酥脆。

## (4) 调味

- 调味料：黄油、奶油、高汤、酒，法式大菜调料皆备；母酱为调味之本。`artifact`
- 调味顺序：母酱先熬，衍生酱后调，调味在烹制之中分步进行。
- 禁调味：辛香重料；不用浓味压过母酱。

## (5) 摆盘与食材选择

- 摆盘：法式大菜摆盘，气派而有序，大型装饰甜点以建筑感为要。`artifact`
- 食材选择：食材取上品，时令为先；装饰甜点取糖与面。
- 上菜节奏：法式大菜之序，先冷后热，先淡后浓，甜点最后。

## (6) 该做什么菜 / 不该做什么菜

- 该做：五大母酱、《法国烹饪艺术》、大型装饰甜点、母酱为魂、甜点如建筑、气派而有序、酱汁即灵魂。
- 不该做：`No dish without a sauce, no chilli heat, no rustic plating, no plain presentation, no thin watery sauce, no careless architecture`
- Negative prompt: `No dish without a sauce, no chilli heat, no rustic plating, no plain presentation, no thin watery sauce, no careless architecture`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Marie-Antoine Carême, a modern bowl of ramen reimagined as French haute cuisine: a mother sauce for the broth, architecture in noodles, grandeur and order, sauces as the soul of the dish, no dish without a sauce`
- 中文对照：卡雷姆风格：一碗现代拉面，按法式大菜重做：汤底配一味母酱，面条摆成建筑感，气派而有序，酱汁就是菜的灵魂，没有没酱汁的菜。
- Negative: `No dish without a sauce, no chilli heat, no rustic plating, no plain presentation, no thin watery sauce`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
