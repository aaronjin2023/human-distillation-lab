# Gustave Courbet — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Realism, heavy palette-knife paint, earthy muted palette, monumental scale for ordinary people, blunt unflattering truth, thick material surface`
- ZH: 现实主义，厚重的调色刀用色，土色克制色调，普通人画成纪念碑尺寸，直白不加美化，厚重的物质表面。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、熟褐、土黄、墨绿、铅白、墨黑、暗红。`verbatim`
- 主色是暗沉土色 + 铅白，整体低明度、低饱和，亮部是白衣与面部，暗部是褐与黑。`verbatim`
- 辅色：灰蓝、灰绿、暖灰。
- 禁色：粉彩甜腻；高饱和艳色；平滑学院渐变；美化修饰。
- 冷暖：暖土色为主，冷绿与灰蓝作点缀；冷暖对比弱，明暗对比强。
- 明暗 / 饱和：低明度、低饱和、高明暗对比；亮部直接用铅白厚涂，不经灰调过渡。

## (3) 笔触与线条

- 笔触：调色刀厚涂 + 笔刷并用；颜料堆积如泥，表面粗糙有物质感。`verbatim`
- 线条：轮廓线粗而实在，形靠厚涂块面收住；无精细勾线。
- 质感：厚涂堆积，调色刀痕迹清晰；表面如泥土与岩石，物质感是风格本体。

## (4) 构图习惯

- 画幅：大幅横幅为主；《奥尔南的葬礼》1849–1850 年，315×668cm，普通人葬礼画成历史画尺寸；《画室》1854–1855 年，同样大幅。
- 视点：平视，观者站在送葬队伍对面、与送葬者同高；无俯仰，视线横扫横排人物。
- 布局：横排浮雕式：送葬者横排站满画面，背景是奥尔南山崖；视线落点在棺材与神父。
- 裁切：人物常顶边、裁边，队伍绵延出画边；不留安全边距。

## (5) 光影与透视

- 光源：均匀的阴天光，无固定光源；亮在白衣与面部，暗部是黑衣送葬者。
- 阴影：阴影是褐、黑的厚涂，沉重不透明；明暗靠厚涂的起伏不靠渐变。
- 透视：浅空间，人物贴近画面；无焦点透视，空间靠人物前后错落。

## (6) 该画什么 / 不该画什么

- 该画：葬礼、采石工人、海浪与山崖、画室群像、普通劳动者。`verbatim`
- 不该画：美化；粉彩；平滑渐变；神话与历史英雄；艳色。
- Negative prompt: `beautified idealisation, rococo pastel, smooth academic blending, mythological heroes, high-saturation colour, photorealistic polish`

## (7) 测试提示词示例（现代题材：清晨菜市场）

- Prompt: `In the style of Gustave Courbet, a morning vegetable market in a modern city, Realism, heavy palette-knife paint, earthy muted palette, monumental ordinary people, blunt unflattering truth, thick material surface`
- 中文对照：库尔贝风格，现代城市里一个清晨菜市场，现实主义，厚重调色刀用色，土色克制色调，普通人画成纪念碑尺寸，直白不加美化，厚重物质表面。
- Negative: 见第 (6) 节。
- 检验点：菜贩与顾客是否画成纪念碑尺寸、是否厚涂如泥，而不是轻快的印象派小品；色调是否土色沉重。
