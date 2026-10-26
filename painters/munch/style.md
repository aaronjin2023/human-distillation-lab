# Edvard Munch — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edvard Munch, Symbolist oil, tempera and pastel on unprimed cardboard, wavy rhythmic brushstrokes, blood-red and orange sky against cold blue-black fjord, distorted skeletal figure, anxiety made visible`
- ZH: 蒙克风格，象征主义油彩、蛋彩与粉彩画于无底卡纸，波浪形韵律笔触，血红橙黄天空对冷蓝黑峡湾，扭曲的骷髅般人物，焦虑变得可见。

## (2) 色板方向

- 主色（7 色，颜料名）：血红、橙黄、冷蓝、深黑、灰绿、土黄、苍白肤色。`verbatim`
- 主色血红 + 橙黄的天空对冷蓝黑的水与地；高对比、非自然。禁：明亮愉快的纯色大面积、平滑学院渐变。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：波浪形、流动的长笔触，天空、水面、人物轮廓同向弯曲；颜料薄涂，卡纸纹理可见；线条：人物轮廓线颤抖、断续，形体边缘融化进背景。质感：薄涂 + 粉彩干擦，无厚涂堆积。

## (4) 构图习惯

- 画幅：竖幅为主；视点：桥面斜切入画的强对角线，人物居前景中央偏右；布局：桥的直线对天空与水面的波浪线，直线锚住现实、波浪线表示动荡；地平线高，人物顶天。裁切：桥栏杆斜切出画，人物头部近画幅顶边。

## (5) 光影与透视

- 光源：无写实光源，红天空本身就是光源与情绪源；阴影用深蓝黑平涂，不用纯黑渐变。透视：桥的直线有透视收束，但天空与水面是平面波纹，透视只留一半、另一半被情绪压平。

## (6) 该画什么 / 不该画什么

- 该画：《生命的饰带》系列：呐喊、圣母、病孩、吻、吸血鬼（爱、焦虑、疾病、死亡）。
- 不该画：见下 Negative prompt。
- Negative prompt: `no smooth academic blending, no cheerful bright palette, no photographic realism, no calm naturalistic landscape`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Edvard Munch, a small Yorkshire terrier sitting on a subway seat, Symbolist oil, tempera and pastel on unprimed cardboard, wavy rhythmic brushstrokes, blood-red and orange sky against cold blue-black fjord, distorted skeletal figure, anxiety made visible`
- 中文对照：蒙克风格，一只坐在地铁里的约克夏犬，象征主义油彩、蛋彩与粉彩画于无底卡纸，波浪形韵律笔触，血红橙黄天空对冷蓝黑峡湾，扭曲的骷髅般人物，焦虑变得可见。
- Negative: 见第 (6) 节。
- 检验点：题材是否被蒙克的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
