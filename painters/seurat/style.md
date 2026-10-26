# Georges Seurat — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Neo-Impressionism and Pointillism, tiny dots of pure colour, optical mixing, orderly classical composition, stillness, luminous and timeless, no visible brushstrokes`
- ZH: 新印象派与点彩，纯色小点，光学混合，秩序井然的古典构图，寂静，发光而永恒，无可见笔触。

## (2) 色板方向

- 主色（7 色，颜料名）：钴蓝、群青、铬黄、朱红、翠绿、紫罗兰、铅白。`verbatim`
- 主色是纯色小点并置：蓝与橙、红与绿光学混合；整体明亮、发光，阴影用彩色点不用黑。`verbatim`
- 辅色：粉红、淡紫、湖绿。
- 禁色：混合调色；黑色轮廓线；平滑学院渐变；印象派碎笔。
- 冷暖：冷暖并置：同一水面里蓝与橙、绿与红点彩并置，冷暖对比是光的来源。
- 明暗 / 饱和：高明度、高饱和、中对比；亮部是点彩的光学混合，不经调色盘调和。

## (3) 笔触与线条

- 笔触：点彩小点，均匀、秩序井然；点本身就是笔触，方向一致、大小相近。`verbatim`
- 线条：无轮廓线，形靠点彩的疏密收住；不是线描，是“点围合”。
- 质感：薄涂点彩，表面均匀细腻；无厚涂堆积，点的起伏极小。

## (4) 构图习惯

- 画幅：大幅横幅为主；《大碗岛的星期天下午》1884–1886 年，207×308cm，横幅大场面；《阿尼埃尔的浴者》1883–1884 年，横幅。
- 视点：平视，观者站在河岸边；视线被点彩的光牵着在人群间游走。
- 布局：古典秩序：人物横排如浮雕，树木垂直，河岸水平；视线落点在前景女子与狗。
- 裁切：人物常顶边，树木裁边；不留安全边距。

## (5) 光影与透视

- 光源：散射的夏日阳光，无固定光源；亮在水面与草地，暗部是树荫。
- 阴影：阴影是彩色的点（蓝紫、墨绿），不用纯黑；明暗靠点的疏密不靠灰阶。
- 透视：古典透视 + 点彩平面：远景淡、模糊，近景实；空间靠点的疏密推远近。

## (6) 该画什么 / 不该画什么

- 该画：大碗岛人群、阿尼埃尔浴者、马戏团、河岸风景。`verbatim`
- 不该画：混合调色；黑色轮廓线；平滑渐变；印象派碎笔；戏剧性动势。
- Negative prompt: `mixed muddy colour, black outlines, smooth academic blending, impressionist broken dabs, dramatic action, photorealistic detail`

## (7) 测试提示词示例（现代题材：雨夜公交站）

- Prompt: `In the style of Georges Seurat, a rainy bus stop at night in a modern city, Neo-Impressionism and Pointillism, tiny dots of pure colour, optical mixing, orderly classical composition, stillness, luminous and timeless`
- 中文对照：修拉风格，现代城市里一个雨夜公交站，新印象派与点彩，纯色小点，光学混合，秩序井然的古典构图，寂静，发光而永恒。
- Negative: 见第 (6) 节。
- 检验点：公交站是否画成均匀小点、光是否光学混合、构图是否古典秩序，而不是印象派碎笔与柔光。
