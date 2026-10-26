# Jacques-Louis David — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Neoclassical oil painting, sharp sculptural outlines, smooth invisible brushwork, austere frieze-like composition, restrained palette, moral clarity, frozen heroic gesture`
- ZH: 新古典主义油画，锋利雕塑感轮廓，平滑无笔触，严整浮雕式构图，克制色调，道德清晰，凝固的英雄姿态。

## (2) 色板方向

- 主色（7 色，颜料名）：铅白、赭石、熟褐、群青、朱红、墨绿、暖灰。`verbatim`
- 主色克制：白、赭、褐、群青为主，朱红只给披风与血点；整体低饱和、高明度对比靠明暗不靠艳色。`verbatim`
- 辅色：淡黄、灰蓝、土黄。
- 禁色：洛可可粉彩；高饱和艳色铺满；可见的粗笔触；模糊雾调。
- 冷暖：冷调为主，暖色只作点缀（朱红披风、暖肤色）；冷暖对比弱，明暗对比强。
- 明暗 / 饱和：中明度、高明暗对比、低饱和；亮部平滑、暗部深沉但仍有形。

## (3) 笔触与线条

- 笔触：平滑、几乎看不见笔触；多层薄涂罩染打磨，追求大理石般的表面。`verbatim`
- 线条：轮廓线锋利、精确、连续，是画面的骨架；线条优先于色彩（与德拉克洛瓦对立）。
- 质感：光滑无肌理；肤色如抛光大理石，布料平整，几无厚涂。

## (4) 构图习惯

- 画幅：大幅横幅历史画为主；《荷拉斯兄弟之誓》1784 年，人物如浮雕横排；《马拉之死》1793 年，竖幅极简。
- 视点：平视，观者与人物同高；无俯仰，视线被迫直视道德场景。
- 布局：浮雕式横排：人物并列如浮雕，背景是浅色建筑 / 空白；《荷拉斯兄弟之誓》三兄弟左、父亲中、妇女右，三组分明。
- 裁切：人物不裁边，完整如雕塑；画面留白是建筑与空白墙面，不是雾。

## (5) 光影与透视

- 光源：单侧冷光，均匀照亮人物；无斑驳光，无氛围光。
- 阴影：阴影是暖灰、褐色的平滑渐变，有形有体积，不用纯黑死角。
- 透视：浅空间：人物贴近画面，背景建筑只作浅浮雕；焦点透视弱，空间靠人物前后错落。

## (6) 该画什么 / 不该画什么

- 该画：宣誓、牺牲、殉道、历史与神话题材、雕塑感人体、明确手势。`verbatim`
- 不该画：洛可可粉彩与轻笔；可见笔触；雾感；艳色铺满；戏剧性斜构图。
- Negative prompt: `rococo pastel, visible rough brushstrokes, hazy atmosphere, high-saturation colour, dramatic diagonal chaos, photorealistic texture`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Jacques-Louis David, shared bicycles parked in a neat row on a modern city street at dawn, Neoclassical oil painting, sharp sculptural outlines, smooth invisible brushwork, frieze-like composition, restrained palette, moral clarity`
- 中文对照：大卫风格，黎明时现代城市街道上一排整齐停放的共享单车，新古典主义油画，锋利雕塑感轮廓，平滑无笔触，浮雕式构图，克制色调，道德清晰。
- Negative: 见第 (6) 节。
- 检验点：单车是否排成“浮雕横排”、轮廓是否锋利如雕塑，而不是印象派碎笔；色调是否克制而不是艳丽。
