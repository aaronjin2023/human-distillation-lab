# Hugo Pratt — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hugo Pratt, elegant thin ink line, black-and-white watercolour wash, vast sea and sky, heavy black masses, romantic adventure comics page`
- ZH: 普拉特风格，优雅细墨线，黑白水彩晕染，辽阔海天，大块黑面，浪漫冒险漫画页。

## (2) 线条、网点/色彩

- 线条：细而优雅的线，时断时续；黑块与留白对比强烈；水彩晕染造氛围。`verbatim`
- 网点/色彩：以黑白为主，间有淡彩；海蓝、沙黄只作点缀；明暗靠墨的浓淡。
- 质感：水彩晕染 + 细墨线；纸面有水渍感，无数码平涂。

## (3) 分镜

- 格数与格形：格数少，大格多；横长格展现海天；节奏缓慢，留白多。
- 节奏：节奏缓慢如航行，大格与留白拉长时间；对话少，凝视多。
- 视线引导：欧式阅读顺序左→右；视线沿海平面走，跨页视线跳接少。

## (4) 角色造型

- 造型：科托·马耳他：耳环、船长帽、侧脸线条；人物多为浪子、水手、沙漠旅人；女性造型优雅神秘。
- 角色类型：浪子水手、沙漠旅人、神秘女性、历史人物；主角永远在路上。
- 动作：动作少而优雅，拔枪、扬帆、骑行；动态靠姿态不靠速度线。

## (5) 对话框与拟声词

- 对话框：对话框少，旁白多，文学性强。
- 拟声词：拟声词罕见；海浪与风声以画面代替。
- 文字量：每页文字密度低，旁白文学化，对话精简。

## (6) 该画什么 / 不该画什么

- 该画：大海与帆船、沙漠与绿洲、科托·马耳他的耳环与船长帽、第一次世界大战前后的异域港口、神秘符号与塔罗、安娜与丛林、威尼斯与东方、流浪与告别。`verbatim`
- 不该画：不画密集小格、不画滑稽笑料、不画鲜亮卡通色、不画拥挤对话框、不画写实毛发细节。
- Negative prompt: `No dense small panels, no slapstick gags, no bright cartoon colours, no crowded dialogue, no photorealistic detail`

## (7) 测试提示词示例（现代题材：深夜出租车穿过城市）

- Prompt: `In the style of Hugo Pratt, a taxi crossing a modern city at night, elegant thin ink line, black-and-white watercolour wash, vast empty streets, romantic adventure mood`
- 中文对照：普拉特风格：一辆出租车深夜穿过现代城市，优雅细墨线，黑白水彩晕染，空旷街道，浪漫冒险气息。
- Negative: `No dense small panels, no slapstick gags, no bright cartoon colours`
- 检验点：海天式的空旷是否还在（街道如海面）；线是否细而优雅；黑块与留白对比是否成立。
