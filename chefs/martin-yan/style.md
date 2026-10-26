# Martin Yan — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martin Yan: Cantonese cooking made teachable, Yan Can Cook, fast wok, clear steps, joyful and generous, American-Chinese, no dish too hard to try`
- ZH: 甄文达风格：粤菜讲得明白，Yan Can Cook，快炒，步骤清楚，欢快大方，美式中餐，没有难到不敢试的菜。

## (2) 味型方向

- 主味：咸鲜——咸、鲜并重，粤菜之魂，为美国调和。`impression`
- 辅味：甜，美式中餐的甜味稍重。`impression`
- 禁味：麻辣、生辣、死咸。
- 味型层次：单味直给而清楚，步骤清楚即是味型清楚。`impression`
- 浓淡对比度：浓淡适中，以清楚见长；咸度中，酸度低，辣度低。

## (3) 刀工与火候

- 刀工：粤菜刀工，切法清楚，片、丝、丁皆匀，刀工讲得明白。`impression`
- 火候：爆炒镬气，火大而快，步骤清楚，火候讲得明白。`impression`
- 质感：嫩、脆、滑并存；快炒靠大火得嫩，刀工靠均匀得脆。

## (4) 调味

- 调味料：酱油、蚝油、酒、姜、葱，粤菜调料皆备。`impression`
- 调味顺序：调味在烹制之中分步进行，步骤清楚，调味讲得明白。
- 禁调味：麻辣、花椒；不用生辣压过咸鲜。

## (5) 摆盘与食材选择

- 摆盘：电视摆盘，满盘丰盛，清楚为要，摆盘讲得明白。`impression`
- 食材选择：食材取当季，步骤清楚，食材讲得明白。
- 上菜节奏：电视之序，先备料后烹制，先讲步骤后上菜。

## (6) 该做什么菜 / 不该做什么菜

- 该做：Yan Can Cook、中餐电视推广、美式中餐、快炒、步骤清楚、欢快大方、人人能煮。
- 不该做：`No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no confusing steps, no dish too hard to try`
- Negative prompt: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no confusing steps, no dish too hard to try`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Martin Yan, a modern bowl of ramen reimagined as teachable Cantonese: fast wok, clear steps announced as you go, joyful and generous, American-Chinese flavours, no dish too hard to try`
- 中文对照：甄文达风格：一碗现代拉面，按电视粤菜重做：快炒，步骤一边做一边讲清楚，欢快大方，美式中餐味，没有难到不敢试的菜。
- Negative: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no confusing steps`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
