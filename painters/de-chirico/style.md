# Giorgio de Chirico — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giorgio de Chirico, Metaphysical oil painting, empty Italian piazza, long shadows, classical arcade and tower, a small figure or statue, melancholic stillness, dreamlike clarity`
- ZH: 基里科风格，形而上绘画油画，空旷的意大利广场，长长的影子，古典拱廊与高塔，小小的人物或雕像，忧郁的寂静，梦般的清晰。

## (2) 色板方向

- 主色（7 色，颜料名）：暖金、赭石、土黄、深绿、冷蓝、白色、黑色。`verbatim`
- 主色暖金 + 赭石的意大利午后对冷蓝阴影；明亮但寂静。禁：高饱和情绪色、厚涂笔触、模糊梦境。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：平滑、均匀，几乎无笔触；线条：建筑轮廓线精确、锐利。质感：平面、光滑，如舞台布景。

## (4) 构图习惯

- 画幅：中小幅为主；视点：低地平线、一点透视但空间空旷；布局：广场占大半画面，拱廊一侧、高塔一角、人物极小；留白即空广场。裁切：建筑顶边出画，人物完整、孤立。

## (5) 光影与透视

- 光源：低角度的午后阳光，长影斜 across 广场；阴影清晰、冷蓝。透视：一点透视，但透视越正确、空间越空旷荒诞。

## (6) 该画什么 / 不该画什么

- 该画：意大利广场、拱廊、高塔、长影、雕像、人体模型、火车、旗。
- 不该画：见下 Negative prompt。
- Negative prompt: `no crowd, no visible brushstrokes, no thick impasto, no bright emotional colour, no blurred dreamy atmosphere`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Giorgio de Chirico, a cup of coffee on a windowsill, Metaphysical oil painting, empty Italian piazza, long shadows, classical arcade and tower, a small figure or statue, melancholic stillness, dreamlike clarity`
- 中文对照：基里科风格，一杯放在窗台上的咖啡，形而上绘画油画，空旷的意大利广场，长长的影子，古典拱廊与高塔，小小的人物或雕像，忧郁的寂静，梦般的清晰。
- Negative: 见第 (6) 节。
- 检验点：题材是否被基里科的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
