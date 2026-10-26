# Andy Warhol — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Andy Warhol, Pop Art silkscreen, repeated Campbell's soup cans and Marilyn faces, flat bright colour, registration errors, commercial image repeated until it becomes art`
- ZH: 沃霍尔风格，波普艺术丝网版画，重复的金宝汤罐头与玛丽莲面孔，扁平的亮色，套印错位，商业图像重复直至成艺术。

## (2) 色板方向

- 主色（7 色，颜料名）：亮红、亮黄、亮蓝、亮粉、黑色、白色、银色。`verbatim`
- 主色商业亮色 + 黑白；色彩不自然、任意填充。禁：手绘笔触、写实明暗、灰调、唯一原作感。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：无手绘笔触——丝网印刷的机械平涂；套印错位与漏印是画面的一部分。线条：印刷网点的边缘即线。质感：平面、光滑、商业印刷感。

## (4) 构图习惯

- 画幅：网格重复为主（32 罐汤、双联画）；视点：正面、平视；布局：同一图像重复排列，网格即构图；单幅亦居中、孤立。裁切：图像完整、重复出画。

## (5) 光影与透视

- 光源：无光源、无阴影；明暗只来自印刷色的明度。透视：无透视，绝对平面。

## (6) 该画什么 / 不该画什么

- 该画：金宝汤罐头、玛丽莲、可口可乐瓶、毛泽东、死亡与灾难系列。
- 不该画：见下 Negative prompt。
- Negative prompt: `no hand-painted brushstrokes, no smooth academic shading, no grey muted palette, no single unique original, no deep perspective`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Andy Warhol, a cup of coffee on a windowsill, Pop Art silkscreen, repeated Campbell's soup cans and Marilyn faces, flat bright colour, registration errors, commercial image repeated until it becomes art`
- 中文对照：沃霍尔风格，一杯放在窗台上的咖啡，波普艺术丝网版画，重复的金宝汤罐头与玛丽莲面孔，扁平的亮色，套印错位，商业图像重复直至成艺术。
- Negative: 见第 (6) 节。
- 检验点：题材是否被沃霍尔的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
