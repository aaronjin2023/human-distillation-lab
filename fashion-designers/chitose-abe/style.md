# Chitose Abe — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chitose Abe, hybrid splicing, two garments in one, mixed fabrics, elegant everyday standard, pleats and knits, quiet subversion`
- ZH: 阿部千登势风格：混合拼接，一衣两穿，混合面料，优雅的日常标准，褶皱与针织，安静的颠覆。

## (2) 廓形方向

主廓形 2 种：一是拼接廓形——两件衣服拼成一件，前后、左右衣片各属不同单品；二是混合面料廓形——针织与梭织、褶皱与平挺同件并置。`artifact`
- 比例：上身拼接、下身直筒，视觉落点在拼接缝而非腰线；裙长多及膝，裤长直筒。`impression`

## (3) 面料与色彩

面料：主面料为针织、棉、羊毛、聚酯，配褶皱布与牛仔；织法重针织与梭织的并置，厚度中。`artifact`
- 色彩：主色为黑、白、灰、卡其、海军蓝，辅色为单色亮色点缀；禁艳色大面积印花。冷暖偏冷，饱和度低—中。`impression`

## (4) 剪裁与结构

剪裁：拼接剪裁——两件单品的衣片按同一版型拼接；平裁为主，立裁为辅；省道保留，靠拼接缝立形。`artifact`
- 结构：单层与双层并存，拼接缝外露或隐藏；内衬轻薄；穿脱简洁，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以翻领、立领、连帽拼接为主；袖为针织袖与梭织袖拼接；扣多用拉链与按扣；拼接缝是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——拼接包、针织围巾；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：混合拼接、一衣两穿、针织与梭织并置、褶皱与平挺并置、黑白灰卡其的低调色盘、优雅的日常标准。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、繁复装饰、合体收腰、单面料单廓形、街头夸张。
- Negative prompt: `No bright all-over print, no heavy ornament, no body-con fit, no single-fabric single-silhouette, no exaggerated street style`

## (7) 测试提示词示例（现代题材：机场地勤人员的制服）

- Prompt: `In the style of Chitose Abe, an airport ground staff uniform, hybrid splicing, two garments in one, mixed fabrics, elegant everyday standard, pleats and knits`
- 中文对照：阿部千登势风格：机场地勤人员的制服，混合拼接，一衣两穿，混合面料，优雅的日常标准，褶皱与针织。
- Negative: `No bright all-over print, no heavy ornament, no body-con fit, no single-fabric single-silhouette, no exaggerated street style`
- 检验点：拼接是否成立而不是拼凑；混合面料是否对话而不是冲突；日常感是否优雅而不是平庸。
