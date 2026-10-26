# Joan Miró — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joan Miró, Surrealist oil painting, playful biomorphic signs on a flat ground, black lines, red yellow blue dots, stars and moons, childlike freedom, automatic drawing`
- ZH: 米罗风格，超现实主义油画，平面底色上俏皮的有机符号，黑线、红黄蓝圆点、星与月，孩童般的自由，自动性绘画。

## (2) 色板方向

- 主色（7 色，颜料名）：天蓝、朱红、铬黄、黑色、白色、绿色、橙色。`verbatim`
- 主色红、黄、蓝三原色点 + 黑线，白或蓝底；明亮、俏皮。禁：灰暗土色、写实明暗、具象写实。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：自由、轻快的线与点，笔触轻而不厚；线条：黑色自由线，粗细变化，是画面的骨架。质感：薄涂、平面，无厚涂。

## (4) 构图习惯

- 画幅：中小幅为主，《星座系列》为小幅组画；视点：无视点；布局：符号漂浮于底色，无上下、无中心，疏密有致；留白即底色本身。裁切：符号常出画，画面是更大星空的切片。

## (5) 光影与透视

- 光源：无光源、无阴影；明暗只来自色点的明度。透视：无透视，绝对平面。

## (6) 该画什么 / 不该画什么

- 该画：星、月、鸟、女人、眼、小丑、梯子。
- 不该画：见下 Negative prompt。
- Negative prompt: `no recognisable realistic object, no single-point perspective, no smooth academic shading, no grey muted palette, no thick impasto`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Joan Miró, a small Yorkshire terrier sitting on a subway seat, Surrealist oil painting, playful biomorphic signs on a flat ground, black lines, red yellow blue dots, stars and moons, childlike freedom, automatic drawing`
- 中文对照：米罗风格，一只坐在地铁里的约克夏犬，超现实主义油画，平面底色上俏皮的有机符号，黑线、红黄蓝圆点、星与月，孩童般的自由，自动性绘画。
- Negative: 见第 (6) 节。
- 检验点：题材是否被米罗的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
