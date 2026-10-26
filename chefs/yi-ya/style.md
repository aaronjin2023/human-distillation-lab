# Yi Ya — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yi Ya: the first master of the five flavours at court, seasoning as precision, exact balance of sweet sour bitter pungent salty, banquet perfection, no flavour left untempered`
- ZH: 易牙风格：宫廷五味第一人，调味即精密，五味分毫不差，宴飨之极致，没有一味未经调和。

## (2) 味型方向

- 主味：五味调和——甘、酸、苦、辛、咸五味皆备，分毫不差，合君之口。`artifact`
- 辅味：鲜，取食材之鲜，以调味衬鲜，不以调味盖鲜。
- 禁味：单味独大、生涩未调、过咸过酸。
- 味型层次：多层复合，味随菜变，一菜一味型。`impression`
- 浓淡对比度：浓淡适中，以精准见长；酸度与辣度均低而准。

## (3) 刀工与火候

- 刀工：宫廷刀工，片、丝、丁皆匀，刀工服务于调味的均匀。`impression`
- 火候：火候精准，炖、蒸、煮并用，火候为调味服务。`impression`
- 质感：嫩、滑、酥、爽并存，质感随菜式而变，不以一种质感贯穿全席。

## (4) 调味

- 调味料：五味调料皆备，甘酸苦辛咸分量精准；调料为春秋宫廷所有，无后世酱料。`impression`
- 调味顺序：先尝后调，味随君好，调味在烹制前中后分步进行。`impression`
- 禁调味：粗放下料、一味到底、不用尝味就调味。

## (5) 摆盘与食材选择

- 摆盘：宫廷宴飨之序，器皿按礼制，丰盛而有序，青铜与陶器并用。`impression`
- 食材选择：齐地物产，禽兽鱼鳖皆取上品，时令为先。
- 上菜节奏：宴飨之序，先凉后热，先淡后浓，一席多味。

## (6) 该做什么菜 / 不该做什么菜

- 该做：五味调和、宫廷宴飨、鼎鼐调和、味随菜变、分毫不差的调味、一菜一味型。
- 不该做：`No single untempered flavour, no crude seasoning, no one-flavour-fits-all, no rustic presentation, no heavy grease, no unseasoned blandness`
- Negative prompt: `No single untempered flavour, no crude seasoning, no one-flavour-fits-all, no rustic presentation, no heavy grease, no unseasoned blandness`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Yi Ya, a modern bowl of ramen reimagined as court precision: five flavours balanced to the exact measure, broth tasted and adjusted three times, each topping seasoned separately, banquet order on a single bowl, no flavour left untempered`
- 中文对照：易牙风格：一碗现代拉面，按宫廷精密重做：五味分毫不差，汤尝过三遍才定，每样配料单独调味，一碗之中见宴飨之序，没有一味未经调和。
- Negative: `No single untempered flavour, no crude seasoning, no one-flavour-fits-all, no heavy grease`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
