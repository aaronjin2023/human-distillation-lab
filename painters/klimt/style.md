# Gustav Klimt — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gustav Klimt, Symbolist oil painting with gold leaf, flat ornamental mosaic patterns, geometric rectangles for the male figure and circular floral motifs for the female, sensual figures dissolving into decoration`
- ZH: 克里姆特风格，象征主义油画加金箔，平面装饰性马赛克图案，男性矩形几何纹、女性圆形花纹，感性人物融化进装饰之中。

## (2) 色板方向

- 主色（7 色，颜料名）：金箔金、银箔银、深红、墨绿、群青、赭石、象牙白。`verbatim`
- 主色金箔 + 深红、墨绿、群青；金是画面本体而非点缀。禁：灰暗土色大面积平涂、写实明暗渐变。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：人物皮肤细腻平滑近乎无笔触，衣袍与背景是精细描绘的几何与花卉纹样；线条纤细、装饰性强，轮廓以金色纹样收边。质感：金箔与银箔的金属光泽 + 油彩平涂，局部有浮雕般的厚涂纹样。

## (4) 构图习惯

- 画幅：方形大画为主（《吻》180×180cm）；视点平视；布局中心对称、人物居中、上下以金色花毯与纹样填满；无地平线，背景即装饰平面；裁切：人物不顶边，下方花毯承托。

## (5) 光影与透视

- 光源：无固定写实光源，光来自金箔本身的反光；明暗对比弱，靠金与暗色的面积对比；阴影不用纯黑，用深绿、深红的平涂。透视：扁平、无焦点透视，空间被装饰平面压平。

## (6) 该画什么 / 不该画什么

- 该画：拥抱的恋人、女性肖像、朱迪思、达那厄、生命之树、三世代女性。
- 不该画：见下 Negative prompt。
- Negative prompt: `no photographic realism, no smooth academic shading, no grey muted palette, no deep perspective, no empty plain background`

## (7) 测试提示词示例（现代题材：现代城市街角的便利店夜景）

- Prompt: `In the style of Gustav Klimt, a small convenience store at night in a modern city, Symbolist oil painting with gold leaf, flat ornamental mosaic patterns, geometric rectangles for the male figure and circular floral motifs for the female, sensual figures dissolving into decoration`
- 中文对照：克里姆特风格，现代城市街角的便利店夜景，象征主义油画加金箔，平面装饰性马赛克图案，男性矩形几何纹、女性圆形花纹，感性人物融化进装饰之中。
- Negative: 见第 (6) 节。
- 检验点：题材是否被克里姆特的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
