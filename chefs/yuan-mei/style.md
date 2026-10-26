# Yuan Mei — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yuan Mei: Suiyuan dining, the ingredient's own flavour above all, mandarin fish and bird's nest, natural and unforced, no heavy sauce, no banquet excess, no luxury for show`
- ZH: 袁枚风格：随园食单，食材本味为上，鳜鱼与燕窝，自然不做作，没有浓酱，没有宴飨排场，没有为奢华而奢华。

## (2) 味型方向

- 主味：本味——食材本味为上，调味只衬本味。`artifact`
- 辅味：鲜，鳜鱼之鲜、燕窝之清鲜为本。
- 禁味：浓酱重味、辛辣、油腻。
- 味型层次：单味直给而深长，清淡之中见本味。`impression`
- 浓淡对比度：淡，以淡见长；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：随园刀工，切法以衬本味为主，片、丝、丁皆匀，不求炫技。`impression`
- 火候：火候温和，鳜鱼以蒸取鲜，燕窝以炖取清。`impression`
- 质感：嫩、滑、清并存；鳜鱼靠蒸得嫩，燕窝靠炖得滑。

## (4) 调味

- 调味料：极简，盐、酒、姜为主，调料只衬本味。`artifact`
- 调味顺序：先尝后调，调味在烹制之后、入口之前，不提前重调。
- 禁调味：浓酱、重油、辛香；不用浓味压过食材本味。

## (5) 摆盘与食材选择

- 摆盘：随园器皿，瓷盘留白多，自然为上，不讲排场。`impression`
- 食材选择：鳜鱼取肥满，燕窝取净，皆取上品而不过奢。
- 上菜节奏：随园之序，先清后鲜，先淡后厚。

## (6) 该做什么菜 / 不该做什么菜

- 该做：鳜鱼、燕窝、本味为上、自然不做作、先尝后调、瓷盘留白、清鲜淡雅。
- 不该做：`No heavy sauce, no banquet excess, no luxury for show, no chilli heat, no greasy richness, no strong seasoning`
- Negative prompt: `No heavy sauce, no banquet excess, no luxury for show, no chilli heat, no greasy richness, no strong seasoning`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Yuan Mei, a modern bowl of ramen reimagined as Suiyuan dining: clear broth, one perfect piece of fish, nothing to hide the ingredient's own flavour, tasted before seasoning, natural and unforced, served in a plain bowl with much empty space, no heavy sauce`
- 中文对照：袁枚风格：一碗现代拉面，按随园食单重做：清汤，一块极好的鱼，不掩盖食材本味，先尝后调，自然不做作，陶碗留白很多，没有浓酱。
- Negative: `No heavy sauce, no banquet excess, no luxury for show, no chilli heat, no greasy richness`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
