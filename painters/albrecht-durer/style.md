# Albrecht Dürer — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Albrecht Dürer, Northern Renaissance engraving and oil, precise burin line, cross-hatching, scientific observation, melancholic intellect, black and white mastery, meticulous detail`
- ZH: 丢勒风格，北方文艺复兴版画与油画，极致精密的刻线，交叉排线，科学观察，忧郁的智性，黑白的 mastery，细节极致。

## (2) 色板方向

- 主色（7 色，颜料名）：墨黑（版画线条）、铅白（纸与高光）、赭石、土黄、群青、朱红、灰褐。`verbatim`
- 辅色：淡灰（中间调）、暖褐（油画底色）。
- 禁色：粗犷笔触；大面积平涂；模糊的轮廓；高饱和的装饰色。
- 冷暖：版画为黑白灰，冷峻；油画偏暖，肤色与衣袍暖而亮。
- 明暗 / 饱和：高对比，黑白分明；中间调由交叉排线的疏密构成，层次极细。

## (3) 笔触与线条

- 笔触：版画无笔触，只有刻线——刻刀（burin）在铜版上刻出的线条精密如发丝，交叉排线构成明暗。`verbatim`
- 线条：线条是本体——排线的方向、疏密、交叉即体积与质感；油画亦以精细线条收形。`artifact`
- 质感：铜版画的黑白层次极细，纸面光滑；油画《四使徒》表面光滑、色彩沉稳。

## (4) 构图习惯

- 画幅：版画为小幅（《忧郁 I》约 24×19 厘米），油画为大竖幅（《四使徒》两联）。`verbatim`
- 视点：平视；《忧郁 I》中天使端坐、目光低垂，周围器物环绕如静物。
- 布局：密集的象征物环绕主体——《忧郁 I》中天使、魔方、沙漏、天秤、狗、蝙蝠挤满画面，无一处空。`verbatim`
- 裁切：几乎不裁切，画面如百科全书般严密；《1500 年自画像》为正面半身，人物居中、目光直视观者。

## (5) 光影与透视

- 光源：均匀、清澈的光，无戏剧光源；明暗由排线疏密构成，不靠色彩。
- 阴影：交叉排线构成的灰调，层次极细，从白到黑有极长的过渡。
- 透视：数学透视——丢勒著有透视理论，画面上的建筑与器物按透视准确定位。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：铜版画、木刻、自画像、四使徒；象征物密集的静物式构图；野兔、草地等自然观察。
- 不该画：粗犷笔触；大面积平涂；模糊轮廓；高饱和装饰色。
- Negative prompt: `rough visible brushstrokes, flat matte colour, blurred outlines, saturated decorative colour, loose impressionist dabs, photorealistic camera blur`

## (7) 测试提示词示例（现代题材：书桌上的野兔与植物标本）

- Prompt: `In the style of Albrecht Dürer, a hare and botanical specimens on a desk, Northern Renaissance engraving, precise burin line, cross-hatching, scientific observation, melancholic intellect, black and white mastery, meticulous detail, watercolour study feeling`
- 中文对照：丢勒风格，书桌上的一只野兔与植物标本，北方文艺复兴版画，极致精密的刻线，交叉排线，科学观察，忧郁的智性，黑白的 mastery，细节极致，水彩习作感。
- Negative: 见第 (6) 节。
- 检验点：线条是否精密如发丝；排线疏密是否构成明暗；细节是否如科学观察般准确。
