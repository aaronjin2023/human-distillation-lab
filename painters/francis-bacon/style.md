# Francis Bacon — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francis Bacon, London School oil painting, distorted screaming figure caged in a glass box, raw pink flesh against black void, smeared brushstrokes, meat and mouth, existential flesh`
- ZH: 培根风格，伦敦画派油画，扭曲的尖叫人物困于玻璃盒，生的粉红肉体对黑色虚空，涂抹的笔触，肉与口，存在主义的肉体。

## (2) 色板方向

- 主色（7 色，颜料名）：粉红肉色、黑色、白色、紫色、橙色、深红、灰色。`verbatim`
- 主色粉红肉色 + 黑虚空 + 白；肉色是 bruised 的粉、紫、橙。禁：愉快亮色、平滑写实肤色、完整优美身体。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：涂抹、刮擦、拖曳，笔触粗暴、可见；线条：轮廓线被涂抹破坏，形体边缘融化。质感：油彩厚薄并置，肉色厚涂、背景薄涂。

## (4) 构图习惯

- 画幅：竖幅三联画与单幅为主；视点平视、近距离；布局：人物困于玻璃盒或几何框，居中、孤立，背景全黑或空；三联画三幅并置。裁切：人物常顶边，盒框切断空间。

## (5) 光影与透视

- 光源：无固定光源，光来自肉色的亮；阴影是黑虚空本身。透视：盒框有透视，但人物无透视，空间被盒子压扁。

## (6) 该画什么 / 不该画什么

- 该画：教皇、尖叫的口、肉、玻璃盒、三联画、自画像。
- 不该画：见下 Negative prompt。
- Negative prompt: `no smooth academic shading, no bright cheerful palette, no photographic realism, no complete beautiful body, no calm balanced pose`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Francis Bacon, a small Yorkshire terrier sitting on a subway seat, London School oil painting, distorted screaming figure caged in a glass box, raw pink flesh against black void, smeared brushstrokes, meat and mouth, existential flesh`
- 中文对照：培根风格，一只坐在地铁里的约克夏犬，伦敦画派油画，扭曲的尖叫人物困于玻璃盒，生的粉红肉体对黑色虚空，涂抹的笔触，肉与口，存在主义的肉体。
- Negative: 见第 (6) 节。
- 检验点：题材是否被培根的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
