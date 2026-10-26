# Peter Paul Rubens — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peter Paul Rubens, Flemish Baroque oil painting, dynamic swirling movement, sensual fleshy bodies, rich luminous colour, oil sketch to monumental canvas, vitality and abundance`
- ZH: 鲁本斯风格，弗兰德斯巴洛克油画，旋转的动感，感性的丰满肉体，浓烈丰盈的色彩，油彩小稿到巨幅，生命力与丰盈。

## (2) 色板方向

- 主色（7 色，颜料名）：朱红、群青、土黄、赭石、淡粉肤色、墨绿、铅白。`verbatim`
- 辅色：金黄（衣袍与光）、胭脂红（织物）。
- 禁色：纤细苍白的人体；静止对称的构图；灰暗土色；小幅精致。
- 冷暖：暖调为主——暖肤、暖红、暖金；群青与墨绿作冷对比，冷暖对撞而和谐。
- 明暗 / 饱和：中高对比，色彩浓烈而透明；亮部金黄、暗部深暖；饱和度高。

## (3) 笔触与线条

- 笔触：油彩小稿笔触自由、肯定；巨幅笔触流畅、厚重，皮肤厚涂、织物薄涂。`verbatim`
- 线条：轮廓线流畅、富有弹性，身体的曲线如旋涡般卷动。
- 质感：布面油画，皮肤如瓷而有温度，织物厚重，毛皮柔软；罩染与厚涂并置。

## (4) 构图习惯

- 画幅：巨幅祭坛画与神话皆有；《卸下十字架》为竖幅三联，中央基督斜垂。`verbatim`
- 视点：平视略仰；《卸下十字架》中基督身体沿对角线斜垂，视线随身体下滑。
- 布局：对角线与旋涡构图——人物如旋风般卷动，身体交错、重叠，视线在旋涡中循环；《爱情花园》人物横向展开如田园诗。`verbatim`
- 裁切：人物常被画框边缘截断，营造近景感与动感；巨幅构图无“边”，视线在画面上环绕。

## (5) 光影与透视

- 光源：暖金光线，光从画面外上方来，全幅一致；光是色彩的一部分。
- 阴影：深暖的阴影，亮暗之间有罩染的透明过渡。
- 透视：空气透视——远景变淡、变蓝；线性透视克制，动感靠身体的交错与对角线。

## (6) 该画什么 / 不该画什么

- 该画：卸下十字架、神话与狩猎、爱情花园、肖像；丰满的裸体与织物；动感群像。
- 不该画：纤细苍白的人体；静止对称的构图；灰暗土色；小幅精致。
- Negative prompt: `slender pale figures, static symmetrical composition, dull muddy palette, small-scale pretty picture, smooth academic blending, photorealistic detail`

## (7) 测试提示词示例（现代题材：户外婚礼花园）

- Prompt: `In the style of Peter Paul Rubens, an outdoor wedding garden in the modern day, Flemish Baroque oil painting, dynamic swirling movement, sensual fleshy bodies, rich luminous colour, warm golden light, vitality and abundance, oil on canvas`
- 中文对照：鲁本斯风格，现代户外婚礼花园，弗兰德斯巴洛克油画，旋转的动感，感性的丰满肉体，浓烈丰盈的色彩，暖金光线，生命力与丰盈，布面油画。
- Negative: 见第 (6) 节。
- 检验点：人物是否如旋风般卷动而不是静止摆拍；色彩是否浓烈丰盈；身体是否有肉感与生命力。
