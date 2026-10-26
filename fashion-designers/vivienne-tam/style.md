# Vivienne Tam — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vivienne Tam, East meets West print, Mao portrait print, qipao-inspired silhouette, bright colours, feminine elegance, cultural dialogue`
- ZH: 谭燕玉风格：东西合璧印花，毛泽东肖像印花，旗袍式廓形，明亮色彩，女性优雅，文化对话。

## (2) 廓形方向

主廓形 2 种：一是旗袍式廓形——收腰、开衩、立领，东方直线与西方合体并置；二是 A 形连衣裙廓形，裙摆流动。`artifact`
- 比例：上身合体、下身流动，视觉落点在印花与开衩而非腰线；裙长多及膝，裤长直筒。`impression`

## (3) 面料与色彩

面料：主面料为真丝、雪纺、棉，配刺绣与印花；织法重轻薄与垂感，厚度薄—中。`artifact`
- 色彩：主色为红、黄、蓝、粉等明亮色，辅色为黑、白打底；禁大面积黑与低饱和灰调。冷暖偏暖，饱和度高，明暗对比强。`impression`

## (4) 剪裁与结构

剪裁：旗袍式剪裁——立领、收腰、开衩，平裁与立裁并用；省道保留，靠收腰与开衩立形。`artifact`
- 结构：单层为主，多层薄纱叠加；内衬轻薄；穿脱靠侧拉链与盘扣，身体活动度中。`impression`

## (5) 细节与配饰

细节：领以立领、翻领为主；袖为短袖、无袖、宽袖；扣多用盘扣；东西合璧印花是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——印花丝巾、刺绣包；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：东西合璧印花、旗袍式廓形、立领与盘扣、明亮色彩、真丝与雪纺、文化对话。`verbatim` / `artifact`
- 不该设计：大面积黑、低饱和灰调、硬挺建筑廓形、解构破洞、极简克制。
- Negative prompt: `No heavy black, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no restrained minimalism`

## (7) 测试提示词示例（现代题材：城市快递员的雨天工作服）

- Prompt: `In the style of Vivienne Tam, a city courier rain outfit, East meets West print, qipao-inspired silhouette, bright colours, feminine elegance, cultural dialogue`
- 中文对照：谭燕玉风格：城市快递员的雨天工作服，东西合璧印花，旗袍式廓形，明亮色彩，女性优雅，文化对话。
- Negative: `No heavy black, no dull grey palette, no stiff architectural silhouette, no deconstructed holes, no restrained minimalism`
- 检验点：印花是否文化对话而不是符号堆砌；旗袍廓形是否成立而不是戏服；色彩是否明亮而不是俗艳。
