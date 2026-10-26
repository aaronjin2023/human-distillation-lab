# El Greco (Doménikos Theotokópoulos) — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of El Greco, Mannerist to Baroque oil painting, elongated flame-like figures, cold acid colours, stormy sky, spiritual ecstasy, Toledo vision, oil on canvas`
- ZH: 埃尔·格列柯风格，矫饰主义—巴洛克过渡油画，拉长如火焰的人物，冷峻的酸性色彩，翻卷的天空，灵魂的狂喜，托莱多幻象，布面油画。

## (2) 色板方向

- 主色（7 色，颜料名）：冷绿、群青、朱红、铅白、土黄、暗褐、柠檬黄。`verbatim`
- 辅色：银灰（天空）、紫灰（阴影）。
- 禁色：写实的比例与解剖；暖金田园光线；优雅的理想人体；均匀漫射光。
- 冷暖：整体偏冷的酸绿与群青，朱红与柠檬黄作暖点；光是冷的、灵魂是热的。
- 明暗 / 饱和：高对比，亮部冷亮、暗部深冷；饱和度在冷绿与柠檬黄处高，整体冷峻。

## (3) 笔触与线条

- 笔触：自由、破碎，笔触如火焰般跳动；近看是色块、远看是形。`verbatim`
- 线条：轮廓线拉长、扭曲，身体的拉长靠轮廓线的张力表达。
- 质感：布面油画，颜料薄涂与厚涂并置；天空用宽笔扫出翻卷的云。

## (4) 构图习惯

- 画幅：祭坛画与风景皆有；《奥尔加斯伯爵的葬礼》为竖幅巨幅，上下两层。`verbatim`
- 视点：平视略仰；《奥尔加斯伯爵的葬礼》下层人间、上层天国，上下两界在同一画面上。
- 布局：上下分层构图——下层葬礼人群横向排列、写实沉稳，上层灵魂升天、人物拉长翻卷；《托莱多风景》城市横卧、星空翻卷。`verbatim`
- 裁切：人物常被画框边缘截断，营造近景感；天国部分无“边”，视线向上翻卷。

## (5) 光影与透视

- 光源：冷峻的光，光从画面外上方来，不暖；光是灵魂的光，不是日光。
- 阴影：深冷的阴影，体积靠冷绿与柠檬黄的对照，不靠暖色过渡。
- 透视：透视克制，空间靠上下分层与色彩的冷暖推远近；天空翻卷，空间如梦境。

## (6) 该画什么 / 不该画什么

- 该画：葬礼与升天、托莱多风景、拉长的人体、翻卷的天空。
- 不该画：写实的比例；暖金田园光线；优雅的理想人体；均匀漫射光。
- Negative prompt: `naturalistic proportions, warm golden pastoral light, idealised graceful figures, uniform diffused light, smooth academic blending, photorealistic detail`

## (7) 测试提示词示例（现代题材：雨夜的城市天际线）

- Prompt: `In the style of El Greco, a city skyline on a rainy night, Mannerist to Baroque oil painting, elongated flame-like buildings, cold acid colours, stormy sky, spiritual ecstasy, Toledo vision, oil on canvas`
- 中文对照：埃尔·格列柯风格，雨夜的城市天际线，矫饰主义—巴洛克过渡油画，拉长如火焰的建筑，冷峻的酸性色彩，翻卷的天空，灵魂的狂喜，托莱多幻象，布面油画。
- Negative: 见第 (6) 节。
- 检验点：建筑是否拉长如火焰；天空是否翻卷；色彩是否冷峻酸性而不是暖金。
