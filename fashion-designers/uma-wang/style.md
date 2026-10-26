# Uma Wang — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Uma Wang, aged fabric, Eastern minimalism, loose layered silhouette, muted earthy palette, texture as colour, quiet poetry`
- ZH: 王汁风格：做旧面料，东方极简，宽松层次廓形，低调大地色盘，肌理即色彩，安静的诗意。

## (2) 廓形方向

主廓形 2 种：一是宽松层次廓形——多层叠加、无腰线；二是直线长款廓形，及踝长度。`artifact`
- 比例：上长下长、等分偏长，视觉落点在面料肌理而非腰线；裙长多及踝，裤长宽松。`impression`

## (3) 面料与色彩

面料：主面料为做旧棉、麻、丝、羊毛，配水洗与磨损处理；织法重肌理与做旧，厚度中。`artifact`
- 色彩：主色为土、灰、米、黑、墨绿等大地色，辅色为做旧后的褪色点缀；禁艳色大面积印花与化纤光泽。冷暖偏暖，饱和度极低，明暗对比弱。`impression`

## (4) 剪裁与结构

剪裁：宽松剪裁——平裁为主，立裁为辅；省道极少，靠层次与肌理立形。`artifact`
- 结构：多层叠加，内衬轻薄或无；穿脱简洁，身体活动度高。`impression`

## (5) 细节与配饰

细节：领以无领、翻领为主；袖为宽袖、落肩袖；扣多用隐藏式与系带；做旧肌理是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——做旧围巾、布包；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：做旧面料、东方极简、宽松层次廓形、大地低调色盘、肌理即色彩、安静的诗意。`verbatim` / `artifact`
- 不该设计：艳色大面积印花、化纤光泽面料、合体收腰、繁复装饰、崭新挺括的面料。
- Negative prompt: `No bright all-over print, no synthetic sheen, no body-con fit, no heavy ornament, no crisp new fabric`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡旁边的家居服）

- Prompt: `In the style of Uma Wang, a home outfit beside a cup of coffee on a windowsill, aged fabric, Eastern minimalism, loose layered silhouette, muted earthy palette, texture as colour`
- 中文对照：王汁风格：一杯放在窗台上的咖啡旁边的家居服，做旧面料，东方极简，宽松层次廓形，低调大地色盘，肌理即色彩。
- Negative: `No bright all-over print, no synthetic sheen, no body-con fit, no heavy ornament, no crisp new fabric`
- 检验点：做旧是否真实而不是脏旧；层次是否安静而不是臃肿；肌理是否成色而不是单调。
