# Guo Pei — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guo Pei, opulent Chinese haute couture, gold embroidery, imperial silhouette, layered grandeur, red and gold, East as spectacle`
- ZH: 郭培风格：华贵中式高级定制，金色刺绣，帝王廓形，层叠华丽，红金配色，东方即盛景。

## (2) 廓形方向

主廓形 2 种：一是帝王式大廓形——宽肩、蓬裙、拖尾，体积宏大；二是修身礼服廓形，配层叠裙摆。`artifact`
- 比例：上身华贵、下身宏大，视觉落点在金色刺绣与拖尾而非腰线；裙长多拖地。`impression`

## (3) 面料与色彩

面料：主面料为真丝、缎、锦、欧根纱，配金线刺绣与钉珠；织法重厚重与光泽，厚度厚。`artifact`
- 色彩：主色为金、红，辅色为黑、白、蓝；禁低饱和灰调与极简克制。冷暖偏暖，饱和度高，明暗对比强。`impression`

## (4) 剪裁与结构

剪裁：高级定制剪裁——立裁为主，平裁为辅；省道保留，靠内衬与骨架立形。`artifact`
- 结构：多层叠加，内衬硬挺，骨架靠裙撑与衬布；穿脱靠系带与拉链，身体活动度低（礼服）。`impression`

## (5) 细节与配饰

细节：领以立领、翻领为主；袖为宽袖、披肩袖；扣多用盘扣与隐藏式；金色刺绣与钉珠是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——金色头饰、刺绣披肩、礼服鞋；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：金色刺绣与钉珠、帝王式大廓形、真丝缎锦的厚重面料、红金配色、拖尾与层叠裙摆、东方盛景。`verbatim` / `artifact`
- 不该设计：低饱和灰调、极简克制、合体日常款、解构破洞、街头元素。
- Negative prompt: `No dull grey palette, no restrained minimalism, no plain everyday fit, no deconstructed holes, no street elements`

## (7) 测试提示词示例（现代题材：城市跑者的晨跑套装）

- Prompt: `In the style of Guo Pei, a city runner morning running outfit, opulent Chinese haute couture, gold embroidery, imperial silhouette, layered grandeur, red and gold`
- 中文对照：郭培风格：城市跑者的晨跑套装，华贵中式高级定制，金色刺绣，帝王廓形，层叠华丽，红金配色。
- Negative: `No dull grey palette, no restrained minimalism, no plain everyday fit, no deconstructed holes, no street elements`
- 检验点：金色刺绣是否华贵而不是俗艳；廓形是否宏大而不是臃肿；东方元素是否盛景而不是符号堆砌。
