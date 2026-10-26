# Hu Sihui — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hu Sihui: Yuan court food therapy, medicine and food from one source, Mongol and Han dishes in one book, nourishing broths and congees, no excess, no heavy seasoning`
- ZH: 忽思慧风格：元代宫廷食疗，药食同源，蒙汉膳食同书，滋补汤粥为主，没有过量，没有重味。

## (2) 味型方向

- 主味：滋补——温补而不燥，汤粥之鲜为本。`artifact`
- 辅味：甘，谷物与肉食的天然甘味。
- 禁味：辛辣、生冷、油腻、过咸。
- 味型层次：单味直给而深长，清淡之中见补益。`impression`
- 浓淡对比度：淡，以淡见长；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：宫廷刀工，整料为主，刀工服务于食疗的温和。`impression`
- 火候：文火久炖，汤粥以慢火出味，火小而长。`artifact`
- 质感：软烂、汤清、温润；软烂靠久炖，汤清靠少油少料。

## (4) 调味

- 调味料：极简，盐少许而已，药材即调料。`artifact`
- 调味顺序：先炖后调，出锅前少许盐提鲜，不夺药食之味。
- 禁调味：辛香重料、浓油赤酱；不用浓味压过食疗本味。

## (5) 摆盘与食材选择

- 摆盘：宫廷器皿，陶碗瓷盘，肃穆简朴，食疗即摆盘的理由。`impression`
- 食材选择：蒙汉食材并用，肉食与谷物皆取上品，时令为先。
- 上菜节奏：食疗之序，先汤粥后实菜，先淡后补。

## (6) 该做什么菜 / 不该做什么菜

- 该做：宫廷食疗、滋补汤粥、药食同源、蒙汉膳食、文火久炖、陶碗盛汤、温补不燥。
- 不该做：`No chilli heat, no heavy sauce, no greasy richness, no raw cold dishes, no strong seasoning, no lavish presentation`
- Negative prompt: `No chilli heat, no heavy sauce, no greasy richness, no raw cold dishes, no strong seasoning, no lavish presentation`

## (7) 测试提示词示例（现代题材：一份深夜便利店的关东煮）

- Prompt: `In the style of Hu Sihui, a late-night convenience store oden reimagined as court food therapy: clear nourishing broth, fish cake and radish simmered until soft, a small bowl of congee on the side, medicine and food from one source, served warm in plain bowls, no excess`
- 中文对照：忽思慧风格：一份深夜便利店关东煮，按宫廷食疗重做：清汤滋补，鱼糕萝卜文火炖到软烂，旁边一小碗粥，药食同源，陶碗盛着趁热吃，没有过量。
- Negative: `No chilli heat, no heavy sauce, no greasy richness, no raw cold dishes, no strong seasoning`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
