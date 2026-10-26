# Wang Yijun — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Yijun: Shandong cooking, braised sea cucumber with scallion, nine-turn large intestine, salty fresh and mellow, precise fire, grandeur without roughness`
- ZH: 王义均风格：鲁菜，葱烧海参，九转大肠，咸鲜醇厚，火候精准，气派而不粗野。

## (2) 味型方向

- 主味：咸鲜醇厚——咸、鲜、醇并重，鲁菜之魂。`artifact`
- 辅味：甜，九转大肠的糖色，甜衬咸鲜。`impression`
- 禁味：麻辣、生辣、死咸。
- 味型层次：多层复合，咸鲜在前，醇厚在后，分层调准。`impression`
- 浓淡对比度：浓，以浓见长；咸度中高，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：鲁菜刀工，整料为主，刀工服务于火候的均匀。`impression`
- 火候：火候精准，葱烧海参以小火烧入味，九转大肠以文火炖酥烂。`impression`
- 质感：嫩、滑、酥、糯并存；海参靠小火得嫩，大肠靠文火得酥烂。

## (4) 调味

- 调味料：葱、姜、酱油、糖、酒，鲁菜调料皆备；葱为鲁菜之魂。`artifact`
- 调味顺序：葱油先炸出香，酱油后下提咸，糖色最后收亮。
- 禁调味：麻辣、花椒；不用生辣压过咸鲜。

## (5) 摆盘与食材选择

- 摆盘：鲁菜摆盘，满盘丰盛而有序，亮泽为要，葱烧海参以亮泽为要。`impression`
- 食材选择：海参取肥，大肠取净，皆取上品。
- 上菜节奏：鲁菜之序，先凉后热，先淡后浓，葱烧海参与九转大肠多为热菜。

## (6) 该做什么菜 / 不该做什么菜

- 该做：葱烧海参、九转大肠、鲁菜泰斗、咸鲜醇厚、葱油提香、糖色收亮、气派而不粗野。
- 不该做：`No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no crude presentation, no bland adaptation`
- Negative prompt: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no crude presentation, no bland adaptation`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Wang Yijun, a modern bowl of ramen reimagined as Shandong cooking: braised sea cucumber over noodles, scallion oil fragrance first, soy and sugar glaze bright last, salty fresh and mellow, precise fire, grandeur without roughness`
- 中文对照：王义均风格：一碗现代拉面，按鲁菜重做：葱烧海参盖面，葱油香在前，酱油糖色收亮在后，咸鲜醇厚，火候精准，气派而不粗野。
- Negative: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no bland adaptation`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
