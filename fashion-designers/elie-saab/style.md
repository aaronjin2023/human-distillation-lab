# Elie Saab — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Elie Saab, romantic Lebanese haute couture, embroidered evening gown, feminine silhouette, nude and pastel palette, silk and lace, dreamy glamour`
- ZH: 艾莉·萨博风格：浪漫黎巴嫩高级定制，刺绣晚礼服，女性化廓形，裸色与粉彩色盘，真丝与蕾丝，梦幻华丽。

## (2) 廓形方向

主廓形 2 种：一是女性化晚礼服廓形——收腰、蓬裙、拖尾；二是修身礼服廓形，配柔和肩线。`artifact`
- 比例：上身合体、下身流动，视觉落点在刺绣与裙摆而非腰线；裙长多拖地。`impression`

## (3) 面料与色彩

面料：主面料为真丝、雪纺、蕾丝、欧根纱，配刺绣与钉珠；织法重轻薄与透感，厚度薄—中。`artifact`
- 色彩：主色为裸色、粉、米白、香槟，辅色为红、蓝点缀；禁大面积黑与艳色撞色。冷暖偏暖，饱和度中—低。`impression`

## (4) 剪裁与结构

剪裁：高级定制剪裁——立裁为主，平裁为辅；省道保留，靠收腰与蓬裙立形。`artifact`
- 结构：多层薄纱叠加，内衬轻软；穿脱靠侧拉链，身体活动度中。`impression`

## (5) 细节与配饰

细节：领以无领、圆领、翻领为主；袖为无袖、长袖、披肩袖；扣多用隐藏式；刺绣与钉珠是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——晚宴包、头饰；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：刺绣晚礼服、女性化廓形、真丝与蕾丝、裸色粉彩色盘、收腰与蓬裙、梦幻华丽。`verbatim` / `artifact`
- 不该设计：大面积黑、艳色大面积撞色、硬挺建筑廓形、解构破洞、街头元素。
- Negative prompt: `No heavy black, no bright clashing colours, no stiff architectural silhouette, no deconstructed holes, no street elements`

## (7) 测试提示词示例（现代题材：深夜拉面店店主的围裙套装）

- Prompt: `In the style of Elie Saab, a late-night ramen shop owner apron outfit, romantic haute couture, embroidered silhouette, feminine shape, nude and pastel palette, silk and lace`
- 中文对照：艾莉·萨博风格：深夜拉面店店主的围裙套装，浪漫高级定制，刺绣廓形，女性化造型，裸色与粉彩色盘，真丝与蕾丝。
- Negative: `No heavy black, no bright clashing colours, no stiff architectural silhouette, no deconstructed holes, no street elements`
- 检验点：刺绣是否梦幻而不是俗艳；廓形是否女性化而不是束缚；色彩是否柔和而不是平淡。
