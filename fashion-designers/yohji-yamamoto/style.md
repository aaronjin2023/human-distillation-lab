# Yohji Yamamoto — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yohji Yamamoto, black deconstruction, oversized asymmetric silhouette, draped layers, unfinished seams, poetic imperfection, anti-fashion elegance`
- ZH: 山本耀司风格：黑色解构，超大不对称廓形，垂坠层次，未完成接缝，诗意的不完美，反时装的优雅。

## (2) 廓形方向

主廓形 3 种：一是超大不对称廓形——落肩、宽身、衣片错位；二是垂坠层次廓形——多层长款叠加；三是解构西装廓形，肩线松垮、长度拉长。`artifact`
- 比例：上长下长、等分偏长，视觉落点在不对称的垂线上而非腰线；裙长多及踝，裤长宽松盖鞋面。`impression`

## (3) 面料与色彩

面料：主面料为黑色羊毛、棉、真丝、亚麻，配做旧与磨损处理；织法重垂感与哑光，厚度中—厚。`artifact`
- 色彩：主色为黑，辅色为白、灰、米，偶见暗红点缀；禁艳色大面积平铺与印花。冷暖偏冷，饱和度极低，明暗对比靠黑的层次。`impression`

## (4) 剪裁与结构

剪裁：解构剪裁——接缝外露、不对称衣片、未完成感；立裁与平裁并用，省道取消或移位。`artifact`
- 结构：多层叠加，内衬轻软或无；开衩与系带不对称；穿脱宽松，身体活动度极高。`impression`

## (5) 细节与配饰

细节：领以无领、翻领错位为主；袖为超长袖、落肩袖；扣多用隐藏式与不对称扣；未完成接缝与毛边是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——宽檐帽、长围巾、厚底鞋；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：黑色解构廓形、超大不对称剪裁、垂坠层次叠加、未完成接缝与毛边、黑白灰米的极低饱和色盘、诗意的不完美。`verbatim` / `artifact`
- 不该设计：合体收腰、艳色大面积印花、对称完美的剪裁、繁复装饰、性感裸露。
- Negative prompt: `No body-con fit, no bright all-over print, no symmetrical perfect tailoring, no heavy ornament, no sexy revealing cut`

## (7) 测试提示词示例（现代题材：深夜拉面店店主的围裙套装）

- Prompt: `In the style of Yohji Yamamoto, a late-night ramen shop owner apron outfit, black deconstruction, oversized asymmetric silhouette, draped layers, unfinished seams, poetic imperfection`
- 中文对照：山本耀司风格：深夜拉面店店主的围裙套装，黑色解构，超大不对称廓形，垂坠层次，未完成接缝，诗意的不完美。
- Negative: `No body-con fit, no bright all-over print, no symmetrical perfect tailoring, no heavy ornament, no sexy revealing cut`
- 检验点：黑色层次是否丰富而不是死黑一片；不对称是否成立而不是凌乱；未完成感是否克制而不是破烂。
