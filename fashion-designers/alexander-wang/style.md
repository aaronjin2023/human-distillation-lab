# Alexander Wang — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alexander Wang, sporty luxury, downtown cool, relaxed tailoring, black and grey, T-shirt ease, urban edge`
- ZH: 王大仁风格：运动奢华，市中心酷感，宽松剪裁，黑灰色盘，T 恤式自在，城市边缘。

## (2) 廓形方向

主廓形 2 种：一是宽松直筒廓形——落肩、宽身、无腰线；二是运动廓形——卫衣、短裤、T 恤的奢华版。`artifact`
- 比例：上身宽松、下身直筒，视觉落点在材质与细节而非腰线；裙长多及膝，裤长宽松。`impression`

## (3) 面料与色彩

面料：主面料为棉、针织、皮革、牛仔，配技术面料；织法重柔软与垂感，厚度中。`artifact`
- 色彩：主色为黑、灰、白，辅色为单色亮色点缀；禁艳色大面积印花。冷暖偏冷，饱和度低，明暗对比弱。`impression`

## (4) 剪裁与结构

剪裁：宽松剪裁——平裁为主，立裁为辅；省道极少，靠宽松与垂感立形。`artifact`
- 结构：单层为主，多层叠加；内衬轻薄；穿脱简洁，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以圆领、连帽为主；袖为落肩袖、长袖；扣多用拉链与按扣；T 恤式细节是核心。`artifact`
- 配饰：只写与时装一体设计的配饰——链条包、厚底鞋；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：运动奢华、宽松直筒廓形、黑灰白的低调色盘、T 恤式自在、棉针织皮革的材质对话、城市边缘。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、繁复装饰、合体收腰、硬挺建筑廓形、古典优雅。
- Negative prompt: `No bright all-over print, no heavy ornament, no body-con fit, no stiff architectural silhouette, no classical elegance`

## (7) 测试提示词示例（现代题材：共享单车骑行者的通勤装）

- Prompt: `In the style of Alexander Wang, a bike-sharing commuter outfit, sporty luxury, downtown cool, relaxed tailoring, black and grey, T-shirt ease`
- 中文对照：王大仁风格：共享单车骑行者的通勤装，运动奢华，市中心酷感，宽松剪裁，黑灰色盘，T 恤式自在。
- Negative: `No bright all-over print, no heavy ornament, no body-con fit, no stiff architectural silhouette, no classical elegance`
- 检验点：运动感是否奢华而不是廉价；宽松是否酷感而不是松垮；黑灰是否克制而不是单调。
