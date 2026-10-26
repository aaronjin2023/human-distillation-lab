# Shi Zhengliang — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shi Zhengliang: Sichuan cooking, fish-fragrant shrimp balls, chrysanthemum fish, hibiscus chicken slices, refined Sichuan, bold flavours with elegance, no dish without finesse`
- ZH: 史正良风格：川菜，鱼香虾球，菊花鱼，芙蓉鸡片，精致川菜，浓烈而雅致，没有没讲究的菜。

## (2) 味型方向

- 主味：鱼香麻辣——鱼香、麻、辣并重，精致川菜之魂。`artifact`
- 辅味：甜，鱼香的甜酸相衬。`impression`
- 禁味：生辣刺喉、死咸、油腻。
- 味型层次：多层复合，鱼香在前，麻辣在后，分层调准。`impression`
- 浓淡对比度：浓，以浓见长；辣度中高，麻度中，酸度中。

## (3) 刀工与火候

- 刀工：川菜刀工，菊花鱼刀工讲巧，芙蓉鸡片刀工讲薄，刀工即是菜品的一部分。`impression`
- 火候：爆炒镬气，火大而快，虾球以大火快炒，鸡片以小火滑嫩。`impression`
- 质感：嫩、滑、脆并存；虾球靠大火得滑，鸡片靠小火得嫩。

## (4) 调味

- 调味料：豆瓣、花椒、辣椒、豆豉、蒜、姜、醋、糖，川菜调料皆备。`impression`
- 调味顺序：豆瓣先炒出红油，鱼香汁后下调准，调味在烹制之中分步进行。
- 禁调味：不问火候一味到底；不用生辣压过鲜香。

## (5) 摆盘与食材选择

- 摆盘：川菜摆盘，满盘丰盛，菊花鱼以花形为要，红油亮泽。`impression`
- 食材选择：虾取鲜，鱼取嫩，鸡取嫩，皆取上品。
- 上菜节奏：川菜之序，三道代表菜多为热菜，趁热上桌。

## (6) 该做什么菜 / 不该做什么菜

- 该做：鱼香虾球、菊花鱼、芙蓉鸡片、鱼香、精致川菜、刀工讲巧、浓烈而雅致。
- 不该做：`No raw chilli burn, no dead saltiness, no greasy richness, no crude presentation, no bland adaptation, no careless knife work`
- Negative prompt: `No raw chilli burn, no dead saltiness, no greasy richness, no crude presentation, no bland adaptation, no careless knife work`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Shi Zhengliang, a modern bowl of ramen reimagined as refined Sichuan: fish-fragrant shrimp over noodles, chrysanthemum-cut fish, hibiscus-thin chicken, bold flavours with elegance, knife work as part of the dish, no dish without finesse`
- 中文对照：史正良风格：一碗现代拉面，按精致川菜重做：鱼香虾球盖面，菊花刀切的鱼，芙蓉般薄的鸡片，浓烈而雅致，刀工就是菜品的一部分，没有没讲究的菜。
- Negative: `No raw chilli burn, no dead saltiness, no greasy richness, no crude presentation, no careless knife work`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
