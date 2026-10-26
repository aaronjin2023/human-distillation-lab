# Henri Matisse — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henri Matisse, Fauvist oil painting, large flat areas of pure vivid colour, vermilion red, cobalt blue and emerald green, simplified contour lines, joyful rhythmic figures, space flattened into colour`
- ZH: 马蒂斯风格，野兽派油画，大面积纯粹鲜艳的平涂色，朱红、钴蓝、翠绿，简化的轮廓线，欢快的韵律人物，空间被压平成色彩。

## (2) 色板方向

- 主色（7 色，颜料名）：朱红、钴蓝、翠绿、铬黄、橙色、紫罗兰、黑色轮廓。`verbatim`
- 主色朱红 + 钴蓝 + 翠绿，高饱和、非自然；冷暖对撞但整体明亮愉快。禁：灰暗土色、写实明暗渐变、黑色阴影。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：大面积平涂，笔触几乎不可见；晚期剪纸则无笔触、只有剪刀的边缘。线条：简化的黑色或深色轮廓线，粗细随形体走。质感：平涂、光滑，无厚涂堆积。

## (4) 构图习惯

- 画幅：横幅大画为主；视点平视；布局人物成环（《舞》五人环舞）、或室内一色统摄（《红色的画室》满幅红）；地平线低或消失；留白即色块本身。裁切：人物常顶边，环舞的手牵手出画又入画。

## (5) 光影与透视

- 光源：无固定光源，光即色彩本身；无写实阴影，阴影用另一块纯色代替。透视：扁平、无焦点透视，空间靠色块前后关系暗示。

## (6) 该画什么 / 不该画什么

- 该画：舞者、室内画室、金鱼、窗、女性人体、剪纸植物与人体。
- 不该画：见下 Negative prompt。
- Negative prompt: `no smooth academic shading, no grey muted palette, no photographic realism, no deep perspective, no detailed modelling`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Henri Matisse, a late-night ramen shop, Fauvist oil painting, large flat areas of pure vivid colour, vermilion red, cobalt blue and emerald green, simplified contour lines, joyful rhythmic figures, space flattened into colour`
- 中文对照：马蒂斯风格，深夜拉面店，野兽派油画，大面积纯粹鲜艳的平涂色，朱红、钴蓝、翠绿，简化的轮廓线，欢快的韵律人物，空间被压平成色彩。
- Negative: 见第 (6) 节。
- 检验点：题材是否被马蒂斯的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
