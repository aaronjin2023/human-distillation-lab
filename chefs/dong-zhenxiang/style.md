# Dong Zhenxiang — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dong Zhenxiang: Dadong roast duck, crisp but not greasy, Beijing-Lu fusion, lean and elegant duck, precise fire, no dish too oily to serve`
- ZH: 董振祥风格：大董烤鸭，酥不腻，京鲁融合，瘦而雅致的鸭子，火候精准，没有油腻到上不了桌的菜。

## (2) 味型方向

- 主味：咸鲜——咸、鲜并重，烤鸭之魂。`impression`
- 辅味：甜，烤鸭的甜面酱衬咸鲜。`impression`
- 禁味：麻辣、生辣、死咸、油腻。
- 味型层次：多层复合，酥脆在前，鲜香在后，分层调准。`impression`
- 浓淡对比度：浓淡适中，以酥不腻见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：烤鸭刀工，片鸭讲薄，刀工即是菜品的一部分。`artifact`
- 火候：烤鸭火候，挂炉烤制，火候精准，皮酥肉嫩。`impression`
- 质感：酥、脆、嫩并存；鸭皮靠烤制得酥脆，鸭肉靠火候得嫩。

## (4) 调味

- 调味料：甜面酱、葱、姜、糖，烤鸭调料皆备。`impression`
- 调味顺序：烤制在前，蘸酱在后，调味在入口之前。
- 禁调味：麻辣、花椒；不用浓味压过鸭鲜。

## (5) 摆盘与食材选择

- 摆盘：大董摆盘，满盘丰盛而有序，亮泽为要，烤鸭以皮亮为要。`impression`
- 食材选择：鸭取瘦，取当年新鸭，皆取上品。
- 上菜节奏：京鲁之序，烤鸭现片现吃，趁热上桌。

## (6) 该做什么菜 / 不该做什么菜

- 该做：大董烤鸭、酥不腻烤鸭、京鲁融合、片鸭讲薄、挂炉烤制、瘦而雅致、酥而不腻。
- 不该做：`No greasy richness, no chilli heat, no Sichuan numbing, no dead saltiness, no soggy duck skin, no showy plating`
- Negative prompt: `No greasy richness, no chilli heat, no Sichuan numbing, no dead saltiness, no soggy duck skin, no showy plating`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬的晚餐）

- Prompt: `In the style of Dong Zhenxiang, a tiny dinner for a Yorkshire terrier on a subway seat: one thin slice of crisp roast duck, not greasy, with a dab of sweet sauce, lean and elegant, precise fire, no dish too oily to serve`
- 中文对照：董振祥风格：一只坐在地铁里的约克夏犬的晚餐：一片切得极薄的酥脆烤鸭，不腻，蘸一点甜面酱，瘦而雅致，火候精准，没有油腻到上不了桌的菜。
- Negative: `No greasy richness, no chilli heat, no Sichuan numbing, no dead saltiness, no soggy duck skin`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
