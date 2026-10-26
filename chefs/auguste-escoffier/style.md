# Auguste Escoffier — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Auguste Escoffier: father of modern French cuisine, Le Guide Culinaire, peach Melba, brigade kitchen order, simplified and systematised, classic and precise, no dish without order`
- ZH: 埃斯科菲耶风格：现代法餐之父，《烹饪指南》，桃子梅尔芭，厨房 brigade 之序，简化而体系化，经典而精准，没有没秩序的菜。

## (2) 味型方向

- 主味：经典法味——高汤、黄油、奶油为本，经典而精准。`artifact`
- 辅味：甜，桃子梅尔芭的甜味衬经典。`impression`
- 禁味：辛辣、生辣、酸味过重。
- 味型层次：多层复合，高汤在前，酱汁在后，分层调准。`impression`
- 浓淡对比度：浓淡适中，以精准见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：法式刀工，切法以衬高汤为主，片、丁皆匀。`impression`
- 火候：火候精准，高汤以文火熬制，桃子以小火煮软。`impression`
- 质感：稠滑、嫩、软并存；高汤靠文火得稠滑，桃子靠小火得软。

## (4) 调味

- 调味料：高汤、黄油、奶油、酒，现代法餐调料皆备。`artifact`
- 调味顺序：高汤先熬，酱汁后调，调味在烹制之中分步进行。
- 禁调味：辛香重料；不用浓味压过高汤。

## (5) 摆盘与食材选择

- 摆盘：现代法餐摆盘，经典而有序，桃子梅尔芭以雅致为要。`impression`
- 食材选择：食材取上品，时令为先；桃子取熟透。
- 上菜节奏：现代法餐之序，先冷后热，先淡后浓，甜点最后。

## (6) 该做什么菜 / 不该做什么菜

- 该做：《烹饪指南》、桃子梅尔芭、丽兹 / 萨伏伊厨房体系、高汤为本、brigade 之序、简化而体系化、经典而精准。
- 不该做：`No dish without order, no chilli heat, no rustic plating, no plain presentation, no thin watery stock, no careless brigade`
- Negative prompt: `No dish without order, no chilli heat, no rustic plating, no plain presentation, no thin watery stock, no careless brigade`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Auguste Escoffier, a modern bowl of ramen reimagined as modern French cuisine: a clear superior stock, brigade order in every step, peach Melba elegance in the garnish, simplified and systematised, classic and precise, no dish without order`
- 中文对照：埃斯科菲耶风格：一碗现代拉面，按现代法餐重做：清高汤，每一步都有 brigade 之序，配菜有桃子梅尔芭的雅致，简化而体系化，经典而精准，没有没秩序的菜。
- Negative: `No dish without order, no chilli heat, no rustic plating, no plain presentation, no thin watery stock`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
