# Mark Rothko — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mark Rothko, Colour Field abstract painting, large soft-edged rectangles of orange and yellow floating on a stained ground, thin washes, luminous, silent, no line, no object`
- ZH: 罗斯科风格，色域抽象画，大块边缘柔和的橙与黄矩形漂浮于染色的底上，薄涂晕染，发光、寂静，无线、无物象。

## (2) 色板方向

- 主色（7 色，颜料名）：橙色、黄色、红色、深红、黑色、白色、赭石。`verbatim`
- 主色橙 + 黄（《橙与黄》）或红、深红；色块边缘柔和、晕染。禁：硬边几何、具象物象、可见笔触、黑色轮廓线。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：薄涂晕染，笔触几乎不可见，颜料稀释后层层染；线条：无线，色块边缘是晕染的软边。质感：薄、透、发光，如染色布。

## (4) 构图习惯

- 画幅：大幅竖幅为主；视点：无视点；布局：两至三块横向矩形上下叠置，居中、占满画面；色块边缘不触画边，留出底色呼吸。裁切：色块不顶边，底色即边框。

## (5) 光影与透视

- 光源：无光源，光来自色块本身的发光感；无阴影，色块靠晕染的明暗分离。透视：无透视，色块漂浮于底色中。

## (6) 该画什么 / 不该画什么

- 该画：两至三块横向软边矩形、色域、门式构图。
- 不该画：见下 Negative prompt。
- Negative prompt: `no hard edge, no recognisable object, no visible brushstrokes, no black contour line, no single-point perspective`

## (7) 测试提示词示例（现代题材：现代城市街角的便利店夜景）

- Prompt: `In the style of Mark Rothko, a small convenience store at night in a modern city, Colour Field abstract painting, large soft-edged rectangles of orange and yellow floating on a stained ground, thin washes, luminous, silent, no line, no object`
- 中文对照：罗斯科风格，现代城市街角的便利店夜景，色域抽象画，大块边缘柔和的橙与黄矩形漂浮于染色的底上，薄涂晕染，发光、寂静，无线、无物象。
- Negative: 见第 (6) 节。
- 检验点：题材是否被罗斯科的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
