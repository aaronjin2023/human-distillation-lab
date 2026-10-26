# Dante Gabriel Rossetti — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Pre-Raphaelite, intense jewel-like colour, luminous red hair and pale skin, medieval symbolism, dense detail, dreamlike and sensual, flat decorative pattern`
- ZH: 拉斐尔前派，宝石般浓烈色彩，红发与苍白肌肤，中世纪象征，密集细节，梦境而感性，扁平装饰图案。

## (2) 色板方向

- 主色（7 色，颜料名）：宝石红、翠绿、群青、金黄、铅白、赭石、暗紫。`verbatim`
- 主色是高饱和宝石色：红发、翠绿衣、群青背景、金黄饰物；整体浓烈、装饰性强。`verbatim`
- 辅色：玫瑰红、墨绿、暖灰。
- 禁色：灰调铺满；平滑学院渐变；冷灰雾调；印象派碎笔。
- 冷暖：暖红与暖金为主，翠绿与群青作冷点；冷暖对比强烈，是画面的能量来源。
- 明暗 / 饱和：中明度、高饱和、高对比；亮部是红发与白肤，暗部是深绿与暗紫。

## (3) 笔触与线条

- 笔触：精细、平滑、几乎看不见笔触；多层薄涂，追求宝石般的光泽。`verbatim`
- 线条：轮廓线精细、清晰，红发发丝逐根可辨；线条优先于笔触。
- 质感：光滑薄涂，无厚涂；织物与首饰质感靠淡色点染，不靠刀痕。

## (4) 构图习惯

- 画幅：竖幅为主；《贝娅塔·贝娅特丽克丝》1864–1870 年（一说，见 conflicts.md），竖幅，红发女子仰首；《普罗塞庇娜》1874 年，竖幅，持石榴。
- 视点：平视略低，观者与红发女子同高；视线被红发与石榴牵着望向女子面部。
- 布局：中心单人 + 象征物环绕：红发女子居中，石榴、鸟、花环绕四周；背景是扁平装饰图案。
- 裁切：人物常顶边，红发绵延出画边；不留安全边距。

## (5) 光影与透视

- 光源：均匀的室内光，无固定光源；亮在红发与白肤，暗部是深绿背景。
- 阴影：阴影是暗紫、墨绿的薄涂，透亮不死黑；明暗靠色彩对撞不靠灰阶。
- 透视：扁平空间，人物贴近画面；无焦点透视，空间靠图案层叠。

## (6) 该画什么 / 不该画什么

- 该画：红发美人、石榴、鸟、花、中世纪象征、但丁式恋人。`verbatim`
- 不该画：灰调；印象派碎笔；冷灰雾调；写实肖像的硬轮廓。
- Negative prompt: `grey muted palette, impressionist broken brushstrokes, cold grey haze, hard photorealistic outline, flat vector illustration`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Dante Gabriel Rossetti, a cup of coffee on a windowsill in the morning, Pre-Raphaelite, intense jewel-like colour, luminous red hair and pale skin, medieval symbolism, dense detail, dreamlike and sensual`
- 中文对照：罗塞蒂风格，清晨窗台上的一杯咖啡，拉斐尔前派，宝石般浓烈色彩，红发与苍白肌肤，中世纪象征，密集细节，梦境而感性。
- Negative: 见第 (6) 节。
- 检验点：咖啡与窗台是否画成宝石般浓烈、象征物环绕的梦境，而不是写实静物；红与绿是否对撞。
