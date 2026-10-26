# Thom Browne — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thom Browne, shrunken grey suit, cropped trousers, precise tailoring, grey palette, white shirt and tie, uniform as theatre`
- ZH: 汤姆·布朗风格：缩水灰色西装，短裤西装，精确剪裁，灰色色盘，白衬衫领带，制服即戏剧。

## (2) 廓形方向

主廓形 2 种：一是缩水西装廓形——收短、收窄、露踝；二是短裤西装廓形——西装配短裤。`artifact`
- 比例：上身缩短、下身露踝，视觉落点在缩水的比例而非腰线；裤长露踝，裙长及膝。`impression`

## (3) 面料与色彩

面料：主面料为灰色羊毛、棉、真丝，配条纹；织法重挺括与平滑，厚度中。`artifact`
- 色彩：主色为灰，辅色为白、黑、海军蓝，偶见红白蓝条纹点缀；禁艳色大面积印花。冷暖偏冷，饱和度极低，明暗对比弱。`impression`

## (4) 剪裁与结构

剪裁：精确剪裁——平裁为主，立裁为辅；省道保留，靠缩水比例立形。`artifact`
- 结构：单层为主，内衬轻挺；穿脱靠扣与拉链，身体活动度中。`impression`

## (5) 细节与配饰

细节：领以翻领为主；袖为短袖、长袖；扣多用纽扣；红白蓝条纹是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——领带、长袜、皮鞋；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：缩水灰色西装、短裤西装、精确剪裁、灰色色盘、白衬衫领带、制服即戏剧。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、繁复装饰、宽松廓形、合体收腰、街头元素。
- Negative prompt: `No bright all-over print, no heavy ornament, no oversized silhouette, no body-con fit, no street elements`

## (7) 测试提示词示例（现代题材：地铁站务员的制服）

- Prompt: `In the style of Thom Browne, a subway station staff uniform, shrunken grey suit, cropped trousers, precise tailoring, grey palette, white shirt and tie`
- 中文对照：汤姆·布朗风格：地铁站务员的制服，缩水灰色西装，短裤西装，精确剪裁，灰色色盘，白衬衫领带。
- Negative: `No bright all-over print, no heavy ornament, no oversized silhouette, no body-con fit, no street elements`
- 检验点：缩水比例是否精确而不是滑稽；灰色是否克制而不是单调；制服感是否戏剧而不是刻板。
