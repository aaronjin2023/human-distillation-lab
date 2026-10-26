# Derek Lam — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Derek Lam, refined American minimalism, clean architectural tailoring, muted palette, silk and wool, effortless polish, quiet luxury`
- ZH: 林建德风格：精致美式极简，干净建筑式剪裁，低调色盘，真丝与羊毛，毫不费力的精致，安静的奢华。

## (2) 廓形方向

主廓形 2 种：一是修身直筒廓形——柔和肩线、无腰线；二是 A 形裙廓形，裙摆流动。`artifact`
- 比例：上身修身、下身流动，视觉落点在整体纵线而非腰线；裙长多及膝，裤长直筒。`impression`

## (3) 面料与色彩

面料：主面料为真丝、羊毛、棉，配皮革；织法重柔软与垂感，厚度中。`artifact`
- 色彩：主色为米白、灰、黑、驼，辅色为单色亮色点缀；禁艳色大面积印花。冷暖偏冷，饱和度低，明暗对比弱。`impression`

## (4) 剪裁与结构

剪裁：建筑式剪裁——平裁为主，立裁为辅；省道保留，靠版型精度立形。`artifact`
- 结构：单层为主，内衬轻薄；穿脱简洁，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以圆领、翻领、无领为主；袖为直袖、落肩袖；扣多用隐藏式；极简细节是核心。`artifact`
- 配饰：只写与时装一体设计的配饰——简约手袋、细腰带；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：精致美式极简、干净建筑式剪裁、米白灰黑驼的低调色盘、真丝与羊毛、毫不费力的精致、安静的奢华。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、繁复装饰、合体收腰、硬挺夸张廓形、街头元素。
- Negative prompt: `No bright all-over print, no heavy ornament, no body-con fit, no stiff exaggerated silhouette, no street elements`

## (7) 测试提示词示例（现代题材：地铁站务员的制服）

- Prompt: `In the style of Derek Lam, a subway station staff uniform, refined American minimalism, clean architectural tailoring, muted palette, silk and wool, effortless polish`
- 中文对照：林建德风格：地铁站务员的制服，精致美式极简，干净建筑式剪裁，低调色盘，真丝与羊毛，毫不费力的精致。
- Negative: `No bright all-over print, no heavy ornament, no body-con fit, no stiff exaggerated silhouette, no street elements`
- 检验点：剪裁是否建筑式而不是生硬；色盘是否低调而不是平淡；精致是否毫不费力而不是刻意。
