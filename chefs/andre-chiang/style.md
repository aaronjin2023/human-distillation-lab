# André Chiang — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of André Chiang: new Chinese, octaphilosophy, pure salt artisan south wind water unique memory taste, minimal and precise, Taiwanese ingredients French technique, no dish without memory`
- ZH: 江振诚风格：新中餐，八角哲学，纯粹、盐、匠心、南风、水、独特、记忆、味觉，极简而精准，台湾食材法国技法，没有没记忆的菜。

## (2) 味型方向

- 主味：纯粹——纯粹为本，食材本味为上。`artifact`
- 辅味：盐，盐为八角之一，盐提本味。`impression`
- 禁味：厚重油腻、直白饱腹、浓酱重味。
- 味型层次：多层复合，纯粹在前，记忆在后，分层调准。`impression`
- 浓淡对比度：淡而集中，以极简见浓味；酸度中，辣度低。

## (3) 刀工与火候

- 刀工：新中餐刀工，切法以极简为要，刀工服务于纯粹。`impression`
- 火候：法式火候，低温慢煮、炭火并用，火候以精准为要。`impression`
- 质感：嫩、滑、脆并存；低温慢煮靠精准得嫩，炭火靠烟熏得香。

## (4) 调味

- 调味料：盐为本，台湾食材为味之本，调料极简。`artifact`
- 调味顺序：盐先提本味，调味在烹制之中分步进行。
- 禁调味：浓酱、辛香；不用浓味压过纯粹。

## (5) 摆盘与食材选择

- 摆盘：极简摆盘，留白多，雕塑感器皿，小份量为要。`impression`
- 食材选择：台湾食材为本，法国技法为形；食材取上品，时令为先。
- 上菜节奏：套餐之序，八角为序，一道一记忆。

## (6) 该做什么菜 / 不该做什么菜

- 该做：八角哲学、Restaurant André、新中餐、纯粹、台湾食材法国技法、极简精准、记忆。
- 不该做：`No heavy stew, no large comfort portions, no rustic plating, no overpowering sauce, no dish without memory, no plain presentation`
- Negative prompt: `No heavy stew, no large comfort portions, no rustic plating, no overpowering sauce, no dish without memory, no plain presentation`

## (7) 测试提示词示例（现代题材：一份深夜便利店的关东煮）

- Prompt: `In the style of André Chiang, a late-night convenience store oden reimagined as new Chinese: clear broth as water, one perfect piece of fish as memory, salt only, minimal and precise, Taiwanese ingredients French technique, no dish without memory`
- 中文对照：江振诚风格：一份深夜便利店关东煮，按新中餐重做：清汤是水，一块极好的鱼是记忆，只用盐，极简而精准，台湾食材法国技法，没有没记忆的菜。
- Negative: `No heavy stew, no large comfort portions, no rustic plating, no overpowering sauce, no dish without memory`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
