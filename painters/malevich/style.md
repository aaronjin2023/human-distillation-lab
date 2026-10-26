# Kazimir Malevich — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kazimir Malevich, Suprematist abstract painting, black square on white ground, floating geometric shapes, supremacy of pure feeling, no object, no horizon, white infinity`
- ZH: 马列维奇风格，至上主义抽象画，白底上的黑方块，漂浮的几何形，纯粹感觉至上，无物象、无地平线，白色的无限。

## (2) 色板方向

- 主色（6 色，颜料名）：黑色、白色、原色红、原色黄、原色蓝、灰色。`verbatim`
- 主色黑 + 白；红、黄、蓝只作小色块点缀。禁：写实色彩、渐变、曲线、具象物象。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：平涂，黑方块边缘略有手工颤抖与裂纹；线条：几何形的直边即线。质感：平面、薄涂，黑方块表面有细微裂纹与笔痕。

## (4) 构图习惯

- 画幅：方形为主；视点：无视点；布局：一个黑方块居中或斜置，或数个几何形漂浮于白底；无上下、无地平线。裁切：形常出画，白底即无限。

## (5) 光影与透视

- 光源：无光源、无阴影；黑与白的对比即全部明暗。透视：无透视，形漂浮于白的无限中。

## (6) 该画什么 / 不该画什么

- 该画：黑方块、白上方块、红方块、十字、圆、漂浮的几何群。
- 不该画：见下 Negative prompt。
- Negative prompt: `no recognisable object, no horizon, no gradient, no curve, no muted realistic colour`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Kazimir Malevich, a late-night ramen shop, Suprematist abstract painting, black square on white ground, floating geometric shapes, supremacy of pure feeling, no object, no horizon, white infinity`
- 中文对照：马列维奇风格，深夜拉面店，至上主义抽象画，白底上的黑方块，漂浮的几何形，纯粹感觉至上，无物象、无地平线，白色的无限。
- Negative: 见第 (6) 节。
- 检验点：题材是否被马列维奇的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
