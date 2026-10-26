# Zeng Yi — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zeng Yi: late Qing household cooking, frugal and exact, everyday dishes done right, nothing wasted, no banquet excess, no showy technique`
- ZH: 曾懿风格：清末中馈，家常菜，节俭而精当，样样做对，什么都不浪费，没有宴飨排场，没有炫技。

## (2) 味型方向

- 主味：家常咸鲜——咸鲜适口，家常之味不求复合，但求恰当。`artifact`
- 辅味：甘，谷物与蔬菜的天然甘味。
- 禁味：辛辣刺激、油腻重酱。
- 味型层次：单味直给，家常之味不求复合，但求恰当。`impression`
- 浓淡对比度：淡而有味，以恰当见长；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：家常刀工，切法以实用为主，片、丝、丁皆有，不求炫技。`impression`
- 火候：火候温和，蒸、煮、炖、炒并用，不求镬气。`impression`
- 质感：嫩、爽、软、滑并存，质感随菜式而变。

## (4) 调味

- 调味料：盐、酱、醋、酒为主，调料皆家常所有。`artifact`
- 调味顺序：先备后调，调味在烹制之中，分步进行。
- 禁调味：辛香重料、浓油赤酱；不用重味压过家常本味。

## (5) 摆盘与食材选择

- 摆盘：家常器皿，陶碗瓷盘，满而不乱，丰盛即家常。`impression`
- 食材选择：时令蔬菜、鱼肉皆取当季，节俭不浪费。
- 上菜节奏：家常之序，先凉后热，先淡后浓。

## (6) 该做什么菜 / 不该做什么菜

- 该做：家常菜、节俭饮食、《中馈录》、咸鲜适口、时令蔬菜、什么都不浪费、精当恰当。
- 不该做：`No banquet excess, no showy technique, no chilli heat, no heavy sauce, no greasy richness, no wasteful luxury`
- Negative prompt: `No banquet excess, no showy technique, no chilli heat, no heavy sauce, no greasy richness, no wasteful luxury`

## (7) 测试提示词示例（现代题材：一份深夜便利店的关东煮）

- Prompt: `In the style of Zeng Yi, a late-night convenience store oden reimagined as late Qing household cooking: fish cake and radish simmered in a light broth, seasonal vegetables simply done, nothing wasted, served in plain bowls, frugal and exact, no banquet excess`
- 中文对照：曾懿风格：一份深夜便利店关东煮，按清末家常菜重做：鱼糕萝卜清汤炖着，时令蔬菜简单做对，什么都不浪费，陶碗瓷盘盛着，节俭而精当，没有宴飨排场。
- Negative: `No banquet excess, no showy technique, no chilli heat, no heavy sauce, no greasy richness, no wasteful luxury`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
