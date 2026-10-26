# Pierre-Auguste Renoir — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Impressionism, warm luminous palette, feathery broken brushstrokes, dappled sunlight through leaves, pearly skin, joyful leisure, flickering light`
- ZH: 印象派，暖调明亮色调，羽毛状破碎笔触，树叶间斑驳阳光，珍珠般肌肤，欢愉休闲，闪烁的光。

## (2) 色板方向

- 主色（7 色，颜料名）：朱红、铬黄、钴蓝、翠绿、铅白、赭石、玫瑰红。`verbatim`
- 主色是暖调明亮：朱红、铬黄、玫瑰红为主，蓝绿作点缀；整体高明度、高饱和，阳光感强。`verbatim`
- 辅色：淡紫、粉红、暖灰。
- 禁色：纯黑；黑色轮廓线；冷灰雾调；沉闷土色。
- 冷暖：暖调为主，冷蓝绿作点缀；冷暖对比明快但不刺眼。
- 明暗 / 饱和：高明度、高饱和、中对比；亮部是阳光斑驳与珍珠肌肤，不经灰调过渡。

## (3) 笔触与线条

- 笔触：羽毛状破碎笔触，轻快、闪烁；笔触方向跟随光斑，不跟随形体。`verbatim`
- 线条：无轮廓线，形靠色块与光斑收住；不是线描，是“光斑围合”。
- 质感：薄涂 + 局部稍厚；表面有碎笔的起伏，无厚涂堆积。

## (4) 构图习惯

- 画幅：横幅大幅为主；《煎饼磨坊的舞会》1876 年，横幅舞会；《游船上的午餐》1880–1881 年，横幅十四人聚会。
- 视点：平视，观者站在舞会 / 阳台边；视线被阳光斑驳牵着在人群间游走。
- 布局：人群满幅 + 阳光斑驳：舞会人群横排，阳台聚会十四人围桌；视线落点在前景女子与阳光处。
- 裁切：人物常顶边、裁边，制造“撞见聚会”的现场感；不留安全边距。

## (5) 光影与透视

- 光源：阳光透过树叶 / 阳台的斑驳光，无固定光源；亮在肌肤、裙摆与酒杯。
- 阴影：阴影是彩色的（蓝紫、墨绿），不用纯黑；明暗靠光斑疏密不靠灰阶。
- 透视：浅空间，人物贴近画面；无焦点透视，空间靠光斑与人物前后错落。

## (6) 该画什么 / 不该画什么

- 该画：舞会、聚会、浴女、阳光下的肌肤、巴黎郊游。`verbatim`
- 不该画：黑色轮廓线；冷灰雾调；沉闷土色；摆拍历史画。
- Negative prompt: `black outlines, cold grey haze, dull earthy palette, staged history painting, smooth academic blending, photorealistic detail`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Pierre-Auguste Renoir, a late-night ramen shop in a modern city, Impressionism, warm luminous palette, feathery broken brushstrokes, dappled warm light, pearly skin, joyful leisure, flickering light`
- 中文对照：雷诺阿风格，现代城市里一家深夜拉面店，印象派，暖调明亮色调，羽毛状破碎笔触，斑驳暖光，珍珠般肌肤，欢愉休闲，闪烁的光。
- Negative: 见第 (6) 节。
- 检验点：拉面店是否阳光斑驳、人物是否欢愉、肌肤是否珍珠般闪烁，而不是冷调写实的夜景。
