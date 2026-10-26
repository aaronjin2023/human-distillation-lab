# Lee Kum Sheung — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lee Kum Sheung: Cantonese oyster sauce, the sea condensed into one spoon, umami without heaviness, a sauce that lifts rather than covers, frugal village craft turned world pantry staple`
- ZH: 李锦裳风格：粤式蚝油，海味浓缩成一勺，鲜而不重，提味而不盖味，乡野手艺做成世界调味品。

## (2) 味型方向

- 主味：蚝鲜——蚝油之鲜，海味浓缩，鲜而不腥。`artifact`
- 辅味：甘，蚝油的天然甘味，不加糖而甘。
- 禁味：辛辣刺激、过咸死咸、油腻重酱。
- 味型层次：单味直给而深长，鲜是底味，甘是余味。`impression`
- 浓淡对比度：鲜浓而用量少，一勺即足；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：调味品无需刀工；蚝油用于菜品时，刀工随粤菜而变。`impression`
- 火候：蚝熬制火候为要，火小而长，熬过火即成蚝油——传说如此，见 conflicts.md。`artifact`
- 质感：稠滑、亮泽；蚝油靠熬制得稠滑，菜品靠蚝油得亮泽。

## (4) 调味

- 调味料：蚝油为本，虾酱为辅，调料皆海味。`artifact`
- 调味顺序：蚝油后下，提鲜收尾，不提前久煮。`impression`
- 禁调味：重酱、辛香；不用浓味压过蚝鲜。

## (5) 摆盘与食材选择

- 摆盘：粤菜摆盘，满盘丰盛，蚝油菜品以亮泽为要。`impression`
- 食材选择：蚝取新鲜，菜取时令；蚝油只选好蚝。
- 上菜节奏：粤菜之序，蚝油菜品多为热菜，趁热上桌。

## (6) 该做什么菜 / 不该做什么菜

- 该做：蚝油、虾酱、李锦记、粤式提鲜、海味浓缩、一勺即足、鲜而不重。
- 不该做：`No chilli heat, no heavy sauce masking the ingredient, no dead saltiness, no greasy richness, no showy plating, no artificial flavouring`
- Negative prompt: `No chilli heat, no heavy sauce masking the ingredient, no dead saltiness, no greasy richness, no showy plating, no artificial flavouring`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Lee Kum Sheung, a modern bowl of ramen reimagined as Cantonese oyster sauce cooking: clear broth lifted with one spoon of oyster sauce, no other seasoning, toppings glazed to a shine, the sea condensed into one spoon, umami without heaviness`
- 中文对照：李锦裳风格：一碗现代拉面，按粤式蚝油重做：清汤只加一勺蚝油提鲜，不再下别的调料，配料裹上亮泽，海味浓缩成一勺，鲜而不重。
- Negative: `No chilli heat, no heavy sauce masking the ingredient, no dead saltiness, no greasy richness, no artificial flavouring`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
