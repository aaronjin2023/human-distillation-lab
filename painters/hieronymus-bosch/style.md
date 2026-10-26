# Hieronymus Bosch — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hieronymus Bosch, Northern Renaissance oil on panel, fantastical moral allegory, teeming tiny figures in a vast world landscape, muted greens and browns, grotesque hybrid creatures, triptych, precise detail`
- ZH: 博斯风格，北方文艺复兴木板油画，怪诞的道德寓言，广阔世界风景中密密麻麻的小人物，灰绿与土褐，怪异的混合生物，三联画，精确细节。

## (2) 色板方向

- 主色（7 色，颜料名）：墨绿、土黄、赭石、灰蓝、淡粉肤色、铅白、暗褐。`verbatim`
- 辅色：暗红（地狱火光）、灰绿（远景）。
- 禁色：明朗的田园风景；优雅的理想人体；大面积高饱和色；巴洛克式戏剧光影。
- 冷暖：整体偏冷的灰绿与土褐，中央乐园略暖、地狱以暗红火光作暖点。
- 明暗 / 饱和：中低对比，色彩灰而透明；亮部在乐园、暗部在地狱，明暗即道德。

## (3) 笔触与线条

- 笔触：极细、极薄，层层罩染；小人物与怪诞生物用细笔逐一描摹，细节极致。`verbatim`
- 线条：轮廓线精细、清晰，怪诞生物的边缘如刀刻般准确。
- 质感：木板油画的平滑质感；三联画外侧为灰色单色画（grisaille），内侧为彩色，是开合的对照。`artifact`

## (4) 构图习惯

- 画幅：三联画为主；《人间乐园》展开约 3.9 米，左为伊甸园、中为乐园、右为地狱。`verbatim`
- 视点：高视点俯瞰——世界风景从高处展开，地平线高，地面占大幅。
- 布局：三联分三段叙事，左中右即过去、现在、未来；中央乐园人物密密麻麻、无中心，视线在细节中游走。`verbatim`
- 裁切：人物极小、数量极多，无一处裁切，画面如百科全书般铺满。

## (5) 光影与透视

- 光源：均匀的漫射光，无戏剧光源；乐园最亮、地狱最暗，光即道德判断。
- 阴影：淡而清晰的阴影，体积靠罩染的透明层次。
- 透视：高视点世界风景——远景变淡、变蓝，空气透视与线性透视并用；空间深远而拥挤。

## (6) 该画什么 / 不该画什么

- 该画：三联画寓意、伊甸园与地狱、怪诞混合生物、巨型水果与器物中的小人物。
- 不该画：明朗的田园风景；优雅的理想人体；大面积高饱和色；单一主角的肖像。
- Negative prompt: `bright pastoral landscape, idealised graceful figures, large areas of saturated colour, single-portrait composition, dramatic Baroque spotlight, loose impressionist dabs`

## (7) 测试提示词示例（现代题材：夜市摊位）

- Prompt: `In the style of Hieronymus Bosch, a night market in a modern city, Northern Renaissance oil on panel, fantastical moral allegory, teeming tiny figures in a vast market landscape, muted greens and browns, grotesque hybrid details, triptych feeling, precise detail`
- 中文对照：博斯风格，现代城市的夜市，北方文艺复兴木板油画，怪诞的道德寓言，广阔市集风景中密密麻麻的小人物，灰绿与土褐，怪异的混合细节，三联画感，精确细节。
- Negative: 见第 (6) 节。
- 检验点：画面是否密密麻麻、细节极致；是否有道德寓言的意味而不是单纯的热闹；色彩是否灰绿克制。
