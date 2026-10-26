# Joël Robuchon — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joël Robuchon: French cuisine, pommes purée, butter as the measure, L'Atelier counter dining, perfection in simplicity, no dish without precision`
- ZH: 罗布松风格：法餐，土豆泥，黄油就是度量，L'Atelier 吧台用餐，简单中的极致，没有不精准的菜。

## (2) 味型方向

- 主味：黄油之味——黄油为本，土豆泥的灵魂。`artifact`
- 辅味：奶油与牛奶，土豆泥的底味。`impression`
- 禁味：辛辣、生辣、酸味过重。
- 味型层次：单味直给而深长，黄油之中见土豆本味。`impression`
- 浓淡对比度：浓，以浓见长；咸度中，酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：法式刀工，切法以衬黄油为主，片、丁皆匀。`impression`
- 火候：火候精准，土豆泥以文火煮软，黄油以小火融化。`impression`
- 质感：稠滑、细腻并存；土豆泥靠过筛得细腻，黄油靠小火得稠滑。

## (4) 调味

- 调味料：黄油、奶油、牛奶、盐，土豆泥调料皆备。`artifact`
- 调味顺序：黄油后下，盐少许，调味在烹制之后。
- 禁调味：辛香重料；不用浓味压过黄油。

## (5) 摆盘与食材选择

- 摆盘：L'Atelier 摆盘，吧台式用餐，精致而有序，土豆泥以细腻为要。`impression`
- 食材选择：土豆取粉质，黄油取上品，皆取上品。
- 上菜节奏：法餐之序，先冷后热，先淡后浓，土豆泥为配菜之首。

## (6) 该做什么菜 / 不该做什么菜

- 该做：土豆泥、L'Atelier de Joël Robuchon、米其林三星纪录、黄油为度、简单中的极致、吧台用餐、精准。
- 不该做：`No dish without precision, no chilli heat, no rustic plating, no lumpy mash, no stingy butter, no plain presentation`
- Negative prompt: `No dish without precision, no chilli heat, no rustic plating, no lumpy mash, no stingy butter, no plain presentation`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Joël Robuchon, a modern bowl of ramen reimagined as French precision: pommes purée smooth as silk beside the noodles, butter as the measure, L'Atelier counter precision, perfection in simplicity, no dish without precision`
- 中文对照：罗布松风格：一碗现代拉面，按法餐精准重做：旁边一勺细腻如丝的土豆泥，黄油就是度量，L'Atelier 吧台的精准，简单中的极致，没有不精准的菜。
- Negative: `No dish without precision, no chilli heat, no rustic plating, no lumpy mash, no stingy butter`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
