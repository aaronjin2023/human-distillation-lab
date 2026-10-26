# Yeung Koon-yat — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yeung Koon-yat: Cantonese abalone, slow-braised in its own sauce, abalone as the whole dish, rich without heaviness, precise fire, luxury earned by patience`
- ZH: 杨贯一风格：粤式鲍鱼，文火久扣，鲍鱼就是整道菜，浓而不腻，火候精准，奢华靠耐心换来。

## (2) 味型方向

- 主味：鲍鲜——鲍鱼之鲜，鲍汁之浓，鲜而不腥。`artifact`
- 辅味：甘，鲍汁的天然甘味，不加糖而甘。
- 禁味：麻辣、生辣、死咸。
- 味型层次：多层复合，鲍鲜在前，鲍汁在后，分层调准。`impression`
- 浓淡对比度：浓，以浓见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：鲍鱼刀工，切法以衬鲍鱼为主，刀工服务于火候的均匀。`impression`
- 火候：文火久扣，鲍鱼以慢火出鲜，火小而长。`artifact`
- 质感：嫩、滑、糯并存；鲍鱼靠文火得嫩，鲍汁靠久扣得稠滑。

## (4) 调味

- 调味料：鲍汁为本，蚝油、酱油为辅，调料皆为衬鲍鱼。`impression`
- 调味顺序：鲍汁先熬，鲍鱼后扣，调味在烹制之中分步进行。
- 禁调味：麻辣、花椒；不用浓味压过鲍鲜。

## (5) 摆盘与食材选择

- 摆盘：Forum 摆盘，满盘丰盛而有序，亮泽为要，鲍鱼以亮泽为要。`impression`
- 食材选择：鲍鱼取上品，辽参取肥，皆取上品。
- 上菜节奏：粤菜之序，鲍鱼多为热菜，趁热上桌。

## (6) 该做什么菜 / 不该做什么菜

- 该做：阿一鲍鱼、鲍汁扣辽参、Forum、鲍鲜、文火久扣、鲍汁浓稠、奢华靠耐心。
- 不该做：`No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no rushed abalone, no showy plating`
- Negative prompt: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no rushed abalone, no showy plating`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Yeung Koon-yat, a modern bowl of ramen reimagined as Cantonese abalone: one perfect abalone slow-braised in its own sauce over noodles, rich without heaviness, precise fire, luxury earned by patience, no rushed abalone`
- 中文对照：杨贯一风格：一碗现代拉面，按粤式鲍鱼重做：一只极好的鲍鱼文火久扣，鲍汁盖面，浓而不腻，火候精准，奢华靠耐心换来，没有仓促的鲍鱼。
- Negative: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no rushed abalone`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
