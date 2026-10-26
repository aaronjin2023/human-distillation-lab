# Zheng Xiusheng — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zheng Xiusheng: Beijing Hotel cooking, Tan family cuisine, Huaiyang finesse, official banquet elegance, salty fresh and mellow, no dish without ceremony`
- ZH: 郑秀生风格：北京饭店，谭家菜，淮扬精致，官府宴飨之雅，咸鲜醇厚，没有没规矩的菜。

## (2) 味型方向

- 主味：咸鲜醇厚——咸、鲜、醇并重，官府菜之魂。`impression`
- 辅味：甜，淮扬菜的甜味衬咸鲜。`impression`
- 禁味：麻辣、生辣、死咸。
- 味型层次：多层复合，咸鲜在前，醇厚在后，分层调准。`impression`
- 浓淡对比度：浓淡适中，以精致见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：淮扬刀工，文思豆腐刀工讲细，刀工即是菜品的一部分。`impression`
- 火候：火候精准，谭家菜以文火炖酥烂，淮扬菜以小火烧入味。`impression`
- 质感：嫩、滑、酥、糯并存；豆腐靠刀工得细，鱼肉靠小火得嫩。

## (4) 调味

- 调味料：酱油、酒、姜、葱、高汤，官府菜调料皆备；高汤为谭家菜之魂。`impression`
- 调味顺序：高汤先熬，调味后下，调味在烹制之中分步进行。
- 禁调味：麻辣、花椒；不用生辣压过咸鲜。

## (5) 摆盘与食材选择

- 摆盘：北京饭店摆盘，满盘丰盛而有序，亮泽为要，官府菜以规矩为要。`impression`
- 食材选择：鱼肉取嫩，豆腐取细，皆取上品。
- 上菜节奏：官府之序，先凉后热，先淡后浓，谭家菜多为热菜。

## (6) 该做什么菜 / 不该做什么菜

- 该做：谭家菜、淮扬菜、北京饭店、咸鲜醇厚、高汤为魂、文思豆腐刀工、官府之雅。
- 不该做：`No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no crude presentation, no dish without ceremony`
- Negative prompt: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no crude presentation, no dish without ceremony`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Zheng Xiusheng, a modern bowl of ramen reimagined as Tan family cuisine: clear superior stock, one perfect piece of fish, tofu cut hair-thin, salty fresh and mellow, official banquet elegance, no dish without ceremony`
- 中文对照：郑秀生风格：一碗现代拉面，按谭家菜与淮扬菜重做：清高汤，一块极好的鱼，豆腐切得细如发丝，咸鲜醇厚，官府宴飨之雅，没有没规矩的菜。
- Negative: `No chilli heat, no Sichuan numbing, no dead saltiness, no greasy richness, no dish without ceremony`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
