# Edgar Degas — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Impressionism and Realism, off-centre cropped composition, fleeting ballet poses, pastel and oil, cool blue and warm flesh, artificial stage light, unsentimental observation`
- ZH: 印象派与现实主义，非常规裁切构图，瞬间芭蕾姿态，粉彩与油画，冷蓝与暖肤色，舞台人工光，冷静观察。

## (2) 色板方向

- 主色（7 色，颜料名）：钴蓝、群青、铅白、赭石、玫瑰红、墨绿、土黄。`verbatim`
- 主色是冷蓝（蓝衣舞者）+ 暖肤色对撞，粉彩的粉、蓝、绿并置；整体明亮但冷峻。`verbatim`
- 辅色：淡紫、粉红、暖灰。
- 禁色：粉彩甜腻；平滑学院渐变；纪念碑式对称；美化修饰。
- 冷暖：冷蓝为主，暖肤色与玫瑰红作点缀；冷暖对比是舞台光的来源。
- 明暗 / 饱和：中明度、中饱和、中对比；亮部是舞裙蓝与肌肤白，暗部是舞台深色。

## (3) 笔触与线条

- 笔触：粉彩短笔 + 油彩薄涂并用；粉彩的粉末感与油彩的平滑感交织，是其标志。`verbatim`
- 线条：轮廓线精细、断续，舞者姿态线是画面的骨架；无硬线勾边。
- 质感：粉彩粉末感 + 油彩平滑感交织；舞裙薄纱质感靠粉彩淡涂，不靠厚涂。

## (4) 构图习惯

- 画幅：横幅与竖幅并存；《蓝衣舞者》约 1895 年（粉彩），横幅，四位舞者；浴女系列多为竖幅。
- 视点：俯视 / 仰视并存：舞者常从高处俯视，浴女常从低处仰视；非常规视点是其标志。
- 布局：非常规裁切：舞者被画边裁掉一半，浴女被浴缸裁掉下半；视线落点在舞裙与肌肤。
- 裁切：裁切是本体：人物常被画边裁掉，制造“偶然撞见”的现场感；不摆纪念碑式中心对称。

## (5) 光影与透视

- 光源：舞台人工光 + 室内散射光，无固定光源；亮在舞裙蓝与肌肤白。
- 阴影：阴影是彩色的（蓝紫、墨绿），不用纯黑；明暗靠冷暖对撞不靠灰阶。
- 透视：非常规透视：俯视地板倾斜、浴缸变形，空间靠裁切与视点推远近；无严格焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：芭蕾舞者、浴女、洗衣妇、赛马、剧场观众。`verbatim`
- 不该画：美化；粉彩甜腻；平滑渐变；纪念碑式对称；摆拍历史画。
- Negative prompt: `beautified idealisation, pastel sweetness, smooth academic blending, symmetrical monument, staged history painting, photorealistic polish`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Edgar Degas, shared bicycles parked in a neat row on a modern city street at dawn, off-centre cropped composition, fleeting poses, pastel and oil, cool blue and warm flesh, artificial light, unsentimental observation`
- 中文对照：德加风格，黎明时现代城市街道上一排整齐停放的共享单车，非常规裁切构图，瞬间姿态，粉彩与油画，冷蓝与暖肤色，人工光，冷静观察。
- Negative: 见第 (6) 节。
- 检验点：单车是否被画边裁掉一半、视点是否非常规俯视，而不是大卫式浮雕横排；冷蓝与暖肤色是否对撞。
