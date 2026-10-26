# Phillip Lim — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Phillip Lim, effortless minimalism, clean relaxed tailoring, muted palette, silk and cotton, downtown ease, quiet luxury`
- ZH: 林能平风格：毫不费力的极简，干净宽松剪裁，低调色盘，真丝与棉，市中心自在，安静的奢华。

## (2) 廓形方向

主廓形 2 种：一是宽松直筒廓形——落肩、宽身、无腰线；二是修身套装廓形，配柔和肩线。`artifact`
- 比例：上身宽松、下身直筒，视觉落点在整体纵线而非腰线；裙长多及膝，裤长直筒。`impression`

## (3) 面料与色彩

面料：主面料为真丝、棉、羊毛，配皮革；织法重柔软与垂感，厚度中。`artifact`
- 色彩：主色为米白、灰、黑、海军蓝，辅色为单色亮色点缀；禁艳色大面积印花。冷暖偏冷，饱和度低，明暗对比弱。`impression`

## (4) 剪裁与结构

剪裁：宽松剪裁——平裁为主，立裁为辅；省道极少，靠宽松与垂感立形。`artifact`
- 结构：单层为主，内衬轻薄；穿脱简洁，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以圆领、翻领、无领为主；袖为直袖、落肩袖；扣多用隐藏式；极简细节是核心。`artifact`
- 配饰：只写与时装一体设计的配饰——Pashli 手袋、细腰带；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：毫不费力的极简、宽松直筒廓形、米白灰黑的低调色盘、真丝与棉、市中心自在、安静的奢华。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、繁复装饰、合体收腰、硬挺建筑廓形、古典优雅。
- Negative prompt: `No bright all-over print, no heavy ornament, no body-con fit, no stiff architectural silhouette, no classical elegance`

## (7) 测试提示词示例（现代题材：机场地勤人员的制服）

- Prompt: `In the style of Phillip Lim, an airport ground staff uniform, effortless minimalism, clean relaxed tailoring, muted palette, silk and cotton, downtown ease`
- 中文对照：林能平风格：机场地勤人员的制服，毫不费力的极简，干净宽松剪裁，低调色盘，真丝与棉，市中心自在。
- Negative: `No bright all-over print, no heavy ornament, no body-con fit, no stiff architectural silhouette, no classical elegance`
- 检验点：极简是否毫不费力而不是单调；宽松是否干净而不是松垮；色盘是否低调而不是平淡。
