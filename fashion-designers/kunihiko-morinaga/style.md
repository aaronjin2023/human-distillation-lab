# Kunihiko Morinaga — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kunihiko Morinaga, light and shadow print, photochromic and reflective fabric, patchwork geometry, everyday unreality, technology as poetry`
- ZH: 森永邦彦风格：光影印花，感光与反光面料，拼贴几何，日常的非现实，科技即诗意。

## (2) 廓形方向

主廓形 2 种：一是拼贴几何廓形——三角形拼贴、衣片重组；二是直线廓形，配光影印花的视觉错觉。`artifact`
- 比例：上身直线、下身直筒，视觉落点在光影变化而非腰线；长度多及膝，裤长直筒。`impression`

## (3) 面料与色彩

面料：主面料为感光变色布、反光布、棉、聚酯，配拼贴面料；织法重光影反应，厚度中。`artifact`
- 色彩：主色为白、黑，辅色为光影变化中的红、蓝；禁艳色大面积印花。冷暖随光影变，饱和度低—中。`impression`

## (4) 剪裁与结构

剪裁：拼贴剪裁——三角形衣片拼接；平裁为主，立裁为辅；省道保留，靠拼贴缝立形。`artifact`
- 结构：单层与双层并存，光影面料是结构的一部分；内衬轻薄；穿脱简洁，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以圆领、翻领为主；袖为直袖、落肩袖；扣多用隐藏式与拉链；光影印花与三角形拼贴是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——光影围巾、几何包；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：光影印花、感光与反光面料、三角形拼贴几何、日常的非现实、白黑的低调色盘、科技即诗意。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、繁复装饰、合体收腰、传统印花、无科技的常规款。
- Negative prompt: `No bright all-over print, no heavy ornament, no body-con fit, no traditional print, no plain conventional design`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡旁边的家居服）

- Prompt: `In the style of Kunihiko Morinaga, a home outfit beside a cup of coffee on a windowsill, light and shadow print, photochromic and reflective fabric, patchwork geometry, everyday unreality`
- 中文对照：森永邦彦风格：一杯放在窗台上的咖啡旁边的家居服，光影印花，感光与反光面料，拼贴几何，日常的非现实。
- Negative: `No bright all-over print, no heavy ornament, no body-con fit, no traditional print, no plain conventional design`
- 检验点：光影是否随环境变化而不是固定印花；拼贴是否几何化而不是凌乱；日常感是否带非现实而不是平庸。
