# Utagawa Hiroshige — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Ukiyo-e landscape woodblock print, atmospheric rain snow and mist, bokashi gradation skies, bold foreground framing, vertical ōban views of famous places, quiet and lyrical`
- ZH: 浮世绘风景版画，雨雪雾的气氛，摺印渐变的天空，前景大物遮挡的取景，竖幅大判名所，安静抒情。

## (2) 色板方向

- 主色（7 色，颜料名）：普鲁士蓝、淡蓝、灰色、淡绿、淡粉（胭脂红）、赭石、墨色。`verbatim` / `artifact`
- 比北斋更淡、更灰：广重的蓝是“天气的蓝”，雨天灰蓝、雪天淡蓝、晴天淡青，同一套蓝分出四季与天气。`verbatim`
- 辅色：淡粉染朝霞与樱花、赭石画屋顶与地面。
- 禁色：高饱和大面积平涂；粗黑硬线主导全幅；油画式明暗。
- 冷暖：整体偏冷偏淡，暖色只作小面积点缀（朝霞、灯火、樱花）。
- 明暗 / 饱和：靠摺印渐变（bokashi）染天色与水面，明暗极柔；饱和度低，亮在雨后的空处。

## (3) 笔触与线条

- 笔触：不是笔触，是刀味与渐变——轮廓线比北斋更细更柔，雨丝、雪点以细线密排；天色以渐变染出。`verbatim`
- 线条：细而均匀的轮廓线，雨线斜密、雪点疏朗；前景大物（桥、树、屋檐）以粗线收边，形成画框。`verbatim`
- 质感：木刻版画的平滑纸面 + 渐变天色 + 平涂色块；雨与雪是“线”而不是“色”。

## (4) 构图习惯

- 画幅：竖幅大判（ōban）为主，尤以《名所江户百景》的竖幅为代表；东海道一路横幅亦多。`artifact`
- 视点：高视点俯瞰 + 前景遮挡：近景常以桥、树、屋檐的大形压住画面一角，视线从遮挡后探出去。`verbatim`（《大桥骤雨》）
- 布局：一角式前景 + 远景名所，前景大、远景小，中间留空给雨、雪、雾。
- 裁切：前景大物常被裁掉边缘，桥与树出画，远景完整。`verbatim`

## (5) 光影与透视

- 光源：无固定光源；亮在雨后的天光与雪地的白处。
- 阴影：无写实阴影；天气即明暗，雨天全幅偏暗、雪天全幅偏亮。
- 透视：西洋透视的浮世绘化——近大远小是有的，但前景大物是装饰性的“画框”，不参与透视计算。

## (6) 该画什么 / 不该画什么

- 该画：东海道驿站、江户名所、雨雪雾天气、桥与河、樱花与朝霞、旅人。`verbatim`
- 不该画：巨浪式的激烈动势；高饱和大面积平涂；无前景遮挡的平铺风景；油画式明暗。
- Negative prompt: `dramatic giant waves, high-saturation flat colour, oil-painting shading, photorealistic perspective, no foreground framing`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Utagawa Hiroshige, a ramen shop late at night in a modern city, ukiyo-e landscape woodblock print, rain slanting in fine lines, bokashi gradation night sky, a large bridge beam framing the foreground, the shop's warm light small in the distance, vertical ōban`
- 中文对照：广重风格，深夜的拉面店，浮世绘风景版画，细密的斜雨线，摺印渐变夜空，前景大桥梁遮挡取景，店的暖光在远处很小，竖幅大判。
- Negative: 见第 (6) 节。
- 检验点：雨线是否细密斜排、天色是否有渐变；前景是否有大物遮挡；暖光是否小而克制。
