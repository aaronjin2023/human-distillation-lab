# Francisco de Goya — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Spanish Romanticism, raw expressive brushwork, harsh single lantern light against black night, earthy ochre and bone white, unflinching brutality, no idealisation`
- ZH: 西班牙浪漫主义，粗粝表现性笔触，提灯强光对撞黑夜，土黄赭石与骨白，直面残暴，毫不美化。

## (2) 色板方向

- 主色（7 色，颜料名）：骨白、赭石、土黄、熟褐、墨黑、暗红、灰绿。`verbatim`
- 主色是暗调土色 + 骨白高光；红只给血与衣饰一小点，整体低明度、低饱和，亮处刺眼。`verbatim`
- 辅色：灰蓝、暗紫、暖灰。
- 禁色：粉彩甜腻；高饱和艳色铺满；平滑学院渐变；美化修饰。
- 冷暖：暖黄灯光对撞冷黑夜色；冷暖对比极端，靠一盏灯的光完成。
- 明暗 / 饱和：低明度、高明暗对比、低饱和；亮部是提灯照亮的白衣与面部，暗部近乎纯黑。

## (3) 笔触与线条

- 笔触：粗、快、近乎涂抹的笔触；晚期黑色绘画直接画在墙上，笔触更粗粝、更自由。`verbatim`
- 线条：轮廓线粗而断续，形靠明暗块面收住；无精细勾线。
- 质感：厚薄不均：亮部颜料稍厚，暗部薄涂近乎干擦；黑色绘画有墙面粗糙感。

## (4) 构图习惯

- 画幅：横幅为主；《1808年5月3日》1814 年，横幅大场面；黑色绘画是墙面原作（后揭取上画布），尺寸不一。
- 视点：平视，观者站在行刑队对面、与受害者同高；无俯仰，视线被迫直视枪口与白衣。
- 布局：左右对峙：左受害者亮群、右行刑队暗排，中间是提灯；视线落点在中央白衣男子的张开双臂。
- 裁切：行刑者常被画边裁掉（只见背影与枪管），受害者完整；裁切本身就是立场。

## (5) 光影与透视

- 光源：提灯单光源：画面中央一盏灯照亮受害者，行刑者背光成黑影。`verbatim`
- 阴影：阴影近乎纯黑，但仍有褐、绿的微差；暗部不透明到底，留有笔触。
- 透视：浅空间，人物贴近画面；无焦点透视，空间靠明暗两块（亮左 / 暗右）划分。

## (6) 该画什么 / 不该画什么

- 该画：行刑、受害者、提灯、黑夜、农神与巨口、疯癫与恐惧的直面。`verbatim`
- 不该画：美化；粉彩；平滑渐变；英雄式纪念碑构图；艳色。
- Negative prompt: `rococo pastel, smooth academic blending, beautified idealisation, heroic monument, high-saturation colour, photorealistic polish`

## (7) 测试提示词示例（现代题材：便利店夜景）

- Prompt: `In the style of Francisco de Goya, a small convenience store at night in a modern city, raw expressive brushwork, harsh lantern light against black night, earthy ochre and bone white, unflinching, no idealisation, oil on canvas`
- 中文对照：戈雅风格，现代城市里一家深夜便利店，粗粝表现性笔触，提灯强光对撞黑夜，土黄赭石与骨白，直面毫不美化，布面油画。
- Negative: 见第 (6) 节。
- 检验点：便利店灯光是否如提灯般“审判”画面、暗部是否近乎纯黑，而不是均匀明亮的夜景插画。
