# Nie Fengqiao — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nie Fengqiao: Qing dynasty ingredient science, knowing each ingredient's nature before cooking, choosing by season and character, exact and frugal, no banquet excess, no heavy seasoning`
- ZH: 聂凤乔风格：清代烹饪原料学，先知原料性味再下厨，按时令与性味选材，精当节俭，没有宴飨排场，没有重味。

## (2) 味型方向

- 主味：本味——先知原料性味，再以本味为上。`artifact`
- 辅味：鲜，取食材之鲜，以选材衬鲜。
- 禁味：辛辣、油腻、重酱。
- 味型层次：单味直给而有依据，清淡之中见原料之性。`impression`
- 浓淡对比度：淡，以淡见长；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：原料刀工，切法随原料性味而变，片、丝、丁皆有。`impression`
- 火候：火候随原料而变，炖、蒸、煮、炒各随其性。`impression`
- 质感：嫩、爽、酥、滑并存，质感随原料而变。

## (4) 调味

- 调味料：盐、酱、醋、酒为主，调料随原料性味而选。`artifact`
- 调味顺序：先知性味后调味，调味在备料之后、烹制之中。
- 禁调味：不问性味一味到底；不用浓味压过原料本味。

## (5) 摆盘与食材选择

- 摆盘：家常器皿，陶碗瓷盘，满而不乱，精当即家常。`impression`
- 食材选择：按时令与性味选材，性味不合宁可不做。
- 上菜节奏：家常之序，先凉后热，先淡后浓。

## (6) 该做什么菜 / 不该做什么菜

- 该做：原料学、按性味选材、时令选材、本味为上、《醒园录》、精当节俭、先知后烹。
- 不该做：`No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no seasoning without knowing the ingredient, no lavish presentation`
- Negative prompt: `No banquet excess, no heavy sauce, no chilli heat, no greasy richness, no seasoning without knowing the ingredient, no lavish presentation`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Nie Fengqiao, a modern bowl of ramen reimagined as ingredient science: each topping chosen by its nature and season, noodles by wheat character, broth by bone character, seasoned only after knowing each ingredient, exact and frugal, no heavy seasoning`
- 中文对照：聂凤乔风格：一碗现代拉面，按烹饪原料学重做：每样配料按性味与时令选，面按麦性，汤按骨性，先知原料再调味，精当节俭，没有重味。
- Negative: `No heavy sauce, no chilli heat, no greasy richness, no seasoning without knowing the ingredient, no lavish presentation`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
