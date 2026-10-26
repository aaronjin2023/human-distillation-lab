# Michel Guérard — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michel Guérard: nouvelle cuisine, cuisine minceur, slimming without sacrifice, vegetable purées and fromage blanc instead of butter, light and precise, no dish too heavy to serve`
- ZH: 盖拉尔风格：新法餐，瘦身美食，轻盈而不牺牲味道，蔬菜泥与白奶酪代黄油，轻而精准，没有重到上不了桌的菜。

## (2) 味型方向

- 主味：轻盈之味——轻而不淡，蔬菜泥的鲜为本。`artifact`
- 辅味：酸，瘦身美食的酸味提亮。`impression`
- 禁味：黄油、奶油、糖、盐过量。
- 味型层次：多层复合，蔬菜泥在前，酸味在后，分层调准。`impression`
- 浓淡对比度：淡，以淡见长；酸度中高，辣度近于无。

## (3) 刀工与火候

- 刀工：法式刀工，切法以衬蔬菜泥为主，片、丁皆匀。`impression`
- 火候：火候精准，鱼肉以密封蒸取鲜，蔬菜以文火煮软。`impression`
- 质感：细腻、滑、嫩并存；蔬菜泥靠过筛得细腻，鱼肉靠密封蒸得嫩。

## (4) 调味

- 调味料：蔬菜泥、fromage blanc、香草，瘦身美食调料皆备；黄油奶油不用。`artifact`
- 调味顺序：蔬菜泥先备，酸味后下提亮，调味在烹制之中分步进行。
- 禁调味：黄油、奶油、糖、盐过量；不用浓味压过轻盈。

## (5) 摆盘与食材选择

- 摆盘：Les Prés d'Eugénie 摆盘，精致而有序，轻盈为要。`impression`
- 食材选择：蔬菜取当季，鱼肉取鲜，皆取上品。
- 上菜节奏：法餐之序，先冷后热，先淡后浓，瘦身菜品为热菜之首。

## (6) 该做什么菜 / 不该做什么菜

- 该做：瘦身美食、Les Prés d'Eugénie、法式精致料理、蔬菜泥代黄油、轻盈而不牺牲、密封蒸取鲜、酸味提亮。
- 不该做：`No butter and cream excess, no heavy stew, no sugar overload, no salty excess, no dish too heavy to serve, no plain presentation`
- Negative prompt: `No butter and cream excess, no heavy stew, no sugar overload, no salty excess, no dish too heavy to serve, no plain presentation`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Michel Guérard, a modern bowl of ramen reimagined as cuisine minceur: clear light broth, vegetable purée instead of fat, fish steamed sealed with herbs, acidity to brighten, light and precise, no dish too heavy to serve`
- 中文对照：盖拉尔风格：一碗现代拉面，按瘦身美食重做：清汤轻盈，蔬菜泥代油脂，鱼密封蒸着配香草，酸味提亮，轻而精准，没有重到上不了桌的菜。
- Negative: `No butter and cream excess, no heavy stew, no sugar overload, no salty excess, no dish too heavy to serve`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
