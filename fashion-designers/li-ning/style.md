# Li Ning — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Ning, sporty Chinese fashion,悟道 wudao philosophy, relaxed athletic silhouette, red and black, Chinese elements as streetwear, function meets fashion`
- ZH: 李宁风格：运动中国风，悟道哲学，宽松运动廓形，红黑色盘，中国元素街头化，功能与时装合一。

## (2) 廓形方向

主廓形 2 种：一是宽松运动廓形——卫衣、运动裤、T 恤的时装版；二是直线廓形，配中国元素细节。`artifact`
- 比例：上身宽松、下身直筒，视觉落点在印花与细节而非腰线；长度多及膝，裤长宽松。`impression`

## (3) 面料与色彩

面料：主面料为棉、针织、技术面料，配防水处理；织法重功能与舒适，厚度中。`artifact`
- 色彩：主色为红、黑、白，辅色为黄、蓝点缀；禁艳色大面积撞色。冷暖偏暖，饱和度中—高。`impression`

## (4) 剪裁与结构

剪裁：运动剪裁——平裁为主；省道极少，靠宽松与功能立形。`artifact`
- 结构：单层为主，多层叠加；内衬轻薄；穿脱简洁，身体活动度极高。`impression`

## (5) 细节与配饰

细节：领以圆领、连帽为主；袖为落肩袖、长袖；扣多用拉链与按扣；中国元素印花与汉字是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——运动鞋、双肩包；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：运动中国风、悟道哲学、宽松运动廓形、红黑白的配色、中国元素街头化、功能与时装合一。`verbatim` / `artifact`
- 不该设计：艳色大面积撞色、繁复装饰、合体收腰、硬挺建筑廓形、古典优雅。
- Negative prompt: `No bright clashing colours, no heavy ornament, no body-con fit, no stiff architectural silhouette, no classical elegance`

## (7) 测试提示词示例（现代题材：城市跑者的晨跑套装）

- Prompt: `In the style of Li Ning, a city runner morning running outfit, sporty Chinese fashion, relaxed athletic silhouette, red and black, Chinese elements as streetwear`
- 中文对照：李宁风格：城市跑者的晨跑套装，运动中国风，宽松运动廓形，红黑色盘，中国元素街头化。
- Negative: `No bright clashing colours, no heavy ornament, no body-con fit, no stiff architectural silhouette, no classical elegance`
- 检验点：中国元素是否街头化而不是符号堆砌；运动感是否时装化而不是运动器材；红黑是否克制而不是刺眼。
