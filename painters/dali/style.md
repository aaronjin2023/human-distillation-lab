# Salvador Dalí — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Salvador Dalí, Surrealist oil painting, photographic miniature realism, soft melting watches draped over a branch and a shelf, barren Catalan coast, dream logic, hard made soft and soft made hard`
- ZH: 达利风格，超现实主义油画，照相般的微型写实，柔软的表搭在树枝与台架上，荒凉的加泰罗尼亚海岸，梦的逻辑，硬变软、软变硬。

## (2) 色板方向

- 主色（7 色，颜料名）：暖金、橄榄绿、天蓝、赭石、苍白肤色、深褐、白色。`verbatim`
- 主色暖金 + 橄榄绿 + 天蓝，亮而干净的梦境光；硬物与软物同色。禁：厚涂笔触、灰暗土色、模糊印象派笔触。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：极细、极平滑，几乎无笔触痕迹，如照相写实；线条：精确、锐利的轮廓线，物象边缘清晰。质感：光滑、精细，小幅画如微型画。

## (4) 构图习惯

- 画幅：小幅为主（《记忆的永恒》仅 24×33cm）；视点：低地平线、远景开阔；布局：前景软表、中景海岸、远景悬崖三段；物象孤立、间距大。裁切：物象完整、不顶边，空旷即梦境。

## (5) 光影与透视

- 光源：明亮、干净的日光，无阴影浑浊；阴影清晰、锐利。透视：写实透视，但物象比例失常（巨蚁、软表），透视正确、逻辑荒诞。

## (6) 该画什么 / 不该画什么

- 该画：软表、蚂蚁、拐杖、抽屉、蛋、纳西索斯、加泰罗尼亚海岸。
- 不该画：见下 Negative prompt。
- Negative prompt: `no visible brushstrokes, no thick impasto, no grey muted palette, no impressionist broken colour, no ordinary logical scale`

## (7) 测试提示词示例（现代题材：一辆停在街边的共享单车）

- Prompt: `In the style of Salvador Dalí, a shared bicycle parked on a city street, Surrealist oil painting, photographic miniature realism, soft melting watches draped over a branch and a shelf, barren Catalan coast, dream logic, hard made soft and soft made hard`
- 中文对照：达利风格，一辆停在街边的共享单车，超现实主义油画，照相般的微型写实，柔软的表搭在树枝与台架上，荒凉的加泰罗尼亚海岸，梦的逻辑，硬变软、软变硬。
- Negative: 见第 (6) 节。
- 检验点：题材是否被达利的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
