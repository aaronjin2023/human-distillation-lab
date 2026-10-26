# Hanae Mori — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hanae Mori, elegant haute couture, butterfly print, kimono-inspired gown, soft draping, refined colour, East meets West`
- ZH: 森英惠风格：优雅高级定制，蝴蝶印花，和服式礼服，柔软垂坠，精致色彩，东西合璧。

## (2) 廓形方向

主廓形 2 种：一是和服式礼服廓形——直线剪裁、宽袖、腰带式收束，东方直线与西方立体并置；二是柔软垂坠的 A 形晚礼服，肩线柔和、裙摆流动。`artifact`
- 比例：上身直线、下身流动，视觉落点在腰带与裙摆的垂线上。`impression`

## (3) 面料与色彩

面料：主面料为真丝、雪纺、乔其纱、欧根纱，配刺绣与印花；织法重轻薄与垂感，厚度薄。`artifact`
- 色彩：主色为粉、紫、蓝、米白等柔和色，辅色为金、银点缀；禁大面积浓黑与高对比撞色。冷暖偏暖，饱和度中—低。`impression`

## (4) 剪裁与结构

剪裁：平裁与立裁并用；和服式直线剪裁作骨架，西方立裁作合体；省道少，靠腰带与垂坠立形。`artifact`
- 结构：单层为主，多层薄纱叠加；内衬轻软；穿脱靠腰带与侧拉链，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以和服式交领、翻领为主；袖为宽袖、和服袖；扣多用隐藏式与系带；蝴蝶印花与刺绣是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——丝巾、腰带、小手袋；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：蝴蝶印花与刺绣、和服式礼服廓形、真丝与雪纺的柔软垂坠、粉紫蓝米白的柔和色盘、宽袖与腰带式收束、东西合璧的优雅。`verbatim` / `artifact`
- 不该设计：浓黑大面积、高对比撞色、硬挺建筑廓形、解构破洞、街头元素。
- Negative prompt: `No heavy black, no high-contrast clash, no stiff architectural silhouette, no deconstructed holes, no street elements`

## (7) 测试提示词示例（现代题材：植物园讲解员的制服）

- Prompt: `In the style of Hanae Mori, a botanical garden guide uniform, elegant haute couture, butterfly print, kimono-inspired silhouette, soft draping, refined colour`
- 中文对照：森英惠风格：植物园讲解员的制服，优雅高级定制，蝴蝶印花，和服式廓形，柔软垂坠，精致色彩。
- Negative: `No heavy black, no high-contrast clash, no stiff architectural silhouette, no deconstructed holes, no street elements`
- 检验点：蝴蝶印花是否精致而不是俗艳；和服式廓形是否成立；色彩是否柔和而不是浓烈。
