# Jackson Pollock — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jackson Pollock, Abstract Expressionist drip painting, enamel paint poured and flung onto unstretched canvas on the floor, all-over web of black white yellow and brown lines, no centre, no object, pure action`
- ZH: 波洛克风格，抽象表现主义滴洒画，珐琅漆泼洒于铺在地面的无框画布，黑白黄棕线网满幅，无中心、无物象，纯粹的行动。

## (2) 色板方向

- 主色（7 色，颜料名）：黑色、白色、黄色、棕色、灰色、暗红、铝银色。`verbatim`
- 主色黑、白、黄、棕的线网；《秋韵》以棕、白、黑为主。禁：具象物象、单点透视、平滑渐变、空白留白。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：无笔触——滴、泼、甩、洒，漆线是身体运动的轨迹；工具：棍、刷、破罐、注射器，不用画笔触画布。线条：漆线本身即线，粗细随速度与高度变化。质感：漆面光亮、层层叠加，画布纹理与漆滴并存。

## (4) 构图习惯

- 画幅：大幅横幅为主（《秋韵》近 2.7×5.3 米）；视点：俯视画布（画在地上）；布局：满幅（all-over），无中心、无上下、无边缘；线网铺满每一寸。裁切：画面即切片，线网出画。

## (5) 光影与透视

- 光源：无光源、无阴影；明暗只来自漆线的颜色与密度。透视：无透视，平面即全部。

## (6) 该画什么 / 不该画什么

- 该画：线网、数字编号（不命名，只编号）、大尺幅。
- 不该画：见下 Negative prompt。
- Negative prompt: `no recognisable object, no centre, no single-point perspective, no brushstrokes touching canvas, no empty background, no smooth blending`

## (7) 测试提示词示例（现代题材：一辆停在街边的共享单车）

- Prompt: `In the style of Jackson Pollock, a shared bicycle parked on a city street, Abstract Expressionist drip painting, enamel paint poured and flung onto unstretched canvas on the floor, all-over web of black white yellow and brown lines, no centre, no object, pure action`
- 中文对照：波洛克风格，一辆停在街边的共享单车，抽象表现主义滴洒画，珐琅漆泼洒于铺在地面的无框画布，黑白黄棕线网满幅，无中心、无物象，纯粹的行动。
- Negative: 见第 (6) 节。
- 检验点：题材是否被波洛克的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
