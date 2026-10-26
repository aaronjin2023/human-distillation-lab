# Van Gogh — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Post-Impressionist oil painting, thick impasto, swirling directional brushstrokes, high-chroma chrome yellow and cobalt blue, night sky in rhythmic spirals, emotional, non-naturalistic colour`
- ZH: 后印象派油画，厚涂堆积，旋涡状方向性笔触，高饱和铬黄对撞钴蓝，夜空呈节奏性旋涡，情绪化、非写实色彩。

## (2) 色板方向

- 主色：铬黄 / 镉黄、钴蓝 / 群青 / 普鲁士蓝、翠绿。`verbatim`
- 辅色：朱红 / 茜素红（花卉、屋顶）、赭石 / 熟褐（地面、村庄暗部）。
- 禁色：灰暗土色大面积平涂；纯黑大面积阴影——阴影用彩色（蓝紫、深绿）不用纯黑。`verbatim`
- 冷暖：暖黄与冷蓝对撞是核心；同一画面里黄—蓝、橙—紫成对出现。`verbatim`
- 明暗 / 饱和：高饱和、高对比；亮部直接用管装纯色，不经灰调过渡。`verbatim`
- 注意：铬黄、茜素湖等颜料会褪色变暗（见 `conflicts.md`），今天看到的《向日葵》黄色比刚画完时暗——蒸风格时按“刚画完的鲜亮”还是“今天的褪色态”，需在 `manifest.json` 注明，本 pilot 按鲜亮态。

## (3) 笔触与线条

- 笔触：短促、厚涂（impasto）、方向跟随形体走——天空旋涡、山丘横向、柏树竖向；笔触本身就是构图线。`verbatim`
- 工具：硬毛笔 + 调色刀，颜料有时直接出管上画，不等干、湿画叠加。`artifact`（致提奥信件谈厚涂；博物馆技法分析）
- 线条：无精细轮廓线，形体边缘由笔触方向的转折界定；不是线描，是“笔触围合”。
- 质感：油彩堆积隆起可达数毫米级（《星夜》天空），光线下有真实起伏；局部也有薄涂、甚至留白画布处（晚期个别作品），不能全画都当厚涂。`artifact`（v0.1 所写“2–4 mm”精确数字未找到出处，v0.2 已改为“数毫米级”，见 conflicts.md 第 6 条）

## (4) 构图习惯

- 画幅：多为横幅风景 / 竖幅静物；《星夜》为横幅，三段式：天空（约 2/3）— 村庄横带 — 前景柏树左竖。
- 视点：平视偏高，略带俯瞰；无严格焦点透视，空间靠色彩冷暖与笔触疏密推远近。
- 布局：对角线 + 旋涡中心；大面积天空 + 一条暗色前景（柏树 / 麦田）压住画面下沿；地平线偏低，天空占主导。
- 裁切：主体常顶到画边（向日葵花头、柏树顶），不留“安全边距”。

## (5) 光影与透视

- 光源：无固定写实光源；星月自发光，亮部是“画出来的光”，不是照出来的光。`verbatim`
- 阴影：彩色阴影（蓝紫、墨绿），不用纯黑；明暗对比靠补色对撞，不靠灰阶渐变。
- 透视：近似焦点透视但被笔触节奏打散；远景不靠空气透视变淡，靠笔触变小、变横。

## (6) 该画什么 / 不该画什么

- 该画：夜空旋涡、星月、柏树、向日葵、麦田、鸢尾、乡村屋顶、椅子、靴子等日常物——把日常物画成有情绪的主角。`verbatim`
- 不该画：平滑无笔触的学院式渐变；灰调写实；黑色轮廓线勾边的卡通化；扁平矢量插画感。
- Negative prompt: `smooth academic blending, photorealistic, grey muted palette, flat vector illustration, black outline cartoon, no visible brushstrokes`

## (7) 测试提示词示例（现代题材：便利店夜景）

- Prompt: `In the style of Vincent van Gogh, a small convenience store at night in a modern city, thick impasto, swirling directional brushstrokes, chrome yellow shop sign glowing against deep cobalt blue night sky, cypress-like dark trees, rhythmic stars, emotional non-naturalistic colour, oil on canvas`
- 中文对照：梵高风格，现代城市里一家深夜便利店，厚涂、旋涡方向笔触，铬黄招牌在深钴蓝夜空里发光，深色柏树状树影，节奏性星空，情绪化非写实色彩，布面油画。
- Negative: 见第 (6) 节。
- 检验点：招牌黄是否“发光”而不是“贴上去”；天空笔触是否有旋涡方向，而不是均匀噪点；柏树 / 电线杆是否竖向压住画面。
