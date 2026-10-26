# Zuhair Murad — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zuhair Murad, glamorous Lebanese haute couture, sequinned evening gown, sculpted feminine silhouette, rich jewel palette, silk and tulle, red-carpet drama`
- ZH: 祖海·慕拉德风格：华丽黎巴嫩高级定制，亮片晚礼服，雕塑式女性廓形，宝石色盘，真丝与薄纱，红毯戏剧。

## (2) 廓形方向

主廓形 2 种：一是雕塑式女性廓形——收腰、贴身、拖尾；二是蓬裙晚礼服廓形，裙摆宏大。`artifact`
- 比例：上身贴身、下身流动，视觉落点在亮片与裙摆而非腰线；裙长多拖地。`impression`

## (3) 面料与色彩

面料：主面料为真丝、薄纱、蕾丝，配亮片与刺绣；织法重闪耀与透感，厚度薄—中。`artifact`
- 色彩：主色为红、蓝、绿、金等宝石色，辅色为裸色打底；禁大面积黑与低饱和灰调。冷暖偏暖，饱和度高，明暗对比强。`impression`

## (4) 剪裁与结构

剪裁：高级定制剪裁——立裁为主，平裁为辅；省道保留，靠贴身与蓬裙立形。`artifact`
- 结构：多层薄纱叠加，内衬贴身；穿脱靠侧拉链，身体活动度低（礼服）。`impression`

## (5) 细节与配饰

细节：领以无领、深 V、露肩为主；袖为无袖、长袖、披肩袖；扣多用隐藏式；亮片与刺绣是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——晚宴包、头饰；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：亮片晚礼服、雕塑式女性廓形、宝石色盘、真丝与薄纱、贴身收腰与拖尾、红毯戏剧。`verbatim` / `artifact`
- 不该设计：大面积黑、低饱和灰调、硬挺建筑廓形、解构破洞、极简克制。
- Negative prompt: `No heavy black, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no restrained minimalism`

## (7) 测试提示词示例（现代题材：城市快递员的雨天工作服）

- Prompt: `In the style of Zuhair Murad, a city courier rain outfit, glamorous haute couture, sequinned silhouette, sculpted feminine shape, rich jewel palette, silk and tulle`
- 中文对照：祖海·慕拉德风格：城市快递员的雨天工作服，华丽高级定制，亮片廓形，雕塑式女性造型，宝石色盘，真丝与薄纱。
- Negative: `No heavy black, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no restrained minimalism`
- 检验点：亮片是否华丽而不是俗艳；廓形是否雕塑而不是束缚；宝石色是否浓郁而不是刺眼。
