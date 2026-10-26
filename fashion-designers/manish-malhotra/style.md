# Manish Malhotra — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Manish Malhotra, glamorous Bollywood couture, embroidered sari and lehenga, rich jewel palette, silk and chiffon, cinematic drama`
- ZH: 马尼什·马尔霍特拉风格：华丽宝莱坞高级定制，刺绣纱丽与裙装，宝石色盘，真丝与雪纺，电影式戏剧。

## (2) 廓形方向

主廓形 2 种：一是刺绣纱丽廓形——垂坠、层叠、拖尾；二是宝莱坞礼服廓形——收腰、蓬裙、拖尾。`artifact`
- 比例：上身合体、下身流动，视觉落点在刺绣与垂坠而非腰线；裙长多拖地。`impression`

## (3) 面料与色彩

面料：主面料为真丝、雪纺、欧根纱，配刺绣与亮片；织法重轻薄与闪耀，厚度薄—中。`artifact`
- 色彩：主色为红、金、粉、蓝、绿等宝石色，辅色为米白打底；禁大面积黑与低饱和灰调。冷暖偏暖，饱和度高，明暗对比强。`impression`

## (4) 剪裁与结构

剪裁：宝莱坞剪裁——立裁为主，平裁为辅；省道保留，靠收腰与垂坠立形。`artifact`
- 结构：多层薄纱叠加，内衬轻软；穿脱靠系带与拉链，身体活动度中。`impression`

## (5) 细节与配饰

细节：领以无领、圆领、露肩为主；袖为无袖、长袖、披肩袖；扣多用隐藏式；刺绣与亮片是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——刺绣披肩、头饰；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：刺绣纱丽与裙装、宝莱坞礼服、宝石色盘、真丝与雪纺、垂坠与拖尾、电影式戏剧。`verbatim` / `artifact`
- 不该设计：大面积黑、低饱和灰调、硬挺建筑廓形、解构破洞、极简克制。
- Negative prompt: `No heavy black, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no restrained minimalism`

## (7) 测试提示词示例（现代题材：深夜便利店夜班店员的制服）

- Prompt: `In the style of Manish Malhotra, a late-night convenience store clerk uniform, glamorous Bollywood couture, embroidered silhouette, rich jewel palette, silk and chiffon, cinematic drama`
- 中文对照：马尼什·马尔霍特拉风格：深夜便利店夜班店员的制服，华丽宝莱坞高级定制，刺绣廓形，宝石色盘，真丝与雪纺，电影式戏剧。
- Negative: `No heavy black, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no restrained minimalism`
- 检验点：刺绣是否电影式而不是俗艳；纱丽垂坠是否成立而不是拖沓；宝石色是否浓郁而不是刺眼。
