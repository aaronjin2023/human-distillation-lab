# 管道升 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guan Daosheng: running and regular script, elegant and firm, close to Zhao Mengfu yet more delicate, strokes smooth and restrained, characters neat and graceful`
- ZH: 管道升风格：行楷秀媚劲健，近赵孟頫而更秀，用笔圆转内敛，结字端整清丽。

## (2) 笔法

- 用笔圆转内敛，中锋为主，提按和缓；起笔藏锋，收笔回锋，锋芒内敛而不外露。`impression` 笔法与赵孟頫相近而更秀，线条清丽劲健。`impression` 禁笔：不用方折硬朗的棱角，不用侧锋刷字的锋芒，不用枯笔飞白。`impression`

## (3) 结字与章法

- 结字端整清丽，重心居中，字形大小均匀而略有参差；疏密适中，不欹不险。`impression` 章法行距均匀，行气端直，留白适中。`impression` 幅式多为卷、册，落款小字。`artifact`

## (4) 墨色与节奏

- 墨色匀而清，一幅之内浓淡变化和缓，少枯笔；笔画墨色均匀，如玉温润。`impression` 节奏中速平稳，起笔缓、行笔匀、收笔回。`impression` 纸多用熟纸与绢，墨色附着清丽。`impression`

## (5) 书体与取法

- 书体以行书、楷书为主；取法二王，与赵孟頫同法而自成秀媚一路；为赵孟頫夫人，书画皆精。`artifact` 演变：早年取法二王较谨，中年秀媚已成，晚年更趋清丽。`impression`

## (6) 该写什么 / 不该写什么

- 该写：圆转内敛的中锋用笔、端整清丽的结字、均匀清润的墨色、疏密适中的章法、近赵孟頫而更秀的气息。
- 不该写：方折硬朗的棱角、侧锋刷字的锋芒、枯笔飞白、欹侧险绝的结字、浓艳重彩。
- Negative prompt: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no gaudy colour, no printed typeface`

## (7) 测试提示词示例（现代题材：“约克夏犬坐在地铁座位上”行书）

- Prompt: `In the style of Guan Daosheng, running script calligraphy writing 'a Yorkshire terrier sitting on a subway seat' in Chinese characters, smooth restrained strokes, neat graceful characters, even clear ink`
- 中文对照：管道升风格：行书写一句“约克夏犬坐在地铁座位上”，圆转内敛，端整清丽，墨匀而清。
- Negative: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no gaudy colour, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
