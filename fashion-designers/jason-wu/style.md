# Jason Wu — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jason Wu, refined American couture, elegant evening gown, feminine tailoring, muted luxe palette, silk and lace, quiet glamour`
- ZH: 吴季刚风格：精致美式高级定制，优雅晚礼服，女性化剪裁，低调奢华色盘，真丝与蕾丝，安静的华丽。

## (2) 廓形方向

主廓形 2 种：一是女性化晚礼服廓形——收腰、蓬裙、拖尾；二是修身套装廓形，配柔和肩线。`artifact`
- 比例：上身合体、下身流动，视觉落点在腰线与裙摆而非装饰；裙长多及踝，裤长修身。`impression`

## (3) 面料与色彩

面料：主面料为真丝、雪纺、蕾丝、欧根纱，配刺绣；织法重轻薄与垂感，厚度薄—中。`artifact`
- 色彩：主色为米白、粉、灰、黑，辅色为红、蓝点缀；禁艳色大面积撞色。冷暖偏暖，饱和度中—低。`impression`

## (4) 剪裁与结构

剪裁：女性化剪裁——立裁为主，平裁为辅；省道保留，靠收腰与蓬裙立形。`artifact`
- 结构：单层与多层并存，内衬轻软；穿脱靠侧拉链，身体活动度中。`impression`

## (5) 细节与配饰

细节：领以圆领、翻领、无领为主；袖为短袖、无袖、长袖；扣多用隐藏式；蕾丝与刺绣是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——晚宴包、细腰带；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：优雅晚礼服、女性化剪裁、真丝与蕾丝、米白粉灰黑的低调色盘、收腰与蓬裙、安静的华丽。`verbatim` / `artifact`
- 不该设计：艳色大面积撞色、繁复装饰、硬挺建筑廓形、解构破洞、街头元素。
- Negative prompt: `No bright clashing colours, no heavy ornament, no stiff architectural silhouette, no deconstructed holes, no street elements`

## (7) 测试提示词示例（现代题材：图书馆管理员的工作装）

- Prompt: `In the style of Jason Wu, a librarian work outfit in a modern city library, refined American couture, elegant silhouette, feminine tailoring, muted luxe palette, silk and lace`
- 中文对照：吴季刚风格：现代城市图书馆管理员的工作装，精致美式高级定制，优雅廓形，女性化剪裁，低调奢华色盘，真丝与蕾丝。
- Negative: `No bright clashing colours, no heavy ornament, no stiff architectural silhouette, no deconstructed holes, no street elements`
- 检验点：廓形是否优雅而不是刻板；蕾丝是否精致而不是俗艳；色彩是否低调奢华而不是平淡。
