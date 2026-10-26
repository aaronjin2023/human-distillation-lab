# 沈度 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Du: regular script of the early Ming court, upright and warm, strokes rounded and full, characters neat and dignified, ink even and mellow, the model of the guange manner`
- ZH: 沈度风格：明初台阁体楷书，端正温润，用笔圆满，结字端整庄重，墨匀而醇，馆阁之范。

## (2) 笔法

- 用笔圆满，中锋为主，提按和缓；起笔藏锋，收笔回锋，笔画丰满而不瘦硬。`impression` 楷书笔法取法二王与赵孟頫，温润端整。`impression` 禁笔：不用方折硬朗的棱角，不用侧锋刷字，不用枯笔飞白，不用欹侧险绝。`impression`

## (3) 结字与章法

- 结字端整庄重，重心居中，字形大小均匀，疏密适中；行列分明，行气端直。`impression` 章法行距均匀，留白适中，落款小字，钤印讲究。`artifact` 幅式多为卷、册、碑。`artifact`

## (4) 墨色与节奏

- 墨色匀而醇，一幅之内浓淡变化极小，少枯笔；笔画墨色均匀饱满。`impression` 节奏匀速平稳，一字一顿，笔笔有法。`impression` 纸多用熟纸，墨色附着温润。`impression`

## (5) 书体与取法

- 书体以楷书为主，兼擅行书；取法二王、赵孟頫，明初台阁体的代表。`artifact` 演变：早年取法赵孟頫较谨，中年台阁体已成，晚年更趋温润庄重。`impression`

## (6) 该写什么 / 不该写什么

- 该写：圆满的中锋用笔、端整庄重的结字、均匀醇厚的墨色、行列分明的章法、台阁体的温润气息。
- 不该写：方折硬朗的棱角、侧锋刷字的锋芒、枯笔飞白、欹侧险绝的结字、大小悬殊的参差。
- Negative prompt: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no extreme size contrast, no printed typeface`

## (7) 测试提示词示例（现代题材：地铁站名楷书）

- Prompt: `In the style of Shen Du, regular script calligraphy writing modern subway station names, rounded full centre-brush strokes, upright dignified characters, even mellow ink, neat columns`
- 中文对照：沈度风格：楷书写地铁站名，圆满中锋，端整庄重，墨匀而醇，行列分明。
- Negative: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no extreme size contrast, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
