# Wassily Kandinsky — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wassily Kandinsky, abstract oil painting, musical composition of colour, free floating biomorphic forms, black lines like notation, yellow red blue chords, no object, only vibration`
- ZH: 康定斯基风格，抽象油画，色彩的音乐构成，自由漂浮的有机形态，黑色线条如乐谱，黄红蓝和弦，无物象，只有振动。

## (2) 色板方向

- 主色（7 色，颜料名）：铬黄、朱红、钴蓝、黑色、白色、橙色、紫罗兰。`verbatim`
- 主色黄、红、蓝三原色和弦；高饱和、音乐性。禁：写实土色大面积、灰调、具象物象。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：自由、有机的曲线笔触，时而厚涂、时而薄涂；线条：黑色自由线如乐谱，粗细变化大，是画面的骨架。质感：油彩厚薄并置，无写实肌理。

## (4) 构图习惯

- 画幅：横幅大画为主（《构成VII》近 2×3 米）；视点：无视点、无地平线；布局：形与色漂浮于画面，无上下、无中心，靠色彩重量平衡；留白即白底本身。

## (5) 光影与透视

- 光源：无光源，光即色彩的振动；无阴影，形与形靠色彩对比分离。透视：无透视，空间即色彩的深浅关系。

## (6) 该画什么 / 不该画什么

- 该画：圆、三角、黑线、马、骑手、号角、山、洪水。
- 不该画：见下 Negative prompt。
- Negative prompt: `no recognisable object, no single-point perspective, no smooth academic shading, no grey muted palette, no photographic realism`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Wassily Kandinsky, a small Yorkshire terrier sitting on a subway seat, abstract oil painting, musical composition of colour, free floating biomorphic forms, black lines like notation, yellow red blue chords, no object, only vibration`
- 中文对照：康定斯基风格，一只坐在地铁里的约克夏犬，抽象油画，色彩的音乐构成，自由漂浮的有机形态，黑色线条如乐谱，黄红蓝和弦，无物象，只有振动。
- Negative: 见第 (6) 节。
- 检验点：题材是否被康定斯基的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
