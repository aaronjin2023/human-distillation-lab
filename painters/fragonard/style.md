# Jean-Honoré Fragonard — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Rococo, feathery fluid brushstrokes, luminous pastel palette of butter pink, cream and leaf green, swirling garden movement, playful erotic charm, sun-dappled light`
- ZH: 洛可可，羽毛状流畅笔触，奶油粉、乳白与叶绿的明亮粉彩，旋转的花园动势，俏皮风流，阳光斑驳。

## (2) 色板方向

- 主色（7 色，颜料名）：奶油粉、乳白、叶绿、淡金黄、天青蓝、玫瑰红、赭石。`verbatim`
- 主色是明亮粉彩，粉红与叶绿对撞但都提亮；整体高明度、阳光感强，比瓦托更艳、更暖。`verbatim`
- 辅色：淡紫、浅褐、暖灰。
- 禁色：暗沉土色大面积；纯黑阴影；冷灰雾调铺满。
- 冷暖：暖粉与暖金为主，叶绿与天青作冷点；冷暖对比明快但不刺眼。
- 明暗 / 饱和：高明度、中高饱和、中对比；亮部直接用乳白与淡金，不经灰调过渡。

## (3) 笔触与线条

- 笔触：羽毛状、流畅、快速的笔触；树叶用碎笔点染，衣裙用长而弯的笔触带出飞动感。`verbatim`
- 线条：轮廓线轻而流动，人物边缘溶入光斑；无硬线，形靠色彩与笔触收住。
- 质感：薄涂 + 局部厚涂并存；阳光处颜料稍厚，树叶处薄而透。

## (4) 构图习惯

- 画幅：横幅与竖幅并存；《秋千》1767 年，画面以秋千斜线为骨架，树丛满幅。
- 视点：平视略低，观者如藏在树丛后偷看；视线随秋千弧线上下走。
- 布局：对角线 + 弧线：秋千绳索成斜线，裙摆与飞鞋成弧线，树丛作画框；视线落点在秋千上的女子。
- 裁切：树丛常裁掉画边，人物顶边，制造“撞见私密瞬间”的现场感。

## (5) 光影与透视

- 光源：阳光透过树叶的斑驳光，无固定光源；亮在裙摆、肤色与飞鞋。
- 阴影：阴影是绿、蓝灰的薄涂，透亮不死黑；暗部仍有色彩。
- 透视：空气透视弱，空间靠树丛层叠与光斑疏密；远景几乎被绿叶填满。

## (6) 该画什么 / 不该画什么

- 该画：秋千上的女子、飞起的鞋、花园幽会、丘比特小像、爱情追逐。`verbatim`
- 不该画：庄严历史画；冷灰雾调；硬轮廓；沉闷土色。
- Negative prompt: `dark earthy palette, hard black outlines, cold grey haze, solemn history painting, photorealistic detail, flat vector illustration`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Jean-Honore Fragonard, a late-night ramen shop in a modern city, Rococo, feathery fluid brushstrokes, butter pink and leaf green pastel palette, swirling movement, playful warm light, oil on canvas`
- 中文对照：弗拉戈纳尔风格，现代城市里一家深夜拉面店，洛可可，羽毛状流畅笔触，奶油粉与叶绿粉彩，旋转动势，俏皮暖光，布面油画。
- Negative: 见第 (6) 节。
- 检验点：拉面店是否“飞起来”——蒸汽、灯光与人物有弧线动势，而不是静态室内；粉彩是否明亮而不是灰暗。
