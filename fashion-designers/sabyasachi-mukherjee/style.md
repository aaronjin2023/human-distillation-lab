# Sabyasachi Mukherjee — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sabyasachi Mukherjee, vintage Indian bridal couture, embroidered lehenga and sari, muted jewel palette, silk and velvet, heritage opulence`
- ZH: 萨比亚萨奇·穆克吉风格：复古印度婚纱高级定制，刺绣裙装与纱丽，低调宝石色盘，真丝与丝绒，传承的华丽。

## (2) 廓形方向

主廓形 2 种：一是刺绣裙装廓形——收腰、蓬裙、拖尾；二是纱丽廓形——垂坠、层叠、拖尾。`artifact`
- 比例：上身合体、下身流动，视觉落点在刺绣与垂坠而非腰线；裙长多拖地。`impression`

## (3) 面料与色彩

面料：主面料为真丝、丝绒、欧根纱，配刺绣与金线；织法重厚重与光泽，厚度中—厚。`artifact`
- 色彩：主色为红、酒红、金、墨绿等低调宝石色，辅色为米白打底；禁艳色大面积撞色与低饱和灰调。冷暖偏暖，饱和度中—高。`impression`

## (4) 剪裁与结构

剪裁：复古印度剪裁——立裁为主，平裁为辅；省道保留，靠收腰与垂坠立形。`artifact`
- 结构：多层叠加，内衬厚重；穿脱靠系带与拉链，身体活动度中。`impression`

## (5) 细节与配饰

细节：领以无领、圆领为主；袖为无袖、长袖、披肩袖；扣多用隐藏式；刺绣与金线是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——刺绣披肩、头饰；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：刺绣裙装与纱丽、复古印度、低调宝石色盘、真丝与丝绒、垂坠与拖尾、传承的华丽。`verbatim` / `artifact`
- 不该设计：艳色大面积撞色、低饱和灰调、硬挺建筑廓形、解构破洞、街头元素。
- Negative prompt: `No bright clashing colours, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no street elements`

## (7) 测试提示词示例（现代题材：城市快递员的雨天工作服）

- Prompt: `In the style of Sabyasachi Mukherjee, a city courier rain outfit, vintage Indian bridal couture, embroidered silhouette, muted jewel palette, silk and velvet, heritage opulence`
- 中文对照：萨比亚萨奇·穆克吉风格：城市快递员的雨天工作服，复古印度婚纱高级定制，刺绣廓形，低调宝石色盘，真丝与丝绒，传承的华丽。
- Negative: `No bright clashing colours, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no street elements`
- 检验点：刺绣是否传承华丽而不是俗艳；复古是否克制而不是陈旧；宝石色是否低调而不是刺眼。
