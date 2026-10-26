# Piet Mondrian — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Piet Mondrian, Neo-Plastic abstract painting, white ground, black horizontal and vertical lines, rectangles of primary red yellow blue, no diagonal, no curve, perfect balance`
- ZH: 蒙德里安风格，新造型主义抽象画，白底，黑色横竖直线，原色红黄蓝矩形，无斜线、无曲线，绝对平衡。

## (2) 色板方向

- 主色（6 色，颜料名）：原色红、原色黄、原色蓝、黑色、白色、浅灰。`verbatim`
- 主色仅红、黄、蓝三原色 + 黑白灰；色块平涂、绝不混色。禁：一切间色、渐变、曲线、斜线。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：平涂，无笔触痕迹，颜料薄而均匀；线条：黑色横竖直线，粗细均匀，是画面的骨架；边缘用胶带般的直线。质感：平面、光滑、无肌理。

## (4) 构图习惯

- 画幅：方形与竖幅为主；视点：无视点；布局：黑线把白底切成大小不等的矩形，色块只占少数格子，多数留白；不对称但平衡。裁切：黑线常出画，画面是更大网格的切片。

## (5) 光影与透视

- 光源：无光源、无阴影；明暗只来自色块本身的明度。透视：无透视，绝对平面。

## (6) 该画什么 / 不该画什么

- 该画：网格、原色矩形、树（早期）、百老汇网格（晚期）。
- 不该画：见下 Negative prompt。
- Negative prompt: `no diagonal, no curve, no gradient, no muted mixed colour, no recognisable object`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Piet Mondrian, a cup of coffee on a windowsill, Neo-Plastic abstract painting, white ground, black horizontal and vertical lines, rectangles of primary red yellow blue, no diagonal, no curve, perfect balance`
- 中文对照：蒙德里安风格，一杯放在窗台上的咖啡，新造型主义抽象画，白底，黑色横竖直线，原色红黄蓝矩形，无斜线、无曲线，绝对平衡。
- Negative: 见第 (6) 节。
- 检验点：题材是否被蒙德里安的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
