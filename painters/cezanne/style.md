# Paul Cézanne — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Post-Impressionism, constructive brushstrokes building form, warm ochre and cool blue, geometric simplification, multiple viewpoints, solid and timeless, no outlines`
- ZH: 后印象派，建构性笔触搭建形体，暖赭与冷蓝，几何简化，多视点，坚实而永恒，不用轮廓线。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、土黄、钴蓝、群青、翠绿、铅白、熟褐。`verbatim`
- 主色是暖赭 + 冷蓝的对撞，整体低饱和、高明度，亮在天空与山体，暗部是褐与墨绿。`verbatim`
- 辅色：淡紫、粉红、暖灰。
- 禁色：黑色轮廓线；平滑学院渐变；高饱和艳色铺满；印象派碎笔。
- 冷暖：暖赭与冷蓝对撞是核心；同一画面里赭—蓝成对出现。
- 明暗 / 饱和：中明度、低饱和、中对比；亮部直接用暖赭薄涂，不经灰调过渡。

## (3) 笔触与线条

- 笔触：建构性短笔触，方向跟随形体走；笔触本身就是结构，方向一乱形就散。`verbatim`
- 线条：无轮廓线，形靠色块并置收住；不是线描，是“色块围合”。
- 质感：薄涂 + 局部稍厚；表面有建构笔触的起伏，无厚涂堆积。

## (4) 构图习惯

- 画幅：横幅与竖幅并存；《圣维克多山》系列多幅横幅，山体横卧；《玩纸牌者》系列五幅，人物围桌。
- 视点：多视点：同一画面里桌子、瓶子、山体各有自己的视点，是其标志；无单一视点。
- 布局：几何简化：山体成三角，桌子成梯形，人物成圆柱；视线落点在山体与纸牌者。
- 裁切：人物与山体常顶边，桌子裁边；不留安全边距。

## (5) 光影与透视

- 光源：散射的普罗旺斯阳光，无固定光源；亮在山体与天空，暗部是前景树木。
- 阴影：阴影是彩色的（蓝紫、墨绿），不用纯黑；明暗靠色块并置不靠灰阶。
- 透视：多视点 + 空气透视：远景山体淡、模糊，近景桌子实；空间靠色块疏密推远近。

## (6) 该画什么 / 不该画什么

- 该画：圣维克多山、玩纸牌者、静物（苹果与瓶子）、浴女、普罗旺斯风景。`verbatim`
- 不该画：黑色轮廓线；平滑渐变；高饱和艳色；印象派碎笔；历史画。
- Negative prompt: `black outlines, smooth academic blending, high-saturation colour, impressionist broken dabs, staged history painting, photorealistic detail`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Paul Cezanne, shared bicycles parked in a neat row on a modern city street at dawn, Post-Impressionism, constructive brushstrokes building form, warm ochre and cool blue, geometric simplification, multiple viewpoints, solid and timeless`
- 中文对照：塞尚风格，黎明时现代城市街道上一排整齐停放的共享单车，后印象派，建构性笔触搭建形体，暖赭与冷蓝，几何简化，多视点，坚实而永恒。
- Negative: 见第 (6) 节。
- 检验点：单车是否画成几何色块、是否多视点、是否坚实如建筑，而不是印象派碎笔与柔光。
