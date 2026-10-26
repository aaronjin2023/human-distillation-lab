# Egon Schiele — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Egon Schiele, Expressionist oil and watercolour on paper, sharp angular contour lines, emaciated twisted bodies, raw ochre and pale flesh against empty background, nervous erotic tension`
- ZH: 席勒风格，表现主义油彩与水彩画于纸，锐利的角形轮廓线，瘦削扭曲的身体，粗糙赭石与苍白肤色对空背景，神经质的张力。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、苍白肤色、土黄、深褐、暗红、墨黑、灰绿。`verbatim`
- 主色苍白肤色 + 赭石、土黄；低饱和、近乎素描的用色。禁：明亮高饱和大面积、平滑写实肤色、装饰性金色。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：水彩薄涂 + 油彩干擦，笔触短促、干涩；线条是本体——粗细不均、断续、颤抖的轮廓线，形体靠线不靠明暗。质感：纸面干、涩，无厚涂。

## (4) 构图习惯

- 画幅：竖幅肖像为主；视点平视、近距离；布局人物占满画面、常顶边裁切，背景全空；身体扭曲成角形，关节处折断式转折。裁切：手足常被画幅切断。

## (5) 光影与透视

- 光源：无固定光源，无写实明暗；体积靠轮廓线与局部赭石晕染，不靠渐变。透视：无透视，人物贴在平面上，背景无空间。

## (6) 该画什么 / 不该画什么

- 该画：自画像、瓦莉肖像、扭曲裸体、母子、风景中的枯树。
- 不该画：见下 Negative prompt。
- Negative prompt: `no smooth academic shading, no bright cheerful palette, no photographic realism, no decorative gold, no calm balanced pose`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Egon Schiele, a cup of coffee on a windowsill, Expressionist oil and watercolour on paper, sharp angular contour lines, emaciated twisted bodies, raw ochre and pale flesh against empty background, nervous erotic tension`
- 中文对照：席勒风格，一杯放在窗台上的咖啡，表现主义油彩与水彩画于纸，锐利的角形轮廓线，瘦削扭曲的身体，粗糙赭石与苍白肤色对空背景，神经质的张力。
- Negative: 见第 (6) 节。
- 检验点：题材是否被席勒的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
