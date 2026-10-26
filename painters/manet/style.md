# Édouard Manet — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Modernist oil painting, flat planes of colour, stark black and white contrasts, minimal modelling, direct confrontational gaze, contemporary Parisian life, no idealisation`
- ZH: 现代主义油画，扁平色块，黑白强烈对比，极少明暗造型，直视观者的对抗目光，当代巴黎生活，拒绝美化。

## (2) 色板方向

- 主色（7 色，颜料名）：墨黑、铅白、赭石、朱红、群青、土黄、灰绿。`verbatim`
- 主色是黑白对撞 + 土色，红只给花束与唇一小点；整体低饱和、高对比，亮部是白肤与白床单。`verbatim`
- 辅色：淡粉、灰蓝、暖灰。
- 禁色：粉彩甜腻；平滑学院渐变；高饱和艳色铺满；神话美化。
- 冷暖：冷黑白为主，暖肤色与朱红作点缀；冷暖对比弱，明暗对比极强。
- 明暗 / 饱和：中明度、低饱和、高明暗对比；亮部是扁平的白，不经灰调过渡。

## (3) 笔触与线条

- 笔触：宽笔、扁平、快速的笔触；笔触可见但不堆积，形靠色块不靠渐变。`verbatim`
- 线条：轮廓线硬而简，形靠黑白块面收住；无精细勾线。
- 质感：薄涂平滑，局部稍厚；表面无厚涂堆积，扁平是风格本体。

## (4) 构图习惯

- 画幅：横幅大幅为主；《草地上的午餐》1863 年，横幅野餐；《奥林匹亚》1863 年，横幅横卧裸女。
- 视点：平视，观者与裸女同高、被其直视；无俯仰，视线被目光钉住。
- 布局：横卧 / 横排：奥林匹亚横卧满幅，午餐四人横排；背景是扁平的深色 / 树林，无纵深。
- 裁切：人物常顶边，野餐篮与衣物裁边；不留安全边距。

## (5) 光影与透视

- 光源：均匀的室内 / 户外光，无固定光源；亮在白肤与白床单，暗部是黑衣与深色背景。
- 阴影：阴影是扁平的黑与灰，无渐变；明暗靠黑白块面对撞不靠灰阶。
- 透视：扁平空间，人物贴近画面；无焦点透视，远景人物（午餐背景涉水女子）比例失调是其标志。`verbatim`

## (6) 该画什么 / 不该画什么

- 该画：横卧裸女、野餐、酒吧女、斗牛、现代巴黎生活。`verbatim`
- 不该画：神话美化；粉彩；平滑渐变；艳色铺满；历史英雄。
- Negative prompt: `mythological beautification, rococo pastel, smooth academic blending, high-saturation colour, heroic history painting, photorealistic polish`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Edouard Manet, a late-night ramen shop in a modern city, modernist oil painting, flat planes of colour, stark black and white contrasts, minimal modelling, direct confrontational gaze, contemporary life, no idealisation`
- 中文对照：马奈风格，现代城市里一家深夜拉面店，现代主义油画，扁平色块，黑白强烈对比，极少明暗造型，直视观者的对抗目光，当代生活，拒绝美化。
- Negative: 见第 (6) 节。
- 检验点：拉面店是否扁平、黑白对撞、人物直视观者，而不是印象派碎笔与柔光；远景比例是否敢失调。
