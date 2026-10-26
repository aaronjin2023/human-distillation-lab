# Paul Gauguin — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Post-Impressionism and Synthetism, large flat areas of unnatural colour, dark cloisonnist outlines, symbolic red and yellow, simplified forms, dreamlike and primitive`
- ZH: 后印象派与综合主义，大面积非自然色平涂，深色分隔轮廓，象征性红与黄，简化形体，梦境而原始。

## (2) 色板方向

- 主色（7 色，颜料名）：朱红、铬黄、钴蓝、翠绿、墨黑、赭石、铅白。`verbatim`
- 主色是大面积非自然色：红田野、黄基督、绿人影；整体高饱和、扁平，红黄是象征色。`verbatim`
- 辅色：橙黄、紫罗兰、暖灰。
- 禁色：灰调铺满；平滑学院渐变；写实固有色；印象派碎笔。
- 冷暖：暖红黄为主，冷蓝绿作点缀；冷暖对比强烈，是象征的来源。
- 明暗 / 饱和：中明度、高饱和、高对比；亮部是黄基督与红田野，不经灰调过渡。

## (3) 笔触与线条

- 笔触：平涂为主，笔触几乎看不见；大面积平涂 + 深色轮廓，是其标志。`verbatim`
- 线条：深色轮廓线（cloisonnisme，分隔主义）是本体：形靠深色线围合，如彩色玻璃铅条。
- 质感：薄涂平滑，无厚涂；表面如彩色玻璃，平涂是风格本体。

## (4) 构图习惯

- 画幅：横幅为主；《布道后的幻象》1888 年，横幅，红田野 + 雅各与天使摔跤；《黄色基督》1889 年，横幅，黄基督十字架。
- 视点：平视略高，观者站在布道妇女身后；视线被红田野牵着望向幻象。
- 布局：对角线分隔：布道妇女在前景，红田野在中景，幻象在远景；树干斜线分隔现实与幻象。
- 裁切：人物常顶边，树干裁边；不留安全边距。

## (5) 光影与透视

- 光源：无固定光源；亮在黄基督与红田野，亮本身就是象征。
- 阴影：阴影是彩色的（暗红、墨绿），不用纯黑；明暗靠平涂色块不靠灰阶。
- 透视：扁平空间，人物贴近画面；无焦点透视，空间靠色块层叠。

## (6) 该画什么 / 不该画什么

- 该画：布道妇女、雅各与天使、黄基督、塔希提妇女、原始象征。`verbatim`
- 不该画：灰调；平滑渐变；写实固有色；印象派碎笔；历史画。
- Negative prompt: `grey muted palette, smooth academic blending, naturalistic local colour, impressionist broken dabs, staged history painting, photorealistic detail`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Paul Gauguin, a cup of coffee on a windowsill in the morning, Post-Impressionism and Synthetism, large flat areas of unnatural colour, dark cloisonnist outlines, symbolic red and yellow, simplified forms, dreamlike`
- 中文对照：高更风格，清晨窗台上的一杯咖啡，后印象派与综合主义，大面积非自然色平涂，深色分隔轮廓，象征性红与黄，简化形体，梦境。
- Negative: 见第 (6) 节。
- 检验点：咖啡与窗台是否画成大面积红黄平涂、深色轮廓围合，而不是写实静物；红黄是否象征而不是固有色。
