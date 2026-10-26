# 赵孟頫 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhao Mengfu: regular and running script reviving the Two Wangs, upright and elegant, strokes smooth and rounded, characters neat yet lively, ink even and warm`
- ZH: 赵孟頫风格：楷行复古二王，端正秀润，用笔圆转流畅，结字端整而活，墨匀而温。

## (2) 笔法

- 用笔圆转流畅，中锋为主，提按和缓，起笔藏锋，收笔回锋；转折圆转，不尚方折。`verbatim` 笔法善用“用笔千古不易”的中锋圆笔，线条温润如玉。`artifact` 禁笔：不用方折硬朗的棱角，不用侧锋刷字的锋芒，不用枯笔飞白。`impression`

## (3) 结字与章法

- 结字端正秀润，重心居中，字形大小均匀而略有参差；疏密适中，不欹不险。`verbatim` 章法行距均匀，行气端直，留白适中；楷书行列分明，行书牵丝和缓。`verbatim` 幅式多为卷、册、碑，落款小字，钤印讲究。`artifact`

## (4) 墨色与节奏

- 墨色匀而温，一幅之内浓淡变化和缓，少枯笔；楷书墨浓而匀，行书墨润而活。`verbatim` 节奏中速平稳，起笔缓、行笔匀、收笔回，一字一顿而不滞。`impression` 纸多用熟纸与绢，墨色附着温润。`impression`

## (5) 书体与取法

- 书体楷、行皆精，兼擅篆、隶、草；取法二王，复古一路，反对宋人尚意之病，自称“用笔千古不易，结字因时相传”。`artifact` 演变：早年取法二王较谨，中年端正秀润已成，晚年更趋温润圆融。`impression`

## (6) 该写什么 / 不该写什么

- 该写：圆转流畅的中锋用笔、端正秀润的结字、均匀温润的墨色、疏密适中的章法、复古二王的雅正气息。
- 不该写：方折硬朗的棱角、侧锋刷字的锋芒、枯笔飞白、欹侧险绝的结字、浓艳重彩。
- Negative prompt: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no gaudy colour, no printed typeface`

## (7) 测试提示词示例（现代题材：“约克夏犬坐在地铁座位上”行书）

- Prompt: `In the style of Zhao Mengfu, running script calligraphy writing 'a Yorkshire terrier sitting on a subway seat' in Chinese characters, smooth rounded centre-brush strokes, upright elegant characters, even warm ink, neat columns`
- 中文对照：赵孟頫风格：行书写一句“约克夏犬坐在地铁座位上”，圆转流畅，端正秀润，墨匀而温，行列端直。
- Negative: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no gaudy colour, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
