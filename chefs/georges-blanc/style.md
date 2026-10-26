# Georges Blanc — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georges Blanc: French cuisine, Bresse chicken, Village Blanc, the finest chicken in France, cream and morels, generous and precise, no dish without the best chicken`
- ZH: 布朗风格：法餐，布雷斯鸡，Village Blanc，法国最好的鸡，奶油与羊肚菌，慷慨而精准，没有不用最好的鸡的菜。

## (2) 味型方向

- 主味：鸡鲜——布雷斯鸡之鲜，奶油与羊肚菌衬鲜。`artifact`
- 辅味：奶油，法餐的底味。`impression`
- 禁味：辛辣、生辣、酸味过重。
- 味型层次：多层复合，鸡鲜在前，奶油在后，分层调准。`impression`
- 浓淡对比度：浓，以浓见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：法式刀工，布雷斯鸡切法以衬鸡鲜为主，刀工服务于火候的均匀。`impression`
- 火候：火候精准，布雷斯鸡以文火炖酥嫩，奶油以小火收浓。`impression`
- 质感：嫩、滑、鲜并存；布雷斯鸡靠文火得嫩，奶油靠小火得滑。

## (4) 调味

- 调味料：奶油、羊肚菌、高汤、酒，法餐调料皆备。`artifact`
- 调味顺序：高汤先熬，奶油后下，调味在烹制之中分步进行。
- 禁调味：辛香重料；不用浓味压过鸡鲜。

## (5) 摆盘与食材选择

- 摆盘：Village Blanc 摆盘，慷慨而有序，布雷斯鸡以金黄为要。`impression`
- 食材选择：布雷斯鸡取 AOC，羊肚菌取当季，皆取上品。
- 上菜节奏：法餐之序，先冷后热，先淡后浓，布雷斯鸡为热菜之首。

## (6) 该做什么菜 / 不该做什么菜

- 该做：布雷斯鸡、Village Blanc、法式精致料理、法国最好的鸡、奶油与羊肚菌、慷慨而精准、文火炖酥嫩。
- 不该做：`No dish without the best chicken, no chilli heat, no rustic plating, no overcooked chicken, no heavy sauce, no plain presentation`
- Negative prompt: `No dish without the best chicken, no chilli heat, no rustic plating, no overcooked chicken, no heavy sauce, no plain presentation`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬的晚餐）

- Prompt: `In the style of Georges Blanc, a tiny dinner for a Yorkshire terrier on a subway seat: one perfect piece of Bresse chicken, cream and morels, generous and precise, the finest chicken in France, no dish without the best chicken`
- 中文对照：布朗风格：一只坐在地铁里的约克夏犬的晚餐：一块极好的布雷斯鸡，奶油与羊肚菌，慷慨而精准，法国最好的鸡，没有不用最好的鸡的菜。
- Negative: `No dish without the best chicken, no chilli heat, no rustic plating, no overcooked chicken, no heavy sauce`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
