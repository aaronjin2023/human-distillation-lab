# Junya Watanabe — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Junya Watanabe, technical fabric, deconstructed denim, precise pattern-cutting, functional detail, muted palette, innovation as elegance`
- ZH: 渡边淳弥风格：技术面料，解构牛仔，精确打版，功能细节，低调色盘，创新即优雅。

## (2) 廓形方向

主廓形 2 种：一是解构牛仔廓形——牛仔衣片重组、接缝错位；二是技术面料廓形——防水、透气面料的直线与 A 形。`artifact`
- 比例：上身合体偏宽、下身直筒，视觉落点在面料与接缝而非腰线；长度多及膝，裤长直筒。`impression`

## (3) 面料与色彩

面料：主面料为技术面料（防水透气）、牛仔、棉、聚酯，配机能面料；织法重功能处理，厚度中。`artifact`
- 色彩：主色为牛仔蓝、黑、灰、卡其，辅色为白点缀；禁艳色大面积印花。冷暖偏冷，饱和度低—中。`impression`

## (4) 剪裁与结构

剪裁：精确打版——平裁为主，立裁为辅；解构手法为衣片重组与接缝错位，但版型精度极高。`artifact`
- 结构：单层与多层并存，机能口袋与拉链是结构的一部分；内衬轻薄；穿脱功能性强。`impression`

## (5) 细节与配饰

细节：领以翻领、立领为主；袖为直袖、机能袖；扣多用拉链与按扣；机能口袋与牛仔接缝是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——机能包、牛仔帽；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：技术面料与机能处理、解构牛仔重组、精确打版、机能口袋与拉链、牛仔蓝黑灰的低调色盘、创新即优雅。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、繁复装饰、合体收腰、柔软垂坠的薄纱、无功能的装饰。
- Negative prompt: `No bright all-over print, no heavy ornament, no body-con fit, no soft sheer drape, no non-functional decoration`

## (7) 测试提示词示例（现代题材：共享单车骑行者的通勤装）

- Prompt: `In the style of Junya Watanabe, a bike-sharing commuter outfit, technical fabric, deconstructed denim, precise pattern-cutting, functional detail, muted palette`
- 中文对照：渡边淳弥风格：共享单车骑行者的通勤装，技术面料，解构牛仔，精确打版，功能细节，低调色盘。
- Negative: `No bright all-over print, no heavy ornament, no body-con fit, no soft sheer drape, no non-functional decoration`
- 检验点：技术面料是否功能化而不是噱头；牛仔解构是否精确而不是凌乱；机能细节是否真实而不是装饰。
