# Peng Chang-kuei — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peng Chang-kuei: Hunan cooking, General Tso's chicken, sour and spicy, crisp outside tender inside, lettuce cups with shrimp, bold without heaviness, no dish without bite`
- ZH: 彭长贵风格：湘菜，左宗棠鸡，酸辣，外脆内嫩，生菜虾松，浓烈而不腻，没有没嚼头的菜。

## (2) 味型方向

- 主味：酸辣——酸与辣并重，湘菜之魂。`artifact`
- 辅味：甜，左宗棠鸡的甜味衬酸辣，不夺酸辣。`impression`
- 禁味：麻（花椒之麻非湘菜之要）、死咸、油腻。
- 味型层次：多层复合，酸辣在前，鲜香在后，分层调准。`impression`
- 浓淡对比度：浓，以浓见长；辣度中高，酸度中高，麻度低。

## (3) 刀工与火候

- 刀工：湘菜刀工，丁、丝、片皆匀，刀工服务于火候的均匀。`impression`
- 火候：爆炒镬气，火大而快，左宗棠鸡以大火炸脆再炒，虾松以小火炒嫩。`impression`
- 质感：脆、嫩、酸、辣并存；鸡丁靠大火得脆，虾松靠小火得嫩。

## (4) 调味

- 调味料：辣椒、醋、蒜、姜、豆豉，湘菜调料皆备；花椒少用。`impression`
- 调味顺序：辣椒先炒出香，醋后下提酸，调味在烹制之中分步进行。
- 禁调味：花椒提麻（非湘菜之要）；不用生辣压过鲜香。

## (5) 摆盘与食材选择

- 摆盘：彭园摆盘，满盘丰盛，红亮为要，左宗棠鸡以红亮脆嫩为要。`impression`
- 食材选择：鸡丁取嫩，虾取鲜，皆取上品。
- 上菜节奏：湘菜之序，左宗棠鸡与生菜虾松多为热菜，趁热上桌。

## (6) 该做什么菜 / 不该做什么菜

- 该做：左宗棠鸡、生菜虾松、彭园、酸辣、外脆内嫩、辣椒提香、醋提酸。
- 不该做：`No raw chilli burn, no dead saltiness, no greasy richness, no Sichuan numbing, no bland adaptation, no soggy chicken`
- Negative prompt: `No raw chilli burn, no dead saltiness, no greasy richness, no Sichuan numbing, no bland adaptation, no soggy chicken`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Peng Chang-kuei, a modern bowl of ramen reimagined as Hunan cooking: General Tso's chicken over noodles, sour and spicy, crisp outside tender inside, chilli fragrance first, vinegar brightness last, bold without heaviness`
- 中文对照：彭长贵风格：一碗现代拉面，按湘菜重做：左宗棠鸡盖面，酸辣，外脆内嫩，辣椒香在前，醋的亮在后，浓烈而不腻。
- Negative: `No raw chilli burn, no dead saltiness, no greasy richness, no Sichuan numbing, no soggy chicken`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
