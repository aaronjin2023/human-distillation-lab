# Jean-François Millet — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Realism, monumental peasant figures, earthy golden palette, soft diffused light, smooth modelling, quiet dignity, timeless agrarian solemnity`
- ZH: 现实主义，纪念碑般的农民形象，土色金黄调，柔和散射光，平滑造型，寂静尊严，永恒的田园庄严。

## (2) 色板方向

- 主色（7 色，颜料名）：土黄、赭石、熟褐、金黄、墨绿、铅白、灰蓝。`verbatim`
- 主色是土黄 + 金黄的暖调，整体低饱和、高明度，亮在麦田与夕阳，暗部是褐与墨绿。`verbatim`
- 辅色：淡紫、暖灰、暗红。
- 禁色：粉彩甜腻；高饱和艳色；粗笔触；戏剧性动势。
- 冷暖：暖金为主，灰蓝与墨绿作冷点；冷暖对比柔和，靠明度分层。
- 明暗 / 饱和：中高明度、低饱和、中对比；亮部是麦田金黄，暗部是劳动者剪影。

## (3) 笔触与线条

- 笔触：平滑、柔和、几乎看不见笔触；多层薄涂，追求雕塑般的体积感。`verbatim`
- 线条：轮廓线柔和、清晰，劳动者剪影线是画面的骨架；无硬线勾边。
- 质感：光滑薄涂，无厚涂；麦田质感靠淡色碎笔点染，不靠刀痕。

## (4) 构图习惯

- 画幅：横幅与竖幅并存；《拾穗者》1857 年，横幅，三位拾穗妇女弯腰横排；《晚钟》1857–1859 年，竖幅，夫妇低头祈祷。
- 视点：平视略低，观者站在田野边、与劳动者同高；视线被弯腰姿态牵着望向地面。
- 布局：横排 + 金字塔：拾穗者三人弯腰横排，晚钟夫妇成金字塔；地平线低，天空与麦田占主导。
- 裁切：劳动者常顶边，麦田绵延出画边；不留安全边距。

## (5) 光影与透视

- 光源：散射的夕阳光，无固定光源；亮在麦田与天空，劳动者是暗剪影。
- 阴影：阴影是褐、墨绿的薄涂，透亮不死黑；劳动者剪影是全画最暗处。
- 透视：空气透视柔和：远景麦田淡、模糊，近景劳动者实；空间靠明度分层。

## (6) 该画什么 / 不该画什么

- 该画：拾穗、播种、晚钟祈祷、牧羊、田野劳动者。`verbatim`
- 不该画：美化；粉彩；粗笔触；戏剧性动势；城市题材。
- Negative prompt: `beautified idealisation, rococo pastel, visible rough brushstrokes, dramatic action, urban subject, high-saturation colour`

## (7) 测试提示词示例（现代题材：清晨菜市场）

- Prompt: `In the style of Jean-Francois Millet, a morning vegetable market in a modern city at dawn, Realism, monumental figures, earthy golden palette, soft diffused light, smooth modelling, quiet dignity, timeless solemnity`
- 中文对照：米勒风格，黎明时现代城市里一个清晨菜市场，现实主义，纪念碑般的人物，土色金黄调，柔和散射光，平滑造型，寂静尊严，永恒庄严。
- Negative: 见第 (6) 节。
- 检验点：菜贩是否画成纪念碑般的弯腰剪影、光是否柔和金黄，而不是轻快的印象派小品；色调是否土色庄严。
