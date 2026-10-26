# Wang Shixiong — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Shixiong: Qing food therapy, congee as the first medicine, eating with the seasons and the body, gentle nourishment, no excess, no heavy seasoning`
- ZH: 王士雄风格：清代食疗，粥为第一药，随息而食，温和滋补，没有过量，没有重味。

## (2) 味型方向

- 主味：温和滋补——温而不燥，粥之甘为本。`artifact`
- 辅味：甘，谷物之甘，不加糖而甘。
- 禁味：辛辣、生冷、油腻、过咸。
- 味型层次：单味直给而深长，清淡之中见滋补。`impression`
- 浓淡对比度：淡，以淡见长；酸度低，辣度近于无。

## (3) 刀工与火候

- 刀工：食疗刀工，整料为主，刀工服务于食疗的温和。`impression`
- 火候：文火久熬，粥以慢火出甘，火小而长。`artifact`
- 质感：软烂、稠滑、温润；软烂靠久熬，稠滑靠米油。

## (4) 调味

- 调味料：极简，盐少许而已，药材即调料。`artifact`
- 调味顺序：先熬后调，出锅前少许盐提味，不夺粥甘。
- 禁调味：辛香重料、浓油赤酱；不用浓味压过食疗本味。

## (5) 摆盘与食材选择

- 摆盘：家常器皿，陶碗盛粥，朴素无饰，食疗即摆盘的理由。`impression`
- 食材选择：谷物与药材皆取上品，时令为先，随息而食。
- 上菜节奏：食疗之序，先粥后实菜，先淡后补。

## (6) 该做什么菜 / 不该做什么菜

- 该做：食疗、粥品、随息而食、温和滋补、文火久熬、陶碗盛粥、药食同源。
- 不该做：`No chilli heat, no heavy sauce, no greasy richness, no raw cold dishes, no strong seasoning, no lavish presentation`
- Negative prompt: `No chilli heat, no heavy sauce, no greasy richness, no raw cold dishes, no strong seasoning, no lavish presentation`

## (7) 测试提示词示例（现代题材：一份深夜便利店的关东煮）

- Prompt: `In the style of Wang Shixiong, a late-night convenience store oden reimagined as food therapy: clear nourishing broth, radish simmered until soft, a small bowl of congee on the side, eating with the season and the body, gentle nourishment, served warm in plain bowls, no excess`
- 中文对照：王士雄风格：一份深夜便利店关东煮，按食疗重做：清汤滋补，萝卜文火炖到软烂，旁边一小碗粥，随息而食，温和滋补，陶碗盛着趁热吃，没有过量。
- Negative: `No chilli heat, no heavy sauce, no greasy richness, no raw cold dishes, no strong seasoning`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
