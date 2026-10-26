# Kenzo Takada — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kenzo Takada, joyful floral print, jungle colours, oversized relaxed silhouette, kimono ease, multicultural mix, Paris meets Tokyo`
- ZH: 高田贤三风格：欢乐花卉印花，丛林色彩，宽松廓形，和服式自在，多元文化混搭，巴黎遇见东京。

## (2) 廓形方向

主廓形 2 种：一是宽松直筒廓形——落肩、宽身、无腰线，和服式自在；二是 A 形连衣裙廓形，裙摆流动。`artifact`
- 比例：上身宽松、下身流动，视觉落点在印花而非腰线；裙长多及膝，裤长宽松。`impression`

## (3) 面料与色彩

面料：主面料为棉、真丝、雪纺，配针织；织法重轻薄与透气，厚度薄—中。`artifact`
- 色彩：主色为花卉红、绿、黄、蓝等高饱和丛林色，辅色为白、米白打底；禁大面积黑与低饱和灰调。冷暖偏暖，饱和度高，明暗对比强。`impression`

## (4) 剪裁与结构

剪裁：平裁为主；和服式直线剪裁，省道极少，靠宽松与垂坠立形。`artifact`
- 结构：单层为主，多层薄纱叠加；内衬轻薄；穿脱简洁，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以圆领、翻领为主；袖为宽袖、和服袖、泡泡袖；扣多用隐藏式与系带；花卉印花是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——印花丝巾、宽檐帽、编织包；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：花卉印花与丛林色彩、宽松直筒与 A 形廓形、和服式自在剪裁、棉与真丝的轻薄面料、多元文化混搭、欢乐明亮的气质。`verbatim` / `artifact`
- 不该设计：大面积黑、低饱和灰调、合体收腰、硬挺建筑廓形、极简克制。
- Negative prompt: `No heavy black, no dull grey palette, no body-con fit, no stiff architectural silhouette, no restrained minimalism`

## (7) 测试提示词示例（现代题材：街头花店店主的工作服）

- Prompt: `In the style of Kenzo Takada, a street flower shop owner work outfit, joyful floral print, jungle colours, oversized relaxed silhouette, kimono ease, multicultural mix`
- 中文对照：高田贤三风格：街头花店店主的工作服，欢乐花卉印花，丛林色彩，宽松廓形，和服式自在，多元文化混搭。
- Negative: `No heavy black, no dull grey palette, no body-con fit, no stiff architectural silhouette, no restrained minimalism`
- 检验点：花卉印花是否欢乐而不是俗艳；廓形是否宽松自在而不是松垮；色彩是否明亮而不是灰暗。
