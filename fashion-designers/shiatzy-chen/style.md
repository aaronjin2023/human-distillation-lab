# Shiatzy Chen — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shiatzy Chen, new Chinese chic, qipao-inspired gown, exquisite embroidery, silk and brocade, restrained luxury, East as elegance`
- ZH: 夏姿·陈风格：新中式，旗袍式礼服，精致刺绣，真丝与织锦，克制的奢华，东方即优雅。

## (2) 廓形方向

主廓形 2 种：一是旗袍式礼服廓形——立领、收腰、开衩，东方直线与西方立体并置；二是 A 形礼服廓形，裙摆流动。`artifact`
- 比例：上身合体、下身流动，视觉落点在刺绣与开衩而非腰线；裙长多及踝。`impression`

## (3) 面料与色彩

面料：主面料为真丝、织锦、缎、欧根纱，配刺绣与钉珠；织法重厚重与光泽，厚度中—厚。`artifact`
- 色彩：主色为红、黑、金、米白，辅色为蓝、绿点缀；禁艳色大面积撞色与低饱和灰调。冷暖偏暖，饱和度中—高。`impression`

## (4) 剪裁与结构

剪裁：旗袍式剪裁——立领、收腰、开衩，平裁与立裁并用；省道保留，靠收腰与骨架立形。`artifact`
- 结构：单层与多层并存，内衬轻软；穿脱靠侧拉链与盘扣，身体活动度中。`impression`

## (5) 细节与配饰

细节：领以立领为主；袖为短袖、长袖、宽袖；扣多用盘扣；刺绣是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——刺绣披肩、丝巾、手袋；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：新中式旗袍廓形、精致刺绣、真丝与织锦、红黑金米白的克制色盘、立领与盘扣、东方优雅。`verbatim` / `artifact`
- 不该设计：艳色大面积撞色、低饱和灰调、硬挺建筑廓形、解构破洞、街头元素。
- Negative prompt: `No bright clashing colours, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no street elements`

## (7) 测试提示词示例（现代题材：植物园讲解员的制服）

- Prompt: `In the style of Shiatzy Chen, a botanical garden guide uniform, new Chinese chic, qipao-inspired silhouette, exquisite embroidery, silk and brocade, restrained luxury`
- 中文对照：夏姿·陈风格：植物园讲解员的制服，新中式，旗袍式廓形，精致刺绣，真丝与织锦，克制的奢华。
- Negative: `No bright clashing colours, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no street elements`
- 检验点：刺绣是否精致而不是堆砌；旗袍廓形是否成立而不是戏服；色彩是否克制奢华而不是俗艳。
