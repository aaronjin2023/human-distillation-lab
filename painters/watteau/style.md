# Antoine Watteau — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Rococo fete galante, soft feathery brushstrokes, silvery pastel palette, elegant figures in silk in a hazy parkland, dreamlike, fleeting, melancholic grace`
- ZH: 洛可可雅宴画，轻柔羽毛状笔触，银灰粉彩色调，丝绸华服人物置于朦胧园林，如梦、短暂、忧郁的优雅。

## (2) 色板方向

- 主色（7 色，颜料名）：银灰、珍珠白、淡粉红、天青蓝、淡金黄、橄榄绿、赭石。`verbatim`
- 主色是低饱和的粉彩 + 银灰，亮部偏冷、暖色只作点缀；整体明亮但不艳。`verbatim`
- 辅色：淡紫、湖绿、暖灰。
- 禁色：高饱和原色大面积平涂；纯黑轮廓；巴洛克式强明暗。
- 冷暖：冷灰为底，粉红与淡金作暖点；冷暖对比弱，靠明度微差分层。
- 明暗 / 饱和：中高明度、低—中饱和、弱对比；雾感来自薄涂与空气透视。

## (3) 笔触与线条

- 笔触：轻、快、羽毛状的碎笔触；远景几乎溶化，近景衣纹用稍实的短笔点出。`verbatim`
- 线条：轮廓线淡而断续，人物边缘常溶入背景；无硬线勾边，形靠色块与笔触收住。
- 质感：薄涂油彩 + 透明罩染，布面肌理细腻；丝绸光泽靠淡色提亮，不靠厚涂。

## (4) 构图习惯

- 画幅：横幅为主，《发舟西苔岛》129×194cm（卢浮宫藏，1717年）；人物群像占中景，园林占满幅。
- 视点：平视略高，观者如站在园林小径边旁观；无强制视点，视线在人物间游走。
- 布局：对角线人物链：人物成群沿斜线走向船 / 远方；前景人物大、远景人物小而淡，留白是雾与天。
- 裁切：人物常被画边轻轻裁掉一角，制造“偶然撞见”的现场感；不摆纪念碑式中心对称。

## (5) 光影与透视

- 光源：散射的暮色柔光，无固定光源；亮在丝绸与肤色，暗部是灰绿树荫。
- 阴影：阴影是灰蓝、灰绿的薄涂，不用纯黑；明暗过渡极缓。
- 透视：空气透视为主：远景淡、模糊、偏蓝；无严格焦点透视，空间靠雾的层次推远。

## (6) 该画什么 / 不该画什么

- 该画：丝绸华服的男女、园林雅集、丘比特小像、船与远山、恋人依偎与回望。`verbatim`
- 不该画：历史画的宏大叙事；写实肖像的硬轮廓；高饱和扁平色块；戏剧性强光。
- Negative prompt: `hard black outlines, high-saturation flat colour, dramatic chiaroscuro, heroic history painting, photorealistic detail, sharp focus everywhere`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Antoine Watteau, a cup of coffee on a windowsill in the morning, Rococo fete galante, soft feathery brushstrokes, silvery pastel palette, hazy light, elegant and fleeting mood, oil on canvas`
- 中文对照：瓦托风格，清晨窗台上的一杯咖啡，洛可可雅宴画，轻柔羽毛状笔触，银灰粉彩色调，朦胧光线，优雅而短暂的氛围，布面油画。
- Negative: 见第 (6) 节。
- 检验点：咖啡与窗台是否“溶在雾里”而不是硬边静物；色调是否银灰粉彩而不是高饱和。
