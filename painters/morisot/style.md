# Berthe Morisot — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Impressionism, light feathery brushstrokes, pale luminous palette, white and silver-grey, intimate domestic moments, transparent veil-like paint, quiet and tender`
- ZH: 印象派，轻盈羽毛状笔触，苍白明亮色调，白与银灰，亲密的家庭瞬间，薄纱般透明的颜料，寂静而温柔。

## (2) 色板方向

- 主色（7 色，颜料名）：铅白、银灰、淡粉红、淡金黄、淡青蓝、淡绿、赭石。`verbatim`
- 主色是白与银灰的苍白色调，粉红与淡金只作点缀；整体高明度、低饱和，通透如薄纱。`verbatim`
- 辅色：淡紫、湖绿、暖灰。
- 禁色：高饱和艳色铺满；纯黑；黑色轮廓线；沉闷土色。
- 冷暖：冷白为主，暖粉与淡金作点缀；冷暖对比弱，靠明度微差分层。
- 明暗 / 饱和：高明度、低饱和、低对比；亮在白衣与薄纱，暗部是淡灰。

## (3) 笔触与线条

- 笔触：轻、快、羽毛状的碎笔触；颜料薄而透，近乎水彩感。`verbatim`
- 线条：轮廓线淡而断续，人物边缘溶入薄纱；无硬线勾边。
- 质感：薄涂透明，颜料如薄纱；表面无厚涂堆积，通透是风格本体。

## (4) 构图习惯

- 画幅：横幅与竖幅并存；《摇篮》1872 年，横幅，母亲俯视摇篮；《夏日》1874 年（一说，见 conflicts.md），横幅，湖边女子。
- 视点：平视略低，观者站在室内一角；视线被母亲的目光牵着望向摇篮。
- 布局：室内一角 + 薄纱：母亲与摇篮占中景，薄纱作画框；视线落点在摇篮中的婴儿与母亲的目光。
- 裁切：人物常被画边轻轻裁掉，薄纱绵延出画边；不留安全边距。

## (5) 光影与透视

- 光源：散射的室内光，无固定光源；亮在白衣与薄纱，暗部是淡灰室内。
- 阴影：阴影是淡灰、淡紫的薄涂，透亮不死黑；明暗靠薄纱的层次不靠灰阶。
- 透视：浅空间，人物贴近画面；无焦点透视，空间靠薄纱层叠。

## (6) 该画什么 / 不该画什么

- 该画：摇篮、母子、剧院包厢、湖边女子、室内阅读。`verbatim`
- 不该画：高饱和艳色；纯黑；黑色轮廓线；历史画；戏剧性动势。
- Negative prompt: `high-saturation colour, pure black, black outlines, staged history painting, dramatic action, dull earthy palette`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Berthe Morisot, a cup of coffee on a windowsill in the morning, Impressionism, light feathery brushstrokes, pale luminous palette of white and silver-grey, intimate domestic moment, transparent veil-like paint, quiet and tender`
- 中文对照：莫里索风格，清晨窗台上的一杯咖啡，印象派，轻盈羽毛状笔触，苍白明亮的白与银灰色调，亲密的家庭瞬间，薄纱般透明的颜料，寂静而温柔。
- Negative: 见第 (6) 节。
- 检验点：咖啡与窗台是否画成薄纱般通透、苍白明亮，而不是写实静物；是否轻盈而不是沉重。
